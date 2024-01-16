"""Tools."""

import json
import logging
import os
from operator import itemgetter
from pathlib import Path

import dictdiffer  # type: ignore
from jinja2 import Template
from vhelpers import vre, vlist

import fortigate_api
from fortigate_api import helpers as h
from fortigate_api.schema import custom
from fortigate_api.schema.models import DSchema, Schema
from fortigate_api.types_ import DAny, LStr, LDAny, DDAny, DLDAny

ROOT = Path(__file__).parent.parent.parent
PACKAGE = fortigate_api.__name__
PACKAGE_DIR = PACKAGE.replace("-", "_")


def create_models() -> None:
    """Create cmdb models."""
    version = "6.4.14"
    scope = "cmdb"
    schemas_d: DSchema = read_cmdb_schemas_d(version)
    paths: LStr = list(schemas_d)
    _check_cmdb_types(schemas_d)

    _create_cmdb_app_model(scope, schemas_d)
    _create_cmdb_app(scope, paths)
    _create_scope(scope, paths)


def read_json_cmdb_schemas_d(version: str, scope: str) -> DDAny:
    """Read cmdb schema from the json file in docs."""
    schemas_d: DDAny = {}
    root_o: Path = Path(os.path.abspath(__file__)).parent
    root_o = root_o.joinpath(f"{version}/{scope}/")
    for path in root_o.glob("*.json"):
        name = str(path.name.split()[-1])
        key = name.replace(".json", "")
        with open(path, encoding="utf-8") as file_:
            schema_d: DAny = json.load(file_)
            schemas_d[key] = schema_d
    return schemas_d


def read_cmdb_schemas_d(version: str) -> DSchema:
    """Read cmdb schema models from the json file in docs."""
    scope = "cmdb"
    schemas_d: DSchema = {}
    schemas_d_: DDAny = read_json_cmdb_schemas_d(version, scope)

    for schema_d in schemas_d_.values():
        for key, schema_ in schema_d["paths"].items():
            path_ = str(key)
            if path_.find("/") <= -1:
                raise ValueError(f"/ expected in {path_=}.")
            # schema_w_uid
            if not path_.endswith("}"):
                schemas_d.setdefault(path_, Schema())
                schemas_d[path_].path = path_
                schemas_d[path_].w_uid = schema_
                continue
            # schema_wo_uid
            path_, uid = path_.rsplit("/", maxsplit=1)
            uid = vre.find1(r"{(\S+)}", uid)
            if not uid:
                raise ValueError(f"Value expected in {uid=}.")
            schemas_d.setdefault(path_, Schema())
            schemas_d[path_].path = path_
            schemas_d[path_].wo_uid = schema_
            schemas_d[path_].uid = uid

    return schemas_d


# ============================= helpers ==============================


def _check_cmdb_types(schemas_d: DSchema) -> None:
    """Compare parameters for URLs with/without uid."""
    for schema_o in schemas_d.values():
        if _is_schema_custom(schema_o.path):
            continue
        if not (schema_o.w_uid and schema_o.wo_uid):
            continue

        for method in ["get", "put", "delete", "post"]:
            method_w = schema_o.w_uid.get(method, {})  # with UID
            method_wo = schema_o.wo_uid.get(method, {})  # without UID
            if not (method_w and method_wo):
                continue
            # parameters
            data_w = {d["name"]: d["type"] for d in method_w["parameters"]}  # with UID
            data_wo = {d["name"]: d["type"] for d in method_wo["parameters"]}  # without UID
            common_keys = set(data_w).intersection(set(data_wo))
            data_w = {k: v for k, v in data_w.items() if k in common_keys}
            data_wo = {k: v for k, v in data_wo.items() if k in common_keys}
            if diff := list(dictdiffer.diff(data_w, data_wo)):
                raise ValueError(f"{diff=}")
            # responses
            data_w = {
                k: d["type"]
                for k, d in method_w["responses"]["200"]["schema"]["properties"].items()
            }
            data_wo = {
                k: d["type"]
                for k, d in method_wo["responses"]["200"]["schema"]["properties"].items()
            }
            if diff := list(dictdiffer.diff(data_w, data_wo)):
                raise ValueError(f"{diff=}")


def _create_scope(scope: str, paths: LStr) -> None:
    """Create cmdb files."""
    root_o: Path = ROOT.joinpath(f"{PACKAGE_DIR}/{scope}")
    items: LDAny = []
    for path_ in paths:
        _, app_path, _ = h.path_to_parts(path_)
        app_name, app_file, app_class = h.app_names(scope, app_path)
        item_d: DAny = {
            "path": f"{scope}/{app_path}",
            "app_name": app_name,
            "app_file": app_file,
            "app_class": app_class,
        }
        items.append(item_d)
    items = vlist.no_dupl(items)
    items.sort(key=itemgetter("app_name"))

    # init
    content_j2 = Path("templates/init_scope.j2").read_text(encoding="utf-8")
    scope, scope_file, scope_class = h.scope_names(scope)
    text = Template(content_j2).render(
        docstring=f"{scope} scope connectors.".capitalize(),
        scope_name=scope,
        scope_file=scope_file,
        scope_class=scope_class,
        items=items,
    )
    path: Path = root_o.joinpath("__init__.py")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))

    # scope
    content_j2 = Path("templates/class_scope.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(
        docstring=f"{scope} scope connectors.".capitalize(),
        scope_name=scope,
        scope_class=scope_class,
        items=items,
    )
    path = root_o.joinpath(f"{scope_file}.py")
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def _create_cmdb_app(scope: str, paths: LStr) -> None:
    """Create cmdb/app files."""
    items_d: DLDAny = {}
    for path_ in paths:
        _, app_path, _ = h.path_to_parts(path_)
        _, app_name, model_name = h.path_to_attrs(f"{scope}{path_}")
        model_name, model_class = h.model_names(scope, app_name, model_name)

        items_d.setdefault(app_path, [])
        item_d: DAny = {
            "path": path_,
            "model_name": model_name,
            "model_class": model_class,
        }
        items_d[app_path].append(item_d)

    for app_path, items in items_d.items():
        app_name, app_file, app_class = h.app_names(scope, app_path)

        # init
        content_j2 = Path("templates/init_app.j2").read_text(encoding="utf-8")
        text = Template(content_j2).render(
            docstring=f"{scope}/{app_path} connectors.".capitalize(),
            scope_name=scope,
            app_name=app_name,
            app_file=app_file,
            app_class=app_class,
            items=items,
        )
        path: Path = ROOT.joinpath(f"{PACKAGE_DIR}/{scope}/{app_name}").joinpath("__init__.py")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        logging.info(str(f"Created {path!s}."))

        # app
        content_j2 = Path("templates/class_app.j2").read_text(encoding="utf-8")
        text = Template(content_j2).render(
            docstring=f"{scope}/{app_path} connectors.".capitalize(),
            scope_name=scope,
            app_name=app_name,
            app_class=app_class,
            items=items,
        )
        path = ROOT.joinpath(f"{PACKAGE_DIR}/{scope}/{app_name}").joinpath(f"{app_file}.py")
        path.write_text(text, encoding="utf-8")
        logging.info(str(f"Created {path!s}."))


def _create_cmdb_app_model(scope: str, schemas_d: DSchema) -> None:
    """Create cmdb/app/model files."""
    for schema_o in schemas_d.values():
        path_: str = schema_o.path.strip("/")
        _, app_path, model_path = h.path_to_parts(path_)
        app_name, _, _ = h.app_names(scope, app_path)
        model_name, model_class = h.model_names(scope, app_name, model_path)
        custom_d: DAny = custom.SETTINGS[scope].get(app_path, {}).get(model_path, {})
        path_ui = str(custom_d.get("path_ui") or "")
        # model
        if custom_d.get("is_custom_model"):
            path_s = f"{PACKAGE_DIR}/schema/custom/{scope}/{app_name}/{model_name}.py"
            path: Path = ROOT.joinpath(path_s)
            text = path.read_text(encoding="utf-8")
        else:
            content_j2 = Path("templates/class_model.j2").read_text(encoding="utf-8")
            text = Template(content_j2).render(
                docstring=f"{scope}/{path_} connector.".capitalize(),
                scope_name=scope,
                model_class=model_class,
                path=schema_o.path,
                path_ui=path_ui,
                uid=schema_o.uid,
            )
        path = ROOT.joinpath(f"{PACKAGE_DIR}/{scope}/{app_name}/{model_name}.py")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        logging.info(str(f"Created {path!s}."))


def _is_schema_custom(path: str) -> bool:
    """Return True if the model is custom and does not require generation code."""
    paths = custom.SETTINGS["cmdb"]
    if path in paths:
        return True
    return False


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    # create_models()

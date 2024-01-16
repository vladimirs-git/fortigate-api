"""Create documentation sections."""
import logging
import re
from pathlib import Path

import yaml
from jinja2 import Template

import fortigate_api
from fortigate_api import FortiGateAPI, FortiGate
from fortigate_api import helpers as h
from fortigate_api.schema import tools
from fortigate_api.types_ import LStr, DDAny, DAny

ROOT = Path(__file__).parent.parent
API_CLASS = FortiGateAPI.__name__
API_DIR = API_CLASS.lower()


def create_index() -> None:
    """Create docs/index.rst"""
    path: Path = ROOT.joinpath(f"docs/index.rst")
    text = path.read_text(encoding="utf-8")
    top = re.search(".+pip install.+?----(-)+", text, re.S)[0]
    bottom = re.search(r"----(-)+\s+Indices and tables.+", text, re.S)[0]
    usage = _usage__quickstart()
    text_ = "".join([top, usage, bottom])
    path.write_text(text_)
    logging.info(str(f"Created {path!s}."))


def _usage__quickstart() -> str:
    """Get usage example of Quickstart section in index.rst."""
    items: LStr = []
    for file_name in ["fortigateapi.py", "fortigate.py"]:
        path: Path = ROOT.joinpath(f"examples/quickstart/{file_name}")
        text = path.read_text(encoding="utf-8")
        text = h.rst_code(text)
        items.append(text)
    items = ["", *items, ""]
    text = "\n\n".join(items)
    return text


def create_rest_api_cmdb_yml() -> None:
    """Create FortiGateAPI REST API schemas .yml."""
    version = "6.4.14"
    scope = "cmdb"
    schemas_d: DDAny = tools.read_json_cmdb_schemas_d(version, scope)
    app_paths: LStr = list(schemas_d)

    _create_rest_api_scope(version, scope, app_paths)
    for app_path, schema_d in schemas_d.items():
        _create_rest_api_scope_app_yml(version, scope, app_path, schema_d)


def create_rest_api_cmdb_rst() -> None:
    """Create FortiGateAPI REST API schemas .rst."""
    version = "6.4.14"
    scope = "cmdb"
    schemas_d: DDAny = tools.read_json_cmdb_schemas_d(version, scope)
    app_paths: LStr = list(schemas_d)

    _create_rest_api_scope(version, scope, app_paths)
    for app_path, schema_d in schemas_d.items():
        _create_rest_api_scope_app(version, scope, app_path)


def _create_rest_api_scope_app_yml(version: str, scope: str, app_path: str, schema_d: DAny) -> None:
    """Create docs/rest_api/version/scope/app.yml (docs/rest_api/6.4.14/cmdb/firewall.yml)"""
    path_yml: Path = ROOT.joinpath(f"docs/rest_api/{version}/{scope}/{app_path}.yml")
    path_yml.parent.mkdir(parents=True, exist_ok=True)
    with open(path_yml, "w", encoding="utf-8") as file_:
        yaml.dump(schema_d, file_, default_flow_style=False)
    logging.info(str(f"Created {path_yml!s}."))


def _create_rest_api_scope_app(version: str, scope: str, app_path: str) -> None:
    """Create docs/rest_api/version/scope/app.rst (docs/rest_api/6.4.14/cmdb/firewall.rst)"""
    path: Path = ROOT.joinpath(f"docs/rest_api/{version}/{scope}/{app_path}.rst")
    content_j2 = Path("templates/rest_api/scope_app.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(version=version, scope=scope, app_path=app_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def _create_rest_api_scope(version: str, scope: str, app_paths: LStr) -> None:
    """Create docs/rest_api/version/scope.rst (docs/rest_api/6.4.14/cmdb.rst)"""
    content_j2 = Path("templates/rest_api/scope_contents.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(version=version, scope=scope, app_paths=app_paths)
    path: Path = ROOT.joinpath(f"docs/rest_api/{version}/{scope}.rst")
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def create_fortigateapi_cmdb() -> None:
    """Create FortiGateAPI connectors."""
    scope = "cmdb"
    cmdb = FortiGateAPI(host="host").cmdb
    app_names: LStr = [s for s in dir(cmdb) if s[0].islower()]

    _create_fortigateapi__scope(scope, app_names)
    for app_name in app_names:
        app_o = getattr(cmdb, app_name)
        model_names = [s for s in dir(app_o) if s[0].islower()]
        _create_fortigateapi__scope_app(scope, app_name, model_names)
        for model_name in model_names:
            _create_fortigateapi__scope_app_model(scope, app_name, model_name)


def _create_fortigateapi__scope(scope: str, app_names: LStr) -> None:
    """Create docs/fortigateapi/cmdb/_contents.rst"""
    content_j2 = Path(f"templates/{API_DIR}/scope_contents.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(
        api_class=API_CLASS,
        scope=scope,
        app_names=app_names,
    )
    path: Path = ROOT.joinpath(f"docs/{API_DIR}/{scope}/_contents.rst")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def _create_fortigateapi__scope_app(scope: str, app_name: str, model_names: LStr) -> None:
    """Create docs/fortigateapi/cmdb/firewall/_contents.rst"""
    content_j2 = Path(f"templates/{API_DIR}/app_contents.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(
        api_class=API_CLASS,
        scope=scope,
        app_name=app_name,
        model_names=model_names,
    )
    path: Path = ROOT.joinpath(f"docs/{API_DIR}/{scope}/{app_name}/_contents.rst")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def _create_fortigateapi__scope_app_model(scope: str, app_name: str, model_name: str) -> None:
    """Create docs/fortigateapi/cmdb/firewall/address.rst"""
    content_j2 = Path(f"templates/{API_DIR}/model_class.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(
        package=fortigate_api.__name__,
        api_class=API_CLASS,
        scope=scope,
        app_name=app_name,
        model_name=model_name,
        model_class=h.model_names(scope, app_name, model_name)[1],
        usage=_usage__scope_app_model(scope, app_name, model_name),
    )
    path: Path = ROOT.joinpath(f"docs/{API_DIR}/{scope}/{app_name}/{model_name}.rst")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def _usage__scope_app_model(scope: str, app_name: str, model_name: str) -> str:
    """Get usage example of scope/app/model."""
    path = ROOT.joinpath(f"examples/{scope}/{app_name}/{model_name}.py")
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    return h.rst_code(text)


def create_fortigate(class_name: str) -> None:
    """Create docs/fortigateapi/FortiGate.rst or FortiGateAPI.rst"""
    content_j2 = Path(f"templates/fortigateapi/class_fortigate.j2").read_text(encoding="utf-8")
    text = Template(content_j2).render(
        package=fortigate_api.__name__,
        class_name=class_name,
        usage=_usage__class(class_name),
    )
    path: Path = ROOT.joinpath(f"docs/{API_DIR}/{class_name}.rst")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    logging.info(str(f"Created {path!s}."))


def _usage__class(class_name: str) -> str:
    """Get usage example of FortiGate."""
    file_name = class_name.lower()
    path = ROOT.joinpath(f"examples/{file_name}.py")
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    return h.rst_code(text)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())

    create_index()
    is_json_schema_new = False
    if is_json_schema_new:
        create_rest_api_cmdb_yml()
    create_rest_api_cmdb_rst()
    create_fortigateapi_cmdb()
    create_fortigate(class_name=FortiGate.__name__)
    create_fortigate(class_name=FortiGateAPI.__name__)

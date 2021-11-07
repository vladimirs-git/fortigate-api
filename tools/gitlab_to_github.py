"""prepare files for GitHub"""
import os
import pathlib
import re
import shutil
import logging
import fortigate_api as packet
from fortigate_api.typing_ import IStr
from setup import PACKAGE, PACKAGE_

ROOT = os.path.split(pathlib.Path(__file__).parent.resolve())[0]
VERSION = packet.__version__
GITHUB_URL = f"https://github.com/vladimirs-git/{PACKAGE}"
EMAIL = "vladimir.prusakovs@gmail.com"

README = f"""## Installation
```bash
pip install {packet.__title__}
```

##"""


def valid_project(dirname: str) -> None:
    """Error if dirname is not in path"""
    path = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    dirs = re.split(r"[\\/]", path)
    if not [s for s in dirs if s == dirname]:
        raise ValueError(f"absent {dirname=} in {path=}")


def modify_init() -> None:
    """__init__.py"""
    filepath = os.path.join(ROOT, PACKAGE_, "__init__.py")
    need_replace = [
        ("__email__ =.+?\n", f"__email__ = \"{EMAIL}\"\n"),
        ("__url__ =.+?\n", f"__url__ = \"{GITHUB_URL}\"\n"),
        ("__download_url__ =.+?\n",
         f"__download_url__ = f\"{{__url__}}/archive/refs/tags/{{__version__}}.tar.gz\"\n"),
        ("__project_urls__ =.+?\n", ""),
    ]
    modify_file(filepath, need_replace)


def modify_setup() -> None:
    """setup.py"""
    filepath = os.path.join(ROOT, "setup.py")
    need_replace = [
        (r"\s+project_urls=.+?\n", "\n"),
    ]
    modify_file(filepath, need_replace)


def modify_readme() -> None:
    """README.md"""
    filepath = os.path.join(ROOT, "README.md")
    need_replace = [(r"## Installation.+?##", README)]
    modify_file(filepath, need_replace)


def modify_gitignore():
    """.gitignore"""
    filepath = os.path.join(ROOT, ".gitignore")
    need_replace = [("tools/notes.txt", "tools/")]
    modify_file(filepath, need_replace)


def modify_file(filepath, need_replace, /) -> None:
    """modify file"""
    file_ = pathlib.Path(filepath)
    text = file_.read_text(encoding="utf-8")
    for regex, new in need_replace:
        text = re.sub(regex, new, text, flags=re.DOTALL)
    file_.write_text(text)
    logging.info("modified %s", file_)


def delete_files(files: IStr) -> None:
    """delete files"""
    for filename in files:
        filepath = os.path.join(ROOT, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            logging.info("deleted %s", filepath)


def delete_dirs(dirs: IStr) -> None:
    """delete files"""
    for dirname in dirs:
        path = os.path.join(ROOT, dirname)
        if os.path.exists(path):
            shutil.rmtree(path)
            logging.info("deleted %s", path)


if __name__ == '__main__':
    valid_project(dirname="GitHub")
    modify_init()
    modify_setup()
    modify_readme()
    modify_gitignore()
    delete_files(files=[".gitlab-ci.yml"])
    delete_dirs(dirs=["tests"])

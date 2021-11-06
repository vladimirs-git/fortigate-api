"""prepare files for GitHub"""
import os
import re
import shutil
from setup import PACKAGE, PACKAGE_
from fortigate_api.typing_ import IStr


ROOT = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
PACKAGE_DIR = os.path.join(ROOT, PACKAGE_)

URL = "https://github.com/vladimirs-git"
README_INSTALLATION = f"""## Installation
```bash
pip install {PACKAGE}
```

##"""


def valid_project(dirname: str) -> None:
    """Error if dirname is not in path"""
    path = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
    dirs = re.split(r"[\\/]", path)
    if not [s for s in dirs if s == dirname]:
        raise ValueError(f"absent {dirname=} in {path=}")


def modify_setup() -> None:
    """modify setup.py"""
    filepath = os.path.join(ROOT, "setup.py")
    need_replace = [
        (r"URL =.+?\n", f"URL = \"{URL}\"\n"),
        (r"DOWNLOAD_URL =.+?\n",
         f"DOWNLOAD_URL = f\"{{URL}}/archive/refs/tags/{{VERSION}}.tar.gz\"\n"),
    ]
    modify_file(filepath, need_replace)


def modify_readme() -> None:
    """modify README.md"""
    filepath = os.path.join(ROOT, "README.md")
    need_replace = [(r"## Installation.+?##", README_INSTALLATION)]
    modify_file(filepath, need_replace)


def modify_gitignore():
    """modify .gitignore"""
    filepath = os.path.join(ROOT, ".gitignore")
    need_replace = [("tools/notes.txt", "tools/")]
    modify_file(filepath, need_replace)


def modify_file(filepath, need_replace, /) -> None:
    """modify file"""
    with open(filepath, mode="r+") as f:
        text = f.read()
        for regex, new in need_replace:
            text = re.sub(regex, new, text, flags=re.DOTALL)
        f.seek(0)
        f.write(text)
        f.truncate()


def delete_files(files: IStr) -> None:
    """delete files"""
    for filename in files:
        filepath = os.path.join(ROOT, filename)
        if os.path.exists(filepath):
            os.remove(filepath)


def delete_dirs(dirs: IStr) -> None:
    """delete files"""
    for dirname in dirs:
        path = os.path.join(ROOT, dirname)
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    valid_project(dirname="GitHub")
    modify_setup()
    modify_readme()
    modify_gitignore()
    delete_files(files=[".gitlab-ci.yml"])
    delete_dirs(dirs=["tests"])

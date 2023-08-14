import shutil
import sys
from pathlib import Path

from staticjinja import Site
from yaml import Loader, load

import sass


def load_page_data():
    yaml = Path("./data").glob("*.yaml")
    return {
        file_path.stem: load(file_path.read_text(), Loader=Loader) for file_path in yaml
    }


def clean_buildpath(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)


def main():
    try:
        build_dir_str = sys.argv[1]
    except IndexError:
        build_dir_str = "output"

    buildpath = Path(build_dir_str)
    clean_buildpath(buildpath)

    site = Site.make_site()
    site.outpath = buildpath
    site.contexts = [(".*.html", load_page_data)]
    # disable automatic reloading
    site.render(use_reloader=False)

    # copy the static folder
    shutil.copytree("static", buildpath / "static")

    # compile sass to css
    sass.compile(dirname=("sass", buildpath / "static/css"))


if __name__ == "__main__":
    main()

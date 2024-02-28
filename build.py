import shutil
import sys
from functools import partial
from pathlib import Path

from staticjinja import Site
from yaml import Loader, load

import sass


def load_page_data(template, /, *, base_url=None):
    context_objects = Path("./data").glob("*.yaml")
    context_mapping = {
        file_path.stem: load(file_path.read_text(), Loader=Loader)
        for file_path in context_objects
    }
    if base_url is not None:
        context_mapping["base"]["base_url"] = base_url
    return context_mapping


def clean_buildpath(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)


def main():
    try:
        build_dir_str = sys.argv[1]
    except IndexError:
        build_dir_str = "output"

    try:
        custom_domain_cli_arg = sys.argv[2]
    except IndexError:
        custom_domain_cli_arg = None

    buildpath = Path(build_dir_str)
    clean_buildpath(buildpath)

    site = Site.make_site()
    site.outpath = buildpath

    load_page_data_callable = partial(load_page_data, base_url=custom_domain_cli_arg)
    site.contexts = [(".*.html", load_page_data_callable)]
    # disable automatic reloading
    site.render(use_reloader=False)

    # copy the static folder
    shutil.copytree("static", buildpath / "static")

    # compile sass to css
    sass.compile(dirname=("sass", buildpath / "static/css"))


if __name__ == "__main__":
    main()

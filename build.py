import shutil
import sass
import glob

from pathlib import Path
from staticjinja import Site
from yaml import load, Loader

def data():
    data_dict = {}
    yaml = glob.glob("data/*.yaml")

    for file_path in yaml:
        file_name = file_path.split("/")[-1].split(".")[0]
        with open(file_path, "r") as file:
            data_dict[file_name] = load(file, Loader=Loader)

    return data_dict

buildpath = Path('output')

if buildpath.exists() and buildpath.is_dir():
    shutil.rmtree(buildpath)

if __name__ == "__main__":

    site = Site.make_site()
    site.outpath=buildpath
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)

    # copy the static folder
    shutil.copytree('static', buildpath / 'static')

    # compile sass to css
    sass.compile(dirname=('sass', buildpath / 'static/css'))

from copystatic import copy_files
from gencontent import generate_page


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    copy_files(dir_path_static, dir_path_public)
    generate_page("./content/index.md", './template.html', './public/index.html')


main()

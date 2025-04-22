from copystatic import copy_files
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"


def main():
    copy_files(dir_path_static, dir_path_public)
    generate_pages_recursive("./content", './template.html', './public')


main()

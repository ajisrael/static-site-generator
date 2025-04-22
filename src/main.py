import sys
from copystatic import copy_files
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"


def main():
    basepath = '/'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    copy_files(dir_path_static, dir_path_public)
    generate_pages_recursive("./content", "./template.html", dir_path_public, basepath)


main()

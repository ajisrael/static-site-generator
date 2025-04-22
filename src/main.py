from copystatic import copy_files

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    copy_files(dir_path_static, dir_path_public)


main()

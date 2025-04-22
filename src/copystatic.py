import os
import shutil


def copy_files(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Check paths are valid directories
    if not os.path.isdir(source_dir_path):
        raise ValueError(f"Invalid source_dir_path path: {source_dir_path}\nMust be to a directory")

    # Delete contents of dest_dir_pathination directory
    if len(os.listdir(dest_dir_path)) > 0:
        print(f"Clearing contents of {dest_dir_path}")
        shutil.rmtree(dest_dir_path)
        os.mkdir(dest_dir_path)

    # Copy contents of source_dir_path directory to dest_dir_pathination
    items = os.listdir(source_dir_path)
    for item in items:
        source_dir_path_path = os.path.join(source_dir_path, item)
        dest_dir_path_path = os.path.join(dest_dir_path, item) 

        if os.path.isdir(source_dir_path_path):
            print(f"Making new directory {dest_dir_path_path}")
            os.mkdir(dest_dir_path_path)
            copy_files(source_dir_path_path, dest_dir_path_path)
        else:
            print(f"Copying {item} to {dest_dir_path}")
            shutil.copy(source_dir_path_path, dest_dir_path_path)

__author__ = 'wenychan'


def copy_file():
    import shutil
    import os

    for sample_file in os.listdir("."):
        if os.path.splitext(sample_file)[1] == ".py":
            print sample_file
            shutil.copy(sample_file, os.path.join("backup", sample_file))


def copy_remove_directory_tree():
    import shutil
    import os

    SOURCE = "samples"
    BACKUP = "samples-bak"

    # create a backup directory
    shutil.copytree(SOURCE, BACKUP)
    print os.listdir(BACKUP)

    # remove it
    shutil.rmtree(BACKUP)
    print os.listdir(BACKUP)
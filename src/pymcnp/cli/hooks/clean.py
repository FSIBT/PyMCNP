import shutil
import pathlib


def main(path):
    path = pathlib.Path(path)

    for file_or_dir in path.rglob('*'):
        shutil.rmtree(file_or_dir)

    path.rmdir()

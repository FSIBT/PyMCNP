import pathlib


def main(path, command):
    path = pathlib.Path(path)

    for file_or_dir in path.rglob('*'):
        if file_or_dir.is_file():
            file_or_dir.unlink()
        else:
            file_or_dir.rmdir()

    path.rmdir()

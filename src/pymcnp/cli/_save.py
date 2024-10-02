"""
'_save'
"""


import os.path

from ..files import inp


class Save:
    """
    'Save'
    """

    PYMCNP_DIR = ".pymcnp/"
    PYMCNP_SAVE_FILE = PYMCNP_DIR + "pymcnp-save.txt"

    @staticmethod
    def get_save() -> dict:
        """
        'get_save'
        """

        with open(Save.PYMCNP_SAVE_FILE) as file:
            lines = file.readlines()

        inpts = {}
        for line in lines:
            if not line:
                continue

            alias, path = line.strip().split(" ")

            if not os.path.isfile(path):
                continue

            inpts[alias] = (path, inp.Inp.from_mcnp_file(path))

        return inpts

    @staticmethod
    def set_save(inpts) -> None:
        """
        'set_save'
        """

        output = ""
        for alias, (path, inpt) in inpts.items():
            output += f"{alias} {path}\n"

        with open(Save.PYMCNP_SAVE_FILE, "w") as file:
            file.write(output)

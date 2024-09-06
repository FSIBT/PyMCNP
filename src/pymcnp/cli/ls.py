"""
'ls' contains functions for printing INP object information.
"""


import sys


from typing import Self

from ..files import inp
from . import _save
from . import _io


class Ls:
    """
    'Ls'
    """

    def __init__(self, inpt: inp.Inp) -> Self:
        """
        ``__init__`` initializes ``Ls``.
        """

        self.inpt = inpt

    @staticmethod
    def list_cells(self) -> str:
        """
        'list_cells' outputs strings of INP object cell information.

        Returns:
            out : String of INP object cell information.
        """

        out = "\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^25.25}\x1b[24m\n"
        out = out.format("NUMBER", "MATERIAL", "DENSITY", "GEOMETRY")

        for cell in inpt.cells._cards.values():
            out += f"{cell.number:<12} {cell.material:<12} {cell.density if cell.density else '':<12} "
            out += f"{cell.geometry.to_mcnp()}\n"

        return out

    @staticmethod
    def list_surfaces(self) -> str:
        """
        'list_surfaces' outputs strings of INP object surface information.

        Returns:
            out : String of INP object surface information.
        """

        out = "\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m\n"
        out = out.format("NUMBER", "MNEMONIC", "TRANSFORM")

        for surface in inpt.surfaces._cards.values():
            out += f"{surface.number:<12} {surface.mnemonic:<12} {surface.transfrom if surface.transform else '':<12}\n"

        return out

    @staticmethod
    def list_data(self) -> str:
        """
        'list_data' outputs strings of INP object datum information.

        Returns:
            out : String of INP object datum information.
        """

        out = "\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m\n".format("MNEMONIC", "NUMBER")

        for datum in inpt.data._cards.values():
            out += f"{datum.mnemonic:<12.12} {datum.number if datum.number else '':<12.12}\n"

        return out

    @staticmethod
    def list_inp(self) -> str:
        """
        'list_inp' outputs strings of all INP object information.

        Returns:
            out : String of all INP object information.
        """

        return "\n" + Ls.list_cells() + "\n" + Ls.list_surfaces() + "\n" + Ls.list_data()


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    'main' runs the command line for printing INP object information.

    Parameters:
        argv (list[str]): Arguments list.
    """

    inpts = _save.Save.get_save()

    match argv[0] if argv else None:
        case arg if arg is not None and arg[0] != "-":
            if argv[0] not in inpts:
                _io.error(_io.ERROR_ALIAS_NOT_FOUND)

            try:
                match argv[1] if argv[1:] else None:
                    case "-c" | "--cells":
                        print(Ls.list_cells(inpts[argv[0]][1]), end="")
                    case "-s" | "--surfaces":
                        print(Ls.list_surfaces(inpts[argv[0]][1]), end="")
                    case "-d" | "--data":
                        print(Ls.list_data(inpts[argv[0]][1]), end="")
                    case "-a" | "--arguments":
                        print(inpts[argv[0]][1].to_arguments())
                    case None:
                        print(Ls.list_inp(inpts[argv[0]][1]))
                    case _:
                        _io.error(_io.ERROR_UNRECOGNIZED_OPTION)
            except SyntaxError:
                _io.error("INP SyntaxError")
            except ValueError:
                _io.error("INP ValueError")

        case "-a" | "--all":
            for alias, value in inpts.items():
                path, inpt = value
                print(f"\n\x1b[4mOBJECT:\x1b[24m {alias}" + "\n" + Ls.list_inp(inpt))

        case None:
            out = "\x1b[4m{:^25.25}\x1b[24m \x1b[4m{:^51.51}\x1b[24m \x1b[4m{:^51.51}\x1b[24m"
            print(out.format("NAME", "TITLE", "OTHER"))
            for name, value in inpts.items():
                path, inpt = value
                print(f"{name:<25.25} {inpt.title:<51.51} {repr(inpt.other):<51.51}")

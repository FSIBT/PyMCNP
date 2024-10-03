"""
``ls`` provides utilities for listing MCNP information.

``ls`` contains the procedures for executing the ``pymcnp ls`` command and
utilities for listing MCNP information.
"""


import sys

import docopt

from .. import files
from . import _save
from . import _io


class Ls:
    """
    ``Ls``
    """

    def __init__(self, inp: files.inp.Inp):
        """
        ``__init__`` initializes ``Ls``.
        """

        if inp is None:
            raise ValueError

        self.inp: final[files.inp.Inp] = inp

    def list_cells(self) -> str:
        """
        ``list_cells`` tabulates INP object cell card information.

        Returns:
            String of INP object cell information.
        """

        out = "\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^25.25}\x1b[24m\n"
        out = out.format("NUMBER", "MATERIAL", "DENSITY", "GEOMETRY")

        for cell in self.inp.cells._cards.values():
            out += f"{cell.number:<12} {cell.material:<12} {cell.density if cell.density else '':<12} {cell.geometry.to_mcnp():<25}\n"

        return out

    def list_surfaces(self) -> str:
        """
        ``list_surfaces`` tabulates INP object surface card information.

        Returns:
            String of INP object surface information.
        """

        out = "\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m\n"
        out = out.format("NUMBER", "MNEMONIC", "TRANSFORM")

        for surface in self.inp.surfaces._cards.values():
            out += f"{surface.number:<12} {surface.mnemonic:<12} {surface.transfrom if surface.transform else '':<12}\n"

        return out

    def list_data(self) -> str:
        """
        ``list_data`` tabulates INP object data card information.

        Returns:
            String of INP object data information.
        """

        out = "\x1b[4m{:^12.12}\x1b[24m\n".format("MNEMONIC")

        for datum in self.inp.data._cards.values():
            out += f"{datum.mnemonic:<12.12}\n"

        return out

    @staticmethod
    def list_inps(inps: tuple[str, files.inp.Inp]) -> str:
        """
        ``list_inps`` tabulates INP objects.

        Returns:
            String of INP object inp information.
        """

        out = "\x1b[4m{:^25.25}\x1b[24m \x1b[4m{:^51.51}\x1b[24m \x1b[4m{:^51.51}\x1b[24m\n".format("NAME", "TITLE", "OTHER")
        for alias, inp in list(inps):
            out += f"{alias:<25.25} {inp.title:<51.51} {repr(inp.other):<51.51}\n"

        return out


PYMCNP_LS_DOC = f"""
Usage:
    pymcnp ls [(<alias> (--cells|--surfaces|--data)...)]

Options:
    -f --file      List from INP file.
    -c --cells     List aliased INP cell cards.
    -s --surfaces  List aliased INP surface cards.
    -d --data      List aliased INP data cards.
"""


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    ``main`` executes the ``pymcnp ls`` command.

    ``main`` processes the given command line arguments, and it lists, prints,
    and tabulates PyMCNP object contents.

    Parameters:
        argv: Tokenized list of CLI arguments.
    """

    args = docopt.docopt(PYMCNP_LS_DOC, argv=argv)
    aliases = _save.Save.get_save()

    if args["<alias>"]:
        inp = aliases[args["<alias>"]][1]

    if args["<alias>"]:
        # Listing aliased PyMCNP object content.
        ls = Ls(inp)

        if args["--cells"]:
            print(ls.list_cells())
        if args["--surfaces"]:
            print(ls.list_surfaces())
        if args["--data"]:
            print(ls.list_data())
    else:
        # Listing all aliased PyMCNP objects.
        print(Ls.list_inps([(alias, inp) for alias, (path, inp) in aliases.items()]))

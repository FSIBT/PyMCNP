"""
``ls`` provides utilities for listing MCNP information.

``ls`` contains the procedures for executing the ``pymcnp ls`` command and
utilities for listing MCNP information.
"""

import sys
from typing import Final

import docopt

from ..files import inp
from . import _state


class Ls:
    """
    ``Ls``
    """

    def __init__(self, inpt: inp.Inp):
        """
        ``__init__`` initializes ``Ls``.
        """

        if inpt is None:
            raise ValueError

        self.inpt: Final[inp.Inp] = inpt

    def list_cells(self) -> str:
        """
        ``list_cells`` tabulates INP object cell card information.

        Returns:
            String of INP object cell information.
        """

        out = (
            '\x1b[4m{:^12.12}\x1b[24m ' * 3 + '\x1b[4m{:^25.25}\x1b[24m \x1b[4m{:^25.25}\x1b[24m\n'
        )
        out = out.format('NUMBER', 'MATERIAL', 'DENSITY', 'GEOMETRY', 'OPTIONS')

        for cell in self.inpt.cells._cards.values():
            out += (
                f"{cell.number.to_mcnp():<12} "
                f"{cell.material.to_mcnp():<12} "
                f"{cell.density.to_mcnp() if cell.density.to_mcnp() else '':<12} "
                f"{cell.geometry.to_mcnp():<25} {'':<25}\n"
            )

        return out

    def list_surfaces(self) -> str:
        """
        ``list_surfaces`` tabulates INP object surface card information.

        Returns:
            String of INP object surface information.
        """

        out = '\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^51.51}\x1b[24m\n'
        out = out.format('NUMBER', 'MNEMONIC', 'TRANSFORM', 'PARAMETERS')

        for surface in self.inpt.surfaces._cards.values():
            out += (
                f"{surface.number.to_mcnp():<12} "
                f"{surface.mnemonic.to_mcnp():<12} "
                f"{surface.transfrom.to_mcnp() if surface.transform else '':<12} "
                f"{'':<51}\n"
            )

        return out

    def list_data(self) -> str:
        """
        ``list_data`` tabulates INP object data card information.

        Returns:
            String of INP object data information.
        """

        out = '\x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^12.12}\x1b[24m \x1b[4m{:^51.51}\x1b[24m\n'
        out = out.format('NUMBER', 'SUFFIX', 'DESIGNATOR', 'PARAMETERS')

        for datum in self.inpt.data._cards.values():
            out += (
                f"{datum.mnemonic:<12.12} "
                f"{datum.suffix.to_mcnp() if hasattr(datum, 'suffix') else '':<12} "
                f"{datum.designator.to_mcnp() if hasattr(datum, 'designator') else '':<12} "
                f"{'':<51.51}\n"
            )

        return out

    @staticmethod
    def list_inpts(inpts: tuple[str, inp.Inp]) -> str:
        """
        ``list_inpts`` tabulates INP objects.

        Returns:
            String of INP object inpt information.
        """

        out = '\x1b[4m{:^25.25}\x1b[24m \x1b[4m{:^51.51}\x1b[24m \x1b[4m{:^51.51}\x1b[24m\n'.format(
            'NAME', 'TITLE', 'OTHER'
        )
        for alias, inpt in list(inpts):
            out += f'{alias:<25.25} {inpt.title:<51.51} {repr(inpt.other):<51.51}\n'

        return out


PYMCNP_LS_DOC = """
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

    if args['<alias>']:
        # Listing aliased PyMCNP object content.

        try:
            filename = _state.table.access(args['<alias>'])
        except ValueError:
            print('NOPE!')
            exit(1)

        ls = Ls(inp.Inp.from_mcnp_file(filename))

        if args['--cells']:
            print(ls.list_cells())
        if args['--surfaces']:
            print(ls.list_surfaces())
        if args['--data']:
            print(ls.list_data())
    else:
        # Listing all aliased PyMCNP objects.
        print(
            Ls.list_inpts([(alias, inp.Inp.from_mcnp_file(path)) for alias, path in _state.table])
        )

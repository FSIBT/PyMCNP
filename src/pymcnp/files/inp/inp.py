"""
``inp`` contains the class representing INP files.

``inp`` packages the ``Inp`` class, providing an object-oriented, importable
interface for INP files.
"""

from pathlib import Path
import sys
from typing import Final

from rich import print

from . import cells
from . import surfaces
from . import data
from ..utils import _parser
from ..utils import errors


class Inp:
    """
    ``Inp`` represents INP files.

    ``Inp`` implements INP files as a Python class. Its attributes store
    INP blocks, and its methods provide entry points and endpoints for working
    with INP. It represents the INP file syntax element.

    Attributes:
        message: INP message.
        title: INP title.
        cells: INP cell card block.
        surfaces: INP surface card block.
        data: INP data card block.
        other: INP other block.
    """

    def __init__(
        self,
        title: str,
        cells: cells.Cells,
        surfaces: surfaces.Surfaces,
        data: data.Data,
        message: str = '',
        other: str = '',
    ):
        """
        ``__init__`` initializes ``Inp``.
        """

        if message is None:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.INVALID_INP_MESSAGE)

        if title is None or not len(title) < 80:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_TITLE)

        if cells is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_CELLS)

        if surfaces is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_SURFACES)

        if data is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if other is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_OTHER)

        self.message: Final[str] = message
        self.title: Final[str] = title
        self.cells: Final[cells.Cells] = cells
        self.surfaces: Final[surfaces.Surfaces] = surfaces
        self.data: Final[data.Data] = data
        self.other: Final[str] = other

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Inp`` objects from INP.

        ``from_mcnp`` constructs instances of ``Inp`` from INP source strings,
        so it operates as a class constructor method and INP parser.

        Parameters:
            source: Complete INP source string.

        Returns:
            ``Inp`` object.
        """

        source = _parser.Preprocessor.process_inp(source)

        lines = _parser.Parser(
            source.split('\n'),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_INP),
        )

        # Processing Message & Title
        message = lines.popl()[:9] if lines.peekl()[:9] == 'message:' else ''
        title = lines.popl()

        # Processing Cell Cards
        cell_source = ''
        while lines.peekl() != '':
            cell_source += lines.popl() + '\n'
        cell_block = cells.Cells.from_mcnp(cell_source)

        lines.popl()

        # Processing Surface Cards
        surface_source = ''
        while lines and lines.peekl() != '':
            surface_source += lines.popl() + '\n'
        surface_block = surfaces.Surfaces.from_mcnp(surface_source)

        lines.popl()

        # Processing Datum Cards
        data_source = ''
        while lines and lines.peekl() != '':
            data_source += lines.popl() + '\n'

        datum_block = data.Data.from_mcnp(data_source)

        other = ''
        while lines:
            other += lines.popl()

        return Inp(title, cell_block, surface_block, datum_block, message=message, other=other)

    @staticmethod
    def from_mcnp_file(filename: str | Path):
        """
        ``from_mcnp_file`` generates ``Inp`` objects from INP files.

        ``from_mcnp_file`` constructs instances of ``Inp`` from INP files,
        so it operates as a class constructor method and INP parser.

        Parameters:
            filename: Name of file to parse.

        Returns:
            ``Inp`` object.
        """

        filename = Path(filename)
        source = filename.read_text()

        return Inp.from_mcnp(source)

    def to_mcnp(self, comments: bool = True) -> str:
        """
        ``to_mcnp`` generates INP from ``Inp`` objects.

        ``to_mcnp`` creates INP source string from ``INP`` objects, so it
        provides an MCNP endpoint.

        Returns:
            INP string for ``Inp`` object.
        """

        # Appending Message
        source = self.message + '\n' if self.message else ''

        # Appending Title
        source += self.title + '\n'

        # Appending Blocks
        if comments:
            source += 'c ============================================================\n'
            source += 'c                        cell definitions\n'
            source += 'c ============================================================\n'
        source += self.cells.to_mcnp() + '\n'

        if comments:
            source += 'c ============================================================\n'
            source += 'c                        surface definitions\n'
            source += 'c ============================================================\n'
        source += self.surfaces.to_mcnp() + '\n'
        source += self.data.to_mcnp() + '\n'

        return source

    def to_mcnp_file(self, filename: str | Path) -> int:
        """
        ``to_mcnp`` generates INP from ``Inp`` objects.

        ``to_mcnp`` creates INP source string from ``INp`` objects, so it
        provides an MCNP endpoint.

        Parameters:
            filename: Name of file to write INP string for ``Inp`` object.

        Returns:
            Number of bytes written.
        """

        filename = Path(filename)
        filename.write_text(self.to_mcnp())

        return 0

    def to_arguments(self) -> dict:
        """
        ``to_arguments`` makes dictionaries from ``Inp`` objects.

        ``to_arguments`` creates Python dictionaries from ``Inp`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Inp`` object.
        """

        return {
            'message': self.message,
            'title': self.title,
            'cells': self.cells.to_arguments(),
            'surfaces': self.surfaces.to_arguments(),
            'data': self.data.to_arguments(),
            'other': self.other,
        }

    def __str__(self):
        return self.to_mcnp()


def read_input(filename: Path | str) -> Inp:
    filename = Path(filename)

    if not filename.is_file():
        print(f'[red]ERROR[/] Input file {filename} does not exists.')
        sys.exit(1)

    return Inp.from_mcnp_file(filename)

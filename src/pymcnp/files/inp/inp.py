"""
``inp`` contains the class representing INP files.

``inp`` packages the ``Inp`` class, providing an object-oriented, importable
interface for INP files.
"""


from . import cells
from . import surfaces
from . import data
from .._utils import parser
from .._utils import errors


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

    def __init__(self):
        """
        '__init__' initializes 'Inp'.
        """

        self.message: str = None
        self.title: str = None
        self.cells: cells.Cells = Cells()
        self.surfaces: surfaces.Surfaces = Surfaces()
        self.data: data.Data = Data()
        self.other: str = None

    def set_message(self, message: str) -> None:
        """
        ``set_message`` stores INP message blocks.

        ``set_message`` checks given arguments before assigning the given
        value to ``Inp.message``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            message: INP message block.

        Raises:
            MCNPSemanticError: INVALID_INP_MESSAGE.
        """

        if message is None or not message[:9] == "message:":
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.INVALID_INP_MESSAGE)

        self.message = message

    def set_title(self, title: str) -> None:
        """
        ``set_title`` stores INP titles.

        ``set_title`` checks given arguments before assigning the given
        value to ``Inp.title``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            title: INP title.

        Raises:
            MCNPSemanticError: INVALID_INP_TITLE.
        """

        if title is None or not len(title) < 80:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_TITLE)

        self.title = title

    def set_cells(self, cells: cells.Cells) -> None:
        """
        ``set_cells`` stores INP cell card blocks.

        ``set_cells`` checks given arguments before assigning the given
        value to ``Inp.cells``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            cells: INP cell card block.

        Raises:
            MCNPSemanticError: INVALID_INP_CELLS.
        """

        if cells is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_CELLS)

        self.cells = cells

    def set_surfaces(self, surfaces: surfaces.Surfaces) -> None:
        """
        ``set_surfaces`` stores INP surface card blocks.

        ``set_surfaces`` checks given arguments before assigning the given
        value to ``Inp.surfaces``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            surfaces: INP surface card block.

        Raises:
            MCNPSemanticError: INVALID_INP_SURFACES.
        """

        if surfaces is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_SURFACES)

        self.surfaces = surfaces

    def set_data(self, data: data.Data) -> None:
        """
        ``set_data`` stores INP data card blocks.

        ``set_data`` checks given arguments before assigning the given
        value to ``Inp.data``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            data: INP data card block.

        Raises:
            MCNPSemanticError: INVALID_INP_DATA.
        """

        if data is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        self.data = data

    def set_other(self, other: str) -> None:
        """
        ``set_other`` stores INP other blocks.

        ``set_other`` checks given arguments before assigning the given
        value to ``Inp.other``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            data: INP other block.

        Raises:
            MCNPSemanticError: INVALID_INP_OTHER.
        """

        if other is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_OTHER)

        self.other = other

    @classmethod
    def from_mcnp(cls, source: str):
        """
        ``from_mcnp`` generates ``Inp`` objects from INP.

        ``from_mcnp`` constructs instances of ``Inp`` from INP source strings,
        so it operates as a class constructor method and INP parser.

        Parameters:
            source: Complete INP source string.

        Returns:
            ``Inp`` object.
        """

        inp = cls()

        source = parser.Preprocessor.process_inp(source)
        lines = parser.Parser(source.split("\n"), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_INP))

        # Processing Message Block
        if lines.peekl()[:9] == "message:":
            inp.set_message(lines.popl())

        # Processing Title
        inp.set_title(lines.popl())

        # Processing Cell Cards
        index = list(lines.deque).index("")
        cell_lines = "\n".join(lines.popl() for _ in range(0, index))
        inp.set_cells(cells.Cells.from_mcnp(cell_lines))

        lines.popl()

        # Processing Surface Cards
        index = list(lines.deque).index("")
        surface_lines = "\n".join(lines.popl() for _ in range(0, index))
        inp.set_surfaces(surfaces.Surfaces.from_mcnp(surface_lines))

        lines.popl()

        # Processing Datum Cards
        index = list(lines.deque).index("") if "" in lines.deque else len(lines.deque)
        datum_lines = "\n".join(lines.popl() for _ in range(0, index))
        inp.set_data(data.Data.from_mcnp(datum_lines))

        other = ""
        while lines:
            other += lines.popl()

        inp.set_other(other)

        return inp

    @classmethod
    def from_mcnp_file(cls, filename: str):
        """
        ``from_mcnp_file`` generates ``Inp`` objects from INP files.

        ``from_mcnp_file`` constructs instances of ``Inp`` from INP files,
        so it operates as a class constructor method and INP parser.

        Parameters:
            filename: Name of file to parse.

        Returns:
            ``Inp`` object.
        """

        source = ""
        with open(filename) as file:
            source = "".join(file.readlines())

        return cls.from_mcnp(source)

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Inp`` objects.

        ``to_mcnp`` creates INP source string from ``INp`` objects, so it
        provides an MCNP endpoint.

        Returns:
            INP string for ``Inp`` object.
        """

        # Appending Message
        source = self.message + "\n" if self.message else ""

        # Appending Title
        source += self.title + "\n"

        # Appending Blocks
        source += Cells.to_mcnp(self.cells) + "\n"
        source += Surfaces.to_mcnp(self.surfaces) + "\n"
        source += Data.to_mcnp(self.data) + "\n"

        return source

    def to_mcnp_file(self, filename: str) -> int:
        """
        ``to_mcnp`` generates INP from ``Inp`` objects.

        ``to_mcnp`` creates INP source string from ``INp`` objects, so it
        provides an MCNP endpoint.

        Parameters:
            filename: Name of file to write INP string for ``Inp`` object.

        Returns:
            Number of bytes written.
        """

        with open(filename, "w") as file:
            return file.write(self.to_mcnp())

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
            "message": self.message,
            "title": self.title,
            "cells": self.cells.to_arguments(),
            "surfaces": self.surfaces.to_arguments(),
            "data": self.data.to_arguments(),
            "other": self.other,
        }

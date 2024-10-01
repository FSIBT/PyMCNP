"""
``inp`` contains the class representing INP files.

``inp`` packages the ``Inp`` class, providing an object-oriented, importable
interface for INP files.
"""


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
        self, title: str, cells: cells.Cells, surfaces: surfaces.Surfaces, data: data.Data, message: str = "", other: str = ""
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

        self.message: final[str] = message
        self.title: final[str] = title
        self.cells: final[cells.Cells] = cells
        self.surfaces: final[surfaces.Surfaces] = surfaces
        self.data: final[data.Data] = data
        self.other: final[str] = other

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

        source = _parser.Preprocessor.process_inp(source, hasComments=False)
        lines = _parser.Parser(source.split("\n"), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_INP))

        # Processing Message & Title
        message = lines.popl()[:9] if lines.peekl()[:9] == "message:" else ""
        title = lines.popl()

        # Processing Cell Cards
        index = list(lines.deque).index("")
        cell_source = "\n".join(lines.popl() for _ in range(0, index))
        cell_block = cells.Cells.from_mcnp(cell_source)

        lines.popl()

        # Processing Surface Cards
        index = list(lines.deque).index("")
        surface_source = "\n".join(lines.popl() for _ in range(0, index))
        surface_block = surfaces.Surfaces.from_mcnp(surface_source)

        lines.popl()

        # Processing Datum Cards
        index = list(lines.deque).index("") if "" in lines.deque else len(lines.deque)
        datum_source = "\n".join(lines.popl() for _ in range(0, index))
        datum_block = data.Data.from_mcnp(datum_source)

        other = ""
        while lines:
            other += lines.popl()

        return Inp(title, cell_block, surface_block, datum_block, message=message, other=other)

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

        ``to_mcnp`` creates INP source string from ``INP`` objects, so it
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

"""
Contains classes representing PTRAC file.
"""

import pathlib
from typing import Generator

from .header import Header
from .history import History
from ..utils import _object


class Ptrac(_object.PyMcnpFileObject):
    """
    Represents PTRAC files.

    ``Ptrac`` implements ``_object.PyMcnpFileObject``.

    Attributes:
        header: PTRAC header.
        history: PTRAC history.
    """

    def __init__(self, header: Header, histories: Generator[History, None, None]):
        """
        Initializes ``Ptrac``.

        Parameters:
            header: PTRAC header.
            history: PTRAC history.
        """

        self.header: Header = header
        self.histories: Generator[History, None, None] = histories

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ptrac`` objects from PTRAC.

        ``from_mcnp`` translates from PTRAC to PyMCNP; it parses PTRAC.

        Parameters:
            source: PTRAC for ``Ptrac``.

        Returns:
            ``Ptrac`` object.
        """

        # Processing Header
        head, lines = Header.from_mcnp(source)

        # Processing History
        def histories(lines):
            while lines:
                history, lines = History.from_mcnp(lines, head)
                yield history
            return

        return Ptrac(head, histories(lines))

    def to_mcnp(self):
        """
        Generates PTRAC from ``Ptrac`` objects.

        ``to_mcnp`` translates from PTRAC to PyMCNP.

        Returns:
            INP for ``Ptrac``.
        """

        assert False, 'NotImplemented'

    @staticmethod
    def from_mcnp_file(filename: str | pathlib.Path):
        """
        Generates ``Ptrac`` objects from MCNP files.

        ``from_mcnp_file`` translates from MCNP files to PyMCNP.

        Parameters:
            filename: MCNP file path.

        Returns:
            ``Ptrac`` object.
        """

        filename = pathlib.Path(filename)
        source = filename.read_text()

        return Ptrac.from_mcnp(source)

    def to_mcnp_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP files from ``Ptrac`` objects.

        ``to_mcnp_file`` translates from PyMCNP to MCNP files.

        Parameters:
            filename: new MCNP file path.
        """

        assert False, 'NotImplemented'

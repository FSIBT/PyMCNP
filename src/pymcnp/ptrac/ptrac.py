"""
Contains classes representing PTRAC file.
"""

import pathlib
from typing import Generator

from .block_header import Header
from .block_history import History
from ..utils import _object


class Ptrac(_object.McnpFile_):
    """
    Represents PTRAC files.

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

        Returns:
            ``Ptrac``.
        """

        self.header: Header = header
        self.histories: Generator[History, None, None] = histories

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ptrac`` from PTRAC.

        Parameters:
            source: PTRAC for ``Ptrac``.

        Returns:
            ``Ptrac``.
        """

        header, lines = Header.from_mcnp(source)

        def histories(lines):
            while histories:
                history, lines = History.from_mcnp(lines, header)
                yield history
            return

        histories = histories(lines)

        return Ptrac(header, histories)

    def to_mcnp(self):
        """
        Generates PTRAC from ``Ptrac``.

        Returns:
            INP for ``Ptrac``.
        """

        assert False, "I'm working on it!"

    @staticmethod
    def from_mcnp_file(filename: str | pathlib.Path):
        """
        Generates ``Ptrac`` from MCNP files.

        Parameters:
            filename: MCNP file path.

        Returns:
            ``Ptrac``.
        """

        filename = pathlib.Path(filename)

        if not filename.is_file():
            raise Exception

        source = filename.read_text()

        return Ptrac.from_mcnp(source)

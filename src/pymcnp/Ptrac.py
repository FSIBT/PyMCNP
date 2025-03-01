"""
Contains classes representing PTRAC file.
"""

from typing import Generator

from . import ptrac
from .utils import errors
from .utils import _object


class Ptrac(_object.McnpFile_):
    """
    Represents PTRAC files.

    Attributes:
        header: PTRAC header.
        history: PTRAC history.
    """

    def __init__(self, header: ptrac.Header, histories: Generator[ptrac.History, None, None]):
        """
        Initializes ``Ptrac``.

        Parameters:
            header: PTRAC header.
            history: PTRAC history.

        Returns:
            ``Ptrac``.
        """

        if header is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_PTRAC_HEADER)

        if histories is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_PTRAC_HISTORY)

        self.header: ptrac.Header = header
        self.histories: Generator[ptrac.History, None, None] = histories

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ptrac`` from PTRAC.

        Parameters:
            source: PTRAC for ``Ptrac``.

        Returns:
            ``Ptrac``.
        """

        header, lines = ptrac.Header.from_mcnp(source)

        def histories(lines):
            while histories:
                history, lines = ptrac.History.from_mcnp(lines, header)
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

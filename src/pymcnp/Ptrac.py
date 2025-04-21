import typing

from . import ptrac
from .utils import errors
from .utils import _object


class Ptrac(_object.McnpFile_):
    """
    Represents PTRAC files.

    Attributes:
        header: PTRAC header.
        histories: PTRAC histories.
    """

    def __init__(
        self, header: ptrac.Header, histories: typing.Generator[ptrac.History, None, None]
    ):
        """
        Initializes ``Ptrac``.

        Parameters:
            header: PTRAC header.
            histories: PTRAC histories.

        Returns:
            ``Ptrac``.

        Raises:
            PtracError: SEMANTICS_PTRAC.
        """

        if header is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_PTRAC)

        if histories is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_PTRAC)

        self.header: typing.Final[ptrac.Header] = header
        self.histories: typing.Final[typing.Generator[ptrac.History, None, None]] = histories

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
            while lines:
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

import re
import typing

from . import ptrac
from .utils import types
from .utils import errors
from .utils import _object


class Ptrac(_object.McnpFile):
    """
    Represents PTRAC files.

    Attributes:
        header: PTRAC header.
        histories: PTRAC histories.
    """

    _REGEX = re.compile(rf'\A({ptrac.Header._REGEX.pattern[2:-2]})((?:{ptrac.History._REGEX.pattern[2:-2]})+)\Z')

    def __init__(self, header: ptrac.Header, histories: typing.Generator[ptrac.History, None, None]):
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
            raise errors.PtracError(errors.PtracCode.SEMANTICS_PTRAC, header)

        if histories is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_PTRAC, histories)

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

        Raises:
            PtracError: SYNTAX_PTRAC.
        """

        tokens = Ptrac._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_PTRAC, source)

        header = ptrac.Header.from_mcnp(tokens[1])
        histories = types.Tuple(ptrac.History.from_mcnp(match[0], header) for match in re.finditer(ptrac.History._REGEX.pattern[2:-2], tokens[10]))

        return Ptrac(header, histories)

    def to_mcnp(self):
        """
        Generates PTRAC from ``Ptrac``.

        Returns:
            PTRAC for ``Ptrac``.
        """

        return self.header.to_mcnp() + ''.join(map(str, self.histories))

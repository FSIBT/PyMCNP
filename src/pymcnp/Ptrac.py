import re
import typing

from . import _file
from . import ptrac
from . import types
from . import errors


class Ptrac(_file.File):
    """
    Represents PTRAC files.

    Attributes:
        header: PTRAC header.
        histories: PTRAC histories.
    """

    _REGEX = re.compile(
        r'\A(   -1\n.{60}\n[^\n]{80}\n(?:\s[^\n]{120}\n)+\s[^\n]{100}\n(?:\s(?:[^\n]{4})+\n)+?)((?:[^\n]+\n(?:(?:(?:(?:\s[^\n]{50})|(?:\s[^\n]{60})|(?:\s[^\n]{60})|(?:\s[^\n]{70})|(?:\s[^\n]{60})|(?:\s[^\n]{70})|(?:\s[^\n]{70})|(?:\s[^\n]{80}))\n(?:\s[^\n]{39})|(?:\s[^\n]{117}))\n)+)+)\Z',
        re.IGNORECASE,
    )

    def __init__(self, header: ptrac.Header, histories: typing.Generator[ptrac.History, None, None]):
        """
        Initializes `Ptrac`.

        Parameters:
            header: PTRAC header.
            histories: PTRAC histories.

        Returns:
            `Ptrac`.

        Raises:
            PtracError: SEMANTICS_FILE.
        """

        if header is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_FILE, header)

        if histories is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_FILE, histories)

        self.header: typing.Final[ptrac.Header] = header
        self.histories: typing.Final[typing.Generator[ptrac.History, None, None]] = histories

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Ptrac` from PTRAC.

        Parameters:
            source: PTRAC for `Ptrac`.

        Returns:
            `Ptrac`.

        Raises:
            PtracError: SYNTAX_FILE.
        """

        tokens = Ptrac._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_FILE, source)

        header = ptrac.Header.from_mcnp(tokens[1])
        histories = types.Tuple(ptrac.History)([ptrac.History.from_mcnp(match[0]) for match in re.finditer(ptrac.History._REGEX.pattern[2:-2], tokens[2])])

        return Ptrac(header, histories)

    def to_mcnp(self):
        """
        Generates PTRAC from `Ptrac`.

        Returns:
            PTRAC for `Ptrac`.
        """

        return self.header.to_mcnp() + ''.join(history.to_mcnp() for history in self.histories)

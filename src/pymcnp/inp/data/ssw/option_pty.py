import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SswOption_Pty(_option.SswOption_, keyword='pty'):
    """
    Represents INP data card data option pty options.

    Attributes:
        tracks: Tracks to record.
    """

    _REGEX = re.compile(r'\Apty(( \S+)+)\Z')

    def __init__(self, tracks: tuple[types.Designator]):
        """
        Initializes ``SswOption_Pty``.

        Parameters:
            tracks: Tracks to record.

        Returns:
            ``SswOption_Pty``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if tracks is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, tracks)

        self.value: typing.Final[tuple[any]] = types._Tuple([tracks])
        self.tracks: typing.Final[tuple[types.Designator]] = tracks

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SswOption_Pty`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SswOption_Pty``.

        Raises:
            McnpError: SYNTAX_SSW_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SswOption_Pty._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SSW_OPTION, source)

        tracks = types._Tuple(
            [types.Designator.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SswOption_Pty(tracks)

import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Leb(_option.DataOption_, keyword='leb'):
    """
    Represents INP data card leb options.

    Attributes:
        yzere: Y0 parameter in level-density formula for Z≤70.
        bzere: B0 parameter in level-density formula for Z≤70.
        yzero: Y0 parameter in level-density formula for Z≥71.
        bzero: B0 parameter in level-density formula for Z≥70.
    """

    _REGEX = re.compile(r'\Aleb( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(self, yzere: types.Real, bzere: types.Real, yzero: types.Real, bzero: types.Real):
        """
        Initializes ``DataOption_Leb``.

        Parameters:
            yzere: Y0 parameter in level-density formula for Z≤70.
            bzere: B0 parameter in level-density formula for Z≤70.
            yzero: Y0 parameter in level-density formula for Z≥71.
            bzero: B0 parameter in level-density formula for Z≥70.

        Returns:
            ``DataOption_Leb``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if yzere is None or not (yzere > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, yzere)
        if bzere is None or not (bzere > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, bzere)
        if yzero is None or not (yzero > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, yzero)
        if bzero is None or not (bzero > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, bzero)

        self.value: typing.Final[tuple[any]] = types._Tuple([yzere, bzere, yzero, bzero])
        self.yzere: typing.Final[types.Real] = yzere
        self.bzere: typing.Final[types.Real] = bzere
        self.yzero: typing.Final[types.Real] = yzero
        self.bzero: typing.Final[types.Real] = bzero

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Leb`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Leb``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Leb._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        yzere = types.Real.from_mcnp(tokens[1])
        bzere = types.Real.from_mcnp(tokens[2])
        yzero = types.Real.from_mcnp(tokens[3])
        bzero = types.Real.from_mcnp(tokens[4])

        return DataOption_Leb(yzere, bzere, yzero, bzero)

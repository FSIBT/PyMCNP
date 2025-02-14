import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Cm(_option.DataOption_, keyword='cm'):
    """
    Represents INP data card cm options.

    Attributes:
        multipliers: Cosine bin multiplier to apply.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Acm(\d+?)(( \S+)+)\Z')

    def __init__(self, multipliers: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Cm``.

        Parameters:
            multipliers: Cosine bin multiplier to apply.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Cm``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if multipliers is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, multipliers)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([multipliers])
        self.multipliers: typing.Final[tuple[types.Real]] = multipliers
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Cm`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Cm``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Cm._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        multipliers = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Cm(multipliers, suffix)

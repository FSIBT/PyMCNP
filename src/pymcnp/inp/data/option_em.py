import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Em(_option.DataOption_, keyword='em'):
    """
    Represents INP data card em options.

    Attributes:
        multipliers: Energy bin multiplier to apply.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Aem(\d+?)(( \S+)+)\Z')

    def __init__(self, multipliers: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Em``.

        Parameters:
            multipliers: Energy bin multiplier to apply.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Em``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([multipliers])
        self.multipliers: typing.Final[tuple[types.Real]] = multipliers
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Em`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Em``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Em._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        multipliers = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Em(multipliers, suffix)

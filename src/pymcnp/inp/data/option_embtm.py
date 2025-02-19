import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Embtm(_option.DataOption_, keyword='embtm'):
    """
    Represents INP data card embtm options.

    Attributes:
        multipliers: Tuple of time multipliers.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Aembtm(\d+?)(( \S+)+)\Z')

    def __init__(self, multipliers: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Embtm``.

        Parameters:
            multipliers: Tuple of time multipliers.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Embtm``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([multipliers])
        self.multipliers: typing.Final[tuple[types.Real]] = multipliers
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Embtm`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Embtm``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Embtm._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        multipliers = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Embtm(multipliers, suffix)

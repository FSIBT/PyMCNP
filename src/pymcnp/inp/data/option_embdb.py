import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Embdb(_option.DataOption_, keyword='embdb'):
    """
    Represents INP data card embdb options.

    Attributes:
        bounds: Tuple of upper dose energy bounds.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Aembdb(\d+?)(( \S+)+)\Z')

    def __init__(self, bounds: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Embdb``.

        Parameters:
            bounds: Tuple of upper dose energy bounds.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Embdb``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, bounds)
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([bounds])
        self.bounds: typing.Final[tuple[types.Real]] = bounds
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Embdb`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Embdb``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Embdb._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        bounds = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Embdb(bounds, suffix)

import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Wwe(_option.DataOption_, keyword='wwe'):
    """
    Represents INP data card wwe options.

    Attributes:
        bounds: Upper energy/time bound.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(r'\Awwe:(\S+?)(( \S+)+)\Z')

    def __init__(self, bounds: tuple[types.Real], designator: types.Designator):
        """
        Initializes ``DataOption_Wwe``.

        Parameters:
            bounds: Upper energy/time bound.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Wwe``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, bounds)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([bounds])
        self.bounds: typing.Final[tuple[types.Real]] = bounds
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Wwe`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Wwe``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Wwe._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        designator = types.Designator.from_mcnp(tokens[1])
        bounds = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Wwe(bounds, designator)

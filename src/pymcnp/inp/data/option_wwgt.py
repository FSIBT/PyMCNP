import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Wwgt(_option.DataOption_, keyword='wwgt'):
    """
    Represents INP data card wwgt options.

    Attributes:
        bounds: Upper time bound for weight-window group to be generated.
    """

    _REGEX = re.compile(r'\Awwgt(( \S+)+)\Z')

    def __init__(self, bounds: tuple[types.Real]):
        """
        Initializes ``DataOption_Wwgt``.

        Parameters:
            bounds: Upper time bound for weight-window group to be generated.

        Returns:
            ``DataOption_Wwgt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if bounds is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, bounds)

        self.value: typing.Final[tuple[any]] = types._Tuple([bounds])
        self.bounds: typing.Final[tuple[types.Real]] = bounds

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Wwgt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Wwgt``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Wwgt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        bounds = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Wwgt(bounds)

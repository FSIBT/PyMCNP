import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Rdum(_option.DataOption_, keyword='rdum'):
    """
    Represents INP data card rdum options.

    Attributes:
        floats: Floating point array.
    """

    _REGEX = re.compile(r'\Ardum(( \S+)+)\Z')

    def __init__(self, floats: tuple[types.Real]):
        """
        Initializes ``DataOption_Rdum``.

        Parameters:
            floats: Floating point array.

        Returns:
            ``DataOption_Rdum``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if floats is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, floats)

        self.value: typing.Final[tuple[any]] = types._Tuple([floats])
        self.floats: typing.Final[tuple[types.Real]] = floats

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Rdum`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Rdum``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Rdum._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        floats = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Rdum(floats)

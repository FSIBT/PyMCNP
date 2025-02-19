import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Lat(_option.DataOption_, keyword='lat'):
    """
    Represents INP data card lat options.

    Attributes:
        type: Tuple of lattice types.
    """

    _REGEX = re.compile(r'\Alat(( \S+)+)\Z')

    def __init__(self, type: tuple[types.Integer]):
        """
        Initializes ``DataOption_Lat``.

        Parameters:
            type: Tuple of lattice types.

        Returns:
            ``DataOption_Lat``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if type is None or not (filter(lambda entry: not (entry == 1 or entry == 2), type)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, type)

        self.value: typing.Final[tuple[any]] = types._Tuple([type])
        self.type: typing.Final[tuple[types.Integer]] = type

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Lat`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Lat``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Lat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        type = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Lat(type)

import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Print(_option.DataOption_, keyword='print'):
    """
    Represents INP data card print options.

    Attributes:
        tables: Tables to print.
    """

    _REGEX = re.compile(r'\Aprint(( \S+)+)?\Z')

    def __init__(self, tables: tuple[types.Integer] = None):
        """
        Initializes ``DataOption_Print``.

        Parameters:
            tables: Tables to print.

        Returns:
            ``DataOption_Print``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tables is not None and not (
            filter(
                lambda entry: entry.value
                not in {
                    10,
                    20,
                    30,
                    32,
                    35,
                    38,
                    40,
                    41,
                    44,
                    50,
                    55,
                    60,
                    62,
                    70,
                    72,
                    80,
                    85,
                    86,
                    87,
                    90,
                    95,
                    98,
                    100,
                    102,
                    110,
                    115,
                    117,
                    118,
                    120,
                    126,
                    128,
                    130,
                    140,
                    150,
                    160,
                    161,
                    162,
                    163,
                    170,
                    175,
                    178,
                    180,
                    190,
                    198,
                    200,
                    210,
                    220,
                    -10,
                    -20,
                    -30,
                    -32,
                    -35,
                    -38,
                    -40,
                    -41,
                    -44,
                    -50,
                    -55,
                    -60,
                    -62,
                    -70,
                    -72,
                    -80,
                    -85,
                    -86,
                    -87,
                    -90,
                    -95,
                    -98,
                    -100,
                    -102,
                    -110,
                    -115,
                    -117,
                    -118,
                    -120,
                    -126,
                    -128,
                    -130,
                    -140,
                    -150,
                    -160,
                    -161,
                    -162,
                    -163,
                    -170,
                    -175,
                    -178,
                    -180,
                    -190,
                    -198,
                    -200,
                    -210,
                    -220,
                },
                tables,
            )
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tables)

        self.value: typing.Final[tuple[any]] = types._Tuple([tables])
        self.tables: typing.Final[tuple[types.Integer]] = tables

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Print`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Print``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Print._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        tables = (
            types._Tuple(
                [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
            )
            if tokens[1]
            else None
        )

        return DataOption_Print(tables)

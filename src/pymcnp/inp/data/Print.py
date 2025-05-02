import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Print(DataOption):
    """
    Represents INP print elements.

    Attributes:
        tables: Tables to print.
    """

    _ATTRS = {
        'tables': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Aprint((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z')

    def __init__(self, tables: types.Tuple[types.IntegerOrJump] = None):
        """
        Initializes ``Print``.

        Parameters:
            tables: Tables to print.

        Raises:
            InpError: SEMANTICS_OPTION.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tables)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tables,
            ]
        )

        self.tables: typing.Final[types.Tuple[types.IntegerOrJump]] = tables


@dataclasses.dataclass
class PrintBuilder:
    """
    Builds ``Print``.

    Attributes:
        tables: Tables to print.
    """

    tables: list[str] | list[int] | list[types.IntegerOrJump] = None

    def build(self):
        """
        Builds ``PrintBuilder`` into ``Print``.

        Returns:
            ``Print`` for ``PrintBuilder``.
        """

        tables = []
        for item in self.tables:
            if isinstance(item, types.IntegerOrJump):
                tables.append(item)
            elif isinstance(item, int):
                tables.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                tables.append(types.IntegerOrJump.from_mcnp(item))
        tables = types.Tuple(tables)

        return Print(
            tables=tables,
        )

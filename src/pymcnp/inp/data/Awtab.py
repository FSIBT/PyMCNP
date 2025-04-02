import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Awtab(DataOption_, keyword='awtab'):
    """
    Represents INP awtab elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'weight_ratios': types.Tuple[types.Substance],
    }

    _REGEX = re.compile(rf'\Aawtab((?: {types.Substance._REGEX.pattern})+?)\Z')

    def __init__(self, weight_ratios: types.Tuple[types.Substance]):
        """
        Initializes ``Awtab``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight_ratios)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight_ratios,
            ]
        )

        self.weight_ratios: typing.Final[types.Tuple[types.Substance]] = weight_ratios

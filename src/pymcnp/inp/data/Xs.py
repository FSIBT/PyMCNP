import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Xs(DataOption_, keyword='xs'):
    """
    Represents INP xs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'weight_ratios': types.Tuple[types.SubstanceEntry],
    }

    _REGEX = re.compile(rf'xs(\S+)(( {types.SubstanceEntry._REGEX.pattern})+)')

    def __init__(self, suffix: types.Integer, weight_ratios: types.Tuple[types.SubstanceEntry]):
        """
        Initializes ``Xs``.

        Parameters:
            suffix: Data card option suffix.
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if weight_ratios is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight_ratios)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight_ratios,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.weight_ratios: typing.Final[types.Tuple[types.SubstanceEntry]] = weight_ratios

import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Cm(DataOption_, keyword='cm'):
    """
    Represents INP cm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Acm(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Cm``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Cosine bin multiplier to apply.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multipliers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.multipliers: typing.Final[types.Tuple[types.RealOrJump]] = multipliers

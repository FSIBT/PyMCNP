import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Embdf(DataOption_, keyword='embdf'):
    """
    Represents INP embdf elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'embdf(\d+)(( {types.Real._REGEX.pattern})+)')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.Real]):
        """
        Initializes ``Embdf``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Tuple of dose energy multipliers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multipliers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.multipliers: typing.Final[types.Tuple[types.Real]] = multipliers

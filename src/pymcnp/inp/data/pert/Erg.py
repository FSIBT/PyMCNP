import re
import typing


from .option_ import PertOption_
from ....utils import types
from ....utils import errors


class Erg(PertOption_, keyword='erg'):
    """
    Represents INP erg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energy_lower_bound': types.RealOrJump,
        'energy_upper_bound': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aerg( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, energy_lower_bound: types.RealOrJump, energy_upper_bound: types.RealOrJump):
        """
        Initializes ``Erg``.

        Parameters:
            energy_lower_bound: Lower bound for energy pertubation.
            energy_upper_bound: Upper bound for energy pertubation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energy_lower_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_lower_bound)
        if energy_upper_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy_upper_bound)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy_lower_bound,
                energy_upper_bound,
            ]
        )

        self.energy_lower_bound: typing.Final[types.RealOrJump] = energy_lower_bound
        self.energy_upper_bound: typing.Final[types.RealOrJump] = energy_upper_bound

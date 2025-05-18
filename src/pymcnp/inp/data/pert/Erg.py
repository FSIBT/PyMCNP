import re
import typing
import dataclasses


from ._option import PertOption
from ....utils import types
from ....utils import errors


class Erg(PertOption):
    """
    Represents INP erg elements.

    Attributes:
        energy_lower_bound: Lower bound for energy pertubation.
        energy_upper_bound: Upper bound for energy pertubation.
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
            InpError: SEMANTICS_OPTION.
        """

        if energy_lower_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_lower_bound)
        if energy_upper_bound is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy_upper_bound)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy_lower_bound,
                energy_upper_bound,
            ]
        )

        self.energy_lower_bound: typing.Final[types.RealOrJump] = energy_lower_bound
        self.energy_upper_bound: typing.Final[types.RealOrJump] = energy_upper_bound


@dataclasses.dataclass
class ErgBuilder:
    """
    Builds ``Erg``.

    Attributes:
        energy_lower_bound: Lower bound for energy pertubation.
        energy_upper_bound: Upper bound for energy pertubation.
    """

    energy_lower_bound: str | float | types.RealOrJump
    energy_upper_bound: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ErgBuilder`` into ``Erg``.

        Returns:
            ``Erg`` for ``ErgBuilder``.
        """

        energy_lower_bound = self.energy_lower_bound
        if isinstance(self.energy_lower_bound, types.Real):
            energy_lower_bound = self.energy_lower_bound
        elif isinstance(self.energy_lower_bound, float) or isinstance(self.energy_lower_bound, int):
            energy_lower_bound = types.RealOrJump(self.energy_lower_bound)
        elif isinstance(self.energy_lower_bound, str):
            energy_lower_bound = types.RealOrJump.from_mcnp(self.energy_lower_bound)

        energy_upper_bound = self.energy_upper_bound
        if isinstance(self.energy_upper_bound, types.Real):
            energy_upper_bound = self.energy_upper_bound
        elif isinstance(self.energy_upper_bound, float) or isinstance(self.energy_upper_bound, int):
            energy_upper_bound = types.RealOrJump(self.energy_upper_bound)
        elif isinstance(self.energy_upper_bound, str):
            energy_upper_bound = types.RealOrJump.from_mcnp(self.energy_upper_bound)

        return Erg(
            energy_lower_bound=energy_lower_bound,
            energy_upper_bound=energy_upper_bound,
        )

import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Erg_0(SdefOption):
    """
    Represents INP erg variation #0 elements.

    Attributes:
        energy: Kinetic energy.
    """

    _ATTRS = {
        'energy': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aerg( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, energy: types.RealOrJump):
        """
        Initializes ``Erg_0``.

        Parameters:
            energy: Kinetic energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy,
            ]
        )

        self.energy: typing.Final[types.RealOrJump] = energy


@dataclasses.dataclass
class ErgBuilder_0:
    """
    Builds ``Erg_0``.

    Attributes:
        energy: Kinetic energy.
    """

    energy: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ErgBuilder_0`` into ``Erg_0``.

        Returns:
            ``Erg_0`` for ``ErgBuilder_0``.
        """

        if isinstance(self.energy, types.Real):
            energy = self.energy
        elif isinstance(self.energy, float) or isinstance(self.energy, int):
            energy = types.RealOrJump(self.energy)
        elif isinstance(self.energy, str):
            energy = types.RealOrJump.from_mcnp(self.energy)

        return Erg_0(
            energy=energy,
        )

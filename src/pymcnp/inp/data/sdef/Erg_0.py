import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Erg_0(_option.SdefOption):
    """
    Represents INP erg variation #0 elements.

    Attributes:
        energy: Kinetic energy.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy': types.Real,
    }

    _REGEX = re.compile(rf'\Aerg( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, energy: types.Real):
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

        self.energy: typing.Final[types.Real] = energy


@dataclasses.dataclass
class ErgBuilder_0(_option.SdefOptionBuilder):
    """
    Builds ``Erg_0``.

    Attributes:
        energy: Kinetic energy.
    """

    energy: str | float | types.Real

    def build(self):
        """
        Builds ``ErgBuilder_0`` into ``Erg_0``.

        Returns:
            ``Erg_0`` for ``ErgBuilder_0``.
        """

        energy = self.energy
        if isinstance(self.energy, types.Real):
            energy = self.energy
        elif isinstance(self.energy, float) or isinstance(self.energy, int):
            energy = types.Real(self.energy)
        elif isinstance(self.energy, str):
            energy = types.Real.from_mcnp(self.energy)

        return Erg_0(
            energy=energy,
        )

    @staticmethod
    def unbuild(ast: Erg_0):
        """
        Unbuilds ``Erg_0`` into ``ErgBuilder_0``

        Returns:
            ``ErgBuilder_0`` for ``Erg_0``.
        """

        return ErgBuilder_0(
            energy=copy.deepcopy(ast.energy),
        )

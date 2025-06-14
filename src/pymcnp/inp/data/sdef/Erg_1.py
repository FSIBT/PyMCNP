import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Erg_1(_option.SdefOption):
    """
    Represents INP erg variation #1 elements.

    Attributes:
        energy: Kinetic energy.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energy': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Aerg( {types.DistributionNumber._REGEX.pattern[2:-2]})\Z')

    def __init__(self, energy: types.DistributionNumber):
        """
        Initializes ``Erg_1``.

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

        self.energy: typing.Final[types.DistributionNumber] = energy


@dataclasses.dataclass
class ErgBuilder_1(_option.SdefOptionBuilder):
    """
    Builds ``Erg_1``.

    Attributes:
        energy: Kinetic energy.
    """

    energy: str | types.DistributionNumber

    def build(self):
        """
        Builds ``ErgBuilder_1`` into ``Erg_1``.

        Returns:
            ``Erg_1`` for ``ErgBuilder_1``.
        """

        energy = self.energy
        if isinstance(self.energy, types.DistributionNumber):
            energy = self.energy
        elif isinstance(self.energy, str):
            energy = types.DistributionNumber.from_mcnp(self.energy)

        return Erg_1(
            energy=energy,
        )

    @staticmethod
    def unbuild(ast: Erg_1):
        """
        Unbuilds ``Erg_1`` into ``ErgBuilder_1``

        Returns:
            ``ErgBuilder_1`` for ``Erg_1``.
        """

        return ErgBuilder_1(
            energy=copy.deepcopy(ast.energy),
        )

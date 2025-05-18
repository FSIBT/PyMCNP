import re
import typing
import dataclasses


from ._option import KpertOption
from ....utils import types
from ....utils import errors


class Erg(KpertOption):
    """
    Represents INP erg elements.

    Attributes:
        energies: List of energies.
    """

    _ATTRS = {
        'energies': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aerg((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, energies: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Erg``.

        Parameters:
            energies: List of energies.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if energies is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energies,
            ]
        )

        self.energies: typing.Final[types.Tuple[types.RealOrJump]] = energies


@dataclasses.dataclass
class ErgBuilder:
    """
    Builds ``Erg``.

    Attributes:
        energies: List of energies.
    """

    energies: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``ErgBuilder`` into ``Erg``.

        Returns:
            ``Erg`` for ``ErgBuilder``.
        """

        if self.energies:
            energies = []
            for item in self.energies:
                if isinstance(item, types.RealOrJump):
                    energies.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    energies.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    energies.append(types.RealOrJump.from_mcnp(item))
            energies = types.Tuple(energies)
        else:
            energies = None

        return Erg(
            energies=energies,
        )

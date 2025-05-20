import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Emesh(FmeshOption):
    """
    Represents INP emesh elements.

    Attributes:
        energy: Values of mesh points in energy.
    """

    _ATTRS = {
        'energy': types.Real,
    }

    _REGEX = re.compile(rf'\Aemesh( {types.Real._REGEX.pattern})\Z')

    def __init__(self, energy: types.Real):
        """
        Initializes ``Emesh``.

        Parameters:
            energy: Values of mesh points in energy.

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
class EmeshBuilder:
    """
    Builds ``Emesh``.

    Attributes:
        energy: Values of mesh points in energy.
    """

    energy: str | float | types.Real

    def build(self):
        """
        Builds ``EmeshBuilder`` into ``Emesh``.

        Returns:
            ``Emesh`` for ``EmeshBuilder``.
        """

        energy = self.energy
        if isinstance(self.energy, types.Real):
            energy = self.energy
        elif isinstance(self.energy, float) or isinstance(self.energy, int):
            energy = types.Real(self.energy)
        elif isinstance(self.energy, str):
            energy = types.Real.from_mcnp(self.energy)

        return Emesh(
            energy=energy,
        )

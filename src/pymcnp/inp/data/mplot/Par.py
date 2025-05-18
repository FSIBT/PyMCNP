import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Par(MplotOption):
    """
    Represents INP par elements.

    Attributes:
        particle: Particle type to plot.
    """

    _ATTRS = {
        'particle': types.Designator,
    }

    _REGEX = re.compile(rf'\Apar( {types.Designator._REGEX.pattern})\Z')

    def __init__(self, particle: types.Designator):
        """
        Initializes ``Par``.

        Parameters:
            particle: Particle type to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if particle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, particle)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                particle,
            ]
        )

        self.particle: typing.Final[types.Designator] = particle


@dataclasses.dataclass
class ParBuilder:
    """
    Builds ``Par``.

    Attributes:
        particle: Particle type to plot.
    """

    particle: str | types.Designator

    def build(self):
        """
        Builds ``ParBuilder`` into ``Par``.

        Returns:
            ``Par`` for ``ParBuilder``.
        """

        particle = self.particle
        if isinstance(self.particle, types.Designator):
            particle = self.particle
        elif isinstance(self.particle, str):
            particle = types.Designator.from_mcnp(self.particle)

        return Par(
            particle=particle,
        )

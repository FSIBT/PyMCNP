import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Mode(DataOption):
    """
    Represents INP mode elements.

    Attributes:
        particles: Tuple of particle designators.
    """

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Amode((?: {types.Designator._REGEX.pattern})+?)\Z')

    def __init__(self, particles: types.Tuple[types.Designator]):
        """
        Initializes ``Mode``.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if particles is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, particles)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                particles,
            ]
        )

        self.particles: typing.Final[types.Tuple[types.Designator]] = particles


@dataclasses.dataclass
class ModeBuilder:
    """
    Builds ``Mode``.

    Attributes:
        particles: Tuple of particle designators.
    """

    particles: list[str] | list[types.Designator]

    def build(self):
        """
        Builds ``ModeBuilder`` into ``Mode``.

        Returns:
            ``Mode`` for ``ModeBuilder``.
        """

        particles = []
        for item in self.particles:
            if isinstance(item, types.Designator):
                particles.append(item)
            elif isinstance(item, str):
                particles.append(types.Designator.from_mcnp(item))
            else:
                particles.append(item.build())
        particles = types.Tuple(particles)

        return Mode(
            particles=particles,
        )

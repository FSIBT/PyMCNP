import re
import typing
import dataclasses


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Nps(PtracOption_, keyword='nps'):
    """
    Represents INP nps elements.

    Attributes:
        particles: Sets the range of particle histories for which events will be output.
    """

    _ATTRS = {
        'particles': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Anps((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, particles: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Nps``.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if particles is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, particles)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                particles,
            ]
        )

        self.particles: typing.Final[types.Tuple[types.IntegerOrJump]] = particles


@dataclasses.dataclass
class NpsBuilder:
    """
    Builds ``Nps``.

    Attributes:
        particles: Sets the range of particle histories for which events will be output.
    """

    particles: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``NpsBuilder`` into ``Nps``.

        Returns:
            ``Nps`` for ``NpsBuilder``.
        """

        particles = []
        for item in self.particles:
            if isinstance(item, types.IntegerOrJump):
                particles.append(item)
            elif isinstance(item, int):
                particles.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                particles.append(types.IntegerOrJump.from_mcnp(item))
        particles = types.Tuple(particles)

        return Nps(
            particles=particles,
        )

import re
import copy
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Nps(PtracOption):
    """
    Represents INP nps elements.

    Attributes:
        particles: Sets the range of particle histories for which events will be output.
    """

    _KEYWORD = 'nps'

    _ATTRS = {
        'particles': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Anps((?: {types.Integer._REGEX.pattern})+?)\Z')

    def __init__(self, particles: types.Tuple[types.Integer]):
        """
        Initializes ``Nps``.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

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

        self.particles: typing.Final[types.Tuple[types.Integer]] = particles


@dataclasses.dataclass
class NpsBuilder:
    """
    Builds ``Nps``.

    Attributes:
        particles: Sets the range of particle histories for which events will be output.
    """

    particles: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``NpsBuilder`` into ``Nps``.

        Returns:
            ``Nps`` for ``NpsBuilder``.
        """

        if self.particles:
            particles = []
            for item in self.particles:
                if isinstance(item, types.Integer):
                    particles.append(item)
                elif isinstance(item, int):
                    particles.append(types.Integer(item))
                elif isinstance(item, str):
                    particles.append(types.Integer.from_mcnp(item))
            particles = types.Tuple(particles)
        else:
            particles = None

        return Nps(
            particles=particles,
        )

    @staticmethod
    def unbuild(ast: Nps):
        """
        Unbuilds ``Nps`` into ``NpsBuilder``

        Returns:
            ``NpsBuilder`` for ``Nps``.
        """

        return Nps(
            particles=copy.deepcopy(ast.particles),
        )

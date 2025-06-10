import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Mode(_option.DataOption):
    """
    Represents INP mode elements.

    Attributes:
        particles: Tuple of particle designators.
    """

    _KEYWORD = 'mode'

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Amode((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z')

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
class ModeBuilder(_option.DataOptionBuilder):
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

        if self.particles:
            particles = []
            for item in self.particles:
                if isinstance(item, types.Designator):
                    particles.append(item)
                elif isinstance(item, str):
                    particles.append(types.Designator.from_mcnp(item))
            particles = types.Tuple(particles)
        else:
            particles = None

        return Mode(
            particles=particles,
        )

    @staticmethod
    def unbuild(ast: Mode):
        """
        Unbuilds ``Mode`` into ``ModeBuilder``

        Returns:
            ``ModeBuilder`` for ``Mode``.
        """

        return ModeBuilder(
            particles=copy.deepcopy(ast.particles),
        )

import re
import copy
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Type(PtracOption):
    """
    Represents INP type elements.

    Attributes:
        particles: Filters events based on one or more particle types.
    """

    _KEYWORD = 'type'

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Atype((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, particles: types.Tuple[types.Designator]):
        """
        Initializes ``Type``.

        Parameters:
            particles: Filters events based on one or more particle types.

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
class TypeBuilder:
    """
    Builds ``Type``.

    Attributes:
        particles: Filters events based on one or more particle types.
    """

    particles: list[str] | list[types.Designator]

    def build(self):
        """
        Builds ``TypeBuilder`` into ``Type``.

        Returns:
            ``Type`` for ``TypeBuilder``.
        """

        if self.particles:
            particles = []
            for item in self.particles:
                if isinstance(item, types.Designator):
                    particles.append(item)
                elif isinstance(item, str):
                    particles.append(types.Designator.from_mcnp(item))
                else:
                    particles.append(item.build())
            particles = types.Tuple(particles)
        else:
            particles = None

        return Type(
            particles=particles,
        )

    @staticmethod
    def unbuild(ast: Type):
        """
        Unbuilds ``Type`` into ``TypeBuilder``

        Returns:
            ``TypeBuilder`` for ``Type``.
        """

        return Type(
            particles=copy.deepcopy(ast.particles),
        )

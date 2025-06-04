import re
import copy
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Pty(SsrOption):
    """
    Represents INP pty elements.

    Attributes:
        particles: Tuple of designators.
    """

    _KEYWORD = 'pty'

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, particles: types.Tuple[types.Designator]):
        """
        Initializes ``Pty``.

        Parameters:
            particles: Tuple of designators.

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
class PtyBuilder:
    """
    Builds ``Pty``.

    Attributes:
        particles: Tuple of designators.
    """

    particles: list[str] | list[types.Designator]

    def build(self):
        """
        Builds ``PtyBuilder`` into ``Pty``.

        Returns:
            ``Pty`` for ``PtyBuilder``.
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

        return Pty(
            particles=particles,
        )

    @staticmethod
    def unbuild(ast: Pty):
        """
        Unbuilds ``Pty`` into ``PtyBuilder``

        Returns:
            ``PtyBuilder`` for ``Pty``.
        """

        return Pty(
            particles=copy.deepcopy(ast.particles),
        )

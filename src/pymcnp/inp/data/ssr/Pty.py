import re
import typing
import dataclasses


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Pty(SsrOption_, keyword='pty'):
    """
    Represents INP pty elements.

    Attributes:
        particles: Tuple of designators.
    """

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern})+?)\Z')

    def __init__(self, particles: types.Tuple[types.Designator]):
        """
        Initializes ``Pty``.

        Parameters:
            particles: Tuple of designators.

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

        particles = []
        for item in self.particles:
            if isinstance(item, types.Designator):
                particles.append(item)
            elif isinstance(item, str):
                particles.append(types.Designator.from_mcnp(item))
            else:
                particles.append(item.build())
        particles = types.Tuple(particles)

        return Pty(
            particles=particles,
        )

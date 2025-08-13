import re

from . import _option
from ... import types
from ... import errors


class Pty(_option.SsrOption):
    """
    Represents INP `pty` elements.
    """

    _KEYWORD = 'pty'

    _ATTRS = {
        'particles': types.Tuple(types.Designator),
    }

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, particles: list[str] | list[types.Designator]):
        """
        Initializes `Pty`.

        Parameters:
            particles: Tuple of designators.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.particles: types.Tuple(types.Designator) = particles

    @property
    def particles(self) -> types.Tuple(types.Designator):
        """
        Tuple of designators

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._particles

    @particles.setter
    def particles(self, particles: list[str] | list[types.Designator]) -> None:
        """
        Sets `particles`.

        Parameters:
            particles: Tuple of designators.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if particles is not None:
            array = []
            for item in particles:
                if isinstance(item, types.Designator):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.Designator.from_mcnp(item))
            particles = types.Tuple(types.Designator)(array)

        if particles is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, particles)

        self._particles: types.Tuple(types.Designator) = particles

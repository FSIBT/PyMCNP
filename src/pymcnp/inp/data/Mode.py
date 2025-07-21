import re

from . import _option
from ... import types
from ... import errors


class Mode(_option.DataOption):
    """
    Represents INP mode elements.
    """

    _KEYWORD = 'mode'

    _ATTRS = {
        'particles': types.Tuple(types.Designator),
    }

    _REGEX = re.compile(rf'\Amode((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, particles: list[str] | list[types.Designator]):
        """
        Initializes ``Mode``.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.particles: types.Tuple(types.Designator) = particles

    @property
    def particles(self) -> types.Tuple(types.Designator):
        """
        Tuple of particle designators

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._particles

    @particles.setter
    def particles(self, particles: list[str] | list[types.Designator]) -> None:
        """
        Sets ``particles``.

        Parameters:
            particles: Tuple of particle designators.

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

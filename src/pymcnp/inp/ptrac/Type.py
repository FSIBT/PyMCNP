import re

from . import _option
from ... import types
from ... import errors


class Type(_option.PtracOption):
    """
    Represents INP `type` elements.
    """

    _KEYWORD = 'type'

    _ATTRS = {
        'particles': types.Tuple(types.Designator),
    }

    _REGEX = re.compile(rf'\Atype((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, particles: list[str] | list[types.Designator]):
        """
        Initializes `Type`.

        Parameters:
            particles: Filters events based on one or more particle types.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.particles: types.Tuple(types.Designator) = particles

    @property
    def particles(self) -> types.Tuple(types.Designator):
        """
        Filters events based on one or more particle types

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
            particles: Filters events based on one or more particle types.

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

import re

from . import _card
from .. import types
from .. import errors


class Mode(_card.Card):
    """
    Represents INP `mode` cards.
    """

    _KEYWORD = 'mode'

    _ATTRS = {
        'particles': types.Tuple(types.Designator),
    }

    _REGEX = re.compile(rf'\Amode((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, particles: list[str] | list[types.Designator]):
        """
        Initializes `Mode`.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.particles: types.Tuple(types.Designator) = particles

    @property
    def particles(self) -> types.Tuple(types.Designator):
        """
        Tuple of particle designators

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._particles

    @particles.setter
    def particles(self, particles: list[str] | list[types.Designator]) -> None:
        """
        Sets `particles`.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            InpError: SEMANTICS_CARD.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, particles)

        self._particles: types.Tuple(types.Designator) = particles

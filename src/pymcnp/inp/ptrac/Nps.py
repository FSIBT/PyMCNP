import re

from . import _option
from ... import types
from ... import errors


class Nps(_option.PtracOption):
    """
    Represents INP `nps` elements.
    """

    _KEYWORD = 'nps'

    _ATTRS = {
        'particles': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Anps((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, particles: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Nps`.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.particles: types.Tuple(types.Integer) = particles

    @property
    def particles(self) -> types.Tuple(types.Integer):
        """
        Sets the range of particle histories for which events will be output

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._particles

    @particles.setter
    def particles(self, particles: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `particles`.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if particles is not None:
            array = []
            for item in particles:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            particles = types.Tuple(types.Integer)(array)

        if particles is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, particles)

        self._particles: types.Tuple(types.Integer) = particles

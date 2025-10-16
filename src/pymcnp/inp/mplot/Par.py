import re

from . import _option
from ... import types
from ... import errors


class Par(_option.MplotOption):
    """
    Represents INP `par` elements.
    """

    _KEYWORD = 'par'

    _ATTRS = {
        'particle': types.Designator,
    }

    _REGEX = re.compile(rf'\Apar( {types.Designator._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, particle: str | types.Designator):
        """
        Initializes `Par`.

        Parameters:
            particle: Particle type to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.particle: types.Designator = particle

    @property
    def particle(self) -> types.Designator:
        """
        Particle type to plot

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._particle

    @particle.setter
    def particle(self, particle: str | types.Designator) -> None:
        """
        Sets `particle`.

        Parameters:
            particle: Particle type to plot.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if particle is not None:
            if isinstance(particle, types.Designator):
                particle = particle
            elif isinstance(particle, str):
                particle = types.Designator.from_mcnp(particle)

        if particle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, particle)

        self._particle: types.Designator = particle

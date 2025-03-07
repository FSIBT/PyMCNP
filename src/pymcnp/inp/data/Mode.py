import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Mode(DataOption_, keyword='mode'):
    """
    Represents INP mode elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'mode(( {types.Designator._REGEX.pattern})+)')

    def __init__(self, particles: types.Tuple[types.Designator]):
        """
        Initializes ``Mode``.

        Parameters:
            particles: Tuple of particle designators.

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

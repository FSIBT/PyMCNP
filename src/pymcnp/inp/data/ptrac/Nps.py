import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Nps(PtracOption_, keyword='nps'):
    """
    Represents INP nps elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'particles': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Anps((?: {types.Integer._REGEX.pattern})+?)\Z')

    def __init__(self, particles: types.Tuple[types.Integer]):
        """
        Initializes ``Nps``.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

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

        self.particles: typing.Final[types.Tuple[types.Integer]] = particles

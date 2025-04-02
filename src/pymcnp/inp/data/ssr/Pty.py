import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Pty(SsrOption_, keyword='pty'):
    """
    Represents INP pty elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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

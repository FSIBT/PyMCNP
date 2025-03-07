import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Type(PtracOption_, keyword='type'):
    """
    Represents INP type elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'particles': types.Tuple[types.Designator],
    }

    _REGEX = re.compile(rf'type(( {types.Designator._REGEX.pattern})+)')

    def __init__(self, particles: types.Tuple[types.Designator]):
        """
        Initializes ``Type``.

        Parameters:
            particles: Filters events based on one or more particle types.

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

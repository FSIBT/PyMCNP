import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Jmesh(FmeshOption_, keyword='jmesh'):
    """
    Represents INP jmesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'locations': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Ajmesh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, locations: types.RealOrJump):
        """
        Initializes ``Jmesh``.

        Parameters:
            locations: Locations of mesh points y/z for rectangular/cylindrical geometry.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, locations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                locations,
            ]
        )

        self.locations: typing.Final[types.RealOrJump] = locations

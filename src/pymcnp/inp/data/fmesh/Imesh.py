import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Imesh(FmeshOption_, keyword='imesh'):
    """
    Represents INP imesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'locations': types.Real,
    }

    _REGEX = re.compile(rf'imesh( {types.Real._REGEX.pattern})')

    def __init__(self, locations: types.Real):
        """
        Initializes ``Imesh``.

        Parameters:
            locations: Locations of mesh points x/r for rectangular/cylindrical geometry.

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

        self.locations: typing.Final[types.Real] = locations

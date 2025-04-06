import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Rad_1(SdefOption_, keyword='rad'):
    """
    Represents INP rad elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'radial_distance': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Arad( {types.DistributionNumber._REGEX.pattern})\Z')

    def __init__(self, radial_distance: types.DistributionNumber):
        """
        Initializes ``Rad_1``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if radial_distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, radial_distance)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                radial_distance,
            ]
        )

        self.radial_distance: typing.Final[types.DistributionNumber] = radial_distance

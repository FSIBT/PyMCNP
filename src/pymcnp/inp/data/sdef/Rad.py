import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Rad(SdefOption_, keyword='rad'):
    """
    Represents INP rad elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'radial_distance': types.Real,
    }

    _REGEX = re.compile(r'rad( \S+)')

    def __init__(self, radial_distance: types.Real):
        """
        Initializes ``Rad``.

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

        self.radial_distance: typing.Final[types.Real] = radial_distance

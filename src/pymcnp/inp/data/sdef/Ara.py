import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Ara(SdefOption_, keyword='ara'):
    """
    Represents INP ara elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'area': types.Real,
    }

    _REGEX = re.compile(r'ara( \S+)')

    def __init__(self, area: types.Real):
        """
        Initializes ``Ara``.

        Parameters:
            area: Area of surface.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if area is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, area)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                area,
            ]
        )

        self.area: typing.Final[types.Real] = area

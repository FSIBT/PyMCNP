import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Ext(SdefOption_, keyword='ext'):
    """
    Represents INP ext elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'distance_cosine': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aext( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, distance_cosine: types.RealOrJump):
        """
        Initializes ``Ext``.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if distance_cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, distance_cosine)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                distance_cosine,
            ]
        )

        self.distance_cosine: typing.Final[types.RealOrJump] = distance_cosine

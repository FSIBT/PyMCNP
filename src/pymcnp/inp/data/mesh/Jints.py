import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Jints(MeshOption_, keyword='jints'):
    """
    Represents INP jints elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Ajints( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Jints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the y/z directions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number

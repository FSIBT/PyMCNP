import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Iints(MeshOption_, keyword='iints'):
    """
    Represents INP iints elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(r'iints( \S+)')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Iints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the x/r directions.

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

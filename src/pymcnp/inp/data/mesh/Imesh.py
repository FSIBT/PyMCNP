import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Imesh(MeshOption_, keyword='imesh'):
    """
    Represents INP imesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aimesh((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Imesh``.

        Parameters:
            vector: Locations of the coarse meshes in the x/r directions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vector)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vector,
            ]
        )

        self.vector: typing.Final[types.Tuple[types.Real]] = vector

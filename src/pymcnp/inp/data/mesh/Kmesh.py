import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Kmesh(MeshOption_, keyword='kmesh'):
    """
    Represents INP kmesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'kmesh(( {types.Real._REGEX.pattern})+)')

    def __init__(self, vector: types.Tuple[types.Real]):
        """
        Initializes ``Kmesh``.

        Parameters:
            vector: Locations of the coarse meshes in the z/theta directions.

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

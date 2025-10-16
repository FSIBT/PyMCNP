import re

from . import _option
from ... import types
from ... import errors


class Kmesh(_option.MeshOption):
    """
    Represents INP `kmesh` elements.
    """

    _KEYWORD = 'kmesh'

    _ATTRS = {
        'vector': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Akmesh((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, vector: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Kmesh`.

        Parameters:
            vector: Locations of the coarse meshes in the z/theta directions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vector: types.Tuple(types.Real) = vector

    @property
    def vector(self) -> types.Tuple(types.Real):
        """
        Locations of the coarse meshes in the z/theta directions

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vector

    @vector.setter
    def vector(self, vector: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `vector`.

        Parameters:
            vector: Locations of the coarse meshes in the z/theta directions.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vector is not None:
            array = []
            for item in vector:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            vector = types.Tuple(types.Real)(array)

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vector)

        self._vector: types.Tuple(types.Real) = vector

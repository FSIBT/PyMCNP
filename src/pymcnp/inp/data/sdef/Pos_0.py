import re

from . import _option
from .... import types
from .... import errors


class Pos_0(_option.SdefOption):
    """
    Represents INP pos variation #0 elements.
    """

    _KEYWORD = 'pos'

    _ATTRS = {
        'vector': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Apos((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, vector: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Pos_0``.

        Parameters:
            vector: Reference point for position sampling in vector notation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vector: types.Tuple(types.Real) = vector

    @property
    def vector(self) -> types.Tuple(types.Real):
        """
        Reference point for position sampling in vector notation

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vector

    @vector.setter
    def vector(self, vector: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``vector``.

        Parameters:
            vector: Reference point for position sampling in vector notation.

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

import re

from . import _option
from ... import types
from ... import errors


class Pos_1(_option.SdefOption):
    """
    Represents INP `pos` elements variation #1.
    """

    _KEYWORD = 'pos'

    _ATTRS = {
        'vector': types.Distribution,
    }

    _REGEX = re.compile(rf'\Apos( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, vector: str | types.Distribution):
        """
        Initializes `Pos_1`.

        Parameters:
            vector: Position sampling vector.
        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vector: types.Distribution = vector

    @property
    def vector(self) -> types.Tuple(types.Distribution):
        """
        Position sampling vector-coordinate.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vector

    @vector.setter
    def vector(self, vector: str | types.Distribution) -> None:
        """
        Sets `vector`.

        Parameters:
            vector: Position sampling vector-coordinate.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vector is not None:
            if isinstance(vector, types.Distribution):
                vector = vector
            elif isinstance(vector, str):
                vector = types.Distribution.from_mcnp(vector)

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vector)

        self._vector: types.Distribution = vector

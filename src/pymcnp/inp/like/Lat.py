import re

from . import _option
from ... import types
from ... import errors


class Lat(_option.LikeOption):
    """
    Represents INP `lat` elements.
    """

    _KEYWORD = 'lat'

    _ATTRS = {
        'shape': types.Integer,
    }

    _REGEX = re.compile(rf'\Alat( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, shape: str | int | types.Integer):
        """
        Initializes `Lat`.

        Parameters:
            shape: Cell lattice shape.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.shape: types.Integer = shape

    @property
    def shape(self) -> types.Integer:
        """
        Gets `shape`.

        Returns:
            `shape`.
        """

        return self._shape

    @shape.setter
    def shape(self, shape: str | int | types.Integer) -> None:
        """
        Sets `shape`.

        Parameters:
            shape: Cell lattice shape.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if shape is not None:
            if isinstance(shape, types.Integer):
                shape = shape
            elif isinstance(shape, int):
                shape = types.Integer(shape)
            elif isinstance(shape, str):
                shape = types.Integer.from_mcnp(shape)

        if shape is None or shape not in {1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, shape)

        self._shape: types.Integer = shape

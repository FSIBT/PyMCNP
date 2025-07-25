import re

from . import _option
from ... import types
from ... import errors


class Lat(_option.DataOption):
    """
    Represents INP lat elements.
    """

    _KEYWORD = 'lat'

    _ATTRS = {
        'type': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Alat((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, type: list[str] | list[int] | list[types.Integer]):
        """
        Initializes ``Lat``.

        Parameters:
            type: Tuple of lattice types.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.type: types.Tuple(types.Integer) = type

    @property
    def type(self) -> types.Tuple(types.Integer):
        """
        Tuple of lattice types

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._type

    @type.setter
    def type(self, type: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``type``.

        Parameters:
            type: Tuple of lattice types.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if type is not None:
            array = []
            for item in type:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            type = types.Tuple(types.Integer)(array)

        if type is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, type)

        self._type: types.Tuple(types.Integer) = type

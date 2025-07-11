import re

from . import _option
from ...utils import types
from ...utils import errors


class Lat(_option.DataOption):
    """
    Represents INP lat elements.

    Attributes:
        type: Tuple of lattice types.
    """

    _KEYWORD = 'lat'

    _ATTRS = {
        'type': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Alat((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, type: list[str] | list[int] | list[types.Integer]):
        """
        Initializes ``Lat``.

        Parameters:
            type: Tuple of lattice types.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.type: types.Tuple[types.Integer] = type

    @property
    def type(self) -> types.Tuple[types.Integer]:
        """
        Gets ``type``.

        Returns:
            ``type``.
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
                else:
                    raise TypeError
            type = types.Tuple(array)

        if type is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, type)

        self._type: types.Tuple[types.Integer] = type

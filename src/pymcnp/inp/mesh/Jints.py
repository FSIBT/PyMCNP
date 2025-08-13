import re

from . import _option
from ... import types
from ... import errors


class Jints(_option.MeshOption):
    """
    Represents INP `jints` elements.
    """

    _KEYWORD = 'jints'

    _ATTRS = {
        'number': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Ajints((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, number: list[str] | list[int] | list[types.Integer]):
        """
        Initializes `Jints`.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the y/z directions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.number: types.Tuple(types.Integer) = number

    @property
    def number(self) -> types.Tuple(types.Integer):
        """
        Number of fine meshes within corresponding coarse meshes in the y/z directions

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `number`.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the y/z directions.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            array = []
            for item in number:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            number = types.Tuple(types.Integer)(array)

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self._number: types.Tuple(types.Integer) = number

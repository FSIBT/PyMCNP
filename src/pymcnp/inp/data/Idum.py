import re

from . import _option
from ... import types
from ... import errors


class Idum(_option.DataOption):
    """
    Represents INP idum elements.
    """

    _KEYWORD = 'idum'

    _ATTRS = {
        'intergers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aidum((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, intergers: list[str] | list[int] | list[types.Integer]):
        """
        Initializes ``Idum``.

        Parameters:
            intergers: Integer array.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.intergers: types.Tuple[types.Integer] = intergers

    @property
    def intergers(self) -> types.Tuple[types.Integer]:
        """
        Integer array

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._intergers

    @intergers.setter
    def intergers(self, intergers: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``intergers``.

        Parameters:
            intergers: Integer array.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if intergers is not None:
            array = []
            for item in intergers:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            intergers = types.Tuple(array)

        if intergers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, intergers)

        self._intergers: types.Tuple[types.Integer] = intergers

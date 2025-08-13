import re

from . import _option
from ... import types
from ... import errors


class Iu(_option.DfOption_1):
    """
    Represents INP `iu` elements.
    """

    _KEYWORD = 'iu'

    _ATTRS = {
        'units': types.Integer,
    }

    _REGEX = re.compile(rf'\Aiu( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, units: str | int | types.Integer):
        """
        Initializes `Iu`.

        Parameters:
            units: Control units.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.units: types.Integer = units

    @property
    def units(self) -> types.Integer:
        """
        Control units

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._units

    @units.setter
    def units(self, units: str | int | types.Integer) -> None:
        """
        Sets `units`.

        Parameters:
            units: Control units.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if units is not None:
            if isinstance(units, types.Integer):
                units = units
            elif isinstance(units, int):
                units = types.Integer(units)
            elif isinstance(units, str):
                units = types.Integer.from_mcnp(units)

        if units is None or not (isinstance(units.value, types.Jump) or units in {1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, units)

        self._units: types.Integer = units

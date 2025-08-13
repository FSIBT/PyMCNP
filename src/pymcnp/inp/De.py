import re

from . import _card
from .. import types
from .. import errors


class De(_card.Card):
    """
    Represents INP de cards.
    """

    _KEYWORD = 'de'

    _ATTRS = {
        'suffix': types.Integer,
        'method': types.String,
        'values': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Ade(\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, values: list[str] | list[float] | list[types.Real], method: str | types.String = None):
        """
        Initializes `De`.

        Parameters:
            suffix: Data card option suffix.
            method: Interpolation method for energy table.
            values: Energy values.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.method: types.String = method
        self.values: types.Tuple(types.Real) = values

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def method(self) -> types.String:
        """
        Interpolation method for energy table

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._method

    @method.setter
    def method(self, method: str | types.String) -> None:
        """
        Sets `method`.

        Parameters:
            method: Interpolation method for energy table.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if method is not None:
            if isinstance(method, types.String):
                method = method
            elif isinstance(method, str):
                method = types.String.from_mcnp(method)

        if method is not None and method.value.lower() not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, method)

        self._method: types.String = method

    @property
    def values(self) -> types.Tuple(types.Real):
        """
        Energy values

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._values

    @values.setter
    def values(self, values: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `values`.

        Parameters:
            values: Energy values.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if values is not None:
            array = []
            for item in values:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            values = types.Tuple(types.Real)(array)

        if values is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, values)

        self._values: types.Tuple(types.Real) = values

import re

from . import _card
from .. import types
from .. import errors


class Ds_0(_card.Card):
    """
    Represents INP `ds` elements variation #0.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'js': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Ads(\d+)( [hls])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, js: list[str] | list[float] | list[types.Real], option: str | types.String = None):
        """
        Initializes `Ds_0`.

        Parameters:
            suffix: Data card option suffix.
            option: Dependent variable setting.
            js: Depdented source dependent variables.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.option: types.String = option
        self.js: types.Tuple(types.Real) = js

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

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def option(self) -> types.String:
        """
        Dependent variable setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | types.String) -> None:
        """
        Sets `option`.

        Parameters:
            option: Dependent variable setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if option is not None:
            if isinstance(option, types.String):
                option = option
            elif isinstance(option, str):
                option = types.String.from_mcnp(option)

        if option is not None and option.value.lower() not in {'h', 'l', 's'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, option)

        self._option: types.String = option

    @property
    def js(self) -> types.Tuple(types.Real):
        """
        Depdented source dependent variables

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._js

    @js.setter
    def js(self, js: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `js`.

        Parameters:
            js: Depdented source dependent variables.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if js is not None:
            array = []
            for item in js:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            js = types.Tuple(types.Real)(array)

        if js is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, js)

        self._js: types.Tuple(types.Real) = js

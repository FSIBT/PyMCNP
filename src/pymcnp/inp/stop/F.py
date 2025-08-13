import re

from . import _option
from ... import types
from ... import errors


class F(_option.StopOption):
    """
    Represents INP `f` elements.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'suffix': types.Integer,
        'e': types.Integer,
    }

    _REGEX = re.compile(rf'\Af(\d+)( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, e: str | int | types.Integer):
        """
        Initializes `F`.

        Parameters:
            suffix: Data card option option suffix.
            e: Tally fluctuation relative error before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.e: types.Integer = e

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def e(self) -> types.Integer:
        """
        Tally fluctuation relative error before stop

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._e

    @e.setter
    def e(self, e: str | int | types.Integer) -> None:
        """
        Sets `e`.

        Parameters:
            e: Tally fluctuation relative error before stop.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if e is not None:
            if isinstance(e, types.Integer):
                e = e
            elif isinstance(e, int):
                e = types.Integer(e)
            elif isinstance(e, str):
                e = types.Integer.from_mcnp(e)

        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, e)

        self._e: types.Integer = e

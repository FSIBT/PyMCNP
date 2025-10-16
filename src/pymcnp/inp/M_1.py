import re

from . import _card
from .. import types
from .. import errors


class M_1(_card.Card):
    """
    Represents INP `m` elements variation #1.
    """

    _KEYWORD = 'm'

    _ATTRS = {
        'suffix': types.Integer,
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Am(\d+)( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, abx: str | types.String):
        """
        Initializes `M_1`.

        Parameters:
            suffix: Data card option suffix.
            abx: Material library.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.abx: types.String = abx

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

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def abx(self) -> types.String:
        """
        Material library

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._abx

    @abx.setter
    def abx(self, abx: str | types.String) -> None:
        """
        Sets `abx`.

        Parameters:
            abx: Material library.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if abx is not None:
            if isinstance(abx, types.String):
                abx = abx
            elif isinstance(abx, str):
                abx = types.String.from_mcnp(abx)

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, abx)

        self._abx: types.String = abx

import re

from . import _card
from .. import types
from .. import errors


class Fc(_card.Card):
    """
    Represents INP `fc` cards.
    """

    _KEYWORD = 'fc'

    _ATTRS = {
        'suffix': types.Integer,
        'info': types.String,
    }

    _REGEX = re.compile(r'\Afc(\d+)( [\S\s]+)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, info: str | types.String):
        """
        Initializes `Fc`.

        Parameters:
            suffix: Data card option suffix.
            info: Title for tally in output and MCTAL file.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.info: types.String = info

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
    def info(self) -> types.String:
        """
        Title for tally in output and MCTAL file

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._info

    @info.setter
    def info(self, info: str | types.String) -> None:
        """
        Sets `info`.

        Parameters:
            info: Title for tally in output and MCTAL file.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if info is not None:
            if isinstance(info, types.String):
                info = info
            elif isinstance(info, str):
                info = types.String.from_mcnp(info)

        if info is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, info)

        self._info: types.String = info

import re

from . import _card
from .. import types
from .. import errors


class Ft(_card.Card):
    """
    Represents INP `ft` cards.
    """

    _KEYWORD = 'ft'

    _ATTRS = {
        'suffix': types.Integer,
        'treatments': types.String,
    }

    _REGEX = re.compile(r'\Aft(\d+)( [\S\s]+)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, treatments: str | types.String):
        """
        Initializes `Ft`.

        Parameters:
            suffix: Data card option suffix.
            treatments: Tally special treatments.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.treatments: types.String = treatments

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
    def treatments(self) -> types.String:
        """
        Tally special treatments

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._treatments

    @treatments.setter
    def treatments(self, treatments: str | types.String) -> None:
        """
        Sets `treatments`.

        Parameters:
            treatments: Tally special treatments.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if treatments is not None:
            if isinstance(treatments, types.String):
                treatments = treatments
            elif isinstance(treatments, str):
                treatments = types.String.from_mcnp(treatments)

        if treatments is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, treatments)

        self._treatments: types.String = treatments

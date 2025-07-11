import re

from . import _option
from ...utils import types
from ...utils import errors


class Ft(_option.DataOption):
    """
    Represents INP ft elements.

    Attributes:
        suffix: Data card option suffix.
        treatments: Tally special treatments.
    """

    _KEYWORD = 'ft'

    _ATTRS = {
        'suffix': types.Integer,
        'treatments': types.String,
    }

    _REGEX = re.compile(r'\Aft(\d+)( [\S\s]+)\Z')

    def __init__(self, suffix: str | int | types.Integer, treatments: str | types.String):
        """
        Initializes ``Ft``.

        Parameters:
            suffix: Data card option suffix.
            treatments: Tally special treatments.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.treatments: types.String = treatments

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

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
            else:
                raise TypeError

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def treatments(self) -> types.String:
        """
        Gets ``treatments``.

        Returns:
            ``treatments``.
        """

        return self._treatments

    @treatments.setter
    def treatments(self, treatments: str | types.String) -> None:
        """
        Sets ``treatments``.

        Parameters:
            treatments: Tally special treatments.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if treatments is not None:
            if isinstance(treatments, types.String):
                treatments = treatments
            elif isinstance(treatments, str):
                treatments = types.String.from_mcnp(treatments)
            else:
                raise TypeError

        if treatments is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, treatments)

        self._treatments: types.String = treatments

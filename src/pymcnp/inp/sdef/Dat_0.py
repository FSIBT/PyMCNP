import re

from . import _option
from ... import types
from ... import errors


class Dat_0(_option.SdefOption):
    """
    Represents INP `dat` elements variation #0.
    """

    _KEYWORD = 'dat'

    _ATTRS = {
        'month': types.Integer,
        'day': types.Integer,
        'year': types.Integer,
    }

    _REGEX = re.compile(rf'\Adat( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, month: str | int | types.Integer, day: str | int | types.Integer, year: str | int | types.Integer):
        """
        Initializes `Dat_0`.

        Parameters:
            month: Month for cosmic-ray & background sources.
            day: Day for cosmic-ray & background sources.
            year: Year for cosmic-ray & background sources.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.month: types.Integer = month
        self.day: types.Integer = day
        self.year: types.Integer = year

    @property
    def month(self) -> types.Integer:
        """
        Month for cosmic-ray & background sources

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._month

    @month.setter
    def month(self, month: str | int | types.Integer) -> None:
        """
        Sets `month`.

        Parameters:
            month: Month for cosmic-ray & background sources.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if month is not None:
            if isinstance(month, types.Integer):
                month = month
            elif isinstance(month, int):
                month = types.Integer(month)
            elif isinstance(month, str):
                month = types.Integer.from_mcnp(month)

        if month is None or not (month >= 1 and month <= 12):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, month)

        self._month: types.Integer = month

    @property
    def day(self) -> types.Integer:
        """
        Day for cosmic-ray & background sources

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._day

    @day.setter
    def day(self, day: str | int | types.Integer) -> None:
        """
        Sets `day`.

        Parameters:
            day: Day for cosmic-ray & background sources.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if day is not None:
            if isinstance(day, types.Integer):
                day = day
            elif isinstance(day, int):
                day = types.Integer(day)
            elif isinstance(day, str):
                day = types.Integer.from_mcnp(day)

        if day is None or not (day >= 1 and day <= 31):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, day)

        self._day: types.Integer = day

    @property
    def year(self) -> types.Integer:
        """
        Year for cosmic-ray & background sources

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._year

    @year.setter
    def year(self, year: str | int | types.Integer) -> None:
        """
        Sets `year`.

        Parameters:
            year: Year for cosmic-ray & background sources.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if year is not None:
            if isinstance(year, types.Integer):
                year = year
            elif isinstance(year, int):
                year = types.Integer(year)
            elif isinstance(year, str):
                year = types.Integer.from_mcnp(year)

        if year is None or not (year >= 1 and year <= 9999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, year)

        self._year: types.Integer = year

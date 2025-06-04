import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Dat(SdefOption):
    """
    Represents INP dat elements.

    Attributes:
        month: Month for cosmic-ray & background sources.
        day: Day for cosmic-ray & background sources.
        year: Year for cosmic-ray & background sources.
    """

    _KEYWORD = 'dat'

    _ATTRS = {
        'month': types.Integer,
        'day': types.Integer,
        'year': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Adat( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, month: types.Integer, day: types.Integer, year: types.Integer):
        """
        Initializes ``Dat``.

        Parameters:
            month: Month for cosmic-ray & background sources.
            day: Day for cosmic-ray & background sources.
            year: Year for cosmic-ray & background sources.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if month is None or not (1 <= month.value <= 12):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, month)
        if day is None or not (1 <= day.value <= 31):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, day)
        if year is None or not (1 <= year.value <= 9999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, year)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                month,
                day,
                year,
            ]
        )

        self.month: typing.Final[types.Integer] = month
        self.day: typing.Final[types.Integer] = day
        self.year: typing.Final[types.Integer] = year


@dataclasses.dataclass
class DatBuilder:
    """
    Builds ``Dat``.

    Attributes:
        month: Month for cosmic-ray & background sources.
        day: Day for cosmic-ray & background sources.
        year: Year for cosmic-ray & background sources.
    """

    month: str | int | types.Integer
    day: str | int | types.Integer
    year: str | int | types.Integer

    def build(self):
        """
        Builds ``DatBuilder`` into ``Dat``.

        Returns:
            ``Dat`` for ``DatBuilder``.
        """

        month = self.month
        if isinstance(self.month, types.Integer):
            month = self.month
        elif isinstance(self.month, int):
            month = types.Integer(self.month)
        elif isinstance(self.month, str):
            month = types.Integer.from_mcnp(self.month)

        day = self.day
        if isinstance(self.day, types.Integer):
            day = self.day
        elif isinstance(self.day, int):
            day = types.Integer(self.day)
        elif isinstance(self.day, str):
            day = types.Integer.from_mcnp(self.day)

        year = self.year
        if isinstance(self.year, types.Integer):
            year = self.year
        elif isinstance(self.year, int):
            year = types.Integer(self.year)
        elif isinstance(self.year, str):
            year = types.Integer.from_mcnp(self.year)

        return Dat(
            month=month,
            day=day,
            year=year,
        )

    @staticmethod
    def unbuild(ast: Dat):
        """
        Unbuilds ``Dat`` into ``DatBuilder``

        Returns:
            ``DatBuilder`` for ``Dat``.
        """

        return Dat(
            month=copy.deepcopy(ast.month),
            day=copy.deepcopy(ast.day),
            year=copy.deepcopy(ast.year),
        )

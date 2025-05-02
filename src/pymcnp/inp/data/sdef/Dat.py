import re
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

    _ATTRS = {
        'month': types.IntegerOrJump,
        'day': types.IntegerOrJump,
        'year': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Adat( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self, month: types.IntegerOrJump, day: types.IntegerOrJump, year: types.IntegerOrJump
    ):
        """
        Initializes ``Dat``.

        Parameters:
            month: Month for cosmic-ray & background sources.
            day: Day for cosmic-ray & background sources.
            year: Year for cosmic-ray & background sources.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if month is None or not (1 <= month <= 12):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, month)
        if day is None or not (1 <= day <= 31):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, day)
        if year is None or not (1 <= year <= 9999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, year)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                month,
                day,
                year,
            ]
        )

        self.month: typing.Final[types.IntegerOrJump] = month
        self.day: typing.Final[types.IntegerOrJump] = day
        self.year: typing.Final[types.IntegerOrJump] = year


@dataclasses.dataclass
class DatBuilder:
    """
    Builds ``Dat``.

    Attributes:
        month: Month for cosmic-ray & background sources.
        day: Day for cosmic-ray & background sources.
        year: Year for cosmic-ray & background sources.
    """

    month: str | int | types.IntegerOrJump
    day: str | int | types.IntegerOrJump
    year: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``DatBuilder`` into ``Dat``.

        Returns:
            ``Dat`` for ``DatBuilder``.
        """

        if isinstance(self.month, types.Integer):
            month = self.month
        elif isinstance(self.month, int):
            month = types.IntegerOrJump(self.month)
        elif isinstance(self.month, str):
            month = types.IntegerOrJump.from_mcnp(self.month)

        if isinstance(self.day, types.Integer):
            day = self.day
        elif isinstance(self.day, int):
            day = types.IntegerOrJump(self.day)
        elif isinstance(self.day, str):
            day = types.IntegerOrJump.from_mcnp(self.day)

        if isinstance(self.year, types.Integer):
            year = self.year
        elif isinstance(self.year, int):
            year = types.IntegerOrJump(self.year)
        elif isinstance(self.year, str):
            year = types.IntegerOrJump.from_mcnp(self.year)

        return Dat(
            month=month,
            day=day,
            year=year,
        )

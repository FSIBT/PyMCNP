import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Dat(SdefOption_, keyword='dat'):
    """
    Represents INP dat elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if month is None or not (1 <= month <= 12):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, month)
        if day is None or not (1 <= day <= 31):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, day)
        if year is None or not (1 <= year <= 9999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, year)

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

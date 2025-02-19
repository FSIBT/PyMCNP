import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Dat(_option.SdefOption_, keyword='dat'):
    """
    Represents INP data card data option dat options.

    Attributes:
        month: Month for cosmic-ray & background sources.
        day: Day for cosmic-ray & background sources.
        year: Year for cosmic-ray & background sources.
    """

    _REGEX = re.compile(r'\Adat( \S+)( \S+)( \S+)\Z')

    def __init__(self, month: types.Integer, day: types.Integer, year: types.Integer):
        """
        Initializes ``SdefOption_Dat``.

        Parameters:
            month: Month for cosmic-ray & background sources.
            day: Day for cosmic-ray & background sources.
            year: Year for cosmic-ray & background sources.

        Returns:
            ``SdefOption_Dat``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if month is None or not (1 <= month <= 12):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, month)
        if day is None or not (1 <= day <= 31):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, day)
        if year is None or not (1 <= year <= 9999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, year)

        self.value: typing.Final[tuple[any]] = types._Tuple([month, day, year])
        self.month: typing.Final[types.Integer] = month
        self.day: typing.Final[types.Integer] = day
        self.year: typing.Final[types.Integer] = year

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Dat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Dat``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Dat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        month = types.Integer.from_mcnp(tokens[1])
        day = types.Integer.from_mcnp(tokens[2])
        year = types.Integer.from_mcnp(tokens[3])

        return SdefOption_Dat(month, day, year)

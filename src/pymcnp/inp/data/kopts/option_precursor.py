import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Precursor(_option.KoptsOption_, keyword='precursor'):
    """
    Represents INP data card data option precursor options.

    Attributes:
        setting: Yes/No detailed precursor information.
    """

    _REGEX = re.compile(r'\Aprecursor( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``KoptsOption_Precursor``.

        Parameters:
            setting: Yes/No detailed precursor information.

        Returns:
            ``KoptsOption_Precursor``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Precursor`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Precursor``.

        Raises:
            McnpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Precursor._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KOPTS_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return KoptsOption_Precursor(setting)

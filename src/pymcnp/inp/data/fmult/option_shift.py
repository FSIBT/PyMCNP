import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmultOption_Shift(_option.FmultOption_, keyword='shift'):
    """
    Represents INP data card data option shift options.

    Attributes:
        setting: Shift method setting.
    """

    _REGEX = re.compile(r'\Ashift( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``FmultOption_Shift``.

        Parameters:
            setting: Shift method setting.

        Returns:
            ``FmultOption_Shift``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmultOption_Shift`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmultOption_Shift``.

        Raises:
            InpError: SYNTAX_FMULT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmultOption_Shift._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return FmultOption_Shift(setting)

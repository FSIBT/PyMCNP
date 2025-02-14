import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SswOption_Sym(_option.SswOption_, keyword='sym'):
    """
    Represents INP data card data option sym options.

    Attributes:
        setting: Symmetric option flag.
    """

    _REGEX = re.compile(r'\Asym( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``SswOption_Sym``.

        Parameters:
            setting: Symmetric option flag.

        Returns:
            ``SswOption_Sym``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {0, 1, 2}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SswOption_Sym`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SswOption_Sym``.

        Raises:
            McnpError: SYNTAX_SSW_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SswOption_Sym._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SSW_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return SswOption_Sym(setting)

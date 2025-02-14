import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmultOption_Data(_option.FmultOption_, keyword='data'):
    """
    Represents INP data card data option data options.

    Attributes:
        setting: Sampling method setting.
    """

    _REGEX = re.compile(r'\Adata( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``FmultOption_Data``.

        Parameters:
            setting: Sampling method setting.

        Returns:
            ``FmultOption_Data``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 2, 3}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmultOption_Data`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmultOption_Data``.

        Raises:
            McnpError: SYNTAX_FMULT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmultOption_Data._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMULT_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return FmultOption_Data(setting)

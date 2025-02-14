import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Sample(_option.ActOption_, keyword='sample'):
    """
    Represents INP data card data option sample options.

    Attributes:
        setting: Flag for correlated or uncorrelated.
    """

    _REGEX = re.compile(r'\Asample( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``ActOption_Sample``.

        Parameters:
            setting: Flag for correlated or uncorrelated.

        Returns:
            ``ActOption_Sample``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'correlate', 'nonfiss_cor'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Sample`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Sample``.

        Raises:
            McnpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Sample._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ACT_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return ActOption_Sample(setting)

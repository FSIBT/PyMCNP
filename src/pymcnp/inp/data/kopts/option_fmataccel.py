import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmataccel(_option.KoptsOption_, keyword='fmataccel'):
    """
    Represents INP data card data option fmataccel options.

    Attributes:
        setting: fmataccel.
    """

    _REGEX = re.compile(r'\Afmataccel( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``KoptsOption_Fmataccel``.

        Parameters:
            setting: fmataccel.

        Returns:
            ``KoptsOption_Fmataccel``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmataccel`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmataccel``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmataccel._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return KoptsOption_Fmataccel(setting)

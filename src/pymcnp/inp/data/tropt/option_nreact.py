import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TroptOption_Nreact(_option.TroptOption_, keyword='nreact'):
    """
    Represents INP data card data option nreact options.

    Attributes:
        setting: Nuclear reactions setting.
    """

    _REGEX = re.compile(r'\Anreact( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``TroptOption_Nreact``.

        Parameters:
            setting: Nuclear reactions setting.

        Returns:
            ``TroptOption_Nreact``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'off', 'on', 'atten', 'remove'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TroptOption_Nreact`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``TroptOption_Nreact``.

        Raises:
            InpError: SYNTAX_TROPT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TroptOption_Nreact._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return TroptOption_Nreact(setting)

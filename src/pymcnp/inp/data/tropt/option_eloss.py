import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TroptOption_Eloss(_option.TroptOption_, keyword='eloss'):
    """
    Represents INP data card data option eloss options.

    Attributes:
        setting: Slowing down energy losses setting.
    """

    _REGEX = re.compile(r'\Aeloss( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``TroptOption_Eloss``.

        Parameters:
            setting: Slowing down energy losses setting.

        Returns:
            ``TroptOption_Eloss``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'off', 'strag1', 'csda'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TroptOption_Eloss`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``TroptOption_Eloss``.

        Raises:
            InpError: SYNTAX_TROPT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TroptOption_Eloss._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return TroptOption_Eloss(setting)

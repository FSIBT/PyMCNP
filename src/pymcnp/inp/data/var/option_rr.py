import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class VarOption_Rr(_option.VarOption_, keyword='rr'):
    """
    Represents INP data card data option rr options.

    Attributes:
        setting: Roulette game for weight windows and cell/energy/time importance off/no.
    """

    _REGEX = re.compile(r'\Arr( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``VarOption_Rr``.

        Parameters:
            setting: Roulette game for weight windows and cell/energy/time importance off/no.

        Returns:
            ``VarOption_Rr``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'no', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``VarOption_Rr`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``VarOption_Rr``.

        Raises:
            InpError: SYNTAX_VAR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = VarOption_Rr._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return VarOption_Rr(setting)

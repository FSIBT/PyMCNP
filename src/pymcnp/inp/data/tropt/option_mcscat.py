import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TroptOption_Mcscat(_option.TroptOption_, keyword='mcscat'):
    """
    Represents INP data card data option mcscat options.

    Attributes:
        setting: Multiple coulomb scattering setting.
    """

    _REGEX = re.compile(r'\Amcscat( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``TroptOption_Mcscat``.

        Parameters:
            setting: Multiple coulomb scattering setting.

        Returns:
            ``TroptOption_Mcscat``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'off', 'fnal1', 'gaussian', 'fnal2'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TroptOption_Mcscat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``TroptOption_Mcscat``.

        Raises:
            InpError: SYNTAX_TROPT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TroptOption_Mcscat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return TroptOption_Mcscat(setting)

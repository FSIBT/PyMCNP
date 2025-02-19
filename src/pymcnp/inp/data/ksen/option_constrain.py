import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KsenOption_Constrain(_option.KsenOption_, keyword='constrain'):
    """
    Represents INP data card data option constrain options.

    Attributes:
        setting: Renormalize sensitivity distribution on/off.
    """

    _REGEX = re.compile(r'\Aconstrain( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``KsenOption_Constrain``.

        Parameters:
            setting: Renormalize sensitivity distribution on/off.

        Returns:
            ``KsenOption_Constrain``.

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
        Generates ``KsenOption_Constrain`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KsenOption_Constrain``.

        Raises:
            InpError: SYNTAX_KSEN_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KsenOption_Constrain._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return KsenOption_Constrain(setting)

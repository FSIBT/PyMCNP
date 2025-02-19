import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmat(_option.KoptsOption_, keyword='fmat'):
    """
    Represents INP data card data option fmat options.

    Attributes:
        setting: Yes/No FMAT.
    """

    _REGEX = re.compile(r'\Afmat( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``KoptsOption_Fmat``.

        Parameters:
            setting: Yes/No FMAT.

        Returns:
            ``KoptsOption_Fmat``.

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
        Generates ``KoptsOption_Fmat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmat``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return KoptsOption_Fmat(setting)

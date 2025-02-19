import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Col(_option.SsrOption_, keyword='col'):
    """
    Represents INP data card data option col options.

    Attributes:
        setting: Collision option setting.
    """

    _REGEX = re.compile(r'\Acol( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``SsrOption_Col``.

        Parameters:
            setting: Collision option setting.

        Returns:
            ``SsrOption_Col``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Col`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Col``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Col._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return SsrOption_Col(setting)

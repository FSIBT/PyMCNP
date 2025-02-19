import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Type(_option.FmeshOption_, keyword='type'):
    """
    Represents INP data card data option type options.

    Attributes:
        setting: Tally quantity.
    """

    _REGEX = re.compile(r'\Atype( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``FmeshOption_Type``.

        Parameters:
            setting: Tally quantity.

        Returns:
            ``FmeshOption_Type``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'flux', 'source'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Type`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Type``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Type._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return FmeshOption_Type(setting)

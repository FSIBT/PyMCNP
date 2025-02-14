import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Tnorm(_option.FmeshOption_, keyword='tnorm'):
    """
    Represents INP data card data option tnorm options.

    Attributes:
        setting: Tally results divided by time yes/no.
    """

    _REGEX = re.compile(r'\Atnorm( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``FmeshOption_Tnorm``.

        Parameters:
            setting: Tally results divided by time yes/no.

        Returns:
            ``FmeshOption_Tnorm``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Tnorm`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Tnorm``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Tnorm._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return FmeshOption_Tnorm(setting)

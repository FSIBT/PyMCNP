import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Out(_option.FmeshOption_, keyword='out'):
    """
    Represents INP data card data option out options.

    Attributes:
        setting: Output format.
    """

    _REGEX = re.compile(r'\Aout( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``FmeshOption_Out``.

        Parameters:
            setting: Output format.

        Returns:
            ``FmeshOption_Out``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'col', 'cf', 'ij', 'ik', 'jk', 'none'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Out`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Out``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Out._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return FmeshOption_Out(setting)

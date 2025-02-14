import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Gas(_option.MOption_, keyword='gas'):
    """
    Represents INP data card data option gas options.

    Attributes:
        setting: Flag for density-effect correction to electron stopping power.
    """

    _REGEX = re.compile(r'\Agas( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``MOption_Gas``.

        Parameters:
            setting: Flag for density-effect correction to electron stopping power.

        Returns:
            ``MOption_Gas``.

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
        Generates ``MOption_Gas`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Gas``.

        Raises:
            McnpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Gas._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_M_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return MOption_Gas(setting)

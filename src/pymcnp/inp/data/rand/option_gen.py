import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class RandOption_Gen(_option.RandOption_, keyword='gen'):
    """
    Represents INP data card data option gen options.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    _REGEX = re.compile(r'\Agen( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``RandOption_Gen``.

        Parameters:
            setting: Type of pseudorandom number generator.

        Returns:
            ``RandOption_Gen``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``RandOption_Gen`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``RandOption_Gen``.

        Raises:
            InpError: SYNTAX_RAND_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = RandOption_Gen._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return RandOption_Gen(setting)

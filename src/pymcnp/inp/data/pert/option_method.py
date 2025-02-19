import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PertOption_Method(_option.PertOption_, keyword='method'):
    """
    Represents INP data card data option method options.

    Attributes:
        setting: Printing and specifies setting.
    """

    _REGEX = re.compile(r'\Amethod( \S+)\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``PertOption_Method``.

        Parameters:
            setting: Printing and specifies setting.

        Returns:
            ``PertOption_Method``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {+1, -1, +2, -2, +3, -3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.Integer] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PertOption_Method`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PertOption_Method``.

        Raises:
            InpError: SYNTAX_PERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PertOption_Method._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])

        return PertOption_Method(setting)

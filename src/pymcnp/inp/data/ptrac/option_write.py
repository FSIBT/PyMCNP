import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Write(_option.PtracOption_, keyword='write'):
    """
    Represents INP data card data option write options.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    _REGEX = re.compile(r'\Awrite( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``PtracOption_Write``.

        Parameters:
            setting: Controls what particle parameters are written.

        Returns:
            ``PtracOption_Write``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'pos', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Write`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Write``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Write._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return PtracOption_Write(setting)

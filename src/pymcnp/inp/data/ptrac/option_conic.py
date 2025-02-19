import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Conic(_option.PtracOption_, keyword='conic'):
    """
    Represents INP data card data option conic options.

    Attributes:
        setting: Activates a PTRAC file format specifically for coincidence tally scoring.
    """

    _REGEX = re.compile(r'\Aconic( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``PtracOption_Conic``.

        Parameters:
            setting: Activates a PTRAC file format specifically for coincidence tally scoring.

        Returns:
            ``PtracOption_Conic``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'col', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Conic`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Conic``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Conic._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return PtracOption_Conic(setting)

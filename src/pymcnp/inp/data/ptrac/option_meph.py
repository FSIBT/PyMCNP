import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Meph(_option.PtracOption_, keyword='meph'):
    """
    Represents INP data card data option meph options.

    Attributes:
        events: Maximum number of events per history to write.
    """

    _REGEX = re.compile(r'\Ameph( \S+)\Z')

    def __init__(self, events: types.Integer):
        """
        Initializes ``PtracOption_Meph``.

        Parameters:
            events: Maximum number of events per history to write.

        Returns:
            ``PtracOption_Meph``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if events is None or not (events > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, events)

        self.value: typing.Final[tuple[any]] = types._Tuple([events])
        self.events: typing.Final[types.Integer] = events

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Meph`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Meph``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Meph._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        events = types.Integer.from_mcnp(tokens[1])

        return PtracOption_Meph(events)

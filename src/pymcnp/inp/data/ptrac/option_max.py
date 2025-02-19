import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Max(_option.PtracOption_, keyword='max'):
    """
    Represents INP data card data option max options.

    Attributes:
        events: Maximum number of events to write.
    """

    _REGEX = re.compile(r'\Amax( \S+)\Z')

    def __init__(self, events: types.Integer):
        """
        Initializes ``PtracOption_Max``.

        Parameters:
            events: Maximum number of events to write.

        Returns:
            ``PtracOption_Max``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if events is None or not (events != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, events)

        self.value: typing.Final[tuple[any]] = types._Tuple([events])
        self.events: typing.Final[types.Integer] = events

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Max`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Max``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Max._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        events = types.Integer.from_mcnp(tokens[1])

        return PtracOption_Max(events)

import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Lost(_option.DataOption_, keyword='lost'):
    """
    Represents INP data card lost options.

    Attributes:
        lost1: Number of particles which can be lost before job termination.
        lost2: Maximum number of debug prints for lost particles..
    """

    _REGEX = re.compile(r'\Alost( \S+)( \S+)\Z')

    def __init__(self, lost1: types.Integer, lost2: types.Integer):
        """
        Initializes ``DataOption_Lost``.

        Parameters:
            lost1: Number of particles which can be lost before job termination.
            lost2: Maximum number of debug prints for lost particles..

        Returns:
            ``DataOption_Lost``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if lost1 is None or not (lost1 >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, lost1)
        if lost2 is None or not (lost2 >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, lost2)

        self.value: typing.Final[tuple[any]] = types._Tuple([lost1, lost2])
        self.lost1: typing.Final[types.Integer] = lost1
        self.lost2: typing.Final[types.Integer] = lost2

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Lost`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Lost``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Lost._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        lost1 = types.Integer.from_mcnp(tokens[1])
        lost2 = types.Integer.from_mcnp(tokens[2])

        return DataOption_Lost(lost1, lost2)

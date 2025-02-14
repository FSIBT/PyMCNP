import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class BfldOption_Maxstep(_option.BfldOption_, keyword='maxstep'):
    """
    Represents INP data card data option maxstep options.

    Attributes:
        size: Maximum step size.
    """

    _REGEX = re.compile(r'\Amaxstep( \S+)\Z')

    def __init__(self, size: types.Real):
        """
        Initializes ``BfldOption_Maxstep``.

        Parameters:
            size: Maximum step size.

        Returns:
            ``BfldOption_Maxstep``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if size is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, size)

        self.value: typing.Final[tuple[any]] = types._Tuple([size])
        self.size: typing.Final[types.Real] = size

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BfldOption_Maxstep`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``BfldOption_Maxstep``.

        Raises:
            McnpError: SYNTAX_BFLD_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BfldOption_Maxstep._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BFLD_OPTION, source)

        size = types.Real.from_mcnp(tokens[1])

        return BfldOption_Maxstep(size)

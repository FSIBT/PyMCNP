import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class BfldOption_Maxdeflc(_option.BfldOption_, keyword='maxdeflc'):
    """
    Represents INP data card data option maxdeflc options.

    Attributes:
        angle: Maximum deflection angles.
    """

    _REGEX = re.compile(r'\Amaxdeflc( \S+)\Z')

    def __init__(self, angle: types.Real):
        """
        Initializes ``BfldOption_Maxdeflc``.

        Parameters:
            angle: Maximum deflection angles.

        Returns:
            ``BfldOption_Maxdeflc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if angle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, angle)

        self.value: typing.Final[tuple[any]] = types._Tuple([angle])
        self.angle: typing.Final[types.Real] = angle

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BfldOption_Maxdeflc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``BfldOption_Maxdeflc``.

        Raises:
            InpError: SYNTAX_BFLD_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BfldOption_Maxdeflc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        angle = types.Real.from_mcnp(tokens[1])

        return BfldOption_Maxdeflc(angle)

import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class DawwgOption_Xsec(_option.DawwgOption_, keyword='xsec'):
    """
    Represents INP data card data option xsec options.

    Attributes:
        count: Number of sample points for each direction in each mesh.
    """

    _REGEX = re.compile(r'\Axsec( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``DawwgOption_Xsec``.

        Parameters:
            count: Number of sample points for each direction in each mesh.

        Returns:
            ``DawwgOption_Xsec``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if count is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, count)

        self.value: typing.Final[tuple[any]] = types._Tuple([count])
        self.count: typing.Final[types.Integer] = count

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DawwgOption_Xsec`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``DawwgOption_Xsec``.

        Raises:
            McnpError: SYNTAX_DAWWG_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DawwgOption_Xsec._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DAWWG_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return DawwgOption_Xsec(count)

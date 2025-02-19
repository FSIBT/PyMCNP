import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Tints(_option.FmeshOption_, keyword='tints'):
    """
    Represents INP data card data option tints options.

    Attributes:
        count: Number of mesh points for each mesh time.
    """

    _REGEX = re.compile(r'\Atints( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``FmeshOption_Tints``.

        Parameters:
            count: Number of mesh points for each mesh time.

        Returns:
            ``FmeshOption_Tints``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[tuple[any]] = types._Tuple([count])
        self.count: typing.Final[types.Integer] = count

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Tints`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Tints``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Tints._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return FmeshOption_Tints(count)

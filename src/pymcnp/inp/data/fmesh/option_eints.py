import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Eints(_option.FmeshOption_, keyword='eints'):
    """
    Represents INP data card data option eints options.

    Attributes:
        count: Number of mesh points for each mesh energy.
    """

    _REGEX = re.compile(r'\Aeints( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``FmeshOption_Eints``.

        Parameters:
            count: Number of mesh points for each mesh energy.

        Returns:
            ``FmeshOption_Eints``.

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
        Generates ``FmeshOption_Eints`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Eints``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Eints._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return FmeshOption_Eints(count)

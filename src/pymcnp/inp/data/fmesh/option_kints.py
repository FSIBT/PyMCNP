import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Kints(_option.FmeshOption_, keyword='kints'):
    """
    Represents INP data card data option kints options.

    Attributes:
        count: Number of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _REGEX = re.compile(r'\Akints( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``FmeshOption_Kints``.

        Parameters:
            count: Number of mesh points z/theta for rectangular/cylindrical geometry.

        Returns:
            ``FmeshOption_Kints``.

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
        Generates ``FmeshOption_Kints`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Kints``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Kints._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return FmeshOption_Kints(count)

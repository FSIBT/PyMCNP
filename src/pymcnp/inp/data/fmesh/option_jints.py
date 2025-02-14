import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Jints(_option.FmeshOption_, keyword='jints'):
    """
    Represents INP data card data option jints options.

    Attributes:
        count: Number of mesh points y/z for rectangular/cylindrical geometry.
    """

    _REGEX = re.compile(r'\Ajints( \S+)\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``FmeshOption_Jints``.

        Parameters:
            count: Number of mesh points y/z for rectangular/cylindrical geometry.

        Returns:
            ``FmeshOption_Jints``.

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
        Generates ``FmeshOption_Jints`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Jints``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Jints._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        count = types.Integer.from_mcnp(tokens[1])

        return FmeshOption_Jints(count)

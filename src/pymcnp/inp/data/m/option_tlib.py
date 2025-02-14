import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Tlib(_option.MOption_, keyword='tlib'):
    """
    Represents INP data card data option tlib options.

    Attributes:
        abx: Default triton table identifier.
    """

    _REGEX = re.compile(r'\Atlib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Tlib``.

        Parameters:
            abx: Default triton table identifier.

        Returns:
            ``MOption_Tlib``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, abx)

        self.value: typing.Final[tuple[any]] = types._Tuple([abx])
        self.abx: typing.Final[types.String] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Tlib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Tlib``.

        Raises:
            McnpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Tlib._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Tlib(abx)

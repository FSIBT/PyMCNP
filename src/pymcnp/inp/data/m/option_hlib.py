import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Hlib(_option.MOption_, keyword='hlib'):
    """
    Represents INP data card data option hlib options.

    Attributes:
        abx: Default proton table identifier.
    """

    _REGEX = re.compile(r'\Ahlib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Hlib``.

        Parameters:
            abx: Default proton table identifier.

        Returns:
            ``MOption_Hlib``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, abx)

        self.value: typing.Final[tuple[any]] = types._Tuple([abx])
        self.abx: typing.Final[types.String] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Hlib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Hlib``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Hlib._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Hlib(abx)

import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Elib(_option.MOption_, keyword='elib'):
    """
    Represents INP data card data option elib options.

    Attributes:
        abx: Default electron table identifier.
    """

    _REGEX = re.compile(r'\Aelib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Elib``.

        Parameters:
            abx: Default electron table identifier.

        Returns:
            ``MOption_Elib``.

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
        Generates ``MOption_Elib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Elib``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Elib._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Elib(abx)

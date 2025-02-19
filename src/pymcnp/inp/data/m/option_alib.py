import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Alib(_option.MOption_, keyword='alib'):
    """
    Represents INP data card data option alib options.

    Attributes:
        abx: Default alpha table identifier.
    """

    _REGEX = re.compile(r'\Aalib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Alib``.

        Parameters:
            abx: Default alpha table identifier.

        Returns:
            ``MOption_Alib``.

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
        Generates ``MOption_Alib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Alib``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Alib._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Alib(abx)

import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Dlib(_option.MOption_, keyword='dlib'):
    """
    Represents INP data card data option dlib options.

    Attributes:
        abx: Default deuteron table identifier.
    """

    _REGEX = re.compile(r'\Adlib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Dlib``.

        Parameters:
            abx: Default deuteron table identifier.

        Returns:
            ``MOption_Dlib``.

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
        Generates ``MOption_Dlib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Dlib``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Dlib._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Dlib(abx)

import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Nlib(_option.MOption_, keyword='nlib'):
    """
    Represents INP data card data option nlib options.

    Attributes:
        abx: Default neutron table identifier.
    """

    _REGEX = re.compile(r'\Anlib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Nlib``.

        Parameters:
            abx: Default neutron table identifier.

        Returns:
            ``MOption_Nlib``.

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
        Generates ``MOption_Nlib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Nlib``.

        Raises:
            McnpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Nlib._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Nlib(abx)

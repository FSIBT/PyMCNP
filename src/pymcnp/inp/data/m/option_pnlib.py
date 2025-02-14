import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Pnlib(_option.MOption_, keyword='pnlib'):
    """
    Represents INP data card data option pnlib options.

    Attributes:
        abx: Default photonuclear table identifier.
    """

    _REGEX = re.compile(r'\Apnlib( \S+)\Z')

    def __init__(self, abx: types.String):
        """
        Initializes ``MOption_Pnlib``.

        Parameters:
            abx: Default photonuclear table identifier.

        Returns:
            ``MOption_Pnlib``.

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
        Generates ``MOption_Pnlib`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Pnlib``.

        Raises:
            McnpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Pnlib._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_M_OPTION, source)

        abx = types.String.from_mcnp(tokens[1])

        return MOption_Pnlib(abx)

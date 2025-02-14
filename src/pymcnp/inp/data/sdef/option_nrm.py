import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Nrm(_option.SdefOption_, keyword='nrm'):
    """
    Represents INP data card data option nrm options.

    Attributes:
        sign: Sign of the surface normal.
    """

    _REGEX = re.compile(r'\Anrm( \S+)\Z')

    def __init__(self, sign: types.Integer):
        """
        Initializes ``SdefOption_Nrm``.

        Parameters:
            sign: Sign of the surface normal.

        Returns:
            ``SdefOption_Nrm``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if sign is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, sign)

        self.value: typing.Final[tuple[any]] = types._Tuple([sign])
        self.sign: typing.Final[types.Integer] = sign

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Nrm`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Nrm``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Nrm._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        sign = types.Integer.from_mcnp(tokens[1])

        return SdefOption_Nrm(sign)

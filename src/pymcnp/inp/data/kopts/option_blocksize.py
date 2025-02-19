import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Blocksize(_option.KoptsOption_, keyword='blocksize'):
    """
    Represents INP data card data option blocksize options.

    Attributes:
        ncy: Number of cycles in every outer iteration.
    """

    _REGEX = re.compile(r'\Ablocksize( \S+)\Z')

    def __init__(self, ncy: types.Integer):
        """
        Initializes ``KoptsOption_Blocksize``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Returns:
            ``KoptsOption_Blocksize``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ncy is None or not (ncy >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ncy)

        self.value: typing.Final[tuple[any]] = types._Tuple([ncy])
        self.ncy: typing.Final[types.Integer] = ncy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Blocksize`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Blocksize``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Blocksize._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        ncy = types.Integer.from_mcnp(tokens[1])

        return KoptsOption_Blocksize(ncy)

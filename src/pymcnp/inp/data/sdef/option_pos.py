import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Pos(_option.SdefOption_, keyword='pos'):
    """
    Represents INP data card data option pos options.

    Attributes:
        vector: Reference point for position sampling in vector notation.
    """

    _REGEX = re.compile(r'\Apos(( \S+)+)\Z')

    def __init__(self, vector: tuple[types.Real]):
        """
        Initializes ``SdefOption_Pos``.

        Parameters:
            vector: Reference point for position sampling in vector notation.

        Returns:
            ``SdefOption_Pos``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, vector)

        self.value: typing.Final[tuple[any]] = types._Tuple([vector])
        self.vector: typing.Final[tuple[types.Real]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Pos`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Pos``.

        Raises:
            McnpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Pos._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SDEF_OPTION, source)

        vector = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SdefOption_Pos(vector)

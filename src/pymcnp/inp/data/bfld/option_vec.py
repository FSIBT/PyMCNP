import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class BfldOption_Vec(_option.BfldOption_, keyword='vec'):
    """
    Represents INP data card data option vec options.

    Attributes:
        vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.
    """

    _REGEX = re.compile(r'\Avec(( \S+)+)\Z')

    def __init__(self, vector: tuple[types.Real]):
        """
        Initializes ``BfldOption_Vec``.

        Parameters:
            vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.

        Returns:
            ``BfldOption_Vec``.

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
        Generates ``BfldOption_Vec`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``BfldOption_Vec``.

        Raises:
            McnpError: SYNTAX_BFLD_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BfldOption_Vec._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BFLD_OPTION, source)

        vector = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return BfldOption_Vec(vector)

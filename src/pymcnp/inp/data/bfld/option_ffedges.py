import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class BfldOption_Ffedges(_option.BfldOption_, keyword='ffedges'):
    """
    Represents INP data card data option ffedges options.

    Attributes:
        numbers: Surface numbers to apply field fringe edges.
    """

    _REGEX = re.compile(r'\Affedges(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Real]):
        """
        Initializes ``BfldOption_Ffedges``.

        Parameters:
            numbers: Surface numbers to apply field fringe edges.

        Returns:
            ``BfldOption_Ffedges``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Real]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BfldOption_Ffedges`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``BfldOption_Ffedges``.

        Raises:
            InpError: SYNTAX_BFLD_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BfldOption_Ffedges._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return BfldOption_Ffedges(numbers)

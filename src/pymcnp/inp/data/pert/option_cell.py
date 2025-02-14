import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PertOption_Cell(_option.PertOption_, keyword='cell'):
    """
    Represents INP data card data option cell options.

    Attributes:
        numbers: List of cells.
    """

    _REGEX = re.compile(r'\Acell(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``PertOption_Cell``.

        Parameters:
            numbers: List of cells.

        Returns:
            ``PertOption_Cell``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PertOption_Cell`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PertOption_Cell``.

        Raises:
            McnpError: SYNTAX_PERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PertOption_Cell._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PERT_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return PertOption_Cell(numbers)

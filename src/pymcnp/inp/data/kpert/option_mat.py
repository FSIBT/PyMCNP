import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KpertOption_Mat(_option.KpertOption_, keyword='mat'):
    """
    Represents INP data card data option mat options.

    Attributes:
        numbers: List of materials.
    """

    _REGEX = re.compile(r'\Amat(( \S+)+)\Z')

    def __init__(self, numbers: tuple[types.Integer]):
        """
        Initializes ``KpertOption_Mat``.

        Parameters:
            numbers: List of materials.

        Returns:
            ``KpertOption_Mat``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KpertOption_Mat`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KpertOption_Mat``.

        Raises:
            InpError: SYNTAX_KPERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KpertOption_Mat._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KpertOption_Mat(numbers)

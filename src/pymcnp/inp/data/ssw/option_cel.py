import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SswOption_Cel(_option.SswOption_, keyword='cel'):
    """
    Represents INP data card data option cel options.

    Attributes:
        cfs: Cells from which KCODE neutrons are written.
    """

    _REGEX = re.compile(r'\Acel(( \S+)+)\Z')

    def __init__(self, cfs: tuple[types.Integer]):
        """
        Initializes ``SswOption_Cel``.

        Parameters:
            cfs: Cells from which KCODE neutrons are written.

        Returns:
            ``SswOption_Cel``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cfs is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), cfs)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cfs)

        self.value: typing.Final[tuple[any]] = types._Tuple([cfs])
        self.cfs: typing.Final[tuple[types.Integer]] = cfs

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SswOption_Cel`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SswOption_Cel``.

        Raises:
            InpError: SYNTAX_SSW_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SswOption_Cel._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        cfs = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SswOption_Cel(cfs)

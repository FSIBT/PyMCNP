import re
import typing

from . import uran
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Uran(_option.DataOption_, keyword='uran'):
    """
    Represents INP data card uran options.

    Attributes:
        transformations: Tuple of stochastic transformations.
    """

    _REGEX = re.compile(r'\Auran((( \S+)( \S+)( \S+)( \S+))+)\Z')

    def __init__(self, transformations: tuple[uran.UranEntry_Transformation]):
        """
        Initializes ``DataOption_Uran``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Returns:
            ``DataOption_Uran``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if transformations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformations)

        self.value: typing.Final[tuple[any]] = types._Tuple([transformations])
        self.transformations: typing.Final[tuple[uran.UranEntry_Transformation]] = transformations

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Uran`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Uran``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Uran._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        transformations = types._Tuple(
            [
                uran.UranEntry_Transformation.from_mcnp(token[0])
                for token in uran.UranEntry_Transformation._REGEX.finditer(tokens[1])
            ]
        )

        return DataOption_Uran(transformations)

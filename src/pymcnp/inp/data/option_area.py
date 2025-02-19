import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Area(_option.DataOption_, keyword='area'):
    """
    Represents INP data card area options.

    Attributes:
        areas: Tuple of surface areas.
    """

    _REGEX = re.compile(r'\Aarea(( \S+)+)\Z')

    def __init__(self, areas: tuple[types.Real]):
        """
        Initializes ``DataOption_Area``.

        Parameters:
            areas: Tuple of surface areas.

        Returns:
            ``DataOption_Area``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if areas is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, areas)

        self.value: typing.Final[tuple[any]] = types._Tuple([areas])
        self.areas: typing.Final[tuple[types.Real]] = areas

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Area`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Area``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Area._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        areas = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Area(areas)

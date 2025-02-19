import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Pwt(_option.DataOption_, keyword='pwt'):
    """
    Represents INP data card pwt options.

    Attributes:
        weights: Relative threshold weight of photons produced at neutron collisions in cell.
    """

    _REGEX = re.compile(r'\Apwt(( \S+)+)\Z')

    def __init__(self, weights: tuple[types.Real]):
        """
        Initializes ``DataOption_Pwt``.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Returns:
            ``DataOption_Pwt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weights is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weights)

        self.value: typing.Final[tuple[any]] = types._Tuple([weights])
        self.weights: typing.Final[tuple[types.Real]] = weights

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Pwt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Pwt``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Pwt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        weights = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return DataOption_Pwt(weights)

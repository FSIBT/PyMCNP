import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellOption_Pwt(_option.CellOption_, keyword='pwt'):
    """
    Represents INP cell card pwt options.

    Attributes:
        weight: Cell weight of photons produced at neutron collisions.
    """

    _REGEX = re.compile(r'\Apwt( \S+)\Z')

    def __init__(self, weight: types.Real):
        """
        Initializes ``CellOption_Pwt``.

        Parameters:
            weight: Cell weight of photons produced at neutron collisions.

        Returns:
            ``CellOption_Pwt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight)

        self.value: typing.Final[tuple[any]] = types._Tuple([weight])
        self.weight: typing.Final[types.Real] = weight

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellOption_Pwt`` from INP.

        Parameters:
            source: INP cell card option.

        Returns:
            ``CellOption_Pwt``.

        Raises:
            InpError: SYNTAX_CELL_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellOption_Pwt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        weight = types.Real.from_mcnp(tokens[1])

        return CellOption_Pwt(weight)

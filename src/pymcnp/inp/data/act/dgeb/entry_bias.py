import re
import typing

from . import _entry
from .....utils import types
from .....utils import errors
from .....utils import _parser


class DgebEntry_Bias(_entry.DgebEntry_):
    """
    Represents INP data card data option act option bias entries.

    Attributes:
        weight: Weight for bin.
        energy: Upper energy for bin.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, weight: types.Real, energy: types.Real):
        """
        Initializes ``DgebEntry_Bias``.

        Parameters:
            weight: Weight for bin.
            energy: Upper energy for bin.

        Returns:
            ``DgebEntryBias``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, weight)
        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, energy)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([weight, energy])
        self.weight: typing.Final[types.Real] = weight
        self.energy: typing.Final[types.Real] = energy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DgebEntry_Bias`` from INP.

        Parameters:
            INP for ``DgebEntry_Bias``.

        Returns:
            ``DgebEntry_Bias``.

        Raises:
            InpError: SYNTAX_DGEB_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DgebEntry_Bias._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        weight = types.Real.from_mcnp(tokens[1])
        energy = types.Real.from_mcnp(tokens[2])

        return DgebEntry_Bias(weight, energy)

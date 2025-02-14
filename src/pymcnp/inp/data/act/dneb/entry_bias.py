import re
import typing

from . import _entry
from .....utils import types
from .....utils import errors
from .....utils import _parser


class DnebEntry_Bias(_entry.DnebEntry_):
    """
    Represents INP data card data option act option bias entries.

    Attributes:
        weight: Weight for bin.
        energy: Upper energy for bin.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, weight: types.Real, energy: types.Real):
        """
        Initializes ``DnebEntry_Bias``.

        Parameters:
            weight: Weight for bin.
            energy: Upper energy for bin.

        Returns:
            ``DnebEntryBias``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if weight is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, weight)
        if energy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, energy)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([weight, energy])
        self.weight: typing.Final[types.Real] = weight
        self.energy: typing.Final[types.Real] = energy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DnebEntry_Bias`` from INP.

        Parameters:
            INP for ``DnebEntry_Bias``.

        Returns:
            ``DnebEntry_Bias``.

        Raises:
            McnpError: SYNTAX_DNEB_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DnebEntry_Bias._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DNEB_ENTRY, source)

        weight = types.Real.from_mcnp(tokens[1])
        energy = types.Real.from_mcnp(tokens[2])

        return DnebEntry_Bias(weight, energy)

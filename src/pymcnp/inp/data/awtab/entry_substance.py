import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class AwtabEntry_Substance(_entry.AwtabEntry_):
    """
    Represents INP data card data option substance entries.

    Attributes:
        zaid: Zaid alias for nuclide.
        weight_ratio: Atomic weight ratios.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, zaid: types.Zaid, weight_ratio: types.Real):
        """
        Initializes ``AwtabEntry_Substance``.

        Parameters:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.

        Returns:
            ``AwtabEntrySubstance``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, zaid)
        if weight_ratio is None or not (weight_ratio > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, weight_ratio)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([zaid, weight_ratio])
        self.zaid: typing.Final[types.Zaid] = zaid
        self.weight_ratio: typing.Final[types.Real] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``AwtabEntry_Substance`` from INP.

        Parameters:
            INP for ``AwtabEntry_Substance``.

        Returns:
            ``AwtabEntry_Substance``.

        Raises:
            McnpError: SYNTAX_AWTAB_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = AwtabEntry_Substance._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_AWTAB_ENTRY, source)

        zaid = types.Zaid.from_mcnp(tokens[1])
        weight_ratio = types.Real.from_mcnp(tokens[2])

        return AwtabEntry_Substance(zaid, weight_ratio)

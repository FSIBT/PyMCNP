import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class XsEntry_Substance(_entry.XsEntry_):
    """
    Represents INP data card data option substance entries.

    Attributes:
        zaid: Zaid alias for nuclide.
        weight_ratio: Atomic weight ratios.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, zaid: types.Zaid, weight_ratio: types.Real):
        """
        Initializes ``XsEntry_Substance``.

        Parameters:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.

        Returns:
            ``XsEntrySubstance``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if zaid is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, zaid)
        if weight_ratio is None or not (weight_ratio > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, weight_ratio)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([zaid, weight_ratio])
        self.zaid: typing.Final[types.Zaid] = zaid
        self.weight_ratio: typing.Final[types.Real] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``XsEntry_Substance`` from INP.

        Parameters:
            INP for ``XsEntry_Substance``.

        Returns:
            ``XsEntry_Substance``.

        Raises:
            InpError: SYNTAX_XS_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = XsEntry_Substance._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        zaid = types.Zaid.from_mcnp(tokens[1])
        weight_ratio = types.Real.from_mcnp(tokens[2])

        return XsEntry_Substance(zaid, weight_ratio)

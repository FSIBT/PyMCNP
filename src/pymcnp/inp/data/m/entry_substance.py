import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MEntry_Substance(_entry.MEntry_):
    """
    Represents INP data card data option substance entries.

    Attributes:
        zaid: Substance ZAID alias.
        fraction: Substance fraction.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, zaid: types.Zaid, fraction: types.Real):
        """
        Initializes ``MEntry_Substance``.

        Parameters:
            zaid: Substance ZAID alias.
            fraction: Substance fraction.

        Returns:
            ``MEntrySubstance``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, zaid)
        if fraction is None or not (-1 <= fraction <= 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, fraction)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([zaid, fraction])
        self.zaid: typing.Final[types.Zaid] = zaid
        self.fraction: typing.Final[types.Real] = fraction

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MEntry_Substance`` from INP.

        Parameters:
            INP for ``MEntry_Substance``.

        Returns:
            ``MEntry_Substance``.

        Raises:
            McnpError: SYNTAX_M_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MEntry_Substance._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_M_ENTRY, source)

        zaid = types.Zaid.from_mcnp(tokens[1])
        fraction = types.Real.from_mcnp(tokens[2])

        return MEntry_Substance(zaid, fraction)

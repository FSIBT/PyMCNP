import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdEntry_Information(_entry.SdEntry_):
    """
    Represents INP data card data option information entries.

    Attributes:
        values: Area, volume, or mass by surface/cell.
    """

    _REGEX = re.compile(r'(( \S+)+)')

    def __init__(self, values: tuple[types.Real]):
        """
        Initializes ``SdEntry_Information``.

        Parameters:
            values: Area, volume, or mass by surface/cell.

        Returns:
            ``SdEntryInformation``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if values is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, values)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([values])
        self.values: typing.Final[tuple[types.Real]] = values

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdEntry_Information`` from INP.

        Parameters:
            INP for ``SdEntry_Information``.

        Returns:
            ``SdEntry_Information``.

        Raises:
            McnpError: SYNTAX_SD_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdEntry_Information._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SD_ENTRY, source)

        values = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SdEntry_Information(values)

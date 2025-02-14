import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class DdEntry_Diagnostic(_entry.DdEntry_):
    """
    Represents INP data card data option diagnostic entries.

    Attributes:
        playing_setting: Criterion for playing Russian roulette for DXTRAN.
        printing_setting: Criterion for printing diagnostics for large contributions for DXTRAN.
    """

    _REGEX = re.compile(r'( \S+)( \S+)')

    def __init__(self, playing_setting: types.Real, printing_setting: types.Real):
        """
        Initializes ``DdEntry_Diagnostic``.

        Parameters:
            playing_setting: Criterion for playing Russian roulette for DXTRAN.
            printing_setting: Criterion for printing diagnostics for large contributions for DXTRAN.

        Returns:
            ``DdEntryDiagnostic``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if playing_setting is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, playing_setting)
        if printing_setting is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, printing_setting)

        self.parameters: typing.Final[tuple[any]] = types._Tuple(
            [playing_setting, printing_setting]
        )
        self.playing_setting: typing.Final[types.Real] = playing_setting
        self.printing_setting: typing.Final[types.Real] = printing_setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DdEntry_Diagnostic`` from INP.

        Parameters:
            INP for ``DdEntry_Diagnostic``.

        Returns:
            ``DdEntry_Diagnostic``.

        Raises:
            McnpError: SYNTAX_DD_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DdEntry_Diagnostic._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DD_ENTRY, source)

        playing_setting = types.Real.from_mcnp(tokens[1])
        printing_setting = types.Real.from_mcnp(tokens[2])

        return DdEntry_Diagnostic(playing_setting, printing_setting)

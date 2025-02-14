import re
import typing

from . import dd
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Dd(_option.DataOption_, keyword='dd'):
    """
    Represents INP data card dd options.

    Attributes:
        diagnostics: Detector diagnostic entries.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Add(\d+?)((( \S+)( \S+))+)\Z')

    def __init__(self, diagnostics: tuple[dd.DdEntry_Diagnostic], suffix: types.Integer):
        """
        Initializes ``DataOption_Dd``.

        Parameters:
            diagnostics: Detector diagnostic entries.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Dd``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if diagnostics is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, diagnostics)
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([diagnostics])
        self.diagnostics: typing.Final[tuple[dd.DdEntry_Diagnostic]] = diagnostics
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Dd`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Dd``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Dd._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        diagnostics = types._Tuple(
            [
                dd.DdEntry_Diagnostic.from_mcnp(token[0])
                for token in dd.DdEntry_Diagnostic._REGEX.finditer(tokens[2])
            ]
        )

        return DataOption_Dd(diagnostics, suffix)

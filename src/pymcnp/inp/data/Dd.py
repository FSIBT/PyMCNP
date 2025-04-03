import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Dd(DataOption_, keyword='dd'):
    """
    Represents INP dd elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'diagnostics': types.Tuple[types.Diagnostic],
    }

    _REGEX = re.compile(rf'\Add(\d+)((?: {types.Diagnostic._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, diagnostics: types.Tuple[types.Diagnostic]):
        """
        Initializes ``Dd``.

        Parameters:
            suffix: Data card option suffix.
            diagnostics: Detector diagnostic entries.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if diagnostics is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, diagnostics)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                diagnostics,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.diagnostics: typing.Final[types.Tuple[types.Diagnostic]] = diagnostics

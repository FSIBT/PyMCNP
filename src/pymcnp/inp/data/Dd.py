import re

from . import dd
from . import _option
from ...utils import types
from ...utils import errors


class Dd(_option.DataOption):
    """
    Represents INP dd elements.
    """

    _KEYWORD = 'dd'

    _ATTRS = {
        'suffix': types.Integer,
        'diagnostics': types.Tuple[dd.Diagnostic],
    }

    _REGEX = re.compile(rf'\Add(\d+)?((?: {dd.Diagnostic._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, diagnostics: list[str] | list[dd.Diagnostic], suffix: str | int | types.Integer = None):
        """
        Initializes ``Dd``.

        Parameters:
            suffix: Data card option suffix.
            diagnostics: Detector diagnostic entries.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.diagnostics: types.Tuple[dd.Diagnostic] = diagnostics

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        self._suffix: types.Integer = suffix

    @property
    def diagnostics(self) -> types.Tuple[dd.Diagnostic]:
        """
        Detector diagnostic entries

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._diagnostics

    @diagnostics.setter
    def diagnostics(self, diagnostics: list[str] | list[dd.Diagnostic]) -> None:
        """
        Sets ``diagnostics``.

        Parameters:
            diagnostics: Detector diagnostic entries.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if diagnostics is not None:
            array = []
            for item in diagnostics:
                if isinstance(item, dd.Diagnostic):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(dd.Diagnostic.from_mcnp(item))
            diagnostics = types.Tuple(array)

        if diagnostics is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, diagnostics)

        self._diagnostics: types.Tuple[dd.Diagnostic] = diagnostics

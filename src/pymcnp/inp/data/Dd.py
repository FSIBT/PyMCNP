import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Dd(DataOption_, keyword='dd'):
    """
    Represents INP dd elements.

    Attributes:
        suffix: Data card option suffix.
        diagnostics: Detector diagnostic entries.
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


@dataclasses.dataclass
class DdBuilder:
    """
    Builds ``Dd``.

    Attributes:
        suffix: Data card option suffix.
        diagnostics: Detector diagnostic entries.
    """

    suffix: str | int | types.Integer
    diagnostics: list[str] | list[types.Diagnostic]

    def build(self):
        """
        Builds ``DdBuilder`` into ``Dd``.

        Returns:
            ``Dd`` for ``DdBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        diagnostics = []
        for item in self.diagnostics:
            if isinstance(item, types.Diagnostic):
                diagnostics.append(item)
            elif isinstance(item, str):
                diagnostics.append(types.Diagnostic.from_mcnp(item))
            else:
                diagnostics.append(item.build())
        diagnostics = types.Tuple(diagnostics)

        return Dd(
            suffix=suffix,
            diagnostics=diagnostics,
        )

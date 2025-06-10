import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Dd(_option.DataOption):
    """
    Represents INP dd elements.

    Attributes:
        suffix: Data card option suffix.
        diagnostics: Detector diagnostic entries.
    """

    _KEYWORD = 'dd'

    _ATTRS = {
        'suffix': types.Integer,
        'diagnostics': types.Tuple[types.Diagnostic],
    }

    _REGEX = re.compile(rf'\Add(\d+)?((?: {types.Diagnostic._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, diagnostics: types.Tuple[types.Diagnostic], suffix: types.Integer = None):
        """
        Initializes ``Dd``.

        Parameters:
            suffix: Data card option suffix.
            diagnostics: Detector diagnostic entries.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if diagnostics is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, diagnostics)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                diagnostics,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.diagnostics: typing.Final[types.Tuple[types.Diagnostic]] = diagnostics


@dataclasses.dataclass
class DdBuilder(_option.DataOptionBuilder):
    """
    Builds ``Dd``.

    Attributes:
        suffix: Data card option suffix.
        diagnostics: Detector diagnostic entries.
    """

    diagnostics: list[str] | list[types.Diagnostic]
    suffix: str | int | types.Integer = None

    def build(self):
        """
        Builds ``DdBuilder`` into ``Dd``.

        Returns:
            ``Dd`` for ``DdBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.diagnostics:
            diagnostics = []
            for item in self.diagnostics:
                if isinstance(item, types.Diagnostic):
                    diagnostics.append(item)
                elif isinstance(item, str):
                    diagnostics.append(types.Diagnostic.from_mcnp(item))
            diagnostics = types.Tuple(diagnostics)
        else:
            diagnostics = None

        return Dd(
            suffix=suffix,
            diagnostics=diagnostics,
        )

    @staticmethod
    def unbuild(ast: Dd):
        """
        Unbuilds ``Dd`` into ``DdBuilder``

        Returns:
            ``DdBuilder`` for ``Dd``.
        """

        return DdBuilder(
            suffix=copy.deepcopy(ast.suffix),
            diagnostics=copy.deepcopy(ast.diagnostics),
        )

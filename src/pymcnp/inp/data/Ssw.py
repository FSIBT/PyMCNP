import re
import copy
import typing
import dataclasses


from . import ssw
from . import _option
from ...utils import types
from ...utils import errors


class Ssw(_option.DataOption):
    """
    Represents INP ssw elements.

    Attributes:
        surfaces: Problem surfaces.
        cells: Problem cells.
        options: Dictionary of options.
    """

    _KEYWORD = 'ssw'

    _ATTRS = {
        'surfaces': types.Tuple[types.Integer],
        'cells': types.Tuple[types.Integer],
        'options': types.Tuple[ssw.SswOption],
    }

    _REGEX = re.compile(rf'\Assw((?: {types.Integer._REGEX.pattern[2:-2]})+?)((?: {types.Integer._REGEX.pattern[2:-2]})+?)?((?: (?:{ssw.SswOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, surfaces: types.Tuple[types.Integer], cells: types.Tuple[types.Integer] = None, options: types.Tuple[ssw.SswOption] = None):
        """
        Initializes ``Ssw``.

        Parameters:
            surfaces: Problem surfaces.
            cells: Problem cells.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if surfaces is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, surfaces)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                surfaces,
                cells,
                options,
            ]
        )

        self.surfaces: typing.Final[types.Tuple[types.Integer]] = surfaces
        self.cells: typing.Final[types.Tuple[types.Integer]] = cells
        self.options: typing.Final[types.Tuple[ssw.SswOption]] = options


@dataclasses.dataclass
class SswBuilder(_option.DataOptionBuilder):
    """
    Builds ``Ssw``.

    Attributes:
        surfaces: Problem surfaces.
        cells: Problem cells.
        options: Dictionary of options.
    """

    surfaces: list[str] | list[int] | list[types.Integer]
    cells: list[str] | list[int] | list[types.Integer] = None
    options: list[str] | list[ssw.SswOption] = None

    def build(self):
        """
        Builds ``SswBuilder`` into ``Ssw``.

        Returns:
            ``Ssw`` for ``SswBuilder``.
        """

        if self.surfaces:
            surfaces = []
            for item in self.surfaces:
                if isinstance(item, types.Integer):
                    surfaces.append(item)
                elif isinstance(item, int):
                    surfaces.append(types.Integer(item))
                elif isinstance(item, str):
                    surfaces.append(types.Integer.from_mcnp(item))
            surfaces = types.Tuple(surfaces)
        else:
            surfaces = None

        if self.cells:
            cells = []
            for item in self.cells:
                if isinstance(item, types.Integer):
                    cells.append(item)
                elif isinstance(item, int):
                    cells.append(types.Integer(item))
                elif isinstance(item, str):
                    cells.append(types.Integer.from_mcnp(item))
            cells = types.Tuple(cells)
        else:
            cells = None

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, ssw.SswOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(ssw.SswOption.from_mcnp(item))
                elif isinstance(item, ssw.SswOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Ssw(
            surfaces=surfaces,
            cells=cells,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Ssw):
        """
        Unbuilds ``Ssw`` into ``SswBuilder``

        Returns:
            ``SswBuilder`` for ``Ssw``.
        """

        return SswBuilder(
            surfaces=copy.deepcopy(ast.surfaces),
            cells=copy.deepcopy(ast.cells),
            options=copy.deepcopy(ast.options),
        )

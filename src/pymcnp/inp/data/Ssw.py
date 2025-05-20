import re
import typing
import dataclasses


from . import ssw
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ssw(DataOption):
    """
    Represents INP ssw elements.

    Attributes:
        surfaces: Problem surfaces.
        cells: Problem cells.
        options: Dictionary of options.
    """

    _ATTRS = {
        'surfaces': types.Tuple[types.Integer],
        'cells': types.Tuple[types.Integer],
        'options': types.Tuple[ssw.SswOption],
    }

    _REGEX = re.compile(
        rf'\Assw((?: {types.Integer._REGEX.pattern})+?)((?: {types.Integer._REGEX.pattern})+?)((?: (?:{ssw.SswOption._REGEX.pattern}))+?)?\Z'
    )

    def __init__(
        self,
        surfaces: types.Tuple[types.Integer],
        cells: types.Tuple[types.Integer],
        options: types.Tuple[ssw.SswOption] = None,
    ):
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
        if cells is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cells)

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
class SswBuilder:
    """
    Builds ``Ssw``.

    Attributes:
        surfaces: Problem surfaces.
        cells: Problem cells.
        options: Dictionary of options.
    """

    surfaces: list[str] | list[int] | list[types.Integer]
    cells: list[str] | list[int] | list[types.Integer]
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
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Ssw(
            surfaces=surfaces,
            cells=cells,
            options=options,
        )

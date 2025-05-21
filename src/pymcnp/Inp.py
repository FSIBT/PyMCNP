import re
import typing
import dataclasses

import pyvista

from . import inp
from .utils import types
from .utils import errors
from .utils import _parser
from .utils import _object
from .utils import _visualization


class Inp(_object.McnpFile):
    """
    Represents INP files.

    Attributes:
        message: INP message.
        title: INP title.
        cells: INP cell card block.
        cells_comments: INP cell card block comments.
        surfaces: INP surface card block.
        surfaces_comments: INP surface card block comments.
        data: INP data card block.
        data_comments: INP data card block comments.
        other: INP other block.
    """

    _REGEX = re.compile(
        r'((?:message:).+\n)?(.+(?:\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n|\Z))([\S\s]+)?'
    )

    def __init__(
        self,
        title: types.String,
        cells: types.Tuple[inp.Cell],
        cells_comments: types.Tuple[inp.Comment],
        surfaces: types.Tuple[inp.Surface],
        surfaces_comments: types.Tuple[inp.Comment],
        data: types.Tuple[inp.Data],
        data_comments: types.Tuple[inp.Comment],
        message: types.String = None,
        other: types.String = None,
    ):
        """
        Initializes ``Inp``.

        Parameters:
            message: INP message.
            title: INP title.
            cells: INP cell card block.
            cells_comments: INP cell card block comments.
            surfaces: INP surface card block.
            surfaces_comments: INP surface card block comments.
            data: INP data card block.
            data_comments: INP data card block comments.
            other: INP other block.

        Returns:
            ``Inp``.

        Raises:
            InpError: SEMATNICS_INP.
        """

        if title is None or not len(title) < 80:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, title)

        if cells is None or None in cells:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, cells)

        if cells_comments is None or None in cells_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, cells_comments)

        if surfaces is None or None in surfaces:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, surfaces)

        if surfaces_comments is None or None in surfaces_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, surfaces_comments)

        if data is None or None in data:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, data)

        if data_comments is None or None in data_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, data_comments)

        self.message: typing.Final[types.String] = message
        self.title: typing.Final[types.String] = title
        self.cells: typing.Final[types.Tuple[inp.Cell]] = cells
        self.cells_comments: typing.Final[types.Tuple[inp.Comment]] = cells_comments
        self.surfaces: typing.Final[types.Tuple[inp.Surface]] = surfaces
        self.surfaces_comments: typing.Final[types.Tuple[inp.Comment]] = surfaces_comments
        self.data: typing.Final[types.Tuple[inp.Data]] = data
        self.data_comments: typing.Final[types.Tuple[inp.Comment]] = data_comments
        self.other: typing.Final[types.String] = other

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Inp`` from INP.

        Parameters:
            source: INP for ``Inp``.

        Returns:
            ``Inp``.

        Raisees:
            InpError: SYNTAX_INP.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Inp._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_INP, source)

        message = types.String.from_mcnp(tokens[1]) if tokens[1] else None
        title = types.String.from_mcnp(tokens[2])

        cells = []
        cells_comments = []
        for line in tokens[3].strip().split('\n'):
            try:
                cells_comments.append(inp.Comment.from_mcnp(line))
                continue
            except errors.InpError:
                pass

            cells.append(inp.Cell.from_mcnp(line))

        surfaces = []
        surfaces_comments = []
        for line in tokens[4].strip().split('\n'):
            try:
                surfaces_comments.append(inp.Comment.from_mcnp(line))
                continue
            except errors.InpError:
                pass

            surfaces.append(inp.Surface.from_mcnp(line))

        data = []
        data_comments = []
        for line in tokens[5].strip().split('\n'):
            try:
                data_comments.append(inp.Comment.from_mcnp(line))
                continue
            except errors.InpError:
                pass

            data.append(inp.Data.from_mcnp(line))

        other = types.String.from_mcnp(tokens[6]) if tokens[6] else None

        return Inp(
            title,
            cells,
            cells_comments,
            surfaces,
            surfaces_comments,
            data,
            data_comments,
            message=message,
            other=other,
        )

    def to_mcnp(self):
        """
        Generates INP from ``Inp``.

        Returns:
            INP for ``Inp``.
        """

        # Appending Message
        source = self.message + '\n' if self.message else ''

        # Appending Title
        source += self.title + '\n'

        # Appending Blocks
        DELIMITER = 'c ' + '=' * 76 + '\n'

        source += DELIMITER
        source += f'c {"cells":^76.76}\n'
        source += DELIMITER
        source += '\n'.join(card.to_mcnp() for card in self.cells)
        source += '\n\n'

        source += DELIMITER
        source += f'c {"surfaces":^76.76}\n'
        source += DELIMITER
        source += '\n'.join(card.to_mcnp() for card in self.surfaces)
        source += '\n\n'

        source += DELIMITER
        source += f'c {"data":^76.76}\n'
        source += DELIMITER
        source += '\n'.join(card.to_mcnp() for card in self.data)
        source += '\n'

        # Appending Extra
        source += self.other if self.other else ''

        return source

    def draw(self) -> pyvista.PolyData:
        """
        Generates ``Visualization`` from ``Inp``.

        Returns:
            ``pyvista.PolyData`` for ``Inp``.
        """

        vis = _visualization.Visualization()

        for surface in self.surfaces:
            vis += _visualization.Visualization(surface.draw())

        return vis.data


@dataclasses.dataclass
class InpBuilder:
    """
    Builds ``Inp``.

    Attributes:
        message: INP message.
        title: INP title.
        cells: INP cell card block.
        surfaces: INP surface card block.
        data: INP data card block.
        other: INP other block.
    """

    title: str
    cells: dict[str, str | inp.Cell | inp.CellBuilder] = dataclasses.field(
        default_factory=lambda _: {}
    )
    surfaces: dict[str, str | inp.Surface | inp.SurfaceBuilder] = dataclasses.field(
        default_factory=lambda _: {}
    )
    data: dict[str, str | inp.Data | inp.DataBuilder] = dataclasses.field(
        default_factory=lambda _: {}
    )
    message: str = ''
    other: str = ''

    def from_mcnp(source: str):
        """
        Initiailizes ``InpBuilder`` from MCNP.

        Attributes:
            source: MCNP for ``Inp``.
        """

        ast = Inp.from_mcnp(source)

        return InpBuilder(
            title=ast.title,
            cells={cell.number.value: cell for cell in ast.cells},
            surfaces={surface.number.value: surface for surface in ast.surfaces},
            data={},
            message=ast.message,
            other=ast.other,
        )

    def build(self):
        """
        Builds ``InpBuilder`` into ``Inp``.

        Returns:
            ``Inp`` for ``InpBuilder``.
        """

        cells = []
        for item in self.cells.values():
            if isinstance(item, inp.Cell):
                cells.append(item)
            elif isinstance(item, str):
                cells.append(inp.Cell.from_mcnp(item))
            else:
                cells.append(item.build())
        cells = types.Tuple(cells)

        surfaces = []
        for item in self.surfaces.values():
            if isinstance(item, inp.Surface):
                surfaces.append(item)
            elif isinstance(item, str):
                surfaces.append(inp.Surface.from_mcnp(item))
            else:
                surfaces.append(item.build())
        surfaces = types.Tuple(surfaces)

        data = []
        for item in self.data.values():
            if isinstance(item, inp.Surface):
                data.append(item)
            elif isinstance(item, str):
                data.append(inp.Data.from_mcnp(item))
            else:
                data.append(item.build())
        data = types.Tuple(data)

        return Inp(
            title=self.title,
            message=self.message,
            other=self.other,
            cells=cells,
            cells_comments=types.Tuple([]),
            surfaces=surfaces,
            surfaces_comments=types.Tuple([]),
            data=data,
            data_comments=types.Tuple([]),
        )

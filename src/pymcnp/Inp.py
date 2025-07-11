import re
import typing


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

    _REGEX = re.compile(r'\A((?:message:).+\n)?(.+(?:\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n|\Z))([\S\s]+)?\Z')

    def __init__(
        self,
        title: types.String,
        cells: types.Tuple[inp.Cell | inp.Like],
        surfaces: types.Tuple[inp.Surface],
        data: types.Tuple[inp.Data],
        cells_comments: types.Tuple[inp.Comment] = None,
        surfaces_comments: types.Tuple[inp.Comment] = None,
        data_comments: types.Tuple[inp.Comment] = None,
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

        if cells_comments is not None and None in cells_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, cells_comments)

        if surfaces is None or None in surfaces:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, surfaces)

        if surfaces_comments is not None and None in surfaces_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, surfaces_comments)

        if data is None or None in data:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, data)

        if data_comments is not None and None in data_comments:
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

            try:
                cells.append(inp.Like.from_mcnp(line))
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
            surfaces,
            data,
            cells_comments=cells_comments,
            surfaces_comments=surfaces_comments,
            data_comments=data_comments,
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
        source += self.title

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

    def draw(self) -> _visualization.Visualization:
        """
        Generates ``Visualization`` from ``Inp``.

        Returns:
            ``Visualization`` for ``Inp``.
        """

        vis = self.surfaces[0].draw()

        for surface in self.surfaces[0:]:
            vis += surface.draw()

        return vis


'''
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

    title: str | types.String
    cells: list[str | inp.Cell | inp.CellBuilder]
    surfaces: list[str | inp.Surface | inp.SurfaceBuilder]
    data: list[str | inp.Data | inp.DataBuilder]
    cells_comments: list[str | inp.Comment | inp.CommentBuilder] = None
    surfaces_comments: list[str | inp.Comment | inp.CommentBuilder] = None
    data_comments: list[str | inp.Comment | inp.CommentBuilder] = None
    message: str | types.String = None
    other: str | types.String = None

    def build(self):
        """
        Builds ``InpBuilder`` into ``Inp``.

        Returns:
            ``Inp`` for ``InpBuilder``.
        """

        title = self.title
        if isinstance(self.title, types.String):
            title = self.title
        elif isinstance(self.title, str):
            title = types.String(self.title)

        if self.cells:
            cells = []
            for item in self.cells:
                if isinstance(item, inp.Cell):
                    cells.append(item)
                elif isinstance(item, str):
                    cells.append(inp.Cell.from_mcnp(item))
                elif isinstance(item, inp.CellBuilder):
                    cells.append(item.build())
            cells = types.Tuple(cells)
        else:
            cells = None

        if self.cells_comments:
            cells_comments = []
            for item in self.cells_comments:
                if isinstance(item, inp.Comment):
                    cells_comments.append(item)
                elif isinstance(item, str):
                    cells_comments.append(inp.Comment.from_mcnp(item))
                elif isinstance(item, inp.CommentBuilder):
                    cells_comments.append(item.build())
            cells_comments = types.Tuple(cells_comments)
        else:
            cells_comments = None

        if self.surfaces:
            surfaces = []
            for item in self.surfaces:
                if isinstance(item, inp.Surface):
                    surfaces.append(item)
                elif isinstance(item, str):
                    surfaces.append(inp.Surface.from_mcnp(item))
                elif isinstance(item, inp.SurfaceBuilder):
                    surfaces.append(item.build())
            surfaces = types.Tuple(surfaces)
        else:
            surfaces = None

        if self.surfaces_comments:
            surfaces_comments = []
            for item in self.surfaces_comments:
                if isinstance(item, inp.Comment):
                    surfaces_comments.append(item)
                elif isinstance(item, str):
                    surfaces_comments.append(inp.Comment.from_mcnp(item))
                elif isinstance(item, inp.CommentBuilder):
                    surfaces_comments.append(item.build())
            surfaces_comments = types.Tuple(surfaces_comments)
        else:
            surfaces_comments = None

        if self.data:
            data = []
            for item in self.data:
                if isinstance(item, inp.Data):
                    data.append(item)
                elif isinstance(item, str):
                    data.append(inp.Data.from_mcnp(item))
                elif isinstance(item, inp.DataBuilder):
                    data.append(item.build())
            data = types.Tuple(data)
        else:
            data = None

        if self.data_comments:
            data_comments = []
            for item in self.data_comments:
                if isinstance(item, inp.Comment):
                    data_comments.append(item)
                elif isinstance(item, str):
                    data_comments.append(inp.Comment.from_mcnp(item))
                elif isinstance(item, inp.CommentBuilder):
                    data_comments.append(item.build())
            data_comments = types.Tuple(data_comments)
        else:
            data_comments = None

        message = self.message
        if isinstance(self.message, types.String):
            message = self.message
        elif isinstance(self.message, str):
            message = types.String(self.message)

        other = self.other
        if isinstance(self.other, types.String):
            other = self.other
        elif isinstance(self.other, str):
            other = types.String(self.other)

        return Inp(
            title=title,
            message=message,
            other=other,
            cells=cells,
            cells_comments=cells_comments,
            surfaces=surfaces,
            surfaces_comments=surfaces_comments,
            data=data,
            data_comments=data_comments,
        )

    @staticmethod
    def unbuild(ast: Inp):
        """
        Unbuilds ``Inp`` into ``InpBuilder``

        Returns:
            ``InpBuilder`` for ``Inp``.
        """

        return InpBuilder(
            title=copy.deepcopy(ast.title),
            cells=copy.deepcopy(ast.cells),
            cells_comments=copy.deepcopy(ast.cells_comments),
            surfaces=copy.deepcopy(ast.surfaces),
            surfaces_comments=copy.deepcopy(ast.surfaces_comments),
            data=copy.deepcopy(ast.data),
            data_comments=copy.deepcopy(ast.data_comments),
            message=copy.deepcopy(ast.message),
            other=copy.deepcopy(ast.other),
        )
'''

import re

from . import inp
from .utils import types
from .utils import errors
from .utils import _parser
from .utils import _object
from .utils import _visualization


class Inp(_object.McnpFile):
    """
    Represents INP files.
    """

    _REGEX = re.compile(r'\A((?:message:).+\n)?(.+(?:\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n|\Z))([\S\s]+)?\Z')

    def __init__(
        self,
        title: types.String,
        cells: types.Tuple[inp.Cell | inp.Like],
        surfaces: types.Tuple[inp.Surface],
        data: types.Tuple[inp.Data],
        message: types.String = None,
        other: types.String = None,
    ):
        """
        Initializes ``Inp``.

        Parameters:
            title: File title.
            cells: File cell card block.
            surfaces: File surface card block.
            data: File data card block.
            message: File message.
            other: File other block.

        Returns:
            ``Inp``.

        Raises:
            InpError: SEMATNICS_INP.
        """

        self.title: types.String = title
        self.cells: types.Tuple[inp.Cell | inp.Like | inp.Comment] = cells
        self.surfaces: types.Tuple[inp.Surface | inp.Comment] = surfaces
        self.data: types.Tuple[inp.Data | inp.Comment] = data
        self.message: types.String = message
        self.other: types.String = other

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Inp`` from INP.

        Parameters:
            source: INP for ``Inp``.

        Returns:
            ``Inp``.

        Raises:
            InpError: SYNTAX_INP.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Inp._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_INP, source)

        message = types.String.from_mcnp(tokens[1]) if tokens[1] else None
        title = types.String.from_mcnp(tokens[2])

        cells = []
        for line in tokens[3].strip().split('\n'):
            try:
                cells.append(inp.Comment.from_mcnp(line))
                continue
            except errors.InpError:
                pass

            if 'like' in line:
                cells.append(inp.Like.from_mcnp(line))
            else:
                cells.append(inp.Cell.from_mcnp(line))

        surfaces = []
        for line in tokens[4].strip().split('\n'):
            try:
                surfaces.append(inp.Comment.from_mcnp(line))
                continue
            except errors.InpError:
                pass

            surfaces.append(inp.Surface.from_mcnp(line))

        data = []
        for line in tokens[5].strip().split('\n'):
            try:
                data.append(inp.Comment.from_mcnp(line))
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
            message=message,
            other=other,
        )

    def to_mcnp(self):
        """
        Generates INP from ``Inp``.

        Returns:
            INP for ``Inp``.
        """

        # DELIMITER = 'c ' + '=' * 76 + '\n'
        # source += DELIMITER
        # source += f'c {"cells":^76.76}\n'
        # source += DELIMITER

        return f"""
{self.message or ""}
{self.title}
{'\n'.join(map(str, self.cells))}

{'\n'.join(map(str, self.surfaces))}

{'\n'.join(map(str, self.data))}
{self.other or ""}
"""[1:-1]

    def draw(self) -> _visualization.Visualization:
        """
        Generates ``Visualization`` from ``Inp``.

        Returns:
            ``Visualization`` for ``Inp``.
        """

        surfaces = list(filter(lambda surface: isinstance(surface, inp.Surface), self.surfaces))

        if surfaces:
            vis = surfaces[0].draw()
            for surface in surfaces[1:]:
                if isinstance(surface, inp.Surface):
                    vis += surface.draw()
            return vis

        return _visualization.Visualization()

    @property
    def title(self) -> types.Integer:
        """
        File title.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._title

    @title.setter
    def title(self, title: str | types.String) -> None:
        """
        Sets ``title``.

        Parameters:
            title: File title.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if title is not None:
            if isinstance(title, types.String):
                title = title
            elif isinstance(title, str):
                title = types.String.from_mcnp(title)

        if title is None or not len(title) < 80:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, title)

        self._title: types.Integer = title

    @property
    def cells(self) -> types.Integer:
        """
        File cells card block.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cells

    @cells.setter
    def cells(self, cells: list[str] | list[inp.Cell | inp.Like | inp.Comment]) -> None:
        """
        Sets ``cells``.

        Parameters:
            cells: File cells.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cells is not None:
            array = []
            for item in cells:
                if isinstance(item, inp.Cell):
                    array.append(item)
                elif isinstance(item, inp.Like):
                    array.append(item)
                elif isinstance(item, inp.Comment):
                    array.append(item)
                elif isinstance(item, str):
                    try:
                        array.append(inp.Comment.from_mcnp(item))
                        continue
                    except errors.InpError:
                        pass

                    if 'like' in item:
                        array.append(inp.Like.from_mcnp(item))
                    else:
                        array.append(inp.Cell.from_mcnp(item))

            cells = types.Tuple(array)

        if cells is None or None in cells:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, cells)

        self._cells: types.Integer = cells

    @property
    def surfaces(self) -> types.Integer:
        """
        File surfaces card block.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._surfaces

    @surfaces.setter
    def surfaces(self, surfaces: list[str] | list[inp.Surface | inp.Comment]) -> None:
        """
        Sets ``surfaces``.

        Parameters:
            surfaces: File surfaces.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if surfaces is not None:
            array = []
            for item in surfaces:
                if isinstance(item, inp.Surface):
                    array.append(item)
                elif isinstance(item, inp.Comment):
                    array.append(item)
                elif isinstance(item, str):
                    try:
                        array.append(inp.Comment.from_mcnp(item))
                        continue
                    except errors.InpError:
                        pass
                    array.append(inp.Surface.from_mcnp(item))

            surfaces = types.Tuple(array)

        if surfaces is None or None in surfaces:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, surfaces)

        self._surfaces: types.Integer = surfaces

    @property
    def data(self) -> types.Integer:
        """
        File data card block.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._data

    @data.setter
    def data(self, data: list[str] | list[inp.Data | inp.Comment]) -> None:
        """
        Sets ``data``.

        Parameters:
            data: File data.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if data is not None:
            array = []
            for item in data:
                if isinstance(item, inp.Data):
                    array.append(item)
                elif isinstance(item, inp.Comment):
                    array.append(item)
                elif isinstance(item, str):
                    try:
                        array.append(inp.Comment.from_mcnp(item))
                        continue
                    except errors.InpError:
                        pass

                    array.append(inp.Data.from_mcnp(item))

            data = types.Tuple(array)

        if data is None or None in data:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP, data)

        self._data: types.Integer = data

    @property
    def message(self) -> types.Integer:
        """
        File message.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._message

    @message.setter
    def message(self, message: str | types.String) -> None:
        """
        Sets ``message``.

        Parameters:
            message: File message.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if message is not None:
            if isinstance(message, types.String):
                message = message
            elif isinstance(message, str):
                message = types.String.from_mcnp(message)

        self._message: types.Integer = message

    @property
    def other(self) -> types.Integer:
        """
        File other.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._other

    @other.setter
    def other(self, other: str | types.String) -> None:
        """
        Sets ``other``.

        Parameters:
            other: File other.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if other is not None:
            if isinstance(other, types.String):
                other = other
            elif isinstance(other, str):
                other = types.String.from_mcnp(other)

        self._other: types.Integer = other

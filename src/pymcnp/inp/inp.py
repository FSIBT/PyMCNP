import re
import typing

import pyvista

from . import card_cell
from . import card_surface
from . import card_data
from . import card_comment
from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _object
from ..utils import _visualization


class Inp(_object.McnpFile_):
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
        cells: tuple[card_cell.Cell],
        cells_comments: tuple[card_comment.Comment],
        surfaces: tuple[card_surface.Surface],
        surfaces_comments: tuple[card_comment.Comment],
        data: tuple[card_data.Data],
        data_comments: tuple[card_comment.Comment],
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
            InpError: SEMATNICS_INP_MESSAGE.
            InpError: SEMATNICS_INP_TITLE.
            InpError: SEMATNICS_INP_CELLS.
            InpError: SEMATNICS_INP_SURFACES.
            InpError: SEMATNICS_INP_DATA.
            InpError: SEMATNICS_INP_OTHER.
        """

        if title is None or not len(title) < 80:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_TITLE, title)

        if cells is None or None in cells:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_CELLS, cells)

        if cells_comments is None or None in cells_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_COMMENTS, cells_comments)

        if surfaces is None or None in surfaces:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_SURFACES, surfaces)

        if surfaces_comments is None or None in surfaces_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_COMMENTS, surfaces_comments)

        if data is None or None in data:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_DATA, data)

        if data_comments is None or None in data_comments:
            raise errors.InpError(errors.InpCode.SEMANTICS_INP_COMMENTS, data_comments)

        self.message: typing.Final[types.String] = message
        self.title: typing.Final[types.String] = title
        self.cells: dict[int, card_cell.Cell] = {cell.number.value: cell for cell in cells}
        self.cells_comments: tuple[card_comment.Comment] = types._Tuple(cells_comments)
        self.surfaces: dict[int, card_surface.Surface] = {
            surface.number.value: surface for surface in surfaces
        }
        self.surfaces_comments: tuple[card_comment.Comment] = types._Tuple(surfaces_comments)
        self.data: dict[int, card_data.Data] = {data.option._KEYWORD: data for data in data}
        self.data_comments: tuple[card_comment.Comment] = types._Tuple(data_comments)
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
                cells_comments.append(card_comment.Comment.from_mcnp(line))
            except errors.InpError:
                cells.append(card_cell.Cell.from_mcnp(line))

        surfaces = []
        surfaces_comments = []
        for line in tokens[4].strip().split('\n'):
            try:
                surfaces_comments.append(card_comment.Comment.from_mcnp(line))
            except errors.InpError:
                surfaces.append(card_surface.Surface.from_mcnp(line))

        data = []
        data_comments = []
        for line in tokens[5].strip().split('\n'):
            try:
                data_comments.append(card_comment.Comment.from_mcnp(line))
            except errors.InpError:
                data.append(card_data.Data.from_mcnp(line))

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
        source += '\n'.join(card.to_mcnp() for card in self.cells.values())
        source += '\n\n'

        source += DELIMITER
        source += f'c {"surfaces":^76.76}\n'
        source += DELIMITER
        source += '\n'.join(card.to_mcnp() for card in self.surfaces.values())
        source += '\n\n'

        source += DELIMITER
        source += f'c {"data":^76.76}\n'
        source += DELIMITER
        source += '\n'.join(card.to_mcnp() for card in self.data.values())
        source += '\nc\n'

        # Appending Extra
        source += self.other if self.other else ''

        return source

    def to_pyvista(self) -> pyvista.PolyData:
        """
        Generates ``pyvista.PolyData`` from ``Inp``.

        Returns:
            ``pyvista.PolyData`` for ``Inp``.
        """

        vis = _visualization.McnpVisualization()

        for surface in self.surfaces.values():
            vis += _visualization.McnpVisualization(surface.to_pyvista())

        return vis.data

    def update_nps(self, npp: int):
        """
        Updates the ``npp`` value on ``nps`` cards.

        Parameters:
            npp: New total number of histories to run.

        Returns:
            Updated ``Inp``.
        """

        if 'nps' in self.data:
            return self.modify(**{'data["nps"].option.npp.value': npp})
        else:
            return self.append(**{'data': card_data.Data.from_mcnp(f'nps {npp}')})

    def update_seed(self, seed: int):
        """
        Updates the ``seed`` option on ``rand`` cards.

        Parameters:
            seed: New random number generator seed.

        Returns:
           Updated ``Inp``.
        """

        if 'rand' in self.data:
            if 'seed' in self.data['rand'].option.options:
                return self.modify(**{'data["rand"].option.options["seed"].value': seed})
            else:
                return self.append(
                    **{
                        'data["rand"].option.options': card_data.data.DataOption_Rand.rand.RandOption_Seed.from_mcnp(
                            f'seed {seed}'
                        )
                    }
                )
        else:
            return self.append(**{'data': card_data.Data.from_mcnp(f'rand seed {seed}')})

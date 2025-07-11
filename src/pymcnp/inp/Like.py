import re

from . import like
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Like(Card):
    """
    Represents INP cell cards.

    Attributes:
        number: cell number.
        cell: cell similar.
        options: cell options.
    """

    _ATTRS = {
        'number': types.Integer,
        'cell': types.Integer,
        'options': types.Tuple[like.LikeOption],
    }

    _REGEX = re.compile(rf'\A(\S+) like (\S+) but((?: (?:{like.LikeOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(
        self,
        number: types.Integer,
        cell: types.Integer,
        options: types.Tuple[like.LikeOption] = None,
    ):
        """
        Initializes ``Like``.

        Parameters:
            number: cell number.
            cell: cell similar.
            options: cell options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.number: types.Integer = number
        self.cell: types.Integer = cell
        self.options: types.Tuple[like.LikeOption] = options

    def to_mcnp(self):
        """
        Generates INP from ``Like``.

        Returns:
            INP cell card.
        """

        source = f'{self.number} like {self.cell} but {self.options or ""}'
        source, comments = _parser.preprocess_inp(source)
        source = _parser.postprocess_inp(source)

        return source

    @property
    def number(self) -> types.Integer:
        """
        Gets ``number``.

        Returns:
            ``number``.
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets ``number``.

        Parameters:
            number: cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)
            else:
                raise TypeError

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)

        self._number: types.Integer = number

    @property
    def cell(self) -> types.Integer:
        """
        Gets ``cell``.

        Returns:
            ``cell``.
        """

        return self._cell

    @cell.setter
    def cell(self, cell: str | int | types.Integer) -> None:
        """
        Sets ``cell``.

        Parameters:
            cell: base cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cell is not None:
            if isinstance(cell, types.Integer):
                cell = cell
            elif isinstance(cell, int):
                cell = types.Integer(cell)
            elif isinstance(cell, str):
                cell = types.Integer.from_mcnp(cell)
            else:
                raise TypeError

        if cell is None or not (1 <= cell <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, cell)

        self._cell: types.Integer = cell

    @property
    def options(self) -> types.Tuple[like.LikeOption]:
        """
        Gets ``options``.

        Returns:
            ``options``.
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[like.LikeOption] = None) -> None:
        """
        Sets ``options``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, like.LikeOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(like.LikeOption.from_mcnp(item))
                else:
                    raise TypeError
            options = types.Tuple(array)

        self._options: types.Tuple[like.LikeOption] = options

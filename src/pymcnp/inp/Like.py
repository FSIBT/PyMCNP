import re

from . import like
from . import _card
from .. import types
from .. import errors


class Like(_card.Card):
    """
    Represents INP cell cards.
    """

    _ATTRS = {
        'number': types.Integer,
        'cell': types.Integer,
        'options': types.Tuple(like.LikeOption),
    }

    _REGEX = re.compile(rf'\A(\S+) like (\S+) but((?: (?:{like.LikeOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(
        self,
        number: types.Integer,
        cell: types.Integer,
        options: types.Tuple(like.LikeOption) = None,
    ):
        """
        Initializes `Like`.

        Parameters:
            number: Cell number.
            cell: Cell similar.
            options: Cell options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.number: types.Integer = number
        self.cell: types.Integer = cell
        self.options: types.Tuple(like.LikeOption) = options

    def to_mcnp(self):
        """
        Generates INP from `Like`.

        Returns:
            INP cell card.
        """

        source = f'{self.number} like {self.cell} but {self.options if self.options is not None else ""}'
        source = _card.Card._postprocess(source)

        return source

    @property
    def number(self) -> types.Integer:
        """
        Cell number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Cell number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)

        self._number: types.Integer = number

    @property
    def cell(self) -> types.Integer:
        """
        Base cell number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._cell

    @cell.setter
    def cell(self, cell: str | int | types.Integer) -> None:
        """
        Sets `cell`.

        Parameters:
            cell: Base cell number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if cell is not None:
            if isinstance(cell, types.Integer):
                cell = cell
            elif isinstance(cell, int):
                cell = types.Integer(cell)
            elif isinstance(cell, str):
                cell = types.Integer.from_mcnp(cell)

        if cell is None or not (1 <= cell <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, cell)

        self._cell: types.Integer = cell

    @property
    def options(self) -> types.Tuple(like.LikeOption):
        """
        Cell options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[like.LikeOption] = None) -> None:
        """
        Sets `options`.

        Parameters:
            options: Cell options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, like.LikeOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(like.LikeOption.from_mcnp(item))

            options = types.Tuple(like.LikeOption)(array)

        self._options: types.Tuple(like.LikeOption) = options

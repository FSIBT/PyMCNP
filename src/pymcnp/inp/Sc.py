import re

from . import _card
from .. import types
from .. import errors


class Sc(_card.Card):
    """
    Represents INP `sc` cards.
    """

    _KEYWORD = 'sc'

    _ATTRS = {
        'suffix': types.Integer,
        'comment': types.Tuple(types.String),
    }

    _REGEX = re.compile(rf'\Asc(\d+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, comment: list[str] | list[types.String]):
        """
        Initializes `Sc`.

        Parameters:
            suffix: Data card option suffix.
            comment: source comment.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.comment: types.Tuple(types.String) = comment

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def comment(self) -> types.Tuple(types.String):
        """
        Source comment

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._comment

    @comment.setter
    def comment(self, comment: list[str] | list[types.String]) -> None:
        """
        Sets `comment`.

        Parameters:
            comment: source comment.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if comment is not None:
            array = []
            for item in comment:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
            comment = types.Tuple(types.String)(array)

        if comment is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, comment)

        self._comment: types.Tuple(types.String) = comment

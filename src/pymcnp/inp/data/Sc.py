import re

from . import _option
from ...utils import types
from ...utils import errors


class Sc(_option.DataOption):
    """
    Represents INP sc elements.

    Attributes:
        suffix: Data card option suffix.
        comment: source comment.
    """

    _KEYWORD = 'sc'

    _ATTRS = {
        'suffix': types.Integer,
        'comment': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Asc(\d+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, comment: list[str] | list[types.String]):
        """
        Initializes ``Sc``.

        Parameters:
            suffix: Data card option suffix.
            comment: source comment.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.comment: types.Tuple[types.String] = comment

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)
            else:
                raise TypeError

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def comment(self) -> types.Tuple[types.String]:
        """
        Gets ``comment``.

        Returns:
            ``comment``.
        """

        return self._comment

    @comment.setter
    def comment(self, comment: list[str] | list[types.String]) -> None:
        """
        Sets ``comment``.

        Parameters:
            comment: source comment.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if comment is not None:
            array = []
            for item in comment:
                if isinstance(item, types.String):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.String.from_mcnp(item))
                else:
                    raise TypeError
            comment = types.Tuple(array)

        if comment is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, comment)

        self._comment: types.Tuple[types.String] = comment

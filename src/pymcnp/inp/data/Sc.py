import re
import copy
import typing
import dataclasses


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

    def __init__(self, suffix: types.Integer, comment: types.Tuple[types.String]):
        """
        Initializes ``Sc``.

        Parameters:
            suffix: Data card option suffix.
            comment: source comment.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (1 <= suffix.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if comment is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, comment)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                comment,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.comment: typing.Final[types.Tuple[types.String]] = comment


@dataclasses.dataclass
class ScBuilder(_option.DataOptionBuilder):
    """
    Builds ``Sc``.

    Attributes:
        suffix: Data card option suffix.
        comment: source comment.
    """

    suffix: str | int | types.Integer
    comment: list[str] | list[types.String]

    def build(self):
        """
        Builds ``ScBuilder`` into ``Sc``.

        Returns:
            ``Sc`` for ``ScBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.comment:
            comment = []
            for item in self.comment:
                if isinstance(item, types.String):
                    comment.append(item)
                elif isinstance(item, str):
                    comment.append(types.String.from_mcnp(item))
            comment = types.Tuple(comment)
        else:
            comment = None

        return Sc(
            suffix=suffix,
            comment=comment,
        )

    @staticmethod
    def unbuild(ast: Sc):
        """
        Unbuilds ``Sc`` into ``ScBuilder``

        Returns:
            ``ScBuilder`` for ``Sc``.
        """

        return ScBuilder(
            suffix=copy.deepcopy(ast.suffix),
            comment=copy.deepcopy(ast.comment),
        )

import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sc(DataOption, keyword='sc'):
    """
    Represents INP sc elements.

    Attributes:
        suffix: Data card option suffix.
        comment: source comment.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'comment': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Asc(\d+)((?: {types.String._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, comment: types.Tuple[types.String]):
        """
        Initializes ``Sc``.

        Parameters:
            suffix: Data card option suffix.
            comment: source comment.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if comment is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, comment)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                comment,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.comment: typing.Final[types.Tuple[types.String]] = comment


@dataclasses.dataclass
class ScBuilder:
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

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        comment = []
        for item in self.comment:
            if isinstance(item, types.String):
                comment.append(item)
            elif isinstance(item, str):
                comment.append(types.String.from_mcnp(item))
            else:
                comment.append(item.build())
        comment = types.Tuple(comment)

        return Sc(
            suffix=suffix,
            comment=comment,
        )

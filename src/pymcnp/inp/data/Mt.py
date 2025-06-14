import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Mt(_option.DataOption):
    """
    Represents INP mt elements.

    Attributes:
        suffix: Data card option suffix.
        identifiers: Corresponding S(α,β) identifier.
    """

    _KEYWORD = 'mt'

    _ATTRS = {
        'suffix': types.Integer,
        'identifiers': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Amt(\d+)((?: {types.String._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, identifiers: types.Tuple[types.String]):
        """
        Initializes ``Mt``.

        Parameters:
            suffix: Data card option suffix.
            identifiers: Corresponding S(α,β) identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if identifiers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, identifiers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                identifiers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.identifiers: typing.Final[types.Tuple[types.String]] = identifiers


@dataclasses.dataclass
class MtBuilder(_option.DataOptionBuilder):
    """
    Builds ``Mt``.

    Attributes:
        suffix: Data card option suffix.
        identifiers: Corresponding S(α,β) identifier.
    """

    suffix: str | int | types.Integer
    identifiers: list[str] | list[types.String]

    def build(self):
        """
        Builds ``MtBuilder`` into ``Mt``.

        Returns:
            ``Mt`` for ``MtBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.identifiers:
            identifiers = []
            for item in self.identifiers:
                if isinstance(item, types.String):
                    identifiers.append(item)
                elif isinstance(item, str):
                    identifiers.append(types.String.from_mcnp(item))
            identifiers = types.Tuple(identifiers)
        else:
            identifiers = None

        return Mt(
            suffix=suffix,
            identifiers=identifiers,
        )

    @staticmethod
    def unbuild(ast: Mt):
        """
        Unbuilds ``Mt`` into ``MtBuilder``

        Returns:
            ``MtBuilder`` for ``Mt``.
        """

        return MtBuilder(
            suffix=copy.deepcopy(ast.suffix),
            identifiers=copy.deepcopy(ast.identifiers),
        )

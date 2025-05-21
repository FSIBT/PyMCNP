import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Mt(DataOption):
    """
    Represents INP mt elements.

    Attributes:
        suffix: Data card option suffix.
        identifiers: Corresponding S(α,β) identifier.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'identifiers': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Amt(\d+)((?: {types.String._REGEX.pattern})+?)\Z')

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
class MtBuilder:
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
                else:
                    identifiers.append(item.build())
            identifiers = types.Tuple(identifiers)
        else:
            identifiers = None

        return Mt(
            suffix=suffix,
            identifiers=identifiers,
        )

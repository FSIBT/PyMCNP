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
        identifier: Corresponding S(α,β) identifier.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'identifier': types.String,
    }

    _REGEX = re.compile(rf'\Amt(\d+)( {types.String._REGEX.pattern})\Z')

    def __init__(self, suffix: types.Integer, identifier: types.String):
        """
        Initializes ``Mt``.

        Parameters:
            suffix: Data card option suffix.
            identifier: Corresponding S(α,β) identifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if identifier is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, identifier)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                identifier,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.identifier: typing.Final[types.String] = identifier


@dataclasses.dataclass
class MtBuilder:
    """
    Builds ``Mt``.

    Attributes:
        suffix: Data card option suffix.
        identifier: Corresponding S(α,β) identifier.
    """

    suffix: str | int | types.Integer
    identifier: str | types.String

    def build(self):
        """
        Builds ``MtBuilder`` into ``Mt``.

        Returns:
            ``Mt`` for ``MtBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.identifier, types.String):
            identifier = self.identifier
        elif isinstance(self.identifier, str):
            identifier = types.String.from_mcnp(self.identifier)

        return Mt(
            suffix=suffix,
            identifier=identifier,
        )

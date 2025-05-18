import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ngroup(BlockOption):
    """
    Represents INP ngroup elements.

    Attributes:
        value: Number of energy groups.
    """

    _ATTRS = {
        'value': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Angroup( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, value: types.IntegerOrJump):
        """
        Initializes ``Ngroup``.

        Parameters:
            value: Number of energy groups.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if value is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, value)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                value,
            ]
        )

        self.value: typing.Final[types.IntegerOrJump] = value


@dataclasses.dataclass
class NgroupBuilder:
    """
    Builds ``Ngroup``.

    Attributes:
        value: Number of energy groups.
    """

    value: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``NgroupBuilder`` into ``Ngroup``.

        Returns:
            ``Ngroup`` for ``NgroupBuilder``.
        """

        value = self.value
        if isinstance(self.value, types.Integer):
            value = self.value
        elif isinstance(self.value, int):
            value = types.IntegerOrJump(self.value)
        elif isinstance(self.value, str):
            value = types.IntegerOrJump.from_mcnp(self.value)

        return Ngroup(
            value=value,
        )

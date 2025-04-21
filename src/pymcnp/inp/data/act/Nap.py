import re
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Nap(ActOption, keyword='nap'):
    """
    Represents INP nap elements.

    Attributes:
        count: Number of activation products.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Anap( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Nap``.

        Parameters:
            count: Number of activation products.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None or not (0 <= count):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count


@dataclasses.dataclass
class NapBuilder:
    """
    Builds ``Nap``.

    Attributes:
        count: Number of activation products.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``NapBuilder`` into ``Nap``.

        Returns:
            ``Nap`` for ``NapBuilder``.
        """

        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Nap(
            count=count,
        )

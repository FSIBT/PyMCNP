import re
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Dnbais(ActOption, keyword='dnbais'):
    """
    Represents INP dnbais elements.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Adnbais( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Dnbais``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None or not (0 <= count <= 10):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count


@dataclasses.dataclass
class DnbaisBuilder:
    """
    Builds ``Dnbais``.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``DnbaisBuilder`` into ``Dnbais``.

        Returns:
            ``Dnbais`` for ``DnbaisBuilder``.
        """

        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Dnbais(
            count=count,
        )

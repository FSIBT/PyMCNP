import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Tints(FmeshOption):
    """
    Represents INP tints elements.

    Attributes:
        count: Number of mesh points for each mesh time.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Atints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Tints``.

        Parameters:
            count: Number of mesh points for each mesh time.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count


@dataclasses.dataclass
class TintsBuilder:
    """
    Builds ``Tints``.

    Attributes:
        count: Number of mesh points for each mesh time.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``TintsBuilder`` into ``Tints``.

        Returns:
            ``Tints`` for ``TintsBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Tints(
            count=count,
        )

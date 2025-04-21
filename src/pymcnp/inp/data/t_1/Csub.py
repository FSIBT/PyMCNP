import re
import typing
import dataclasses


from ._option import T_1Option
from ....utils import types
from ....utils import errors


class Csub(T_1Option, keyword='csub'):
    """
    Represents INP csub elements.

    Attributes:
        count: Number of subdivisions to use.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Acsub( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Csub``.

        Parameters:
            count: Number of subdivisions to use.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count


@dataclasses.dataclass
class CsubBuilder:
    """
    Builds ``Csub``.

    Attributes:
        count: Number of subdivisions to use.
    """

    count: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``CsubBuilder`` into ``Csub``.

        Returns:
            ``Csub`` for ``CsubBuilder``.
        """

        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.IntegerOrJump(self.count)
        elif isinstance(self.count, str):
            count = types.IntegerOrJump.from_mcnp(self.count)

        return Csub(
            count=count,
        )

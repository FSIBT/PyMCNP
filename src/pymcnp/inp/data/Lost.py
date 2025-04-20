import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lost(DataOption_, keyword='lost'):
    """
    Represents INP lost elements.

    Attributes:
        lost1: Number of particles which can be lost before job termination.
        lost2: Maximum number of debug prints for lost particles..
    """

    _ATTRS = {
        'lost1': types.IntegerOrJump,
        'lost2': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Alost( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, lost1: types.IntegerOrJump, lost2: types.IntegerOrJump):
        """
        Initializes ``Lost``.

        Parameters:
            lost1: Number of particles which can be lost before job termination.
            lost2: Maximum number of debug prints for lost particles..

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if lost1 is None or not (lost1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lost1)
        if lost2 is None or not (lost2 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lost2)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lost1,
                lost2,
            ]
        )

        self.lost1: typing.Final[types.IntegerOrJump] = lost1
        self.lost2: typing.Final[types.IntegerOrJump] = lost2


@dataclasses.dataclass
class LostBuilder:
    """
    Builds ``Lost``.

    Attributes:
        lost1: Number of particles which can be lost before job termination.
        lost2: Maximum number of debug prints for lost particles..
    """

    lost1: str | int | types.IntegerOrJump
    lost2: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``LostBuilder`` into ``Lost``.

        Returns:
            ``Lost`` for ``LostBuilder``.
        """

        if isinstance(self.lost1, types.Integer):
            lost1 = self.lost1
        elif isinstance(self.lost1, int):
            lost1 = types.IntegerOrJump(self.lost1)
        elif isinstance(self.lost1, str):
            lost1 = types.IntegerOrJump.from_mcnp(self.lost1)

        if isinstance(self.lost2, types.Integer):
            lost2 = self.lost2
        elif isinstance(self.lost2, int):
            lost2 = types.IntegerOrJump(self.lost2)
        elif isinstance(self.lost2, str):
            lost2 = types.IntegerOrJump.from_mcnp(self.lost2)

        return Lost(
            lost1=lost1,
            lost2=lost2,
        )

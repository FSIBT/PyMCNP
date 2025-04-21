import re
import typing
import dataclasses


from ._option import T_1Option
from ....utils import types
from ....utils import errors


class Cofi(T_1Option, keyword='cofi'):
    """
    Represents INP cofi elements.

    Attributes:
        time: Dead time interval.
    """

    _ATTRS = {
        'time': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Acofi( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, time: types.RealOrJump):
        """
        Initializes ``Cofi``.

        Parameters:
            time: Dead time interval.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time,
            ]
        )

        self.time: typing.Final[types.RealOrJump] = time


@dataclasses.dataclass
class CofiBuilder:
    """
    Builds ``Cofi``.

    Attributes:
        time: Dead time interval.
    """

    time: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``CofiBuilder`` into ``Cofi``.

        Returns:
            ``Cofi`` for ``CofiBuilder``.
        """

        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.RealOrJump(self.time)
        elif isinstance(self.time, str):
            time = types.RealOrJump.from_mcnp(self.time)

        return Cofi(
            time=time,
        )

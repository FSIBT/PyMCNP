import re
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Coni(TOption_1):
    """
    Represents INP coni elements.

    Attributes:
        time: Alive time interval.
    """

    _ATTRS = {
        'time': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aconi( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, time: types.RealOrJump):
        """
        Initializes ``Coni``.

        Parameters:
            time: Alive time interval.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time,
            ]
        )

        self.time: typing.Final[types.RealOrJump] = time


@dataclasses.dataclass
class ConiBuilder:
    """
    Builds ``Coni``.

    Attributes:
        time: Alive time interval.
    """

    time: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ConiBuilder`` into ``Coni``.

        Returns:
            ``Coni`` for ``ConiBuilder``.
        """

        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.RealOrJump(self.time)
        elif isinstance(self.time, str):
            time = types.RealOrJump.from_mcnp(self.time)

        return Coni(
            time=time,
        )

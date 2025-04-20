import re
import typing
import dataclasses


from .option_ import T_1Option_
from ....utils import types
from ....utils import errors


class Cbeg(T_1Option_, keyword='cbeg'):
    """
    Represents INP cbeg elements.

    Attributes:
        time: Reference starting time.
    """

    _ATTRS = {
        'time': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Acbeg( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, time: types.RealOrJump):
        """
        Initializes ``Cbeg``.

        Parameters:
            time: Reference starting time.

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
class CbegBuilder:
    """
    Builds ``Cbeg``.

    Attributes:
        time: Reference starting time.
    """

    time: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``CbegBuilder`` into ``Cbeg``.

        Returns:
            ``Cbeg`` for ``CbegBuilder``.
        """

        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.RealOrJump(self.time)
        elif isinstance(self.time, str):
            time = types.RealOrJump.from_mcnp(self.time)

        return Cbeg(
            time=time,
        )

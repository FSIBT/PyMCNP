import re
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Cfrq(TOption_1):
    """
    Represents INP cfrq elements.

    Attributes:
        frequency: Frequency of cycling.
    """

    _ATTRS = {
        'frequency': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Acfrq( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, frequency: types.RealOrJump):
        """
        Initializes ``Cfrq``.

        Parameters:
            frequency: Frequency of cycling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if frequency is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, frequency)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                frequency,
            ]
        )

        self.frequency: typing.Final[types.RealOrJump] = frequency


@dataclasses.dataclass
class CfrqBuilder:
    """
    Builds ``Cfrq``.

    Attributes:
        frequency: Frequency of cycling.
    """

    frequency: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``CfrqBuilder`` into ``Cfrq``.

        Returns:
            ``Cfrq`` for ``CfrqBuilder``.
        """

        if isinstance(self.frequency, types.Real):
            frequency = self.frequency
        elif isinstance(self.frequency, float) or isinstance(self.frequency, int):
            frequency = types.RealOrJump(self.frequency)
        elif isinstance(self.frequency, str):
            frequency = types.RealOrJump.from_mcnp(self.frequency)

        return Cfrq(
            frequency=frequency,
        )

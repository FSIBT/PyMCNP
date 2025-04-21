import re
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Time(EmbeeOption, keyword='time'):
    """
    Represents INP time elements.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    _ATTRS = {
        'factor': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Atime( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, factor: types.RealOrJump):
        """
        Initializes ``Time``.

        Parameters:
            factor: Multiplicative conversion factor for time-related output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.RealOrJump] = factor


@dataclasses.dataclass
class TimeBuilder:
    """
    Builds ``Time``.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    factor: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``TimeBuilder`` into ``Time``.

        Returns:
            ``Time`` for ``TimeBuilder``.
        """

        if isinstance(self.factor, types.Real):
            factor = self.factor
        elif isinstance(self.factor, float) or isinstance(self.factor, int):
            factor = types.RealOrJump(self.factor)
        elif isinstance(self.factor, str):
            factor = types.RealOrJump.from_mcnp(self.factor)

        return Time(
            factor=factor,
        )

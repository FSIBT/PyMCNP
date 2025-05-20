import re
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Time(EmbeeOption):
    """
    Represents INP time elements.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    _ATTRS = {
        'factor': types.Real,
    }

    _REGEX = re.compile(rf'\Atime( {types.Real._REGEX.pattern})\Z')

    def __init__(self, factor: types.Real):
        """
        Initializes ``Time``.

        Parameters:
            factor: Multiplicative conversion factor for time-related output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if factor is None or not (factor.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.Real] = factor


@dataclasses.dataclass
class TimeBuilder:
    """
    Builds ``Time``.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    factor: str | float | types.Real

    def build(self):
        """
        Builds ``TimeBuilder`` into ``Time``.

        Returns:
            ``Time`` for ``TimeBuilder``.
        """

        factor = self.factor
        if isinstance(self.factor, types.Real):
            factor = self.factor
        elif isinstance(self.factor, float) or isinstance(self.factor, int):
            factor = types.Real(self.factor)
        elif isinstance(self.factor, str):
            factor = types.Real.from_mcnp(self.factor)

        return Time(
            factor=factor,
        )

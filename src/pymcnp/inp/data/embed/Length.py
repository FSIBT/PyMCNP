import re
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Length(EmbedOption):
    """
    Represents INP length elements.

    Attributes:
        factor: Conversion factor to centimeters for all mesh dimentions.
    """

    _ATTRS = {
        'factor': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Alength( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, factor: types.RealOrJump):
        """
        Initializes ``Length``.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

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
class LengthBuilder:
    """
    Builds ``Length``.

    Attributes:
        factor: Conversion factor to centimeters for all mesh dimentions.
    """

    factor: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``LengthBuilder`` into ``Length``.

        Returns:
            ``Length`` for ``LengthBuilder``.
        """

        factor = self.factor
        if isinstance(self.factor, types.Real):
            factor = self.factor
        elif isinstance(self.factor, float) or isinstance(self.factor, int):
            factor = types.RealOrJump(self.factor)
        elif isinstance(self.factor, str):
            factor = types.RealOrJump.from_mcnp(self.factor)

        return Length(
            factor=factor,
        )

import re
import typing
import dataclasses


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Field(BfldOption_, keyword='field'):
    """
    Represents INP field elements.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    _ATTRS = {
        'strength_gradient': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afield( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, strength_gradient: types.RealOrJump):
        """
        Initializes ``Field``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, strength_gradient)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                strength_gradient,
            ]
        )

        self.strength_gradient: typing.Final[types.RealOrJump] = strength_gradient


@dataclasses.dataclass
class FieldBuilder:
    """
    Builds ``Field``.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    strength_gradient: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FieldBuilder`` into ``Field``.

        Returns:
            ``Field`` for ``FieldBuilder``.
        """

        if isinstance(self.strength_gradient, types.Real):
            strength_gradient = self.strength_gradient
        elif isinstance(self.strength_gradient, float) or isinstance(self.strength_gradient, int):
            strength_gradient = types.RealOrJump(self.strength_gradient)
        elif isinstance(self.strength_gradient, str):
            strength_gradient = types.RealOrJump.from_mcnp(self.strength_gradient)

        return Field(
            strength_gradient=strength_gradient,
        )

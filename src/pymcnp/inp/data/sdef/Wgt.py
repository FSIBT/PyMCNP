import re
import typing
import dataclasses


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Wgt(SdefOption_, keyword='wgt'):
    """
    Represents INP wgt elements.

    Attributes:
        weight: Particle weight.
    """

    _ATTRS = {
        'weight': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Awgt( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, weight: types.RealOrJump):
        """
        Initializes ``Wgt``.

        Parameters:
            weight: Particle weight.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight,
            ]
        )

        self.weight: typing.Final[types.RealOrJump] = weight


@dataclasses.dataclass
class WgtBuilder:
    """
    Builds ``Wgt``.

    Attributes:
        weight: Particle weight.
    """

    weight: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``WgtBuilder`` into ``Wgt``.

        Returns:
            ``Wgt`` for ``WgtBuilder``.
        """

        if isinstance(self.weight, types.Real):
            weight = self.weight
        elif isinstance(self.weight, float) or isinstance(self.weight, int):
            weight = types.RealOrJump(self.weight)
        elif isinstance(self.weight, str):
            weight = types.RealOrJump.from_mcnp(self.weight)

        return Wgt(
            weight=weight,
        )

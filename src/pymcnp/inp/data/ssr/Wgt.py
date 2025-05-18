import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Wgt(SsrOption):
    """
    Represents INP wgt elements.

    Attributes:
        constant: Particle weight multiplier.
    """

    _ATTRS = {
        'constant': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Awgt( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, constant: types.RealOrJump):
        """
        Initializes ``Wgt``.

        Parameters:
            constant: Particle weight multiplier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.RealOrJump] = constant


@dataclasses.dataclass
class WgtBuilder:
    """
    Builds ``Wgt``.

    Attributes:
        constant: Particle weight multiplier.
    """

    constant: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``WgtBuilder`` into ``Wgt``.

        Returns:
            ``Wgt`` for ``WgtBuilder``.
        """

        constant = self.constant
        if isinstance(self.constant, types.Real):
            constant = self.constant
        elif isinstance(self.constant, float) or isinstance(self.constant, int):
            constant = types.RealOrJump(self.constant)
        elif isinstance(self.constant, str):
            constant = types.RealOrJump.from_mcnp(self.constant)

        return Wgt(
            constant=constant,
        )

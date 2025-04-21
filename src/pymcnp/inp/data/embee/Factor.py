import re
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Factor(EmbeeOption, keyword='factor'):
    """
    Represents INP factor elements.

    Attributes:
        constant: Multiplicative constant.
    """

    _ATTRS = {
        'constant': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afactor( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, constant: types.RealOrJump):
        """
        Initializes ``Factor``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.RealOrJump] = constant


@dataclasses.dataclass
class FactorBuilder:
    """
    Builds ``Factor``.

    Attributes:
        constant: Multiplicative constant.
    """

    constant: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FactorBuilder`` into ``Factor``.

        Returns:
            ``Factor`` for ``FactorBuilder``.
        """

        if isinstance(self.constant, types.Real):
            constant = self.constant
        elif isinstance(self.constant, float) or isinstance(self.constant, int):
            constant = types.RealOrJump(self.constant)
        elif isinstance(self.constant, str):
            constant = types.RealOrJump.from_mcnp(self.constant)

        return Factor(
            constant=constant,
        )

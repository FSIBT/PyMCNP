import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Psc(SsrOption, keyword='psc'):
    """
    Represents INP psc elements.

    Attributes:
        constant: Constant for approximation in PSC evaluation.
    """

    _ATTRS = {
        'constant': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Apsc( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, constant: types.RealOrJump):
        """
        Initializes ``Psc``.

        Parameters:
            constant: Constant for approximation in PSC evaluation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if constant is None or not (constant >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.RealOrJump] = constant


@dataclasses.dataclass
class PscBuilder:
    """
    Builds ``Psc``.

    Attributes:
        constant: Constant for approximation in PSC evaluation.
    """

    constant: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``PscBuilder`` into ``Psc``.

        Returns:
            ``Psc`` for ``PscBuilder``.
        """

        if isinstance(self.constant, types.Real):
            constant = self.constant
        elif isinstance(self.constant, float) or isinstance(self.constant, int):
            constant = types.RealOrJump(self.constant)
        elif isinstance(self.constant, str):
            constant = types.RealOrJump.from_mcnp(self.constant)

        return Psc(
            constant=constant,
        )

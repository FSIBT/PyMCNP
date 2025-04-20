import re
import typing
import dataclasses


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Inc(FmeshOption_, keyword='inc'):
    """
    Represents INP inc elements.

    Attributes:
        lower: Collision for FMESH tally lower bound.
        upper: Collision for FMESH tally upper bound.
    """

    _ATTRS = {
        'lower': types.RealOrJump,
        'upper': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Ainc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})?\Z'
    )

    def __init__(self, lower: types.RealOrJump, upper: types.RealOrJump = None):
        """
        Initializes ``Inc``.

        Parameters:
            lower: Collision for FMESH tally lower bound.
            upper: Collision for FMESH tally upper bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lower)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lower,
                upper,
            ]
        )

        self.lower: typing.Final[types.RealOrJump] = lower
        self.upper: typing.Final[types.RealOrJump] = upper


@dataclasses.dataclass
class IncBuilder:
    """
    Builds ``Inc``.

    Attributes:
        lower: Collision for FMESH tally lower bound.
        upper: Collision for FMESH tally upper bound.
    """

    lower: str | float | types.RealOrJump
    upper: str | float | types.RealOrJump = None

    def build(self):
        """
        Builds ``IncBuilder`` into ``Inc``.

        Returns:
            ``Inc`` for ``IncBuilder``.
        """

        if isinstance(self.lower, types.Real):
            lower = self.lower
        elif isinstance(self.lower, float) or isinstance(self.lower, int):
            lower = types.RealOrJump(self.lower)
        elif isinstance(self.lower, str):
            lower = types.RealOrJump.from_mcnp(self.lower)

        upper = None
        if isinstance(self.upper, types.Real):
            upper = self.upper
        elif isinstance(self.upper, float) or isinstance(self.upper, int):
            upper = types.RealOrJump(self.upper)
        elif isinstance(self.upper, str):
            upper = types.RealOrJump.from_mcnp(self.upper)

        return Inc(
            lower=lower,
            upper=upper,
        )

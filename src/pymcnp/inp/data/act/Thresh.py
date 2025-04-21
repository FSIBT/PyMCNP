import re
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Thresh(ActOption, keyword='thresh'):
    """
    Represents INP thresh elements.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    _ATTRS = {
        'fraction': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Athresh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fraction: types.RealOrJump):
        """
        Initializes ``Thresh``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fraction is None or not (0 <= fraction <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fraction)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fraction,
            ]
        )

        self.fraction: typing.Final[types.RealOrJump] = fraction


@dataclasses.dataclass
class ThreshBuilder:
    """
    Builds ``Thresh``.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    fraction: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``ThreshBuilder`` into ``Thresh``.

        Returns:
            ``Thresh`` for ``ThreshBuilder``.
        """

        if isinstance(self.fraction, types.Real):
            fraction = self.fraction
        elif isinstance(self.fraction, float) or isinstance(self.fraction, int):
            fraction = types.RealOrJump(self.fraction)
        elif isinstance(self.fraction, str):
            fraction = types.RealOrJump.from_mcnp(self.fraction)

        return Thresh(
            fraction=fraction,
        )

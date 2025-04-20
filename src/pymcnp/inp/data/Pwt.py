import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Pwt(DataOption_, keyword='pwt'):
    """
    Represents INP pwt elements.

    Attributes:
        weights: Relative threshold weight of photons produced at neutron collisions in cell.
    """

    _ATTRS = {
        'weights': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Apwt((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, weights: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Pwt``.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weights is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weights)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weights,
            ]
        )

        self.weights: typing.Final[types.Tuple[types.RealOrJump]] = weights


@dataclasses.dataclass
class PwtBuilder:
    """
    Builds ``Pwt``.

    Attributes:
        weights: Relative threshold weight of photons produced at neutron collisions in cell.
    """

    weights: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``PwtBuilder`` into ``Pwt``.

        Returns:
            ``Pwt`` for ``PwtBuilder``.
        """

        weights = []
        for item in self.weights:
            if isinstance(item, types.RealOrJump):
                weights.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                weights.append(types.RealOrJump(item))
            elif isinstance(item, str):
                weights.append(types.RealOrJump.from_mcnp(item))
        weights = types.Tuple(weights)

        return Pwt(
            weights=weights,
        )

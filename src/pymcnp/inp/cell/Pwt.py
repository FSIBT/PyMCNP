import re
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Pwt(CellOption, keyword='pwt'):
    """
    Represents INP pwt elements.

    Attributes:
        weight: Cell weight of photons produced at neutron collisions.
    """

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Apwt( {types.Real._REGEX.pattern})\Z')

    def __init__(self, weight: types.Real):
        """
        Initializes ``Pwt``.

        Parameters:
            weight: Cell weight of photons produced at neutron collisions.

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

        self.weight: typing.Final[types.Real] = weight


@dataclasses.dataclass
class PwtBuilder:
    """
    Builds ``Pwt``.

    Attributes:
        weight: Cell weight of photons produced at neutron collisions.
    """

    weight: str | float | types.Real

    def build(self):
        """
        Builds ``PwtBuilder`` into ``Pwt``.

        Returns:
            ``Pwt`` for ``PwtBuilder``.
        """

        if isinstance(self.weight, types.Real):
            weight = self.weight
        elif isinstance(self.weight, float) or isinstance(self.weight, int):
            weight = types.Real(self.weight)
        elif isinstance(self.weight, str):
            weight = types.Real.from_mcnp(self.weight)

        return Pwt(
            weight=weight,
        )

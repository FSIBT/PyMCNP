import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Pwt(DataOption):
    """
    Represents INP pwt elements.

    Attributes:
        weights: Relative threshold weight of photons produced at neutron collisions in cell.
    """

    _KEYWORD = 'pwt'

    _ATTRS = {
        'weights': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Apwt((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, weights: types.Tuple[types.Real]):
        """
        Initializes ``Pwt``.

        Parameters:
            weights: Relative threshold weight of photons produced at neutron collisions in cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if weights is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weights)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weights,
            ]
        )

        self.weights: typing.Final[types.Tuple[types.Real]] = weights


@dataclasses.dataclass
class PwtBuilder:
    """
    Builds ``Pwt``.

    Attributes:
        weights: Relative threshold weight of photons produced at neutron collisions in cell.
    """

    weights: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``PwtBuilder`` into ``Pwt``.

        Returns:
            ``Pwt`` for ``PwtBuilder``.
        """

        if self.weights:
            weights = []
            for item in self.weights:
                if isinstance(item, types.Real):
                    weights.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    weights.append(types.Real(item))
                elif isinstance(item, str):
                    weights.append(types.Real.from_mcnp(item))
            weights = types.Tuple(weights)
        else:
            weights = None

        return Pwt(
            weights=weights,
        )

    @staticmethod
    def unbuild(ast: Pwt):
        """
        Unbuilds ``Pwt`` into ``PwtBuilder``

        Returns:
            ``PwtBuilder`` for ``Pwt``.
        """

        return Pwt(
            weights=copy.deepcopy(ast.weights),
        )

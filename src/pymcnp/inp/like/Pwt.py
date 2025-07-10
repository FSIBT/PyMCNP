import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Pwt(_option.LikeOption):
    """
    Represents INP pwt elements.

    Attributes:
        weight: Like weight of photons produced at neutron collisions.
    """

    _KEYWORD = 'pwt'

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Apwt( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, weight: types.Real):
        """
        Initializes ``Pwt``.

        Parameters:
            weight: Like weight of photons produced at neutron collisions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, weight)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight,
            ]
        )

        self.weight: typing.Final[types.Real] = weight


@dataclasses.dataclass
class PwtBuilder(_option.LikeOptionBuilder):
    """
    Builds ``Pwt``.

    Attributes:
        weight: Like weight of photons produced at neutron collisions.
    """

    weight: str | float | types.Real

    def build(self):
        """
        Builds ``PwtBuilder`` into ``Pwt``.

        Returns:
            ``Pwt`` for ``PwtBuilder``.
        """

        weight = self.weight
        if isinstance(self.weight, types.Real):
            weight = self.weight
        elif isinstance(self.weight, float) or isinstance(self.weight, int):
            weight = types.Real(self.weight)
        elif isinstance(self.weight, str):
            weight = types.Real.from_mcnp(self.weight)

        return Pwt(
            weight=weight,
        )

    @staticmethod
    def unbuild(ast: Pwt):
        """
        Unbuilds ``Pwt`` into ``PwtBuilder``

        Returns:
            ``PwtBuilder`` for ``Pwt``.
        """

        return PwtBuilder(
            weight=copy.deepcopy(ast.weight),
        )

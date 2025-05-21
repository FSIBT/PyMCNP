import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Wgt(SdefOption):
    """
    Represents INP wgt elements.

    Attributes:
        weight: Particle weight.
    """

    _KEYWORD = 'wgt'

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern})\Z')

    def __init__(self, weight: types.Real):
        """
        Initializes ``Wgt``.

        Parameters:
            weight: Particle weight.

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
class WgtBuilder:
    """
    Builds ``Wgt``.

    Attributes:
        weight: Particle weight.
    """

    weight: str | float | types.Real

    def build(self):
        """
        Builds ``WgtBuilder`` into ``Wgt``.

        Returns:
            ``Wgt`` for ``WgtBuilder``.
        """

        weight = self.weight
        if isinstance(self.weight, types.Real):
            weight = self.weight
        elif isinstance(self.weight, float) or isinstance(self.weight, int):
            weight = types.Real(self.weight)
        elif isinstance(self.weight, str):
            weight = types.Real.from_mcnp(self.weight)

        return Wgt(
            weight=weight,
        )

    @staticmethod
    def unbuild(ast: Wgt):
        """
        Unbuilds ``Wgt`` into ``WgtBuilder``

        Returns:
            ``WgtBuilder`` for ``Wgt``.
        """

        return Wgt(
            weight=copy.deepcopy(ast.weight),
        )

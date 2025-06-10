import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Refi(_option.MOption_0):
    """
    Represents INP refi elements.

    Attributes:
        refractive_index: Refractive index constant.
    """

    _KEYWORD = 'refi'

    _ATTRS = {
        'refractive_index': types.Real,
    }

    _REGEX = re.compile(rf'\Arefi( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, refractive_index: types.Real):
        """
        Initializes ``Refi``.

        Parameters:
            refractive_index: Refractive index constant.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if refractive_index is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, refractive_index)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                refractive_index,
            ]
        )

        self.refractive_index: typing.Final[types.Real] = refractive_index


@dataclasses.dataclass
class RefiBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Refi``.

    Attributes:
        refractive_index: Refractive index constant.
    """

    refractive_index: str | float | types.Real

    def build(self):
        """
        Builds ``RefiBuilder`` into ``Refi``.

        Returns:
            ``Refi`` for ``RefiBuilder``.
        """

        refractive_index = self.refractive_index
        if isinstance(self.refractive_index, types.Real):
            refractive_index = self.refractive_index
        elif isinstance(self.refractive_index, float) or isinstance(self.refractive_index, int):
            refractive_index = types.Real(self.refractive_index)
        elif isinstance(self.refractive_index, str):
            refractive_index = types.Real.from_mcnp(self.refractive_index)

        return Refi(
            refractive_index=refractive_index,
        )

    @staticmethod
    def unbuild(ast: Refi):
        """
        Unbuilds ``Refi`` into ``RefiBuilder``

        Returns:
            ``RefiBuilder`` for ``Refi``.
        """

        return RefiBuilder(
            refractive_index=copy.deepcopy(ast.refractive_index),
        )

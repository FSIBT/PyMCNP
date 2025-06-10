import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Hlcut(_option.ActOption):
    """
    Represents INP hlcut elements.

    Attributes:
        cutoff: Spontaneous-decay half-life threshold.
    """

    _KEYWORD = 'hlcut'

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Ahlcut( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``Hlcut``.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.Real] = cutoff


@dataclasses.dataclass
class HlcutBuilder(_option.ActOptionBuilder):
    """
    Builds ``Hlcut``.

    Attributes:
        cutoff: Spontaneous-decay half-life threshold.
    """

    cutoff: str | float | types.Real

    def build(self):
        """
        Builds ``HlcutBuilder`` into ``Hlcut``.

        Returns:
            ``Hlcut`` for ``HlcutBuilder``.
        """

        cutoff = self.cutoff
        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.Real(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.Real.from_mcnp(self.cutoff)

        return Hlcut(
            cutoff=cutoff,
        )

    @staticmethod
    def unbuild(ast: Hlcut):
        """
        Unbuilds ``Hlcut`` into ``HlcutBuilder``

        Returns:
            ``HlcutBuilder`` for ``Hlcut``.
        """

        return HlcutBuilder(
            cutoff=copy.deepcopy(ast.cutoff),
        )

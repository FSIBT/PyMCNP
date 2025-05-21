import re
import copy
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Pecut(ActOption):
    """
    Represents INP pecut elements.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    _KEYWORD = 'pecut'

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Apecut( {types.Real._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``Pecut``.

        Parameters:
            cutoff: Delayed-gamma energy cutoff.

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
class PecutBuilder:
    """
    Builds ``Pecut``.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    cutoff: str | float | types.Real

    def build(self):
        """
        Builds ``PecutBuilder`` into ``Pecut``.

        Returns:
            ``Pecut`` for ``PecutBuilder``.
        """

        cutoff = self.cutoff
        if isinstance(self.cutoff, types.Real):
            cutoff = self.cutoff
        elif isinstance(self.cutoff, float) or isinstance(self.cutoff, int):
            cutoff = types.Real(self.cutoff)
        elif isinstance(self.cutoff, str):
            cutoff = types.Real.from_mcnp(self.cutoff)

        return Pecut(
            cutoff=cutoff,
        )

    @staticmethod
    def unbuild(ast: Pecut):
        """
        Unbuilds ``Pecut`` into ``PecutBuilder``

        Returns:
            ``PecutBuilder`` for ``Pecut``.
        """

        return Pecut(
            cutoff=copy.deepcopy(ast.cutoff),
        )

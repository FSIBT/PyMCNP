import re
import copy
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class List(EmbeeOption):
    """
    Represents INP list elements.

    Attributes:
        reactions: List of reactions.
    """

    _KEYWORD = 'list'

    _ATTRS = {
        'reactions': types.Real,
    }

    _REGEX = re.compile(rf'\Alist( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, reactions: types.Real):
        """
        Initializes ``List``.

        Parameters:
            reactions: List of reactions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if reactions is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, reactions)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                reactions,
            ]
        )

        self.reactions: typing.Final[types.Real] = reactions


@dataclasses.dataclass
class ListBuilder:
    """
    Builds ``List``.

    Attributes:
        reactions: List of reactions.
    """

    reactions: str | float | types.Real

    def build(self):
        """
        Builds ``ListBuilder`` into ``List``.

        Returns:
            ``List`` for ``ListBuilder``.
        """

        reactions = self.reactions
        if isinstance(self.reactions, types.Real):
            reactions = self.reactions
        elif isinstance(self.reactions, float) or isinstance(self.reactions, int):
            reactions = types.Real(self.reactions)
        elif isinstance(self.reactions, str):
            reactions = types.Real.from_mcnp(self.reactions)

        return List(
            reactions=reactions,
        )

    @staticmethod
    def unbuild(ast: List):
        """
        Unbuilds ``List`` into ``ListBuilder``

        Returns:
            ``ListBuilder`` for ``List``.
        """

        return List(
            reactions=copy.deepcopy(ast.reactions),
        )

import re

from . import _option
from ....utils import types
from ....utils import errors


class List(_option.EmbeeOption):
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

    def __init__(self, reactions: str | int | float | types.Real):
        """
        Initializes ``List``.

        Parameters:
            reactions: List of reactions.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.reactions: types.Real = reactions

    @property
    def reactions(self) -> types.Real:
        """
        Gets ``reactions``.

        Returns:
            ``reactions``.
        """

        return self._reactions

    @reactions.setter
    def reactions(self, reactions: str | int | float | types.Real) -> None:
        """
        Sets ``reactions``.

        Parameters:
            reactions: List of reactions.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if reactions is not None:
            if isinstance(reactions, types.Real):
                reactions = reactions
            elif isinstance(reactions, int):
                reactions = types.Real(reactions)
            elif isinstance(reactions, float):
                reactions = types.Real(reactions)
            elif isinstance(reactions, str):
                reactions = types.Real.from_mcnp(reactions)
            else:
                raise TypeError

        if reactions is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, reactions)

        self._reactions: types.Real = reactions

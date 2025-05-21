import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Lost(DataOption):
    """
    Represents INP lost elements.

    Attributes:
        lost1: Number of particles which can be lost before job termination.
        lost2: Maximum number of debug prints for lost particles..
    """

    _KEYWORD = 'lost'

    _ATTRS = {
        'lost1': types.Integer,
        'lost2': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Alost( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
    )

    def __init__(self, lost1: types.Integer, lost2: types.Integer):
        """
        Initializes ``Lost``.

        Parameters:
            lost1: Number of particles which can be lost before job termination.
            lost2: Maximum number of debug prints for lost particles..

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if lost1 is None or not (lost1.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lost1)
        if lost2 is None or not (lost2.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lost2)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lost1,
                lost2,
            ]
        )

        self.lost1: typing.Final[types.Integer] = lost1
        self.lost2: typing.Final[types.Integer] = lost2


@dataclasses.dataclass
class LostBuilder:
    """
    Builds ``Lost``.

    Attributes:
        lost1: Number of particles which can be lost before job termination.
        lost2: Maximum number of debug prints for lost particles..
    """

    lost1: str | int | types.Integer
    lost2: str | int | types.Integer

    def build(self):
        """
        Builds ``LostBuilder`` into ``Lost``.

        Returns:
            ``Lost`` for ``LostBuilder``.
        """

        lost1 = self.lost1
        if isinstance(self.lost1, types.Integer):
            lost1 = self.lost1
        elif isinstance(self.lost1, int):
            lost1 = types.Integer(self.lost1)
        elif isinstance(self.lost1, str):
            lost1 = types.Integer.from_mcnp(self.lost1)

        lost2 = self.lost2
        if isinstance(self.lost2, types.Integer):
            lost2 = self.lost2
        elif isinstance(self.lost2, int):
            lost2 = types.Integer(self.lost2)
        elif isinstance(self.lost2, str):
            lost2 = types.Integer.from_mcnp(self.lost2)

        return Lost(
            lost1=lost1,
            lost2=lost2,
        )

    @staticmethod
    def unbuild(ast: Lost):
        """
        Unbuilds ``Lost`` into ``LostBuilder``

        Returns:
            ``LostBuilder`` for ``Lost``.
        """

        return Lost(
            lost1=copy.deepcopy(ast.lost1),
            lost2=copy.deepcopy(ast.lost2),
        )

import re
import copy
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Maxstep(BfldOption):
    """
    Represents INP maxstep elements.

    Attributes:
        size: Maximum step size.
    """

    _KEYWORD = 'maxstep'

    _ATTRS = {
        'size': types.Real,
    }

    _REGEX = re.compile(rf'\Amaxstep( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, size: types.Real):
        """
        Initializes ``Maxstep``.

        Parameters:
            size: Maximum step size.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if size is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, size)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                size,
            ]
        )

        self.size: typing.Final[types.Real] = size


@dataclasses.dataclass
class MaxstepBuilder:
    """
    Builds ``Maxstep``.

    Attributes:
        size: Maximum step size.
    """

    size: str | float | types.Real

    def build(self):
        """
        Builds ``MaxstepBuilder`` into ``Maxstep``.

        Returns:
            ``Maxstep`` for ``MaxstepBuilder``.
        """

        size = self.size
        if isinstance(self.size, types.Real):
            size = self.size
        elif isinstance(self.size, float) or isinstance(self.size, int):
            size = types.Real(self.size)
        elif isinstance(self.size, str):
            size = types.Real.from_mcnp(self.size)

        return Maxstep(
            size=size,
        )

    @staticmethod
    def unbuild(ast: Maxstep):
        """
        Unbuilds ``Maxstep`` into ``MaxstepBuilder``

        Returns:
            ``MaxstepBuilder`` for ``Maxstep``.
        """

        return Maxstep(
            size=copy.deepcopy(ast.size),
        )

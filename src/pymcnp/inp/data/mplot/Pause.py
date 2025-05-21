import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Pause(MplotOption):
    """
    Represents INP pause elements.

    Attributes:
        n: Pause duration.
    """

    _KEYWORD = 'pause'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Apause( {types.Integer._REGEX.pattern})?\Z')

    def __init__(self, n: types.Integer = None):
        """
        Initializes ``Pause``.

        Parameters:
            n: Pause duration.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
            ]
        )

        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class PauseBuilder:
    """
    Builds ``Pause``.

    Attributes:
        n: Pause duration.
    """

    n: str | int | types.Integer = None

    def build(self):
        """
        Builds ``PauseBuilder`` into ``Pause``.

        Returns:
            ``Pause`` for ``PauseBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Pause(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Pause):
        """
        Unbuilds ``Pause`` into ``PauseBuilder``

        Returns:
            ``PauseBuilder`` for ``Pause``.
        """

        return Pause(
            n=copy.deepcopy(ast.n),
        )

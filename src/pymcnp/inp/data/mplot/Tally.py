import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Tally(MplotOption):
    """
    Represents INP tally elements.

    Attributes:
        n: Number of current tally.
    """

    _KEYWORD = 'tally'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Atally( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, n: types.Integer = None):
        """
        Initializes ``Tally``.

        Parameters:
            n: Number of current tally.

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
class TallyBuilder:
    """
    Builds ``Tally``.

    Attributes:
        n: Number of current tally.
    """

    n: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TallyBuilder`` into ``Tally``.

        Returns:
            ``Tally`` for ``TallyBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Tally(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Tally):
        """
        Unbuilds ``Tally`` into ``TallyBuilder``

        Returns:
            ``TallyBuilder`` for ``Tally``.
        """

        return Tally(
            n=copy.deepcopy(ast.n),
        )

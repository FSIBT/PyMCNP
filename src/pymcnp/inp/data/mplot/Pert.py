import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types


class Pert(_option.MplotOption):
    """
    Represents INP pert elements.

    Attributes:
        n: Number on a PERT card.
    """

    _KEYWORD = 'pert'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Apert( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, n: types.Integer = None):
        """
        Initializes ``Pert``.

        Parameters:
            n: Number on a PERT card.

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
class PertBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Pert``.

    Attributes:
        n: Number on a PERT card.
    """

    n: str | int | types.Integer = None

    def build(self):
        """
        Builds ``PertBuilder`` into ``Pert``.

        Returns:
            ``Pert`` for ``PertBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Pert(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Pert):
        """
        Unbuilds ``Pert`` into ``PertBuilder``

        Returns:
            ``PertBuilder`` for ``Pert``.
        """

        return PertBuilder(
            n=copy.deepcopy(ast.n),
        )

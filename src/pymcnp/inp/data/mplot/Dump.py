import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types


class Dump(_option.MplotOption):
    """
    Represents INP dump elements.

    Attributes:
        n: RUNTPE read dump number.
    """

    _KEYWORD = 'dump'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Adump( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, n: types.Integer = None):
        """
        Initializes ``Dump``.

        Parameters:
            n: RUNTPE read dump number.

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
class DumpBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Dump``.

    Attributes:
        n: RUNTPE read dump number.
    """

    n: str | int | types.Integer = None

    def build(self):
        """
        Builds ``DumpBuilder`` into ``Dump``.

        Returns:
            ``Dump`` for ``DumpBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Dump(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Dump):
        """
        Unbuilds ``Dump`` into ``DumpBuilder``

        Returns:
            ``DumpBuilder`` for ``Dump``.
        """

        return DumpBuilder(
            n=copy.deepcopy(ast.n),
        )

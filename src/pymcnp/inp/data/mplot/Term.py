import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Term(MplotOption):
    """
    Represents INP term elements.

    Attributes:
        n: Output decive specifier.
    """

    _KEYWORD = 'term'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aterm( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Term``.

        Parameters:
            n: Output decive specifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if n is None or n.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
            ]
        )

        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class TermBuilder:
    """
    Builds ``Term``.

    Attributes:
        n: Output decive specifier.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``TermBuilder`` into ``Term``.

        Returns:
            ``Term`` for ``TermBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Term(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Term):
        """
        Unbuilds ``Term`` into ``TermBuilder``

        Returns:
            ``TermBuilder`` for ``Term``.
        """

        return Term(
            n=copy.deepcopy(ast.n),
        )

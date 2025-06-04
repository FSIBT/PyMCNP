import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Fixed(MplotOption):
    """
    Represents INP fixed elements.

    Attributes:
        q: Fixed variable.
        n: Bin number.
    """

    _KEYWORD = 'fixed'

    _ATTRS = {
        'q': types.String,
        'n': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Afixed( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(self, q: types.String, n: types.Integer):
        """
        Initializes ``Fixed``.

        Parameters:
            q: Fixed variable.
            n: Bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if q is None or q not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't', 'i', 'j', 'k'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, q)
        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                q,
                n,
            ]
        )

        self.q: typing.Final[types.String] = q
        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class FixedBuilder:
    """
    Builds ``Fixed``.

    Attributes:
        q: Fixed variable.
        n: Bin number.
    """

    q: str | types.String
    n: str | int | types.Integer

    def build(self):
        """
        Builds ``FixedBuilder`` into ``Fixed``.

        Returns:
            ``Fixed`` for ``FixedBuilder``.
        """

        q = self.q
        if isinstance(self.q, types.String):
            q = self.q
        elif isinstance(self.q, str):
            q = types.String.from_mcnp(self.q)

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Fixed(
            q=q,
            n=n,
        )

    @staticmethod
    def unbuild(ast: Fixed):
        """
        Unbuilds ``Fixed`` into ``FixedBuilder``

        Returns:
            ``FixedBuilder`` for ``Fixed``.
        """

        return Fixed(
            q=copy.deepcopy(ast.q),
            n=copy.deepcopy(ast.n),
        )

import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Mt(MplotOption):
    """
    Represents INP mt elements.

    Attributes:
        n: Reaction number to print.
    """

    _KEYWORD = 'mt'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Amt( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Mt``.

        Parameters:
            n: Reaction number to print.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
            ]
        )

        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class MtBuilder:
    """
    Builds ``Mt``.

    Attributes:
        n: Reaction number to print.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``MtBuilder`` into ``Mt``.

        Returns:
            ``Mt`` for ``MtBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Mt(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Mt):
        """
        Unbuilds ``Mt`` into ``MtBuilder``

        Returns:
            ``MtBuilder`` for ``Mt``.
        """

        return Mt(
            n=copy.deepcopy(ast.n),
        )

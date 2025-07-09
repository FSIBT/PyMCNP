import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Title(_option.MplotOption):
    """
    Represents INP title elements.

    Attributes:
        n: Line number.
        aa: Line to substitute.
    """

    _KEYWORD = 'title'

    _ATTRS = {
        'n': types.Integer,
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Atitle( {types.Integer._REGEX.pattern[2:-2]})( \"{types.String._REGEX.pattern[2:-2]}\")\Z')

    def __init__(self, n: types.Integer, aa: types.String):
        """
        Initializes ``Title``.

        Parameters:
            n: Line number.
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if n is None or not (n > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)
        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
                aa,
            ]
        )

        self.n: typing.Final[types.Integer] = n
        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class TitleBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Title``.

    Attributes:
        n: Line number.
        aa: Line to substitute.
    """

    n: str | int | types.Integer
    aa: str | types.String

    def build(self):
        """
        Builds ``TitleBuilder`` into ``Title``.

        Returns:
            ``Title`` for ``TitleBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Title(
            n=n,
            aa=aa,
        )

    @staticmethod
    def unbuild(ast: Title):
        """
        Unbuilds ``Title`` into ``TitleBuilder``

        Returns:
            ``TitleBuilder`` for ``Title``.
        """

        return TitleBuilder(
            n=copy.deepcopy(ast.n),
            aa=copy.deepcopy(ast.aa),
        )

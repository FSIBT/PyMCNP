import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Scales(_option.MplotOption):
    """
    Represents INP scales elements.

    Attributes:
        n: Plot scale setting.
    """

    _KEYWORD = 'scales'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Ascales( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Scales``.

        Parameters:
            n: Plot scale setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if n is None or n.value not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
            ]
        )

        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class ScalesBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Scales``.

    Attributes:
        n: Plot scale setting.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``ScalesBuilder`` into ``Scales``.

        Returns:
            ``Scales`` for ``ScalesBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Scales(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Scales):
        """
        Unbuilds ``Scales`` into ``ScalesBuilder``

        Returns:
            ``ScalesBuilder`` for ``Scales``.
        """

        return ScalesBuilder(
            n=copy.deepcopy(ast.n),
        )

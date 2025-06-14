import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tbin(_option.MplotOption):
    """
    Represents INP tbin elements.

    Attributes:
        n: Time bin to plot.
    """

    _KEYWORD = 'tbin'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Atbin( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Tbin``.

        Parameters:
            n: Time bin to plot.

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
class TbinBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Tbin``.

    Attributes:
        n: Time bin to plot.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``TbinBuilder`` into ``Tbin``.

        Returns:
            ``Tbin`` for ``TbinBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Tbin(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Tbin):
        """
        Unbuilds ``Tbin`` into ``TbinBuilder``

        Returns:
            ``TbinBuilder`` for ``Tbin``.
        """

        return TbinBuilder(
            n=copy.deepcopy(ast.n),
        )

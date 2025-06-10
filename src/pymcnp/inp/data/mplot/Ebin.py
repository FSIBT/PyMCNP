import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ebin(_option.MplotOption):
    """
    Represents INP ebin elements.

    Attributes:
        n: Energy bin to plot.
    """

    _KEYWORD = 'ebin'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aebin( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Ebin``.

        Parameters:
            n: Energy bin to plot.

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
class EbinBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Ebin``.

    Attributes:
        n: Energy bin to plot.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``EbinBuilder`` into ``Ebin``.

        Returns:
            ``Ebin`` for ``EbinBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Ebin(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Ebin):
        """
        Unbuilds ``Ebin`` into ``EbinBuilder``

        Returns:
            ``EbinBuilder`` for ``Ebin``.
        """

        return EbinBuilder(
            n=copy.deepcopy(ast.n),
        )

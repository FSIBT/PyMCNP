import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Fmrelerr(_option.MplotOption):
    """
    Represents INP fmrelerr elements.

    Attributes:
        n: Tally error to plot.
    """

    _KEYWORD = 'fmrelerr'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Afmrelerr( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Fmrelerr``.

        Parameters:
            n: Tally error to plot.

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
class FmrelerrBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Fmrelerr``.

    Attributes:
        n: Tally error to plot.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``FmrelerrBuilder`` into ``Fmrelerr``.

        Returns:
            ``Fmrelerr`` for ``FmrelerrBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Fmrelerr(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Fmrelerr):
        """
        Unbuilds ``Fmrelerr`` into ``FmrelerrBuilder``

        Returns:
            ``FmrelerrBuilder`` for ``Fmrelerr``.
        """

        return FmrelerrBuilder(
            n=copy.deepcopy(ast.n),
        )

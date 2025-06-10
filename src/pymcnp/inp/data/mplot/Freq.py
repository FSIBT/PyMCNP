import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Freq(_option.MplotOption):
    """
    Represents INP freq elements.

    Attributes:
        n: Number of histories between plotting calls.
    """

    _KEYWORD = 'freq'

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Afreq( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Freq``.

        Parameters:
            n: Number of histories between plotting calls.

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
class FreqBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Freq``.

    Attributes:
        n: Number of histories between plotting calls.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``FreqBuilder`` into ``Freq``.

        Returns:
            ``Freq`` for ``FreqBuilder``.
        """

        n = self.n
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Freq(
            n=n,
        )

    @staticmethod
    def unbuild(ast: Freq):
        """
        Unbuilds ``Freq`` into ``FreqBuilder``

        Returns:
            ``FreqBuilder`` for ``Freq``.
        """

        return FreqBuilder(
            n=copy.deepcopy(ast.n),
        )

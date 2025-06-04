import re
import copy
import typing
import dataclasses


from ._option import RandOption
from ....utils import types
from ....utils import errors


class Hist(RandOption):
    """
    Represents INP hist elements.

    Attributes:
        hist: Starting pseudorandom number.
    """

    _KEYWORD = 'hist'

    _ATTRS = {
        'hist': types.Integer,
    }

    _REGEX = re.compile(rf'\Ahist( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, hist: types.Integer):
        """
        Initializes ``Hist``.

        Parameters:
            hist: Starting pseudorandom number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if hist is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hist)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                hist,
            ]
        )

        self.hist: typing.Final[types.Integer] = hist


@dataclasses.dataclass
class HistBuilder:
    """
    Builds ``Hist``.

    Attributes:
        hist: Starting pseudorandom number.
    """

    hist: str | int | types.Integer

    def build(self):
        """
        Builds ``HistBuilder`` into ``Hist``.

        Returns:
            ``Hist`` for ``HistBuilder``.
        """

        hist = self.hist
        if isinstance(self.hist, types.Integer):
            hist = self.hist
        elif isinstance(self.hist, int):
            hist = types.Integer(self.hist)
        elif isinstance(self.hist, str):
            hist = types.Integer.from_mcnp(self.hist)

        return Hist(
            hist=hist,
        )

    @staticmethod
    def unbuild(ast: Hist):
        """
        Unbuilds ``Hist`` into ``HistBuilder``

        Returns:
            ``HistBuilder`` for ``Hist``.
        """

        return Hist(
            hist=copy.deepcopy(ast.hist),
        )

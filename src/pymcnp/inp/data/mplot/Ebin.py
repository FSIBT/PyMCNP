import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Ebin(MplotOption):
    """
    Represents INP ebin elements.

    Attributes:
        n: Energy bin to plot.
    """

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Aebin( {types.Integer._REGEX.pattern})\Z')

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
class EbinBuilder:
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

        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Ebin(
            n=n,
        )

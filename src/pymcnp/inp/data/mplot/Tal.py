import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Tal(MplotOption):
    """
    Represents INP tal elements.

    Attributes:
        n: Tally number.
    """

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Atal( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, n: types.Integer):
        """
        Initializes ``Tal``.

        Parameters:
            n: Tally number.

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
class TalBuilder:
    """
    Builds ``Tal``.

    Attributes:
        n: Tally number.
    """

    n: str | int | types.Integer

    def build(self):
        """
        Builds ``TalBuilder`` into ``Tal``.

        Returns:
            ``Tal`` for ``TalBuilder``.
        """

        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Tal(
            n=n,
        )

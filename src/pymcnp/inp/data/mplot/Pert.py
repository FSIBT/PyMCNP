import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Pert(MplotOption, keyword='pert'):
    """
    Represents INP pert elements.

    Attributes:
        n: Number on a PERT card.
    """

    _ATTRS = {
        'n': types.Integer,
    }

    _REGEX = re.compile(rf'\Apert( {types.Integer._REGEX.pattern})?\Z')

    def __init__(self, n: types.Integer = None):
        """
        Initializes ``Pert``.

        Parameters:
            n: Number on a PERT card.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
            ]
        )

        self.n: typing.Final[types.Integer] = n


@dataclasses.dataclass
class PertBuilder:
    """
    Builds ``Pert``.

    Attributes:
        n: Number on a PERT card.
    """

    n: str | int | types.Integer = None

    def build(self):
        """
        Builds ``PertBuilder`` into ``Pert``.

        Returns:
            ``Pert`` for ``PertBuilder``.
        """

        n = None
        if isinstance(self.n, types.Integer):
            n = self.n
        elif isinstance(self.n, int):
            n = types.Integer(self.n)
        elif isinstance(self.n, str):
            n = types.Integer.from_mcnp(self.n)

        return Pert(
            n=n,
        )

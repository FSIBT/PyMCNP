import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Elpt(DataOption_, keyword='elpt'):
    """
    Represents INP elpt elements.

    Attributes:
        cutoffs: Tuple of cell lower energy cutoffs.
    """

    _ATTRS = {
        'cutoffs': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aelpt((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, cutoffs: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Elpt``.

        Parameters:
            cutoffs: Tuple of cell lower energy cutoffs.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoffs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoffs,
            ]
        )

        self.cutoffs: typing.Final[types.Tuple[types.RealOrJump]] = cutoffs


@dataclasses.dataclass
class ElptBuilder:
    """
    Builds ``Elpt``.

    Attributes:
        cutoffs: Tuple of cell lower energy cutoffs.
    """

    cutoffs: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``ElptBuilder`` into ``Elpt``.

        Returns:
            ``Elpt`` for ``ElptBuilder``.
        """

        cutoffs = []
        for item in self.cutoffs:
            if isinstance(item, types.RealOrJump):
                cutoffs.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                cutoffs.append(types.RealOrJump(item))
            elif isinstance(item, str):
                cutoffs.append(types.RealOrJump.from_mcnp(item))
        cutoffs = types.Tuple(cutoffs)

        return Elpt(
            cutoffs=cutoffs,
        )

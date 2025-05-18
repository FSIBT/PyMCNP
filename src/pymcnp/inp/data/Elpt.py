import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Elpt(DataOption):
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
            InpError: SEMANTICS_OPTION.
        """

        if cutoffs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cutoffs)

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

        if self.cutoffs:
            cutoffs = []
            for item in self.cutoffs:
                if isinstance(item, types.RealOrJump):
                    cutoffs.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    cutoffs.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    cutoffs.append(types.RealOrJump.from_mcnp(item))
            cutoffs = types.Tuple(cutoffs)
        else:
            cutoffs = None

        return Elpt(
            cutoffs=cutoffs,
        )

import re
import typing
import dataclasses


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Ein(KsenOption_, keyword='ein'):
    """
    Represents INP ein elements.

    Attributes:
        energies: List of ranges for incident energies.
    """

    _ATTRS = {
        'energies': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aein((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, energies: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Ein``.

        Parameters:
            energies: List of ranges for incident energies.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energies is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energies,
            ]
        )

        self.energies: typing.Final[types.Tuple[types.RealOrJump]] = energies


@dataclasses.dataclass
class EinBuilder:
    """
    Builds ``Ein``.

    Attributes:
        energies: List of ranges for incident energies.
    """

    energies: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``EinBuilder`` into ``Ein``.

        Returns:
            ``Ein`` for ``EinBuilder``.
        """

        energies = []
        for item in self.energies:
            if isinstance(item, types.RealOrJump):
                energies.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                energies.append(types.RealOrJump(item))
            elif isinstance(item, str):
                energies.append(types.RealOrJump.from_mcnp(item))
        energies = types.Tuple(energies)

        return Ein(
            energies=energies,
        )

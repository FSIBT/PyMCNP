import re
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Sfnu(FmultOption):
    """
    Represents INP sfnu elements.

    Attributes:
        distribution: V bar for or of cumulative distribution the sampling spontaneous fission.
    """

    _ATTRS = {
        'distribution': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Asfnu((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, distribution: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Sfnu``.

        Parameters:
            distribution: V bar for or of cumulative distribution the sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if distribution is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distribution)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                distribution,
            ]
        )

        self.distribution: typing.Final[types.Tuple[types.RealOrJump]] = distribution


@dataclasses.dataclass
class SfnuBuilder:
    """
    Builds ``Sfnu``.

    Attributes:
        distribution: V bar for or of cumulative distribution the sampling spontaneous fission.
    """

    distribution: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``SfnuBuilder`` into ``Sfnu``.

        Returns:
            ``Sfnu`` for ``SfnuBuilder``.
        """

        distribution = []
        for item in self.distribution:
            if isinstance(item, types.RealOrJump):
                distribution.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                distribution.append(types.RealOrJump(item))
            elif isinstance(item, str):
                distribution.append(types.RealOrJump.from_mcnp(item))
        distribution = types.Tuple(distribution)

        return Sfnu(
            distribution=distribution,
        )

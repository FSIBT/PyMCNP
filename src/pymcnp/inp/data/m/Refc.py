import re
import typing
import dataclasses


from ._option import MOption
from ....utils import types
from ....utils import errors


class Refc(MOption, keyword='refc'):
    """
    Represents INP refc elements.

    Attributes:
        coefficents: Cauchy coefficents.
    """

    _ATTRS = {
        'coefficents': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Arefc((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, coefficents: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Refc``.

        Parameters:
            coefficents: Cauchy coefficents.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, coefficents)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                coefficents,
            ]
        )

        self.coefficents: typing.Final[types.Tuple[types.RealOrJump]] = coefficents


@dataclasses.dataclass
class RefcBuilder:
    """
    Builds ``Refc``.

    Attributes:
        coefficents: Cauchy coefficents.
    """

    coefficents: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``RefcBuilder`` into ``Refc``.

        Returns:
            ``Refc`` for ``RefcBuilder``.
        """

        coefficents = []
        for item in self.coefficents:
            if isinstance(item, types.RealOrJump):
                coefficents.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                coefficents.append(types.RealOrJump(item))
            elif isinstance(item, str):
                coefficents.append(types.RealOrJump.from_mcnp(item))
        coefficents = types.Tuple(coefficents)

        return Refc(
            coefficents=coefficents,
        )

import re
import typing
import dataclasses


from ._option import MOption_0
from ....utils import types
from ....utils import errors


class Refs(MOption_0, keyword='refs'):
    """
    Represents INP refs elements.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    _ATTRS = {
        'coefficents': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Arefs((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, coefficents: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Refs``.

        Parameters:
            coefficents: Sellmeier coefficents.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, coefficents)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                coefficents,
            ]
        )

        self.coefficents: typing.Final[types.Tuple[types.RealOrJump]] = coefficents


@dataclasses.dataclass
class RefsBuilder:
    """
    Builds ``Refs``.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    coefficents: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``RefsBuilder`` into ``Refs``.

        Returns:
            ``Refs`` for ``RefsBuilder``.
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

        return Refs(
            coefficents=coefficents,
        )

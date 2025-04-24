import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Thick(MplotOption, keyword='thick'):
    """
    Represents INP thick elements.

    Attributes:
        x: Thickness of plot curves.
    """

    _ATTRS = {
        'x': types.Real,
    }

    _REGEX = re.compile(rf'\Athick( {types.Real._REGEX.pattern})\Z')

    def __init__(self, x: types.Real):
        """
        Initializes ``Thick``.

        Parameters:
            x: Thickness of plot curves.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
            ]
        )

        self.x: typing.Final[types.Real] = x


@dataclasses.dataclass
class ThickBuilder:
    """
    Builds ``Thick``.

    Attributes:
        x: Thickness of plot curves.
    """

    x: str | float | types.Real

    def build(self):
        """
        Builds ``ThickBuilder`` into ``Thick``.

        Returns:
            ``Thick`` for ``ThickBuilder``.
        """

        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        return Thick(
            x=x,
        )

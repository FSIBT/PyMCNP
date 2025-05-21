import re
import copy
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Maxdeflc(BfldOption):
    """
    Represents INP maxdeflc elements.

    Attributes:
        angle: Maximum deflection angles.
    """

    _KEYWORD = 'maxdeflc'

    _ATTRS = {
        'angle': types.Real,
    }

    _REGEX = re.compile(rf'\Amaxdeflc( {types.Real._REGEX.pattern})\Z')

    def __init__(self, angle: types.Real):
        """
        Initializes ``Maxdeflc``.

        Parameters:
            angle: Maximum deflection angles.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if angle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, angle)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                angle,
            ]
        )

        self.angle: typing.Final[types.Real] = angle


@dataclasses.dataclass
class MaxdeflcBuilder:
    """
    Builds ``Maxdeflc``.

    Attributes:
        angle: Maximum deflection angles.
    """

    angle: str | float | types.Real

    def build(self):
        """
        Builds ``MaxdeflcBuilder`` into ``Maxdeflc``.

        Returns:
            ``Maxdeflc`` for ``MaxdeflcBuilder``.
        """

        angle = self.angle
        if isinstance(self.angle, types.Real):
            angle = self.angle
        elif isinstance(self.angle, float) or isinstance(self.angle, int):
            angle = types.Real(self.angle)
        elif isinstance(self.angle, str):
            angle = types.Real.from_mcnp(self.angle)

        return Maxdeflc(
            angle=angle,
        )

    @staticmethod
    def unbuild(ast: Maxdeflc):
        """
        Unbuilds ``Maxdeflc`` into ``MaxdeflcBuilder``

        Returns:
            ``MaxdeflcBuilder`` for ``Maxdeflc``.
        """

        return Maxdeflc(
            angle=copy.deepcopy(ast.angle),
        )

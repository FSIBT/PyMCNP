import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Poa(_option.SsrOption):
    """
    Represents INP poa elements.

    Attributes:
        angle: Angle within which particles accepeted for transport.
    """

    _KEYWORD = 'poa'

    _ATTRS = {
        'angle': types.Real,
    }

    _REGEX = re.compile(rf'\Apoa( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, angle: types.Real):
        """
        Initializes ``Poa``.

        Parameters:
            angle: Angle within which particles accepeted for transport.

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
class PoaBuilder(_option.SsrOptionBuilder):
    """
    Builds ``Poa``.

    Attributes:
        angle: Angle within which particles accepeted for transport.
    """

    angle: str | float | types.Real

    def build(self):
        """
        Builds ``PoaBuilder`` into ``Poa``.

        Returns:
            ``Poa`` for ``PoaBuilder``.
        """

        angle = self.angle
        if isinstance(self.angle, types.Real):
            angle = self.angle
        elif isinstance(self.angle, float) or isinstance(self.angle, int):
            angle = types.Real(self.angle)
        elif isinstance(self.angle, str):
            angle = types.Real.from_mcnp(self.angle)

        return Poa(
            angle=angle,
        )

    @staticmethod
    def unbuild(ast: Poa):
        """
        Unbuilds ``Poa`` into ``PoaBuilder``

        Returns:
            ``PoaBuilder`` for ``Poa``.
        """

        return PoaBuilder(
            angle=copy.deepcopy(ast.angle),
        )

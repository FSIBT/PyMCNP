import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ara(_option.SdefOption):
    """
    Represents INP ara elements.

    Attributes:
        area: Area of surface.
    """

    _KEYWORD = 'ara'

    _ATTRS = {
        'area': types.Real,
    }

    _REGEX = re.compile(rf'\Aara( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, area: types.Real):
        """
        Initializes ``Ara``.

        Parameters:
            area: Area of surface.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if area is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, area)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                area,
            ]
        )

        self.area: typing.Final[types.Real] = area


@dataclasses.dataclass
class AraBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Ara``.

    Attributes:
        area: Area of surface.
    """

    area: str | float | types.Real

    def build(self):
        """
        Builds ``AraBuilder`` into ``Ara``.

        Returns:
            ``Ara`` for ``AraBuilder``.
        """

        area = self.area
        if isinstance(self.area, types.Real):
            area = self.area
        elif isinstance(self.area, float) or isinstance(self.area, int):
            area = types.Real(self.area)
        elif isinstance(self.area, str):
            area = types.Real.from_mcnp(self.area)

        return Ara(
            area=area,
        )

    @staticmethod
    def unbuild(ast: Ara):
        """
        Unbuilds ``Ara`` into ``AraBuilder``

        Returns:
            ``AraBuilder`` for ``Ara``.
        """

        return AraBuilder(
            area=copy.deepcopy(ast.area),
        )

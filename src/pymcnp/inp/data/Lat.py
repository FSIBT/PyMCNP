import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Lat(_option.DataOption):
    """
    Represents INP lat elements.

    Attributes:
        type: Tuple of lattice types.
    """

    _KEYWORD = 'lat'

    _ATTRS = {
        'type': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Alat((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, type: types.Tuple[types.Integer]):
        """
        Initializes ``Lat``.

        Parameters:
            type: Tuple of lattice types.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if type is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, type)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                type,
            ]
        )

        self.type: typing.Final[types.Tuple[types.Integer]] = type


@dataclasses.dataclass
class LatBuilder(_option.DataOptionBuilder):
    """
    Builds ``Lat``.

    Attributes:
        type: Tuple of lattice types.
    """

    type: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``LatBuilder`` into ``Lat``.

        Returns:
            ``Lat`` for ``LatBuilder``.
        """

        if self.type:
            type = []
            for item in self.type:
                if isinstance(item, types.Integer):
                    type.append(item)
                elif isinstance(item, int):
                    type.append(types.Integer(item))
                elif isinstance(item, str):
                    type.append(types.Integer.from_mcnp(item))
            type = types.Tuple(type)
        else:
            type = None

        return Lat(
            type=type,
        )

    @staticmethod
    def unbuild(ast: Lat):
        """
        Unbuilds ``Lat`` into ``LatBuilder``

        Returns:
            ``LatBuilder`` for ``Lat``.
        """

        return LatBuilder(
            type=copy.deepcopy(ast.type),
        )

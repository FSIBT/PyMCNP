import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Lat(_option.CellOption):
    """
    Represents INP lat elements.

    Attributes:
        shape: Cell lattice shape.
    """

    _KEYWORD = 'lat'

    _ATTRS = {
        'shape': types.Integer,
    }

    _REGEX = re.compile(rf'\Alat( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, shape: types.Integer):
        """
        Initializes ``Lat``.

        Parameters:
            shape: Cell lattice shape.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if shape is None or shape not in {1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, shape)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                shape,
            ]
        )

        self.shape: typing.Final[types.Integer] = shape


@dataclasses.dataclass
class LatBuilder(_option.CellOptionBuilder):
    """
    Builds ``Lat``.

    Attributes:
        shape: Cell lattice shape.
    """

    shape: str | int | types.Integer

    def build(self):
        """
        Builds ``LatBuilder`` into ``Lat``.

        Returns:
            ``Lat`` for ``LatBuilder``.
        """

        shape = self.shape
        if isinstance(self.shape, types.Integer):
            shape = self.shape
        elif isinstance(self.shape, int):
            shape = types.Integer(self.shape)
        elif isinstance(self.shape, str):
            shape = types.Integer.from_mcnp(self.shape)

        return Lat(
            shape=shape,
        )

    @staticmethod
    def unbuild(ast: Lat):
        """
        Unbuilds ``Lat`` into ``LatBuilder``

        Returns:
            ``LatBuilder`` for ``Lat``.
        """

        return LatBuilder(
            shape=copy.deepcopy(ast.shape),
        )

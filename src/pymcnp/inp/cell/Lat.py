import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Lat(CellOption_, keyword='lat'):
    """
    Represents INP lat elements.

    Attributes:
        shape: Cell lattice shape.
    """

    _ATTRS = {
        'shape': types.Integer,
    }

    _REGEX = re.compile(rf'\Alat( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, shape: types.Integer):
        """
        Initializes ``Lat``.

        Parameters:
            shape: Cell lattice shape.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if shape is None or shape.value not in {1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, shape)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                shape,
            ]
        )

        self.shape: typing.Final[types.Integer] = shape


@dataclasses.dataclass
class LatBuilder:
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

        if isinstance(self.shape, types.Integer):
            shape = self.shape
        elif isinstance(self.shape, int):
            shape = types.Integer(self.shape)
        elif isinstance(self.shape, str):
            shape = types.Integer.from_mcnp(self.shape)

        return Lat(
            shape=shape,
        )

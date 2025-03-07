import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Geom(FmeshOption_, keyword='geom'):
    """
    Represents INP geom elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(rf'geom( {types.String._REGEX.pattern})')

    def __init__(self, geometry: types.String):
        """
        Initializes ``Geom``.

        Parameters:
            geometry: Mesh geometry.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if geometry is None or geometry not in {'xyz', 'rec', 'rzt', 'cyl'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, geometry)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                geometry,
            ]
        )

        self.geometry: typing.Final[types.String] = geometry

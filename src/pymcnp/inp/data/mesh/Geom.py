import re
import typing


from .option_ import MeshOption_
from ....utils import types
from ....utils import errors


class Geom(MeshOption_, keyword='geom'):
    """
    Represents INP geom elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'geometry': types.String,
    }

    _REGEX = re.compile(rf'\Ageom( {types.String._REGEX.pattern})\Z')

    def __init__(self, geometry: types.String):
        """
        Initializes ``Geom``.

        Parameters:
            geometry: Controls mesh geometry type.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if geometry is None or geometry not in {'xyz', 'rzt', 'rpt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, geometry)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                geometry,
            ]
        )

        self.geometry: typing.Final[types.String] = geometry

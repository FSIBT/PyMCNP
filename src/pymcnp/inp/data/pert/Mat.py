import re
import typing


from .option_ import PertOption_
from ....utils import types
from ....utils import errors


class Mat(PertOption_, keyword='mat'):
    """
    Represents INP mat elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'material': types.Integer,
    }

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, material: types.Integer):
        """
        Initializes ``Mat``.

        Parameters:
            material: Material number to fill cells.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if material is None or not (0 <= material <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, material)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                material,
            ]
        )

        self.material: typing.Final[types.Integer] = material

import re
import typing


from .option_ import DawwgOption_
from ....utils import types
from ....utils import errors


class Xsec(DawwgOption_, keyword='xsec'):
    """
    Represents INP xsec elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'xsec( {types.Integer._REGEX.pattern})')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Xsec``.

        Parameters:
            count: Number of sample points for each direction in each mesh.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count

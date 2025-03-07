import re
import typing


from .option_ import DawwgOption_
from ....utils import types
from ....utils import errors


class Points(DawwgOption_, keyword='points'):
    """
    Represents INP points elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'name': types.String,
    }

    _REGEX = re.compile(rf'points( {types.String._REGEX.pattern})')

    def __init__(self, name: types.String):
        """
        Initializes ``Points``.

        Parameters:
            name: Cross section library.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if name is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, name)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                name,
            ]
        )

        self.name: typing.Final[types.String] = name

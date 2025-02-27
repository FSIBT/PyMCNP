import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Jints(FmeshOption_, keyword='jints'):
    """
    Represents INP jints elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(r'jints( \S+)')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Jints``.

        Parameters:
            count: Number of mesh points y/z for rectangular/cylindrical geometry.

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

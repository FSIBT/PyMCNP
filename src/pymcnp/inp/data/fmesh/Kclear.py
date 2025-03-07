import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Kclear(FmeshOption_, keyword='kclear'):
    """
    Represents INP kclear elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'kclear( {types.Integer._REGEX.pattern})')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Kclear``.

        Parameters:
            count: KCODE cycles between zeros.

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

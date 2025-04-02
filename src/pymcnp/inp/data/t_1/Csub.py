import re
import typing


from .option_ import T_1Option_
from ....utils import types
from ....utils import errors


class Csub(T_1Option_, keyword='csub'):
    """
    Represents INP csub elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Acsub( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Csub``.

        Parameters:
            count: Number of subdivisions to use.

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

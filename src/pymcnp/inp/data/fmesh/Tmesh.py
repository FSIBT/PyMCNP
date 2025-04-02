import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Tmesh(FmeshOption_, keyword='tmesh'):
    """
    Represents INP tmesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Atmesh( {types.Real._REGEX.pattern})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Tmesh``.

        Parameters:
            time: Values of mesh points in time.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time,
            ]
        )

        self.time: typing.Final[types.Real] = time

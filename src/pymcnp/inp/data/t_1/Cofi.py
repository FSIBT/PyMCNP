import re
import typing


from .option_ import T_1Option_
from ....utils import types
from ....utils import errors


class Cofi(T_1Option_, keyword='cofi'):
    """
    Represents INP cofi elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'cofi( {types.Real._REGEX.pattern})')

    def __init__(self, time: types.Real):
        """
        Initializes ``Cofi``.

        Parameters:
            time: Dead time interval.

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

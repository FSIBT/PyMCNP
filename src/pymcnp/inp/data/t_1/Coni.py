import re
import typing


from .option_ import T_1Option_
from ....utils import types
from ....utils import errors


class Coni(T_1Option_, keyword='coni'):
    """
    Represents INP coni elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(r'coni( \S+)')

    def __init__(self, time: types.Real):
        """
        Initializes ``Coni``.

        Parameters:
            time: Alive time interval.

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

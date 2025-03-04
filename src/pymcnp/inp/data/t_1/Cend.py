import re
import typing


from .option_ import T_1Option_
from ....utils import types
from ....utils import errors


class Cend(T_1Option_, keyword='cend'):
    """
    Represents INP cend elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(r'cend( \S+)')

    def __init__(self, time: types.Real):
        """
        Initializes ``Cend``.

        Parameters:
            time: Reference ending time.

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

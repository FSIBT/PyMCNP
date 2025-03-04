import re
import typing


from .option_ import T_1Option_
from ....utils import types
from ....utils import errors


class Cfrq(T_1Option_, keyword='cfrq'):
    """
    Represents INP cfrq elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'frequency': types.Real,
    }

    _REGEX = re.compile(r'cfrq( \S+)')

    def __init__(self, frequency: types.Real):
        """
        Initializes ``Cfrq``.

        Parameters:
            frequency: Frequency of cycling.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if frequency is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, frequency)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                frequency,
            ]
        )

        self.frequency: typing.Final[types.Real] = frequency

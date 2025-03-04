import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Tmp_1(CellOption_, keyword='tmp'):
    """
    Represents INP tmp_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'temperature': tuple[types.Real],
    }

    _REGEX = re.compile(r'tmp( \S+)')

    def __init__(self, temperature: tuple[types.Real]):
        """
        Initializes ``Tmp_1``.

        Parameters:
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if temperature is None or not (min(temperature) > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.temperature: typing.Final[tuple[types.Real]] = temperature

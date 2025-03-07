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
        'temperature': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'tmp(( {types.Real._REGEX.pattern})+)')

    def __init__(self, temperature: types.Tuple[types.Real]):
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

        self.temperature: typing.Final[types.Tuple[types.Real]] = temperature

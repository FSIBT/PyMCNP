import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Tmp_0(CellOption_, keyword='tmp'):
    """
    Represents INP tmp_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'temperature': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'tmp(\d+)(( {types.Real._REGEX.pattern})+)')

    def __init__(self, suffix: types.Integer, temperature: types.Tuple[types.Real]):
        """
        Initializes ``Tmp_0``.

        Parameters:
            suffix: Thermal time index.
            temperature: Temperature at time index.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if temperature is None or not (min(temperature) > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.temperature: typing.Final[types.Tuple[types.Real]] = temperature

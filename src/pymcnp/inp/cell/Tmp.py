import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Tmp(CellOption_, keyword='tmp'):
    """
    Represents INP tmp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'temperature': types.Real,
    }

    _REGEX = re.compile(rf'tmp(\d+)( {types.Real._REGEX.pattern})')

    def __init__(self, suffix: types.Integer, temperature: types.Real):
        """
        Initializes ``Tmp``.

        Parameters:
            suffix: Cell option suffix.
            temperature: Cell temperature at suffix time index.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if temperature is None or not (temperature > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, temperature)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                temperature,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.temperature: typing.Final[types.Real] = temperature

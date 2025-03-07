import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Energy(EmbeeOption_, keyword='energy'):
    """
    Represents INP energy elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'factor': types.Real,
    }

    _REGEX = re.compile(rf'energy( {types.Real._REGEX.pattern})')

    def __init__(self, factor: types.Real):
        """
        Initializes ``Energy``.

        Parameters:
            factor: Multiplicative conversion factor for energy-related output.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.Real] = factor

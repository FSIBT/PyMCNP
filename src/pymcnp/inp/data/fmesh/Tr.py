import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Tr(FmeshOption_, keyword='tr'):
    """
    Represents INP tr elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(r'tr( \S+)')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Tr``.

        Parameters:
            number: Transformation applied to the mesh.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (1 <= number <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number

import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Bflcl(CellOption_, keyword='bflcl'):
    """
    Represents INP bflcl elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(r'bflcl( \S+)')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Bflcl``.

        Parameters:
            number: Cell magnetic field number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (number >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number

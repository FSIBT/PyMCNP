import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Bflcl(DataOption_, keyword='bflcl'):
    """
    Represents INP bflcl elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'bflcl(( \S+)+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Bflcl``.

        Parameters:
            numbers: Tuple of BFLD map numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

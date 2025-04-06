import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Surface(PtracOption_, keyword='surface'):
    """
    Represents INP surface elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'surface(( \S+)+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Surface``.

        Parameters:
            numbers: List of surface numbers for filtering.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

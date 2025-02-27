import re
import typing


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Cell(KpertOption_, keyword='cell'):
    """
    Represents INP cell elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = types.Tuple[types.Integer]

    _REGEX = re.compile(r'cell(( \S+)+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Cell``.

        Parameters:
            numbers: List of cells.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

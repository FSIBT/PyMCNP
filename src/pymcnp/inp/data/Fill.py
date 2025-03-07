import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fill(DataOption_, keyword='fill'):
    """
    Represents INP fill elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'fill(( {types.Integer._REGEX.pattern})+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Fill``.

        Parameters:
            numbers: Tuple of universe numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

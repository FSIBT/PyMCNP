import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Void(DataOption_, keyword='void'):
    """
    Represents INP void elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'void(( \S+)+)?')

    def __init__(self, numbers: types.Tuple[types.Integer] = None):
        """
        Initializes ``Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is not None and not (
            filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

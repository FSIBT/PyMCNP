import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Old(SsrOption_, keyword='old'):
    """
    Represents INP old elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'old(( \S+)+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Old``.

        Parameters:
            numbers: Tuple of surface numbers from subset of surfaces on SSW card.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

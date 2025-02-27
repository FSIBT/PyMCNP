import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Mt(KsenOption_, keyword='mt'):
    """
    Represents INP mt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'mt(( \S+)+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Mt``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

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

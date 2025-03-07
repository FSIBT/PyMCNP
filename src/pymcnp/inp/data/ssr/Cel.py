import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Cel(SsrOption_, keyword='cel'):
    """
    Represents INP cel elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'cel(( {types.Integer._REGEX.pattern})+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Cel``.

        Parameters:
            numbers: Tuple of cell from subset of cells on SSW card.

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

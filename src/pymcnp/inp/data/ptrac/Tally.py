import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Tally(PtracOption_, keyword='tally'):
    """
    Represents INP tally elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'tally(( {types.Integer._REGEX.pattern})+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Tally``.

        Parameters:
            numbers: List of tally numbers for filtering.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (filter(lambda entry: not (entry != 0), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers

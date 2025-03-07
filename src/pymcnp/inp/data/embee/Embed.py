import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Embed(EmbeeOption_, keyword='embed'):
    """
    Represents INP embed elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'embed( {types.Integer._REGEX.pattern})')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Embed``.

        Parameters:
            number: Embedded mesh universe number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number

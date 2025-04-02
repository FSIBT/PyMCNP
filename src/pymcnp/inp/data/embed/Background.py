import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Background(EmbedOption_, keyword='background'):
    """
    Represents INP background elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Abackground( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Background``.

        Parameters:
            number: Background pseudo-cell number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number

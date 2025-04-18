import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Legendre(KsenOption_, keyword='legendre'):
    """
    Represents INP legendre elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'number': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Alegendre( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, number: types.IntegerOrJump):
        """
        Initializes ``Legendre``.

        Parameters:
            number: Order of Legendre moments to calculate sensitivities.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.IntegerOrJump] = number

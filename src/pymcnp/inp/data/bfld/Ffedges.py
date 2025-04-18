import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Ffedges(BfldOption_, keyword='ffedges'):
    """
    Represents INP ffedges elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Affedges((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Ffedges``.

        Parameters:
            numbers: Surface numbers to apply field fringe edges.

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

        self.numbers: typing.Final[types.Tuple[types.RealOrJump]] = numbers

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
        'numbers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'ffedges(( {types.Real._REGEX.pattern})+)')

    def __init__(self, numbers: types.Tuple[types.Real]):
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

        self.numbers: typing.Final[types.Tuple[types.Real]] = numbers

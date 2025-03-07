import re
import typing


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Rxn(KpertOption_, keyword='rxn'):
    """
    Represents INP rxn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'rxn(( {types.Integer._REGEX.pattern})+)')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Rxn``.

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

import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Refc(MOption_, keyword='refc'):
    """
    Represents INP refc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'coefficents': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arefc((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, coefficents: types.Tuple[types.Real]):
        """
        Initializes ``Refc``.

        Parameters:
            coefficents: Cauchy coefficents.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, coefficents)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                coefficents,
            ]
        )

        self.coefficents: typing.Final[types.Tuple[types.Real]] = coefficents

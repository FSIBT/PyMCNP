import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Refs(MOption_, keyword='refs'):
    """
    Represents INP refs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'coefficents': types.Tuple[types.Real],
    }

    _REGEX = re.compile(r'refs(( \S+)+)')

    def __init__(self, coefficents: types.Tuple[types.Real]):
        """
        Initializes ``Refs``.

        Parameters:
            coefficents: Sellmeier coefficents.

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

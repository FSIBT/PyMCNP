import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ksrc(DataOption_, keyword='ksrc'):
    """
    Represents INP ksrc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'locations': types.Tuple[types.LocationEntry],
    }

    _REGEX = re.compile(rf'ksrc(( {types.LocationEntry._REGEX.pattern})+)')

    def __init__(self, locations: types.Tuple[types.LocationEntry]):
        """
        Initializes ``Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, locations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                locations,
            ]
        )

        self.locations: typing.Final[types.Tuple[types.LocationEntry]] = locations

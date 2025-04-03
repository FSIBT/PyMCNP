import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ext(DataOption_, keyword='ext'):
    """
    Represents INP ext elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'stretching': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aext:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, stretching: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Ext``.

        Parameters:
            designator: Data card particle designator.
            stretching: Stretching direction for the cell.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if stretching is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, stretching)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stretching,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.stretching: typing.Final[types.Tuple[types.RealOrJump]] = stretching

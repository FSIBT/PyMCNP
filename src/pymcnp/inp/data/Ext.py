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
        'stretching': types.Tuple[types.Real],
    }

    _REGEX = re.compile(r'ext:(\S+)(( \S+)+)')

    def __init__(self, designator: types.Designator, stretching: types.Tuple[types.Real]):
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
        self.stretching: typing.Final[types.Tuple[types.Real]] = stretching

import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Imp(CellOption_, keyword='imp'):
    """
    Represents INP imp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'importance': types.Real,
    }

    _REGEX = re.compile(rf'\Aimp:(\S+)( {types.Real._REGEX.pattern})\Z')

    def __init__(self, designator: types.Designator, importance: types.Real):
        """
        Initializes ``Imp``.

        Parameters:
            designator: Particle designator.
            importance: Cell particle importance.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if importance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, importance)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                importance,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.importance: typing.Final[types.Real] = importance

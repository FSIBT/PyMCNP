import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Wwn(CellOption_, keyword='wwn'):
    """
    Represents INP wwn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'bound': types.Real,
    }

    _REGEX = re.compile(rf'wwn(\S+):(\S+)( {types.Real._REGEX.pattern})')

    def __init__(self, suffix: types.Integer, designator: types.Designator, bound: types.Real):
        """
        Initializes ``Wwn``.

        Parameters:
            suffix: Cell option suffix.
            designator: Cell particle designator.
            bound: Cell weight-window space, time, or energy lower bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if bound is None or not (bound == -1 or bound >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bound)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bound,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.bound: typing.Final[types.Real] = bound

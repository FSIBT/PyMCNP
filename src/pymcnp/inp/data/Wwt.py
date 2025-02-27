import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwt(DataOption_, keyword='wwt'):
    """
    Represents INP wwt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(r'wwt:(\S+)(( \S+)+)')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.Real]):
        """
        Initializes ``Wwt``.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper time bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds

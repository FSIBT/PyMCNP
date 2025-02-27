import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Elpt(CellOption_, keyword='elpt'):
    """
    Represents INP elpt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'cutoff': types.Real,
    }

    _REGEX = re.compile(r'elpt:(\S+)( \S+)')

    def __init__(self, designator: types.Designator, cutoff: types.Real):
        """
        Initializes ``Elpt``.

        Parameters:
            designator: Cell particle designator.
            cutoff: Cell energy cutoff.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.cutoff: typing.Final[types.Real] = cutoff

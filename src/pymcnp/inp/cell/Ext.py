import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Ext(CellOption_, keyword='ext'):
    """
    Represents INP ext elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'stretch': str,
    }

    _REGEX = re.compile(r'ext:(\S+)( \S+)')

    def __init__(self, designator: types.Designator, stretch: str):
        """
        Initializes ``Ext``.

        Parameters:
            designator: Cell particle designator.
            stretch: Cell exponential transform stretching specifier.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if stretch is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, stretch)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stretch,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.stretch: typing.Final[str] = stretch

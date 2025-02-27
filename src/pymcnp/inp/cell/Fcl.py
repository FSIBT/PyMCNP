import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Fcl(CellOption_, keyword='fcl'):
    """
    Represents INP fcl elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Real,
    }

    _REGEX = re.compile(r'fcl:(\S+)( \S+)')

    def __init__(self, designator: types.Designator, control: types.Real):
        """
        Initializes ``Fcl``.

        Parameters:
            designator: Cell particle designator.
            control: Cell forced-collision control.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if control is None or not (-1 <= control <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, control)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                control,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.control: typing.Final[types.Real] = control

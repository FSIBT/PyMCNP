import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fcl(DataOption_, keyword='fcl'):
    """
    Represents INP fcl elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'control': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Afcl:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, control: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Fcl``.

        Parameters:
            designator: Data card particle designator.
            control: Forced-collision control for cell.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if control is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, control)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                control,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.control: typing.Final[types.Tuple[types.RealOrJump]] = control

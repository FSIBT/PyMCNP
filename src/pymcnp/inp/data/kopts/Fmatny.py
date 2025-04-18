import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatny(KoptsOption_, keyword='fmatny'):
    """
    Represents INP fmatny elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_ny': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatny( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_ny: types.RealOrJump):
        """
        Initializes ``Fmatny``.

        Parameters:
            fmat_ny: fmat_ny.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_ny is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_ny)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_ny,
            ]
        )

        self.fmat_ny: typing.Final[types.RealOrJump] = fmat_ny

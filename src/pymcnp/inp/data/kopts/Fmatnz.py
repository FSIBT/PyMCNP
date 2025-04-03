import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatnz(KoptsOption_, keyword='fmatnz'):
    """
    Represents INP fmatnz elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_nz': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatnz( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_nz: types.RealOrJump):
        """
        Initializes ``Fmatnz``.

        Parameters:
            fmat_nz: fmat_nz.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_nz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_nz)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_nz,
            ]
        )

        self.fmat_nz: typing.Final[types.RealOrJump] = fmat_nz

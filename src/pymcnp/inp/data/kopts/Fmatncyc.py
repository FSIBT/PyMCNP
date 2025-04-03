import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatncyc(KoptsOption_, keyword='fmatncyc'):
    """
    Represents INP fmatncyc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_ncyc': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatncyc( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_ncyc: types.RealOrJump):
        """
        Initializes ``Fmatncyc``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_ncyc is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_ncyc)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_ncyc,
            ]
        )

        self.fmat_ncyc: typing.Final[types.RealOrJump] = fmat_ncyc

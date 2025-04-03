import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatspace(KoptsOption_, keyword='fmatspace'):
    """
    Represents INP fmatspace elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_space': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afmatspace( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fmat_space: types.RealOrJump):
        """
        Initializes ``Fmatspace``.

        Parameters:
            fmat_space: fmat_space.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_space is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_space)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_space,
            ]
        )

        self.fmat_space: typing.Final[types.RealOrJump] = fmat_space

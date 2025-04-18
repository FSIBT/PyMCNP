import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Factor(FmeshOption_, keyword='factor'):
    """
    Represents INP factor elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'multiple': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Afactor( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, multiple: types.RealOrJump):
        """
        Initializes ``Factor``.

        Parameters:
            multiple: Multiplicative factor for each mesh.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if multiple is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multiple)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multiple,
            ]
        )

        self.multiple: typing.Final[types.RealOrJump] = multiple

import re
import typing


from .option_ import FmultOption_
from ....utils import types
from ....utils import errors


class Watt(FmultOption_, keyword='watt'):
    """
    Represents INP watt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'a': types.RealOrJump,
        'b': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Awatt( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, a: types.RealOrJump, b: types.RealOrJump):
        """
        Initializes ``Watt``.

        Parameters:
            a: Watt energy spectrum parameters a.
            b: Watt energy spectrum parameters b.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, b)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                b,
            ]
        )

        self.a: typing.Final[types.RealOrJump] = a
        self.b: typing.Final[types.RealOrJump] = b

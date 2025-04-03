import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Blocksize(KoptsOption_, keyword='blocksize'):
    """
    Represents INP blocksize elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'ncy': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ablocksize( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, ncy: types.IntegerOrJump):
        """
        Initializes ``Blocksize``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ncy is None or not (ncy >= 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ncy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ncy,
            ]
        )

        self.ncy: typing.Final[types.IntegerOrJump] = ncy

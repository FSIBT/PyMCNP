import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Pos(SdefOption_, keyword='pos'):
    """
    Represents INP pos elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vector': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Apos((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Pos``.

        Parameters:
            vector: Reference point for position sampling in vector notation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vector)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vector,
            ]
        )

        self.vector: typing.Final[types.Tuple[types.RealOrJump]] = vector

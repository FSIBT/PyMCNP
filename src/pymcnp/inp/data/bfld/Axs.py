import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Axs(BfldOption_, keyword='axs'):
    """
    Represents INP axs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'vector': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, vector: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Axs``.

        Parameters:
            vector: Direction of the cosines of the quadropole beam axis.

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

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
        'vector': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'pos(( {types.Real._REGEX.pattern})+)')

    def __init__(self, vector: types.Tuple[types.Real]):
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

        self.vector: typing.Final[types.Tuple[types.Real]] = vector

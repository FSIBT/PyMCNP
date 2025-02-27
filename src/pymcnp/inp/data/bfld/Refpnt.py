import re
import typing


from .option_ import BfldOption_
from ....utils import types
from ....utils import errors


class Refpnt(BfldOption_, keyword='refpnt'):
    """
    Represents INP refpnt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'point': types.Tuple[types.Real],
    }

    _REGEX = re.compile(r'refpnt(( \S+)+)')

    def __init__(self, point: types.Tuple[types.Real]):
        """
        Initializes ``Refpnt``.

        Parameters:
            point: Point anywhere on the quadrapole beam.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, point)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                point,
            ]
        )

        self.point: typing.Final[types.Tuple[types.Real]] = point

import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Cos(KsenOption_, keyword='cos'):
    """
    Represents INP cos elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cosines': types.Tuple[types.Real],
    }

    _REGEX = re.compile(r'cos(( \S+)+)')

    def __init__(self, cosines: types.Tuple[types.Real]):
        """
        Initializes ``Cos``.

        Parameters:
            cosines: Range of direction-change cosines.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cosines)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosines,
            ]
        )

        self.cosines: typing.Final[types.Tuple[types.Real]] = cosines

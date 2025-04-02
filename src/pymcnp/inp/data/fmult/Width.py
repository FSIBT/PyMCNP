import re
import typing


from .option_ import FmultOption_
from ....utils import types
from ....utils import errors


class Width(FmultOption_, keyword='width'):
    """
    Represents INP width elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'width': types.Real,
    }

    _REGEX = re.compile(rf'\Awidth( {types.Real._REGEX.pattern})\Z')

    def __init__(self, width: types.Real):
        """
        Initializes ``Width``.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if width is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, width)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                width,
            ]
        )

        self.width: typing.Final[types.Real] = width

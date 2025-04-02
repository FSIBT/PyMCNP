import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Refi(MOption_, keyword='refi'):
    """
    Represents INP refi elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'refractive_index': types.Real,
    }

    _REGEX = re.compile(rf'\Arefi( {types.Real._REGEX.pattern})\Z')

    def __init__(self, refractive_index: types.Real):
        """
        Initializes ``Refi``.

        Parameters:
            refractive_index: Refractive index constant.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if refractive_index is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, refractive_index)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                refractive_index,
            ]
        )

        self.refractive_index: typing.Final[types.Real] = refractive_index

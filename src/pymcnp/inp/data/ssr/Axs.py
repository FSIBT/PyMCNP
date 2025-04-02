import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Axs(SsrOption_, keyword='axs'):
    """
    Represents INP axs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cosines': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, cosines: types.Tuple[types.Real]):
        """
        Initializes ``Axs``.

        Parameters:
            cosines: Direction cosines defining.

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

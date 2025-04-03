import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Tsaepsi(BlockOption_, keyword='tsaepsi'):
    """
    Represents INP tsaepsi elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Atsaepsi( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Tsaepsi``.

        Parameters:
            setting: Convergence criteria for TSA sweeps.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.RealOrJump] = setting

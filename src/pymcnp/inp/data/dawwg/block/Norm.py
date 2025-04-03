import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Norm(BlockOption_, keyword='norm'):
    """
    Represents INP norm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Anorm( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Norm``.

        Parameters:
            setting: Norm.

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

import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Fmmix(BlockOption_, keyword='fmmix'):
    """
    Represents INP fmmix elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'fmmix( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Fmmix``.

        Parameters:
            setting: Read composition from LNK3DNT on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting

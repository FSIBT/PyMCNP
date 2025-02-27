import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Angp(BlockOption_, keyword='angp'):
    """
    Represents INP angp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'angp( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Angp``.

        Parameters:
            setting: Print angular flux on/off.

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

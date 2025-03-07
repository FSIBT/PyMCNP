import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Ibback(BlockOption_, keyword='ibback'):
    """
    Represents INP ibback elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'ibback( {types.Integer._REGEX.pattern})')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ibback``.

        Parameters:
            setting: Back boudary condition.

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

        self.setting: typing.Final[types.Integer] = setting

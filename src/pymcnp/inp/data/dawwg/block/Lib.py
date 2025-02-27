import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Lib(BlockOption_, keyword='lib'):
    """
    Represents INP lib elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'lib( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Lib``.

        Parameters:
            setting: Name of cross-section file.

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

        self.setting: typing.Final[types.String] = setting

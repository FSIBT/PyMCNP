import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Trcor(BlockOption_, keyword='trcor'):
    """
    Represents INP trcor elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'trcor( {types.String._REGEX.pattern})')

    def __init__(self, setting: types.String):
        """
        Initializes ``Trcor``.

        Parameters:
            setting: Trcor.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'diag'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting

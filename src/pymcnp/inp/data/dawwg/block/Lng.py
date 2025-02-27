import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Lng(BlockOption_, keyword='lng'):
    """
    Represents INP lng elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'lng( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Lng``.

        Parameters:
            setting: Number of the last neutron group.

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

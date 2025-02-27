import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Ibt(BlockOption_, keyword='ibt'):
    """
    Represents INP ibt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'ibt( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ibt``.

        Parameters:
            setting: Top boudary condition.

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

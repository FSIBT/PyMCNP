import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Col(SsrOption_, keyword='col'):
    """
    Represents INP col elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'col( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Col``.

        Parameters:
            setting: Collision option setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting

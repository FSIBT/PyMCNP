import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Edoutf(BlockOption_, keyword='edoutf'):
    """
    Represents INP edoutf elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'edoutf( {types.Integer._REGEX.pattern})')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Edoutf``.

        Parameters:
            setting: ASCII output files control.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {-3, -2, -1, 0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting

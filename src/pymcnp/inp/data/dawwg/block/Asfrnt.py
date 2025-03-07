import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Asfrnt(BlockOption_, keyword='asfrnt'):
    """
    Represents INP asfrnt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'asfrnt( {types.Integer._REGEX.pattern})')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Asfrnt``.

        Parameters:
            setting: Back-going flux at plane k.

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

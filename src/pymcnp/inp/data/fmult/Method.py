import re
import typing


from .option_ import FmultOption_
from ....utils import types
from ....utils import errors


class Method(FmultOption_, keyword='method'):
    """
    Represents INP method elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Method``.

        Parameters:
            setting: Gaussian sampling algorithm setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 3, 5, 6, 7}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting

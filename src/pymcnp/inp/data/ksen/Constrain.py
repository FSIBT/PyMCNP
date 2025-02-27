import re
import typing


from .option_ import KsenOption_
from ....utils import types
from ....utils import errors


class Constrain(KsenOption_, keyword='constrain'):
    """
    Represents INP constrain elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'constrain( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Constrain``.

        Parameters:
            setting: Renormalize sensitivity distribution on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting

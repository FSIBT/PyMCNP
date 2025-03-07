import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Tnorm(FmeshOption_, keyword='tnorm'):
    """
    Represents INP tnorm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'tnorm( {types.String._REGEX.pattern})')

    def __init__(self, setting: types.String):
        """
        Initializes ``Tnorm``.

        Parameters:
            setting: Tally results divided by time yes/no.

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

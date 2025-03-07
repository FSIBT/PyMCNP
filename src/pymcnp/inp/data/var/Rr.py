import re
import typing


from .option_ import VarOption_
from ....utils import types
from ....utils import errors


class Rr(VarOption_, keyword='rr'):
    """
    Represents INP rr elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'rr( {types.String._REGEX.pattern})')

    def __init__(self, setting: types.String):
        """
        Initializes ``Rr``.

        Parameters:
            setting: Roulette game for weight windows and cell/energy/time importance off/no.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'no', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting

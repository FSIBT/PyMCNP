import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Cond(MOption_, keyword='cond'):
    """
    Represents INP cond elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Acond( {types.Real._REGEX.pattern})\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``Cond``.

        Parameters:
            setting: Conduction state for EL03 electron-transport evaluation.

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

        self.setting: typing.Final[types.Real] = setting

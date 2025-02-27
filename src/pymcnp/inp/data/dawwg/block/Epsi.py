import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Epsi(BlockOption_, keyword='epsi'):
    """
    Represents INP epsi elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(r'epsi( \S+)')

    def __init__(self, setting: types.Real):
        """
        Initializes ``Epsi``.

        Parameters:
            setting: Convergence precision.

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

import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmat(KoptsOption_, keyword='fmat'):
    """
    Represents INP fmat elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'fmat( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Fmat``.

        Parameters:
            setting: Yes/No FMAT.

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

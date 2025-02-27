import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fc(DataOption_, keyword='fc'):
    """
    Represents INP fc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'info': types.String,
    }

    _REGEX = re.compile(r'fc(\S+)( \S+)')

    def __init__(self, suffix: types.Integer, info: types.String):
        """
        Initializes ``Fc``.

        Parameters:
            suffix: Data card option suffix.
            info: Title for tally in output and MCTAL file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if info is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, info)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                info,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.info: typing.Final[types.String] = info

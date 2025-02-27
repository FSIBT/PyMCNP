import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Unc(DataOption_, keyword='unc'):
    """
    Represents INP unc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'settings': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(r'unc(( \S+)+)')

    def __init__(self, settings: types.Tuple[types.Integer]):
        """
        Initializes ``Unc``.

        Parameters:
            settings: Tuple of uncollided secondary settings.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if settings is None or not (filter(lambda entry: entry.value not in {0, 1}, settings)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.Integer]] = settings

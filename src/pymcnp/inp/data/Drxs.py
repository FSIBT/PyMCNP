import re
import typing


from .option_ import DataOption_
from ...utils import types


class Drxs(DataOption_, keyword='drxs'):
    """
    Represents INP drxs elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(r'drxs(( \S+)+)?')

    def __init__(self, zaids: types.Tuple[types.Zaid] = None):
        """
        Initializes ``Drxs``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids

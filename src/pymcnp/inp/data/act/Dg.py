import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dg(ActOption_, keyword='dg'):
    """
    Represents INP dg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'dg( {types.String._REGEX.pattern})')

    def __init__(self, source: types.String):
        """
        Initializes ``Dg``.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if source is None or source not in {'line', 'mg', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, source)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                source,
            ]
        )

        self.source: typing.Final[types.String] = source

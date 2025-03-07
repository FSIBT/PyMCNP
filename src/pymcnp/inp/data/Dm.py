import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Dm(DataOption_, keyword='dm'):
    """
    Represents INP dm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'dm(( {types.Zaid._REGEX.pattern})+)')

    def __init__(self, zaids: types.Tuple[types.Zaid]):
        """
        Initializes ``Dm``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids

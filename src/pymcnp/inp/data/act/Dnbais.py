import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dnbais(ActOption_, keyword='dnbais'):
    """
    Represents INP dnbais elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Adnbais( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Dnbais``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None or not (0 <= count <= 10):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count

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
        'count': types.Integer,
    }

    _REGEX = re.compile(r'dnbais( \S+)')

    def __init__(self, count: types.Integer):
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

        self.count: typing.Final[types.Integer] = count

import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Talnp(DataOption_, keyword='talnp'):
    """
    Represents INP talnp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'tallies': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Atalnp((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z')

    def __init__(self, tallies: types.Tuple[types.IntegerOrJump] = None):
        """
        Initializes ``Talnp``.

        Parameters:
            tallies: Tallies to exclude from output.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tallies is not None and not (
            filter(lambda entry: not (1 <= entry <= 99_999_999), tallies)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tallies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tallies,
            ]
        )

        self.tallies: typing.Final[types.Tuple[types.IntegerOrJump]] = tallies

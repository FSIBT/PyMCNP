import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Cf(DataOption_, keyword='cf'):
    """
    Represents INP cf elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Acf(\d+)((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, numbers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Cf``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Tallies for problem cell numbers to flag.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if numbers is None or not (filter(lambda entry: not (0 <= entry <= 99_999_999), numbers)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.numbers: typing.Final[types.Tuple[types.IntegerOrJump]] = numbers

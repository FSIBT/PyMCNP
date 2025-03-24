import re
import typing


from .option_ import StopOption_
from ....utils import types
from ....utils import errors


class Fk(StopOption_, keyword='fk'):
    """
    Represents INP fk elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'e': types.Integer,
        'suffix': types.Integer,
    }

    _REGEX = re.compile(rf'fk(\d+)( {types.Integer._REGEX.pattern})')

    def __init__(self, e: types.Integer, suffix: types.Integer):
        """
        Initializes ``Fk``.

        Parameters:
            e: Tally fluctuation relative error before stop.
            suffix: Data card option option suffix.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if e is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, e)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                e,
            ]
        )

        self.e: typing.Final[types.Integer] = e
        self.suffix: typing.Final[types.Integer] = suffix

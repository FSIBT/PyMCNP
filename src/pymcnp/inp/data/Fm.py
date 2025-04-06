import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fm(DataOption_, keyword='fm'):
    """
    Represents INP fm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bins': types.String,
    }

    _REGEX = re.compile(rf'\Afm(\d+)( [\S\s]+)\Z')

    def __init__(self, suffix: types.Integer, bins: types.String):
        """
        Initializes ``Fm``.

        Parameters:
            suffix: Data card option suffix.
            bins: Tally multiplier bins.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if bins is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bins)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bins,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bins: typing.Final[types.String] = bins

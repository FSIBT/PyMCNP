import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ft(DataOption_, keyword='ft'):
    """
    Represents INP ft elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'treatments': types.String,
    }

    _REGEX = re.compile(rf'\Aft(\d+)( {types.String._REGEX.pattern})\Z')

    def __init__(self, suffix: types.Integer, treatments: types.String):
        """
        Initializes ``Ft``.

        Parameters:
            suffix: Data card option suffix.
            treatments: Tally special treatments.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if treatments is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, treatments)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                treatments,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.treatments: typing.Final[types.String] = treatments

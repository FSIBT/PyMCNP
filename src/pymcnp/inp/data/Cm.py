import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Cm(DataOption_, keyword='cm'):
    """
    Represents INP cm elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'multipliers': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'cm(\S+)(( {types.Real._REGEX.pattern})+)')

    def __init__(self, suffix: types.Integer, multipliers: types.Tuple[types.Real]):
        """
        Initializes ``Cm``.

        Parameters:
            suffix: Data card option suffix.
            multipliers: Cosine bin multiplier to apply.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if multipliers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multipliers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multipliers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.multipliers: typing.Final[types.Tuple[types.Real]] = multipliers

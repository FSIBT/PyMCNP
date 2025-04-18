import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ds_1(DataOption_, keyword='ds'):
    """
    Represents INP ds_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'ijs': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) t((?: {types.IndependentDependent._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, ijs: types.Tuple[types.IndependentDependent]):
        """
        Initializes ``Ds_1``.

        Parameters:
            suffix: Data card option suffix.
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if ijs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ijs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ijs,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.ijs: typing.Final[types.Tuple[types.IndependentDependent]] = ijs

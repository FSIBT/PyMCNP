import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Ds_2(DataOption_, keyword='ds'):
    """
    Represents INP ds_2 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'vss': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+)((?: {types.IndependentDependent._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, vss: types.Tuple[types.IndependentDependent]):
        """
        Initializes ``Ds_2``.

        Parameters:
            suffix: Data card option suffix.
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if vss is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vss)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vss,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.vss: typing.Final[types.Tuple[types.IndependentDependent]] = vss

import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Pd(DataOption_, keyword='pd'):
    """
    Represents INP pd elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probabilities': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Apd(\d+):(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        probabilities: types.Tuple[types.RealOrJump],
    ):
        """
        Initializes ``Pd``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            probabilities: Probability of contribution to DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probabilities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probabilities,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.probabilities: typing.Final[types.Tuple[types.RealOrJump]] = probabilities

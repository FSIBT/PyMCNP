import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sp_0(DataOption_, keyword='sp'):
    """
    Represents INP sp_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'probabilities': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Asp(\d+)( [dcvw])?((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        probabilities: types.Tuple[types.RealOrJump],
        option: types.String = None,
    ):
        """
        Initializes ``Sp_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Probability kind setting.
            probabilities: Particle source probabilities.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if probabilities is None or not (
            filter(lambda entry: not (0 <= entry <= 1), probabilities)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probabilities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                probabilities,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.probabilities: typing.Final[types.Tuple[types.RealOrJump]] = probabilities

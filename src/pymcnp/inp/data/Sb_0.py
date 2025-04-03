import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Sb_0(DataOption_, keyword='sb'):
    """
    Represents INP sb_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'option': types.String,
        'biases': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Asb(\d+)( [dcvw])?((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        biases: types.Tuple[types.RealOrJump],
        option: types.String = None,
    ):
        """
        Initializes ``Sb_0``.

        Parameters:
            suffix: Data card option suffix.
            option: Bias kind setting.
            biases: Particle source biases.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if option is not None and option not in {'d', 'c', 'v', 'w'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, option)
        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                option,
                biases,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.option: typing.Final[types.String] = option
        self.biases: typing.Final[types.Tuple[types.RealOrJump]] = biases

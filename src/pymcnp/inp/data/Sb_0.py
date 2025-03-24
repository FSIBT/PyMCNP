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
        'biases': types.Tuple[types.Real],
    }

    _REGEX = re.compile(
        rf'sb(\d+)( {types.String._REGEX.pattern})(( {types.Real._REGEX.pattern})+)'
    )

    def __init__(
        self, suffix: types.Integer, option: types.String, biases: types.Tuple[types.Real]
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
        if option is None or option not in {'d', 'c', 'v', 'w'}:
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
        self.biases: typing.Final[types.Tuple[types.Real]] = biases

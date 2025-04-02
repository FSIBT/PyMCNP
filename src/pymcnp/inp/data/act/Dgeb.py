import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dgeb(ActOption_, keyword='dgeb'):
    """
    Represents INP dgeb elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'biases': types.Tuple[types.Bias],
    }

    _REGEX = re.compile(rf'\Adgeb((?: {types.Bias._REGEX.pattern})+?)\Z')

    def __init__(self, biases: types.Tuple[types.Bias]):
        """
        Initializes ``Dgeb``.

        Parameters:
            biases: Delayed neutron energy biases.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if biases is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, biases)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                biases,
            ]
        )

        self.biases: typing.Final[types.Tuple[types.Bias]] = biases

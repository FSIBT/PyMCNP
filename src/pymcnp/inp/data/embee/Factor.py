import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Factor(EmbeeOption_, keyword='factor'):
    """
    Represents INP factor elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(rf'factor( {types.Real._REGEX.pattern})')

    def __init__(self, constant: types.Real):
        """
        Initializes ``Factor``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.Real] = constant

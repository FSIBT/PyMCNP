import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Wgt(SsrOption_, keyword='wgt'):
    """
    Represents INP wgt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(r'wgt( \S+)')

    def __init__(self, constant: types.Real):
        """
        Initializes ``Wgt``.

        Parameters:
            constant: Particle weight multiplier.

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

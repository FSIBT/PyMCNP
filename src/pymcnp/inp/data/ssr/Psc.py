import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Psc(SsrOption_, keyword='psc'):
    """
    Represents INP psc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(r'psc( \S+)')

    def __init__(self, constant: types.Real):
        """
        Initializes ``Psc``.

        Parameters:
            constant: Constant for approximation in PSC evaluation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if constant is None or not (constant >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.Real] = constant

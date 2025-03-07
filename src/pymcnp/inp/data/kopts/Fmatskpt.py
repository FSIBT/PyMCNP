import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatskpt(KoptsOption_, keyword='fmatskpt'):
    """
    Represents INP fmatskpt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_skip': types.Real,
    }

    _REGEX = re.compile(rf'fmatskpt( {types.Real._REGEX.pattern})')

    def __init__(self, fmat_skip: types.Real):
        """
        Initializes ``Fmatskpt``.

        Parameters:
            fmat_skip: fmat_skip.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_skip is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_skip)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_skip,
            ]
        )

        self.fmat_skip: typing.Final[types.Real] = fmat_skip

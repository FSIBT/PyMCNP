import re
import typing


from .option_ import KoptsOption_
from ....utils import types
from ....utils import errors


class Fmatspace(KoptsOption_, keyword='fmatspace'):
    """
    Represents INP fmatspace elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fmat_space': types.Real,
    }

    _REGEX = re.compile(rf'fmatspace( {types.Real._REGEX.pattern})')

    def __init__(self, fmat_space: types.Real):
        """
        Initializes ``Fmatspace``.

        Parameters:
            fmat_space: fmat_space.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_space is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_space)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fmat_space,
            ]
        )

        self.fmat_space: typing.Final[types.Real] = fmat_space

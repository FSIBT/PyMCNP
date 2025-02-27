import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Factor(FmeshOption_, keyword='factor'):
    """
    Represents INP factor elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'multiple': types.Real,
    }

    _REGEX = re.compile(r'factor( \S+)')

    def __init__(self, multiple: types.Real):
        """
        Initializes ``Factor``.

        Parameters:
            multiple: Multiplicative factor for each mesh.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if multiple is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multiple)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multiple,
            ]
        )

        self.multiple: typing.Final[types.Real] = multiple

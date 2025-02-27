import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Emesh(FmeshOption_, keyword='emesh'):
    """
    Represents INP emesh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'energy': types.Real,
    }

    _REGEX = re.compile(r'emesh( \S+)')

    def __init__(self, energy: types.Real):
        """
        Initializes ``Emesh``.

        Parameters:
            energy: Values of mesh points in energy.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energy,
            ]
        )

        self.energy: typing.Final[types.Real] = energy

import re
import typing


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Rho(KpertOption_, keyword='rho'):
    """
    Represents INP rho elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'densities': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(r'rho(( \S+)+)')

    def __init__(self, densities: types.Tuple[types.Zaid]):
        """
        Initializes ``Rho``.

        Parameters:
            densities: List of densities.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if densities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, densities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                densities,
            ]
        )

        self.densities: typing.Final[types.Tuple[types.Zaid]] = densities

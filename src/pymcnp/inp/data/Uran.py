import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Uran(DataOption_, keyword='uran'):
    """
    Represents INP uran elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'transformations': types.Tuple[types.Stochastic],
    }

    _REGEX = re.compile(rf'uran(( {types.Stochastic._REGEX.pattern})+)')

    def __init__(self, transformations: types.Tuple[types.Stochastic]):
        """
        Initializes ``Uran``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if transformations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, transformations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                transformations,
            ]
        )

        self.transformations: typing.Final[types.Tuple[types.Stochastic]] = transformations

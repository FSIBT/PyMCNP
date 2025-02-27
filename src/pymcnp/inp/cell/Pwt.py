import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Pwt(CellOption_, keyword='pwt'):
    """
    Represents INP pwt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(r'pwt( \S+)')

    def __init__(self, weight: types.Real):
        """
        Initializes ``Pwt``.

        Parameters:
            weight: Cell weight of photons produced at neutron collisions.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, weight)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                weight,
            ]
        )

        self.weight: typing.Final[types.Real] = weight

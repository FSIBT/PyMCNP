import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Wgt(SdefOption_, keyword='wgt'):
    """
    Represents INP wgt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'weight': types.Real,
    }

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern})\Z')

    def __init__(self, weight: types.Real):
        """
        Initializes ``Wgt``.

        Parameters:
            weight: Particle weight.

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

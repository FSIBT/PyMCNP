import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Dir_1(SdefOption_, keyword='dir'):
    """
    Represents INP dir elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cosine': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Adir( {types.DistributionNumber._REGEX.pattern})\Z')

    def __init__(self, cosine: types.DistributionNumber):
        """
        Initializes ``Dir_1``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cosine is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cosine)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosine,
            ]
        )

        self.cosine: typing.Final[types.DistributionNumber] = cosine

import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Pd(CellOption_, keyword='pd'):
    """
    Represents INP pd elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'probability': types.Real,
    }

    _REGEX = re.compile(rf'pd(\d+)( {types.Real._REGEX.pattern})')

    def __init__(self, suffix: types.Integer, probability: types.Real):
        """
        Initializes ``Pd``.

        Parameters:
            suffix: Cell option suffix.
            probability: Cell probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if probability is None or not (0 <= probability <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probability)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probability,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.probability: typing.Final[types.Real] = probability

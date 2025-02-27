import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Dxc(CellOption_, keyword='dxc'):
    """
    Represents INP dxc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probability': types.Real,
    }

    _REGEX = re.compile(r'dxc(\S+):(\S+)( \S+)')

    def __init__(
        self, suffix: types.Integer, designator: types.Designator, probability: types.Real
    ):
        """
        Initializes ``Dxc``.

        Parameters:
            suffix: Cell option suffix.
            designator: Cell particle designator.
            probability: Cell probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if probability is None or not (0 <= probability <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, probability)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probability,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.probability: typing.Final[types.Real] = probability

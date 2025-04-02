import re
import typing


from .option_ import SswOption_
from ....utils import types
from ....utils import errors


class Cel(SswOption_, keyword='cel'):
    """
    Represents INP cel elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cfs': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Acel((?: {types.Integer._REGEX.pattern})+?)\Z')

    def __init__(self, cfs: types.Tuple[types.Integer]):
        """
        Initializes ``Cel``.

        Parameters:
            cfs: Cells from which KCODE neutrons are written.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cfs is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), cfs)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cfs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cfs,
            ]
        )

        self.cfs: typing.Final[types.Tuple[types.Integer]] = cfs

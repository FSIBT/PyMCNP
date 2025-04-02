import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Value(PtracOption_, keyword='value'):
    """
    Represents INP value elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'cutoff': types.Real,
    }

    _REGEX = re.compile(rf'\Avalue( {types.Real._REGEX.pattern})\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``Value``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cutoff,
            ]
        )

        self.cutoff: typing.Final[types.Real] = cutoff

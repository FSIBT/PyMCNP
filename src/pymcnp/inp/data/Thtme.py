import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Thtme(DataOption_, keyword='thtme'):
    """
    Represents INP thtme elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'times': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Athtme((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, times: types.Tuple[types.Real]):
        """
        Initializes ``Thtme``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if times is None or not (filter(lambda entry: not (entry <= 99), times)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, times)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                times,
            ]
        )

        self.times: typing.Final[types.Tuple[types.Real]] = times

import re
import typing


from . import ptrac
from .option_ import DataOption_
from ...utils import types


class Ptrac(DataOption_, keyword='ptrac'):
    """
    Represents INP ptrac elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[ptrac.PtracOption_],
    }

    _REGEX = re.compile(rf'ptrac(( ({ptrac.PtracOption_._REGEX.pattern}))+)?')

    def __init__(self, options: types.Tuple[ptrac.PtracOption_] = None):
        """
        Initializes ``Ptrac``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[ptrac.PtracOption_]] = options

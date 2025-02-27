import re
import typing


from . import sdef
from .option_ import DataOption_
from ...utils import types


class Sdef(DataOption_, keyword='sdef'):
    """
    Represents INP sdef elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[sdef.SdefOption_],
    }

    _REGEX = re.compile(rf'sdef(( ({sdef.SdefOption_._REGEX.pattern}))+)?')

    def __init__(self, options: types.Tuple[sdef.SdefOption_] = None):
        """
        Initializes ``Sdef``.

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

        self.options: typing.Final[types.Tuple[sdef.SdefOption_]] = options

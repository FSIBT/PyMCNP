import re
import typing


from . import dawwg
from .option_ import DataOption_
from ...utils import types


class Dawwg(DataOption_, keyword='dawwg'):
    """
    Represents INP dawwg elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[dawwg.DawwgOption_],
    }

    _REGEX = re.compile(rf'\Adawwg((?: (?:{dawwg.DawwgOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[dawwg.DawwgOption_] = None):
        """
        Initializes ``Dawwg``.

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

        self.options: typing.Final[types.Tuple[dawwg.DawwgOption_]] = options

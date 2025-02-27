import re
import typing


from . import ssr
from .option_ import DataOption_
from ...utils import types


class Ssr(DataOption_, keyword='ssr'):
    """
    Represents INP ssr elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[ssr.SsrOption_],
    }

    _REGEX = re.compile(rf'ssr(( ({ssr.SsrOption_._REGEX.pattern}))+)?')

    def __init__(self, options: types.Tuple[ssr.SsrOption_] = None):
        """
        Initializes ``Ssr``.

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

        self.options: typing.Final[types.Tuple[ssr.SsrOption_]] = options

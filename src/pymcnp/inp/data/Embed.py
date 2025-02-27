import re
import typing


from . import embed
from .option_ import DataOption_
from ...utils import types


class Embed(DataOption_, keyword='embed'):
    """
    Represents INP embed elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'options': types.Tuple[embed.EmbedOption_],
    }

    _REGEX = re.compile(rf'embed(( ({embed.EmbedOption_._REGEX.pattern}))+)?')

    def __init__(self, options: types.Tuple[embed.EmbedOption_] = None):
        """
        Initializes ``Embed``.

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

        self.options: typing.Final[types.Tuple[embed.EmbedOption_]] = options

import re
import typing

from . import data
from .card_ import Card_
from ..utils import errors
from ..utils import _parser


class Data(Card_):
    """
    Represents INP data elements.

    Attributes:
        InpError: SEMANTICS_CARD_VALUE.
    """

    _ATTRS = {'option': data.DataOption_}

    _REGEX = re.compile(rf'( {data.DataOption_._REGEX.pattern})')

    def __init__(self, option: data.DataOption_):
        """
        Initializes ``Data``.

        Parameters:
            option: data option.

        Raises:
            InpError: SEMANTICS_CARD_VALUE.
        """

        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, option)

        self.option: typing.Final[data.DataOption_] = option

    def to_mcnp(self):
        """
        Generates INP from ``Data``.

        Returns:
            INP data card.
        """

        return _parser.postprocess_continuation_line(str(self.option))

import re
import typing

from . import surface
from .card_ import Card_
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Surface(Card_):
    """
    Represents INP surface cards.

    Attributes:
        number: INP surface number.
        transform: INP surface transformation.
        option: INP surface option.
        prefix: INP surface kind setting.
    """

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'option': surface.SurfaceOption_,
    }

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)?( ({surface.SurfaceOption_._REGEX.pattern}))\Z')

    def __init__(
        self,
        number: types.Integer,
        option: surface.SurfaceOption_,
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes ``Surface``.

        Parameters:
            number: INP surface number.
            transform: INP surface transformation.
            option: INP surface option.
            prefix: INP surface kind setting.

        Returns:
            ``Surface``.

        Raises:
            InpError: SEMANTICS_CARD_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999 if not transform else 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, number)
        if transform is not None and not (0 <= transform <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, transform)
        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, option)
        if prefix is not None and prefix not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, prefix)

        self.number: typing.Final[types.Integer] = number
        self.transform: typing.Final[types.Integer] = transform
        self.option: typing.Final[surface.SurfaceOption_] = option
        self.prefix: typing.Final[str] = prefix

    def to_mcnp(self):
        """
        Generates INP from ``Surface``.

        Returns:
            INP surface card.
        """

        return _parser.postprocess_continuation_line(
            f'{self.prefix or ""}{self.number} {self.transform or ""} {self.option}'
        )

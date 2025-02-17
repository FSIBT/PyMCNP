import re
import typing

from . import surface
from . import _card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Surface(_card.InpCard_):
    """
    Represents INP surface cards.

    Attributes:
        number:    INP surface number.
        transform: INP surface transformation.
        option:    INP surface option.
    """

    _REGEX = re.compile(
        r'\A(\+|\*)?(\S+)( \S+)? (((p)( \S+)( \S+)( \S+)( \S+))|((p)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((px)( \S+))|((py)( \S+))|((pz)( \S+))|((so)( \S+))|((s)( \S+)( \S+)( \S+)( \S+))|((sx)( \S+)( \S+))|((sy)( \S+)( \S+))|((sz)( \S+)( \S+))|((c/x)( \S+)( \S+)( \S+))|((c/y)( \S+)( \S+)( \S+))|((c/z)( \S+)( \S+)( \S+))|((cx)( \S+))|((cy)( \S+))|((cz)( \S+))|((k/x)( \S+)( \S+)( \S+)( \S+)( \S+))|((k/y)( \S+)( \S+)( \S+)( \S+)( \S+))|((k/z)( \S+)( \S+)( \S+)( \S+)( \S+))|((kx)( \S+)( \S+)( \S+))|((ky)( \S+)( \S+)( \S+))|((kz)( \S+)( \S+)( \S+))|((sq)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((gq)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((tx)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((ty)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((tz)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((x)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((y)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((z)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((box)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((rpp)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((sph)( \S+)( \S+)( \S+)( \S+))|((rcc)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((rhp)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((rec)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((trc)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((ell)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((wed)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+))|((arb)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)))\Z'
    )

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
            number:    INP surface number.
            transform: INP surface transformation.
            option:    INP surface option.
            prefix:    INP surface kind setting.

        Returns:
            ``Surface``.

        Raises:
            McnpError: SEMANTICS_SURFACE_NUMBER.
            McnpError: SEMANTICS_SURFACE_TRANSFORM.
            McnpError: SEMANTICS_SURFACE_OPTION.
            McnpError: SEMANTICS_SURFACE_PREFIX.
        """

        if number is None or not (1 <= number <= 99_999_999 if not transform else 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_NUMBER, number)

        if transform is not None and not (0 <= transform <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_TRANSFORM, transform)

        if option is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_OPTION, option)

        if prefix is not None and prefix not in {'*', '+'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_SURFACE_PREFIX, prefix)

        self.number: typing.Final[types.Integer] = number
        self.transform: typing.Final[types.Integer] = transform
        self.option: typing.Final[surface.SurfaceOption_] = option
        self.prefix: typing.Final[str] = prefix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Surface`` from INP.

        Parameters:
            source: INP surface card.

        Returns:
            ``Surface``.

        Raises:
            McnpError: SYNTAX_SURFACE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Surface._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SURFACE, source)

        prefix = types.String.from_mcnp(tokens[1]) if tokens[1] else None
        number = types.Integer.from_mcnp(tokens[2])
        transform = types.Integer.from_mcnp(tokens[3]) if tokens[3] else None
        option = next(_parser.process_inp_option(surface.SurfaceOption_, tokens[4]))

        s = Surface(number, option, transform=transform, prefix=prefix)
        s.comments = comments

        return s

    def to_mcnp(self):
        """
        Generates INP from ``Surface``.

        Returns:
            INP surface card.
        """

        return _parser.postprocess_continuation_line(
            f'{self.prefix or ""}{self.number} {self.transform or ""} {self.option}'
        )

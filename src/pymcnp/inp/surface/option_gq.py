import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class SurfaceOption_Gq(_option.SurfaceOption_, keyword='gq'):
    """
    Represents INP surface card gq options.

    Attributes:
        a: Oblique special quadratic A coefficent.
        b: Oblique special quadratic B coefficent.
        c: Oblique special quadratic C coefficent.
        d: Oblique special quadratic D coefficent.
        e: Oblique special quadratic E coefficent.
        f: Oblique special quadratic F coefficent.
        g: Oblique special quadratic G coefficent.
        h: Oblique special quadratic H coefficent.
        j: Oblique special quadratic J coefficent.
        k: Oblique special quadratic K coefficent.
    """

    _REGEX = re.compile(r'\Agq( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        a: types.Real,
        b: types.Real,
        c: types.Real,
        d: types.Real,
        e: types.Real,
        f: types.Real,
        g: types.Real,
        h: types.Real,
        j: types.Real,
        k: types.Real,
    ):
        """
        Initializes ``SurfaceOption_Gq``.

        Parameters:
            a: Oblique special quadratic A coefficent.
            b: Oblique special quadratic B coefficent.
            c: Oblique special quadratic C coefficent.
            d: Oblique special quadratic D coefficent.
            e: Oblique special quadratic E coefficent.
            f: Oblique special quadratic F coefficent.
            g: Oblique special quadratic G coefficent.
            h: Oblique special quadratic H coefficent.
            j: Oblique special quadratic J coefficent.
            k: Oblique special quadratic K coefficent.

        Returns:
            ``SurfaceOption_Gq``.

        Raises:
            InpError: SYNTAX_OPTION_VALUE.
        """

        if a is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, a)
        if b is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, b)
        if c is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, c)
        if d is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, d)
        if e is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, e)
        if f is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, f)
        if g is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, g)
        if h is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, h)
        if j is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, j)
        if k is None:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION_VALUE, k)

        self.value: typing.Final[tuple[any]] = types._Tuple([a, b, c, d, e, f, g, h, j, k])
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b
        self.c: typing.Final[types.Real] = c
        self.d: typing.Final[types.Real] = d
        self.e: typing.Final[types.Real] = e
        self.f: typing.Final[types.Real] = f
        self.g: typing.Final[types.Real] = g
        self.h: typing.Final[types.Real] = h
        self.j: typing.Final[types.Real] = j
        self.k: typing.Final[types.Real] = k

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SurfaceOption_Gq`` from INP.

        Parameters:
            source: INP surface card option.

        Returns:
            ``SurfaceOption_Gq``.

        Raises:
            InpError: SYNTAX_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SurfaceOption_Gq._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        a = types.Real.from_mcnp(tokens[1])
        b = types.Real.from_mcnp(tokens[2])
        c = types.Real.from_mcnp(tokens[3])
        d = types.Real.from_mcnp(tokens[4])
        e = types.Real.from_mcnp(tokens[5])
        f = types.Real.from_mcnp(tokens[6])
        g = types.Real.from_mcnp(tokens[7])
        h = types.Real.from_mcnp(tokens[8])
        j = types.Real.from_mcnp(tokens[9])
        k = types.Real.from_mcnp(tokens[10])

        return SurfaceOption_Gq(a, b, c, d, e, f, g, h, j, k)

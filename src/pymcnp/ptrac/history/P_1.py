import re
import typing

from . import _line
from ...utils import types
from ...utils import errors
from ...utils import _parser


class P_1(_line.HistoryLine):
    """
    Represents PTRAC history block p lines form #2.

    Attributes:
        x: X coordinate of the particle position.
        y: Y coordinate of the particle position.
        z: Z coordinate of the particle position.
        u: Particle direction cosine with x axis.
        v: Particle direction cosine with y axis.
        w: Particle direction cosine with z axis.
        erg: Particle energy.
        wgt: Particle weight.
        tme: Time at the particles position.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        x: types.Integer,
        y: types.Integer,
        z: types.Integer,
        u: types.Integer,
        v: types.Integer,
        w: types.Integer,
        erg: types.Integer,
        wgt: types.Integer,
        tme: types.Integer,
    ):
        """
        Initializes ``P_1``.

        Parameters:
            x: X coordinate of the particle position.
            y: Y coordinate of the particle position.
            z: Z coordinate of the particle position.
            u: Particle direction cosine with x axis.
            v: Particle direction cosine with y axis.
            w: Particle direction cosine with z axis.
            erg: Particle energy.
            wgt: Particle weight.
            tme: Time at the particles position.

        Raises:
            InpError: SEMANTICS_LINE.
        """

        if x is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, x)

        if y is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, y)

        if z is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, z)

        if u is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, u)

        if v is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, v)

        if w is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, w)

        if erg is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, erg)

        if wgt is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, wgt)

        if tme is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, tme)

        self.x: typing.Final[types.Integer] = x
        self.y: typing.Final[types.Integer] = y
        self.z: typing.Final[types.Integer] = z
        self.u: typing.Final[types.Integer] = u
        self.v: typing.Final[types.Integer] = v
        self.w: typing.Final[types.Integer] = w
        self.erg: typing.Final[types.Integer] = erg
        self.wgt: typing.Final[types.Integer] = wgt
        self.tme: typing.Final[types.Integer] = tme

    def from_mcnp(source: str):
        """
        Generates ``P_1`` from PTRAC.

        Parameters:
            source: PTRAC for ``P_1``.

        Returns:
            ``P_1``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = P_1._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        x = types.Integer.from_mcnp(tokens[1])
        y = types.Integer.from_mcnp(tokens[2])
        z = types.Integer.from_mcnp(tokens[3])
        u = types.Integer.from_mcnp(tokens[4])
        v = types.Integer.from_mcnp(tokens[5])
        w = types.Integer.from_mcnp(tokens[6])
        erg = types.Integer.from_mcnp(tokens[7])
        wgt = types.Integer.from_mcnp(tokens[8])
        tme = types.Integer.from_mcnp(tokens[9])

        return P_1(
            x,
            y,
            z,
            u,
            v,
            w,
            erg,
            wgt,
            tme,
        )

import re
import typing

from . import _line
from .... import types
from .... import errors


class P_1(_line.EventLine):
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

    _REGEX = re.compile(r'\A\s(.{13})(.{13})(.{13})(.{13})(.{13})(.{13})(.{13})(.{13})(.{13})\Z', re.IGNORECASE)

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        u: types.Real,
        v: types.Real,
        w: types.Real,
        erg: types.Real,
        wgt: types.Real,
        tme: types.Real,
    ):
        """
        Initializes `P_1`.

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
            PtracError: SEMANTICS_LINE.
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

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.u: typing.Final[types.Real] = u
        self.v: typing.Final[types.Real] = v
        self.w: typing.Final[types.Real] = w
        self.erg: typing.Final[types.Real] = erg
        self.wgt: typing.Final[types.Real] = wgt
        self.tme: typing.Final[types.Real] = tme

    def from_mcnp(source: str):
        """
        Generates `P_1` from PTRAC.

        Parameters:
            source: PTRAC for `P_1`.

        Returns:
            `P_1`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = P_1._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])
        u = types.Real.from_mcnp(tokens[4])
        v = types.Real.from_mcnp(tokens[5])
        w = types.Real.from_mcnp(tokens[6])
        erg = types.Real.from_mcnp(tokens[7])
        wgt = types.Real.from_mcnp(tokens[8])
        tme = types.Real.from_mcnp(tokens[9])

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

    def to_mcnp(self):
        """
        Generates PTRAC from `P_1`.

        Returns:
            PTRAC for `P_1`.
        """

        x = f'{self.x:5.1a}'
        y = f'{self.y:5.1a}'
        z = f'{self.z:5.1a}'
        u = f'{self.u:5.1a}'
        v = f'{self.v:5.1a}'
        w = f'{self.w:5.1a}'
        erg = f'{self.erg:5.1a}'
        wgt = f'{self.wgt:5.1a}'
        tme = f'{self.tme:5.1a}'

        return f'  {x} {y} {z} {u} {v} {w} {erg} {wgt} {tme}'

import re

from . import _line
from .... import types
from .... import errors
from .... import _fields


class P_1(_fields.Fields, _line.EventLine):
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

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    x = _fields.Field(types.Real, 'X coordinate of the particle position')
    y = _fields.Field(types.Real, 'Y coordinate of the particle position')
    z = _fields.Field(types.Real, 'Z coordinate of the particle position')
    u = _fields.Field(types.Real, 'Particle direction cosine with x axis')
    v = _fields.Field(types.Real, 'Particle direction cosine with y axis')
    w = _fields.Field(types.Real, 'Particle direction cosine with z axis')
    erg = _fields.Field(types.Real, 'Particle energy')
    wgt = _fields.Field(types.Real, 'Particle weight')
    tme = _fields.Field(types.Real, 'Time at the particles position')

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

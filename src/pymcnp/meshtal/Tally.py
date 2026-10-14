import re

from . import _line
from .. import types
from .. import errors
from .. import _fields


class Tally(_fields.Fields, _line.Line):
    """
    Represents MESHTAL tally line.

    Attributes:
        x: Tally x direction.
        y: Tally y direction.
        z: Tally z direction.
        energy: Tally energy.
        time: Tally time.
        result: Tally result.
        error: Tally relative error.
    """

    _REGEX = re.compile(r'\A  ([^\n]{9})?([^\n]{11})?([^\n]{9})?([^\n]{10})?([^\n]{10})?([^\n]{12})([^\n]{12})\n?\Z', re.IGNORECASE)

    _ERROR = errors.MeshtalError
    _CODE = errors.MeshtalCode.SEMANTICS_LINE

    result = _fields.Field(types.String, 'Tally result')
    error = _fields.Field(types.String, 'Tally relative error')
    x = _fields.Field(types.String, 'Tally x direction', optional=True)
    y = _fields.Field(types.String, 'Tally y direction', optional=True)
    z = _fields.Field(types.String, 'Tally z direction', optional=True)
    energy = _fields.Field(types.String, 'Tally energy', optional=True)
    time = _fields.Field(types.String, 'Tally time', optional=True)

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Tally` from MESHTAL.

        Parameters:
            source: MESHTAL for `Tally`.
            header: MESHTAL header.
        """

        tokens = Tally._REGEX.match(source)

        if not tokens:
            raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_LINE, source)

        energy = types.String.from_mcnp(tokens[1]) if tokens[1] else None
        time = types.String.from_mcnp(tokens[2]) if tokens[2] else None
        x = types.String.from_mcnp(tokens[3]) if tokens[3] else None
        y = types.String.from_mcnp(tokens[4]) if tokens[4] else None
        z = types.String.from_mcnp(tokens[5]) if tokens[5] else None
        result = types.String.from_mcnp(tokens[6])
        error = types.String.from_mcnp(tokens[7])

        return Tally(
            result,
            error,
            x=x,
            y=y,
            z=z,
            energy=energy,
            time=time,
        )

    def to_mcnp(self):
        """
        Generates MESTHAL from `Tally`.

        Returns:
            INP for `Tally`.
        """

        return f'  {self.energy if self.energy is not None else ""}{self.time if self.time is not None else ""}{self.x if self.x is not None else ""}{self.y if self.y is not None else ""}{self.z if self.z is not None else ""}{self.result}{self.error}'

import re
import typing

from . import _line
from .. import types
from .. import errors


class Tally(_line.Line):
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

    def __init__(
        self,
        result: types.String,
        error: types.String,
        x: types.String = None,
        y: types.String = None,
        z: types.String = None,
        energy: types.String = None,
        time: types.String = None,
    ):
        """
        Initializes `Tally`.

        Parameters:
            x: Tally x direction.
            y: Tally y direction.
            z: Tally z direction.
            energy: Tally energy.
            time: Tally time.
            result: Tally result.
            error: Tally relative error.
        """

        if result is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_LINE, result)

        if error is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_LINE, error)

        self.result: typing.Final[types.String] = result
        self.error: typing.Final[types.String] = error
        self.x: typing.Final[types.String] = x
        self.y: typing.Final[types.String] = y
        self.z: typing.Final[types.String] = z
        self.energy: typing.Final[types.String] = energy
        self.time: typing.Final[types.String] = time

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

import re
import typing

from . import _line
from .Header import Header
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

    _REGEX = re.compile(r'\A\s(.+)\n?\Z')

    def __init__(
        self,
        result: types.Real,
        error: types.Real,
        x: types.Real = None,
        y: types.Real = None,
        z: types.Real = None,
        energy: types.Real = None,
        time: types.Real = None,
    ):
        """
        Initializes ``Tally``.

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

        self.result: typing.Final[types.Real] = result
        self.error: typing.Final[types.Real] = error
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.energy: typing.Final[types.Real] = energy
        self.time: typing.Final[types.Real] = time

    @staticmethod
    def from_mcnp(source: str, header: Header):
        """
        Generates ``Tally`` from MESHTAL.

        Parameters:
            source: MESHTAL for ``Tally``.
            header: MESHTAL header.
        """

        tokens = Tally._REGEX.match(source)
        headings = re.split(r'\s+', header.columns.strip())

        if not tokens:
            raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_LINE, source)

        x = None
        y = None
        z = None
        energy = None
        time = None
        result = None
        error = None

        tokens = re.split(r'\s+', tokens[1].strip())

        for i, heading in enumerate(headings):
            if heading == 'X':
                x = tokens[i]
            elif heading == 'Y':
                y = tokens[i]
            elif heading == 'Z':
                z = tokens[i]
            elif heading == 'Energy':
                energy = tokens[i]
            elif heading == 'Time':
                time = tokens[i]
            elif heading == 'Result':
                result = tokens[i]
            elif heading == 'Rel':
                error = tokens[i]
            elif heading == 'Error':
                pass
            else:
                raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_LINE, source)

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
        Generates MESTHAL from ``Tally``.

        Returns:
            INP for ``Tally``.
        """

        line = ''
        line += f'{self.energy:>11}' if self.energy else ''
        line += f'{self.time:>11}' if self.time else ''
        line += f'{self.x:>10}' if self.x else ''
        line += f'{self.y:>10}' if self.y else ''
        line += f'{self.z:>10}' if self.z else ''
        line += f'{self.result:>12}' if self.result else ''
        line += f'{self.error:>12}' if self.error else ''

        return line

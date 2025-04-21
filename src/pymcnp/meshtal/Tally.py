import re
import typing

from . import _line
from .Header import Header
from ..utils import types
from ..utils import errors


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

    _REGEX = re.compile(r'\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\n([\s\S]+)')

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
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_LINE_VALUE, result)

        if error is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_LINE_VALUE, error)

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.energy: typing.Final[types.Real] = energy
        self.time: typing.Final[types.Real] = time
        self.result: typing.Final[types.Real] = result
        self.error: typing.Final[types.Real] = error

    @staticmethod
    def from_mcnp(source: str, header: Header):
        """
        Generates ``Tally`` from MESHTAL.

        Parameters:
            source: MESHTAL for ``Tally``.
            header: MESHTAL header.
        """

        tokens = Tally._REGEX.match(source)
        headings = re.split(r'\s+', header.columns)

        if not tokens or (len(tokens.groups()) != len(headings) + 2):
            raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_LINE, source)

        x = None
        y = None
        z = None
        energy = None
        time = None
        result = None
        error = None

        for i, heading in enumerate(headings):
            if heading == 'x':
                x = tokens[i + 1]
            elif heading == 'y':
                y = tokens[i + 1]
            elif heading == 'z':
                z = tokens[i + 1]
            elif heading == 'energy':
                energy = tokens[i + 1]
            elif heading == 'time':
                time = tokens[i + 1]
            elif heading == 'result':
                result = tokens[i + 1]
            elif heading == 'rel':
                error = tokens[i + 1]
            elif heading == 'error':
                pass
            else:
                raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_LINE, source)

        return (
            Tally(x, y, z, energy, time, result, error),
            tokens[8],
        )

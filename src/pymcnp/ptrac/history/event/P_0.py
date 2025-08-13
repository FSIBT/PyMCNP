import re
import typing

from . import _line
from .... import types
from .... import errors


class P_0(_line.EventLine):
    """
    Represents PTRAC history block p lines form #1.

    Attributes:
        x: X coordinate of the particle position.
        y: Y coordinate of the particle position.
        z: Z coordinate of the particle position.
    """

    _REGEX = re.compile(r'\A\s(.{13})(.{13})(.{13})\Z', re.IGNORECASE)

    def __init__(
        self,
        x: types.Real,
        y: types.Real,
        z: types.Real,
    ):
        """
        Initializes `P_0`.

        Parameters:
            x: X coordinate of the particle position.
            y: Y coordinate of the particle position.
            z: Z coordinate of the particle position.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if x is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, x)

        if y is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, y)

        if z is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, z)

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z

    def from_mcnp(source: str):
        """
        Generates `P_0` from PTRAC.

        Parameters:
            source: PTRAC for `P_0`.

        Returns:
            `P_0`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = P_0._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])

        return P_0(
            x,
            y,
            z,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `P_0`.

        Returns:
            PTRAC for `P_0`.
        """

        x = f'{self.x:5.1a}'
        y = f'{self.y:5.1a}'
        z = f'{self.z:5.1a}'

        return f'  {x} {y} {z}'

from __future__ import annotations

import typing

from ... import abc
from ... import _show
from ..Card import Card
from .. import literal


class Surface(Card):
    """
    Represents surface cards.
    """

    if typing.TYPE_CHECKING:
        prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
        j: literal.Integer
        keyword: (
            typing.Annotated[abc.Terminal, r'P']
            | typing.Annotated[abc.Terminal, r'PX']
            | typing.Annotated[abc.Terminal, r'PY']
            | typing.Annotated[abc.Terminal, r'PZ']
            | typing.Annotated[abc.Terminal, r'SO']
            | typing.Annotated[abc.Terminal, r'S']
            | typing.Annotated[abc.Terminal, r'SX']
            | typing.Annotated[abc.Terminal, r'SY']
            | typing.Annotated[abc.Terminal, r'SZ']
            | typing.Annotated[abc.Terminal, r'C/X']
            | typing.Annotated[abc.Terminal, r'C/Y']
            | typing.Annotated[abc.Terminal, r'C/Z']
            | typing.Annotated[abc.Terminal, r'CX']
            | typing.Annotated[abc.Terminal, r'CY']
            | typing.Annotated[abc.Terminal, r'CZ']
            | typing.Annotated[abc.Terminal, r'K/X']
            | typing.Annotated[abc.Terminal, r'K/Y']
            | typing.Annotated[abc.Terminal, r'K/Z']
            | typing.Annotated[abc.Terminal, r'KX']
            | typing.Annotated[abc.Terminal, r'KY']
            | typing.Annotated[abc.Terminal, r'KZ']
            | typing.Annotated[abc.Terminal, r'SQ']
            | typing.Annotated[abc.Terminal, r'GQ']
            | typing.Annotated[abc.Terminal, r'TX']
            | typing.Annotated[abc.Terminal, r'TY']
            | typing.Annotated[abc.Terminal, r'TZ']
            | typing.Annotated[abc.Terminal, r'X']
            | typing.Annotated[abc.Terminal, r'Y']
            | typing.Annotated[abc.Terminal, r'Z']
            | typing.Annotated[abc.Terminal, r'BOX']
            | typing.Annotated[abc.Terminal, r'RPP']
            | typing.Annotated[abc.Terminal, r'SPH']
            | typing.Annotated[abc.Terminal, r'RCC']
            | typing.Annotated[abc.Terminal, r'RHP']
            | typing.Annotated[abc.Terminal, r'REC']
            | typing.Annotated[abc.Terminal, r'TRC']
            | typing.Annotated[abc.Terminal, r'ELL']
            | typing.Annotated[abc.Terminal, r'WED']
            | typing.Annotated[abc.Terminal, r'ARB']
        )

    def __and__(a: Surface, b: Surface) -> literal.Geometry:
        """
        Intersects surface cards.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Geometry formula of intersections of surface cards.
        """

        return literal.Geometry.from_mcnp(f'{a.j} {b.j}')[0]

    def __or__(a: Surface, b: Surface) -> literal.Geometry:
        """
        Unites surface cards.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Geometry formula of unions of surface cards.
        """

        return literal.Geometry.from_mcnp(f'({a.j}:{b.j})')[0]

    def __neg__(self) -> literal.Geometry:
        """
        Negates surface cards.

        Returns:
            Geometry formula of surface cards in negative sense.
        """

        return literal.Geometry.from_mcnp(f'-{self.j}')[0]

    def __pos__(self) -> literal.Geometry:
        """
        Asserts surface cards.

        Returns:
            Geometry formula of surface cards in positive sense.
        """

        return literal.Geometry.from_mcnp(f'+{self.j}')[0]

    def to_show(self, shapes: abc.Endpoint = _show.pyvista) -> abc.Visualization:
        """
        Visualizes surface cards.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            Visualization of surface cards.
        """

        raise NotImplementedError

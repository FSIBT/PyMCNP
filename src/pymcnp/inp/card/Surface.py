from __future__ import annotations

import dataclasses

from ... import abc
from ... import _show
from ..Card import Card
from .. import literal


class Surface(Card):
    """
    Represents surface cards.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    def __and__(a: Surface, b: Surface) -> literal.Geometry:
        """
        Intersects surface cards.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Geometry formula of intersections of surface cards.
        """

        assert hasattr(a, 'j')
        assert hasattr(b, 'j')

        return literal.Geometry.from_mcnp(f'{a.j}:{b.j}')[0]

    def __or__(a: Surface, b: Surface) -> literal.Geometry:
        """
        Unites surface cards.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Geometry formula of unions of surface cards.
        """

        assert hasattr(a, 'j')
        assert hasattr(b, 'j')

        return literal.Geometry.from_mcnp(f'({a.j} {b.j})')[0]

    def __neg__(self) -> literal.Geometry:
        """
        Negates surface cards.

        Returns:
            Geometry formula of surface cards in negative sense.
        """

        assert hasattr(self, 'j')

        return literal.Geometry.from_mcnp(f'-{self.j}')[0]

    def __pos__(self) -> literal.Geometry:
        """
        Asserts surface cards.

        Returns:
            Geometry formula of surface cards in positive sense.
        """

        assert hasattr(self, 'j')

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

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
        Unites surface cards.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Formula for union of surface cards.
        """

        assert hasattr(a, 'j')
        assert hasattr(b, 'j')

        return literal.Geometry.from_mcnp(f'{a.j}:{b.j}')[0]

    def __or__(a: Surface, b: Surface) -> literal.Geometry:
        """
        Intersects surface cards.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            Formula for intersection of surface cards.
        """

        assert hasattr(a, 'j')
        assert hasattr(b, 'j')

        return literal.Geometry.from_mcnp(f'({a.j} {b.j})')[0]

    def __neg__(self) -> literal.Geometry:
        """
        Negates surface cards.

        Returns:
            Formula for negated of surface cards.
        """

        assert hasattr(self, 'j')

        return literal.Geometry.from_mcnp(f'-{self.j}')[0]

    def __pos__(self) -> literal.Geometry:
        """
        Asserts surface cards.

        Returns:
            Formula for asserted of surface cards.
        """

        assert hasattr(self, 'j')

        return literal.Geometry.from_mcnp(f'+{self.j}')[0]

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Box_0`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Box_0`.
        """

        raise NotImplementedError

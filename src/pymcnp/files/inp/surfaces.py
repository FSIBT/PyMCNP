"""
``surfaces`` contains the class representing INP surface card blocks.

``surfaces`` packages the ``Surfaces`` class, providing an object-oriented,
importable interface for INP surface card blocks.
"""

from . import _block
from .surface import Surface
from ..utils import _parser


class Surfaces(_block.Block):
    """
    ``Surfaces`` represents INP surfaces card blocks.

    ``Surfaces`` implements INP surfaces card blocks as a Python class. It
    represents the INP surfaces card block syntax element, and it inherits from
    the ``Block`` super class.
    """

    def __init__(self):
        """
        ``__init__`` initalizes ``Surfaces``.
        """

        super().__init__()

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Surfaces`` objects from INP.

        ``from_mcnp`` constructs instances of ``Surfaces`` from INP source
        strings, so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for surface block.

        Returns:
            ``Surfaces`` object.
        """

        block = Surfaces()

        lines = _parser.Preprocessor.process_inp(source).split('\n')
        for line in lines:
            if line == '':
                break
            elif line == 'c' or line[0] == 'c' and not line[1].isalpha():
                continue
            else:
                block.append(Surface.from_mcnp(line))

        return block

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Surfaces`` objects.

        ``to_mcnp`` creates INP source string from ``Surfaces`` objects, so it
        provides an MCNP endpoint.

        Returns:
            INP string for ``Surfaces`` object.
        """

        return '\n'.join([surface.to_mcnp() for surface in self._cards.values()] + [''])

    def to_arguments(self) -> list:
        """
        ``to_arguments`` makes lists from ``Surfaces`` objects.

        ``to_arguments`` creates Python lists from ``Surfaces`` objects, so
        it provides an MCNP endpoint. The list entries are ``Surfaces``
        objects.

        Returns:
            List for ``Surfaces`` objects.
        """

        return [card.to_arguments() for card in self._cards.values()]

    def to_cadquery(self, hasHeader: bool = False) -> str:
        """
        ``to_cadquery`` generates cadquery from ``Surfaces`` objects.

        ``to_cadquery`` creates cadquery source string from ``Surfaces``
        objects, so it provides a cadquery endpoint.

        Parameters:
            hasHeader: Boolean to include cadquery header.

        Returns:
            INP string for ``Surfaces`` object.
        """

        cadquery = 'import cadquery as cq\n\n' if hasHeader else ''
        surfaces_line = '\nsurfaces = cq.Workplane()'

        for surface in self._cards.values():
            if hasattr(surface, 'to_cadquery'):
                new_cadquery = surface.to_cadquery(hasHeader=False)
                surfaces_line += f'.add({new_cadquery.split(maxsplit=1)[0]})'
                cadquery += new_cadquery

        return cadquery + surfaces_line + '\n\n'

    def to_cadquery_file(self, filename: str, hasHeader: bool = True) -> None:
        """
        ``to_cadquery_file`` generates cadquery files from ``Surfaces``
        objects.

        ``to_cadquery_file`` creates cadquery files containg cadquery source
        strings from ``Surfaces`` objects, so it provides a cadquery endpoint.

        Parameters:
            filename: Name of cadquery output file.
            hasHeader: Boolean to include cadquery header.
        """

        with open(filename, 'w') as file:
            file.write(self.to_cadquery(hasHeader))

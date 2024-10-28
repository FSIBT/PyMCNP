"""
``cells`` contains the class representing INP cell card blocks.

``cells`` packages the ``Cells`` class, providing an object-oriented, importable
interface for INP cell card blocks.
"""

from . import _block
from .cell import Cell
from ..utils import _parser


class Cells(_block.Block):
    """
    ``Cells`` represents INP cell card blocks.

    ``Cells`` implements INP cell card blocks as a Python class. It represents
    the INP cell card block syntax element, and it inherits from the ``Block``
    super class.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Cells``.
        """

        super().__init__()

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Cells`` objects from INP.

        ``from_mcnp`` constructs instances of ``Cells`` from INP source
        strings, so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for cell block.

        Returns:
            ``Cells`` object.
        """

        block = Cells()

        lines = _parser.Preprocessor.process_inp(source).split('\n')
        for line in lines:
            if line == '':
                break
            elif line == 'c' or line[0] == 'c' and not line[1].isalpha():
                continue
            else:
                block.append(Cell.from_mcnp(line))

        return block

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Cells`` objects.

        ``to_mcnp`` creates INP source string from ``Cells`` objects, so it
        provides an MCNP endpoint.

        Returns:
            INP string for ``Cells`` object.
        """

        return '\n'.join([cell.to_mcnp() for cell in self._cards.values()] + [''])

    def to_arguments(self) -> list:
        """
        ``to_arguments`` makes lists from ``Cells`` objects.

        ``to_arguments`` creates Python lists from ``Cells`` objects, so
        it provides an MCNP endpoint. The list entries are ``Cell`` objects.

        Returns:
            List for ``Cells`` objects.
        """

        return [card.to_arguments() for card in self._cards.values()]

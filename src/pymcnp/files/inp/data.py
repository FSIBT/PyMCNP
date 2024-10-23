"""
``data`` contains the class representing INP data card blocks.

``data`` packages the ``Data`` class, providing an object-oriented, importable
interface for INP data card blocks.
"""

from . import _block
from .datum import Datum
from ..utils import _parser


class Data(_block.Block):
    """
    ``Data`` represents INP data card blocks.

    ``Data`` implements INP data card blocks as a Python class. It represents
    the INP data card block syntax element, and it inherits from the ``Block``
    super class.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``Data``.
        """

        super().__init__()

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Data`` objects from INP.

        ``from_mcnp`` constructs instances of ``Data`` from INP source
        strings, so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for data block.

        Returns:
            ``Data`` object.
        """

        block = Data()

        lines = _parser.Preprocessor.process_inp(source).split('\n')
        for line in lines:
            if line == '':
                break
            elif line == 'c' or line[0] == 'c' and not line[1].isalpha():
                continue
            else:
                block.append(Datum.from_mcnp(line))

        return block

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Data`` objects.

        ``to_mcnp`` creates INP source string from ``Data`` objects, so it
        provides an MCNP endpoint.

        Returns:
            INP string for ``Data`` object.
        """

        return '\n'.join([datum.to_mcnp() for datum in self._cards.values()])

    def to_arguments(self) -> list:
        """
        ``to_arguments`` makes lists from ``Data`` objects.

        ``to_arguments`` creates Python lists from ``Data`` objects, so
        it provides an MCNP endpoint. The list entries are ``Data`` objects.

        Returns:
            List for ``Data`` objects.
        """

        return [card.to_arguments() for card in self._cards.values()]

    def __getitem__(self, index: str) -> Datum:
        try:
            return self._cards[index]
        except KeyError:
            raise KeyError

    def __contains__(self, item: str) -> Datum:
        return item in self._cards

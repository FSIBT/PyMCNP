"""
``ptrac`` contains classes representing PTRAC files.

``ptrac`` packages the ``Ptrac`` class, providing an object-oriented,
importable interface for PTRAC files.
"""

from typing import Generator

from .header import Header
from .history import History


class Ptrac:
    """
    ``Ptrac`` represents PTRAC files.

    ``Ptrac`` implements PTRAC files as a Python class. Its attributes store
    PTRAC file components, and its methods provide entry points and endpoints
    for working with PTRAC. It represents the PTRAC files syntax element.

    Attributes:
        head: PTRAC header.
        history: PTRAC history.
    """

    def __init__(self, head: Header, histories: Generator[History, None, None]):
        """
        ``__init__`` initializes ``Ptrac``.
        """

        self.header: Header = head
        self.histories: Generator[History] = histories

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Ptrac`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``Inp`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser.

        Parameters:
            source: PTRAC source string.

        Returns:
            ``Ptrac`` object.
        """

        # Processing Header
        head, lines = Header.from_mcnp(source)

        # Processing History
        def histories(lines):
            while lines:
                history, lines = History.from_mcnp(lines, head)
                yield history

        return Ptrac(head, histories(lines))

    @staticmethod
    def from_mcnp_file(filename: str):
        """
        ``from_mcnp_file`` generates ``Ptrac`` objects from PTRAC files.

        ``from_mcnp_file`` constructs instances of ``Ptrac`` from PTRAC files,
        so it operates as a class constructor method and PTRAC parser.

        Parameters:
            filename: Name of file to parse.

        Returns:
            ``Ptrac`` object.
        """

        with open(filename) as file:
            source = ''.join(file.readlines())

        return Ptrac.from_mcnp(source)

    def to_arguments(self) -> dict:
        """
        ``to_arguments`` makes dictionaries from ``Ptrac`` objects.

        ``to_arguments`` creates Python dictionaries from ``Ptrac`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Ptrac`` object.
        """

        return {
            'header': self.header.to_arguments(),
            'histories': [history.to_arguments() for history in self.histories],
        }

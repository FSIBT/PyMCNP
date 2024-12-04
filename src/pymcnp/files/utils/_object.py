"""
Contains abstract classes for MCNP files.
"""

import enum
import pathlib


class PyMcnpObject:
    """
    Represents generic MCNP objects in PyMCNP.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        raise NotImplementedError

    def __eq__(a, b):
        """
        Compares ``PyMcnpObject`` objects for equality.
        """

        return repr(a) == repr(b)

    def __str__(self):
        """
        Stingifies ``PyMcnpObject``.
        """

        return self.to_mcnp()

    def __repr__(self):
        """
        Stringifies ``PyMcnpObject`` for debugging.
        """

        return f"<{self.__class__.__name__} {' '.join(f'{attribute}={self.__dict__[attribute]}' for attribute in self.__dict__)}>"


class PyMcnpKeyword(PyMcnpObject, enum.Enum):
    """
    Represents generic MCNP keyword objects in PyMCNP.

    ``PyMcnpKeyword`` implements ``PyMcnpObject`` and ``str, enum.Enum``
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``PyMcnpKeyword``.

        ``from_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``PyMcnpKeyword``.
        """

        return self.value

    def __repr__(self):
        """
        Stringifies ``PyMcnpObject`` for debugging.
        """

        return f'<{self.__class__.__name__} {self.value}>'


class PyMcnpFileObject(PyMcnpObject):
    """
    Represents generic MCNP file objects in PyMCNP.

    ``PyMcnpKeyword`` implements ``PyMcnpObject``.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        raise NotImplementedError

    @staticmethod
    def from_mcnp_file(filename: str | pathlib.Path):
        raise NotImplementedError

    def to_mcnp_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP from ``PyMcnpFileObject`` objects.

        ``to_mcnp`` translates from PyMCNP to MCNP files.

        Parameters:
            filename: New MCNP file path.
        """

        filename = pathlib.Path(filename)
        filename.write_text(self.to_mcnp())

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


class PyMcnpKeyword(PyMcnpObject, enum.Enum):
    """
    Represents generic MCNP keyword objects in PyMCNP.

    ``PyMcnpKeyword`` implements ``PyMcnpObject`` and ``enum.StrEnum``
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

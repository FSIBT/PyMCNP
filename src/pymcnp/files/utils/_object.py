"""
Contains abstract classes for MCNP files.
"""

import pathlib


class PyMcnpObject:
    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        raise NotImplementedError


class PyMCNPFileObject(PyMcnpObject):
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
        Generates MCNP from ``PyMCNPFileObject`` objects.

        ``to_mcnp`` translates from PyMCNP to MCNP files.

        Parameters:
            filename: New MCNP file path.
        """

        filename = pathlib.Path(filename)
        filename.write_text(self.to_mcnp())

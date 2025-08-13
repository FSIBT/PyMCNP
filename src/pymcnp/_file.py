import abc
import pathlib

from . import errors
from . import _symbol


class File(_symbol.Nonterminal, metaclass=abc.ABCMeta):
    """
    Represents generic MCNP files.
    """

    @classmethod
    def from_file(cls, filename: pathlib.Path | str):
        """
        Generates `McnpFile` from MCNP files.

        Parameters:
            filename: MCNP file path.

        Raises:
            CliError: RUNTIME_PATH.
        """

        filename = pathlib.Path(filename)

        if not filename.is_file():
            raise errors.CliError(errors.CliCode.RUNTIME_PATH, filename)

        source = filename.read_text()

        return cls.from_mcnp(source)

    def to_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP files from `McnpFile`.

        Parameters:
            filename: new MCNP file path.
        """

        filename = pathlib.Path(filename)
        filename.write_text(self.to_mcnp())

import re
import pathlib

from ..utils import errors


class McnpElement_:
    """
    Represents generic MCNP syntax elements.
    """

    _REGEX: re.Pattern

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self):
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (a.__dict__ if a else None) == (b.__dict__ if b else None)


class McnpRegistry_(McnpElement_):
    """
    Represents generic MCNP syntax elements with subclass registries.
    """

    _SUBCLASSES: dict[str, list[McnpElement_]]


class McnpFile_(McnpElement_):
    """
    Represents generic MCNP files.
    """

    @classmethod
    def from_mcnp_file(cls, filename: pathlib.Path | str):
        """
        Generates ``McnpFile_`` from MCNP files.

        Parameters:
            filename: MCNP file path.

        Raises:
            CliError: SEMANTICS_PATH.
        """

        filename = pathlib.Path(filename)

        if not filename.is_file():
            raise errors.CliError(errors.CliCode.SEMANTICS_PATH)

        source = filename.read_text()

        return cls.from_mcnp(source)

    def to_mcnp_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP files from ``McnpFile_``.

        Parameters:
            filename: new MCNP file path.
        """

        filename = pathlib.Path(filename)

        if not filename.is_file():
            raise errors.CliError(errors.CliCode.SEMANTICS_PATH)

        filename.write_text(self.to_mcnp())

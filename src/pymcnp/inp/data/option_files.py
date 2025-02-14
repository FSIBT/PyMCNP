import re
import typing

from . import files
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Files(_option.DataOption_, keyword='files'):
    """
    Represents INP data card files options.

    Attributes:
        creations: Files to create.
    """

    _REGEX = re.compile(r'\Afiles((( \S+)( \S+)( \S+)( \S+)( \S+))+)\Z')

    def __init__(self, creations: tuple[files.FilesEntry_File]):
        """
        Initializes ``DataOption_Files``.

        Parameters:
            creations: Files to create.

        Returns:
            ``DataOption_Files``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if creations is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, creations)

        self.value: typing.Final[tuple[any]] = types._Tuple([creations])
        self.creations: typing.Final[tuple[files.FilesEntry_File]] = creations

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Files`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Files``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Files._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        creations = types._Tuple(
            [
                files.FilesEntry_File.from_mcnp(token[0])
                for token in files.FilesEntry_File._REGEX.finditer(tokens[1])
            ]
        )

        return DataOption_Files(creations)

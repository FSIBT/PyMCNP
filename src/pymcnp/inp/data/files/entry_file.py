import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FilesEntry_File(_entry.FilesEntry_):
    """
    Represents INP data card data option file entries.

    Attributes:
        unit: Unit number of file to create.
        filename: Name of file to create.
        access: access of file to create.
        form: Format of file to create.
        length: Record length of file to create.
    """

    _REGEX = re.compile(r'( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        unit: types.Integer,
        filename: types.String,
        access: types.String,
        form: types.String,
        length: types.Integer,
    ):
        """
        Initializes ``FilesEntry_File``.

        Parameters:
            unit: Unit number of file to create.
            filename: Name of file to create.
            access: access of file to create.
            form: Format of file to create.
            length: Record length of file to create.

        Returns:
            ``FilesEntryFile``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if unit is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, unit)
        if filename is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, filename)
        if access is None or access not in {'sequential', 'direct'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, access)
        if form is None or format not in {'formatted', 'unformatted'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, form)
        if length is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, length)

        self.parameters: typing.Final[tuple[any]] = types._Tuple(
            [unit, filename, access, form, length]
        )
        self.unit: typing.Final[types.Integer] = unit
        self.filename: typing.Final[types.String] = filename
        self.access: typing.Final[types.String] = access
        self.form: typing.Final[types.String] = form
        self.length: typing.Final[types.Integer] = length

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FilesEntry_File`` from INP.

        Parameters:
            INP for ``FilesEntry_File``.

        Returns:
            ``FilesEntry_File``.

        Raises:
            McnpError: SYNTAX_FILES_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FilesEntry_File._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FILES_ENTRY, source)

        unit = types.Integer.from_mcnp(tokens[1])
        filename = types.String.from_mcnp(tokens[2])
        access = types.String.from_mcnp(tokens[3])
        form = types.String.from_mcnp(tokens[4])
        length = types.Integer.from_mcnp(tokens[5])

        return FilesEntry_File(unit, filename, access, form, length)

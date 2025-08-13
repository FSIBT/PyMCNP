import re

from . import _entry
from ... import types
from ... import errors


class File(_entry.FilesEntry):
    """
    Represents INP `file` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'unit': types.Integer,
        'filename': types.String,
        'access': types.String,
        'form': types.String,
        'length': types.Integer,
    }

    _REGEX = re.compile(r'\A(\S+) (\S+)(?: (\S+))?(?: (\S+))?(?: (\S+))?\Z', re.IGNORECASE)

    def __init__(
        self, unit: str | int | types.Integer, filename: str | int | types.String, access: str | types.String = None, form: str | types.String = None, length: str | int | types.Integer = None
    ):
        """
        Initializes `File`.

        Parameters:
            unit: Unit number of file to create.
            filename: Name of file to create.
            access: access of file to create.
            form: Format of file to create.
            length: Record length of file to create.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.unit: types.Integer = unit
        self.filename: types.String = filename
        self.access: types.String = access
        self.form: types.String = form
        self.length: types.Integer = length

    @property
    def unit(self) -> types.Integer:
        """
        Unit number of file to create

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._unit

    @unit.setter
    def unit(self, unit: str | int | types.Integer) -> None:
        """
        Sets `unit`.

        Parameters:
            unit: Unit number of file to create.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if unit is not None:
            if isinstance(unit, types.Integer):
                unit = unit
            elif isinstance(unit, int):
                unit = types.Integer(unit)
            elif isinstance(unit, str):
                unit = types.Integer.from_mcnp(unit)

        if unit is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, unit)

        self._unit: types.Integer = unit

    @property
    def filename(self) -> types.String:
        """
        Name of file to create

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._filename

    @filename.setter
    def filename(self, filename: str | types.String) -> None:
        """
        Sets `filename`.

        Parameters:
            filename: Name of file to create.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if filename is not None:
            if isinstance(filename, types.String):
                filename = filename
            elif isinstance(filename, str):
                filename = types.String.from_mcnp(filename)

        if filename is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, filename)

        self._filename: types.String = filename

    @property
    def access(self) -> types.String:
        """
        Access of file to create

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._access

    @access.setter
    def access(self, access: str | types.String) -> None:
        """
        Sets `access`.

        Parameters:
            access: access of file to create.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if access is not None:
            if isinstance(access, types.String):
                access = access
            elif isinstance(access, str):
                access = types.String.from_mcnp(access)

        if access is not None and access.value.lower() not in {'sequential', 'direct', 's', 'd'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, access)

        self._access: types.String = access

    @property
    def form(self) -> types.String:
        """
        Format of file to create

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._form

    @form.setter
    def form(self, form: str | types.String) -> None:
        """
        Sets `form`.

        Parameters:
            form: Format of file to create.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if form is not None:
            if isinstance(form, types.String):
                form = form
            elif isinstance(form, str):
                form = types.String.from_mcnp(form)

        if form is not None and form.value.lower() not in {'formatted', 'unformatted', 'f', 'u'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, form)

        self._form: types.String = form

    @property
    def length(self) -> types.Integer:
        """
        Record length of file to create

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._length

    @length.setter
    def length(self, length: str | int | types.Integer) -> None:
        """
        Sets `length`.

        Parameters:
            length: Record length of file to create.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if length is not None:
            if isinstance(length, types.Integer):
                length = length
            elif isinstance(length, int):
                length = types.Integer(length)
            elif isinstance(length, str):
                length = types.Integer.from_mcnp(length)

        self._length: types.Integer = length

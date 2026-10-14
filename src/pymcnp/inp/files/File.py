import re

from .. import _field
from . import _entry
from ... import types
from ... import errors


class File(_field.Fields, _entry.FilesEntry):
    """
    Represents INP `file` elements.
    """

    _KEYWORD = ''

    _CODE = errors.InpCode.SEMANTICS_OPTION

    unit = _field.Field(types.Integer, 'Unit number of file to create', required=True, numeric=int)
    filename = _field.Field(types.String, 'Name of file to create', required=True, numeric=())
    access = _field.Field(types.String, 'Access of file to create', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'sequential', 'direct', 's', 'd'})
    form = _field.Field(types.String, 'Format of file to create', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'formatted', 'unformatted', 'f', 'u'})
    length = _field.Field(types.Integer, 'Record length of file to create', numeric=int)

    _REGEX = re.compile(r'\A(\S+) (\S+)(?: (\S+))?(?: (\S+))?(?: (\S+))?\Z', re.IGNORECASE)

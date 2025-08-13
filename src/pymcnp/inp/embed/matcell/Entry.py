import re

from . import _entry
from .... import types
from .... import errors


class Entry(_entry.MatcellEntry):
    """
    Represents INP `entry` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'material': types.Integer,
        'cell': types.Integer,
    }

    _REGEX = re.compile(rf'\A({types.Integer._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, material: str | int | types.Integer, cell: str | int | types.Integer):
        """
        Initializes `Entry`.

        Parameters:
            material: Material number.
            cell: Geometry number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.material: types.Integer = material
        self.cell: types.Integer = cell

    @property
    def material(self) -> types.Integer:
        """
        Material number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._material

    @material.setter
    def material(self, material: str | int | types.Integer) -> None:
        """
        Sets `material`.

        Parameters:
            material: Material number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if material is not None:
            if isinstance(material, types.Integer):
                material = material
            elif isinstance(material, int):
                material = types.Integer(material)
            elif isinstance(material, str):
                material = types.Integer.from_mcnp(material)

        if material is None or not (0 <= material.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, material)

        self._material: types.Integer = material

    @property
    def cell(self) -> types.Integer:
        """
        Geometry number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cell

    @cell.setter
    def cell(self, cell: str | int | types.Integer) -> None:
        """
        Sets `cell`.

        Parameters:
            cell: Geometry number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cell is not None:
            if isinstance(cell, types.Integer):
                cell = cell
            elif isinstance(cell, int):
                cell = types.Integer(cell)
            elif isinstance(cell, str):
                cell = types.Integer.from_mcnp(cell)

        if cell is None or not (0 <= cell.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cell)

        self._cell: types.Integer = cell

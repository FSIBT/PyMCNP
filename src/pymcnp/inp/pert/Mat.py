import re

from . import _option
from ... import types
from ... import errors


class Mat(_option.PertOption):
    """
    Represents INP `mat` elements.
    """

    _KEYWORD = 'mat'

    _ATTRS = {
        'material': types.Integer,
    }

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, material: str | int | types.Integer):
        """
        Initializes `Mat`.

        Parameters:
            material: Material number to fill cells.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.material: types.Integer = material

    @property
    def material(self) -> types.Integer:
        """
        Material number to fill cells

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
            material: Material number to fill cells.

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

        if material is None or not (material >= 0 and material <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, material)

        self._material: types.Integer = material

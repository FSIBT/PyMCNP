import re

from . import _option
from ... import _show
from ... import types
from ... import errors


class Pz(_option.SurfaceOption):
    """
    Represents INP `pz` elements.
    """

    _KEYWORD = 'pz'

    _ATTRS = {
        'd': types.Real,
    }

    _REGEX = re.compile(rf'\Apz( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, d: str | int | float | types.Real):
        """
        Initializes `Pz`.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.d: types.Real = d

    @property
    def d(self) -> types.Real:
        """
        Normal-to-the-z-axis plane D coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._d

    @d.setter
    def d(self, d: str | int | float | types.Real) -> None:
        """
        Sets `d`.

        Parameters:
            d: Normal-to-the-z-axis plane D coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if d is not None:
            if isinstance(d, types.Real):
                d = d
            elif isinstance(d, int) or isinstance(d, float):
                d = types.Real(d)
            elif isinstance(d, str):
                d = types.Real.from_mcnp(d)

        if d is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, d)

        self._d: types.Real = d

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Pz`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Pz`
        """

        vis = shapes.Plane(0, 0, 1, float(self.d))

        return vis

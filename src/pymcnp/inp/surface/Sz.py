import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Sz(_option.SurfaceOption):
    """
    Represents INP sz elements.

    Attributes:
        z: On-z-axis sphere center z component.
        r: On-z-axis sphere radius.
    """

    _KEYWORD = 'sz'

    _ATTRS = {
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Asz( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, z: str | int | float | types.Real, r: str | int | float | types.Real):
        """
        Initializes ``Sz``.

        Parameters:
            z: On-z-axis sphere center z component.
            r: On-z-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.z: types.Real = z
        self.r: types.Real = r

    @property
    def z(self) -> types.Real:
        """
        Gets ``z``.

        Returns:
            ``z``.
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets ``z``.

        Parameters:
            z: On-z-axis sphere center z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z is not None:
            if isinstance(z, types.Real):
                z = z
            elif isinstance(z, int):
                z = types.Real(z)
            elif isinstance(z, float):
                z = types.Real(z)
            elif isinstance(z, str):
                z = types.Real.from_mcnp(z)
            else:
                raise TypeError

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self._z: types.Real = z

    @property
    def r(self) -> types.Real:
        """
        Gets ``r``.

        Returns:
            ``r``.
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets ``r``.

        Parameters:
            r: On-z-axis sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r is not None:
            if isinstance(r, types.Real):
                r = r
            elif isinstance(r, int):
                r = types.Real(r)
            elif isinstance(r, float):
                r = types.Real(r)
            elif isinstance(r, str):
                r = types.Real.from_mcnp(r)
            else:
                raise TypeError

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self._r: types.Real = r

    def draw(self):
        """
        Generates ``Visualization`` from ``Sz``.

        Returns:
            ``pyvista.PolyData`` for ``Sz``
        """

        vis = _visualization.Visualization.get_sphere(float(self.r))
        vis = vis.add_translation(_visualization.Vector(0, 0, self.z))

        return vis

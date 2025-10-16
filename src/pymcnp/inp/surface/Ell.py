import re

import numpy

from . import _option
from ... import types
from ... import errors


class Ell(_option.SurfaceOption):
    """
    Represents INP `ell` elements.
    """

    _KEYWORD = 'ell'

    _ATTRS = {
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
        'rm': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aell( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        v1x: str | int | float | types.Real,
        v1y: str | int | float | types.Real,
        v1z: str | int | float | types.Real,
        v2x: str | int | float | types.Real,
        v2y: str | int | float | types.Real,
        v2z: str | int | float | types.Real,
        rm: str | int | float | types.Real,
    ):
        """
        Initializes `Ell`.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.v1x: types.Real = v1x
        self.v1y: types.Real = v1y
        self.v1z: types.Real = v1z
        self.v2x: types.Real = v2x
        self.v2y: types.Real = v2y
        self.v2z: types.Real = v2z
        self.rm: types.Real = rm

    @property
    def v1x(self) -> types.Real:
        """
        Ellipsoid focus #1 or center x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v1x

    @v1x.setter
    def v1x(self, v1x: str | int | float | types.Real) -> None:
        """
        Sets `v1x`.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v1x is not None:
            if isinstance(v1x, types.Real):
                v1x = v1x
            elif isinstance(v1x, int) or isinstance(v1x, float):
                v1x = types.Real(v1x)
            elif isinstance(v1x, str):
                v1x = types.Real.from_mcnp(v1x)

        if v1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1x)

        self._v1x: types.Real = v1x

    @property
    def v1y(self) -> types.Real:
        """
        Ellipsoid focus #1 or center y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v1y

    @v1y.setter
    def v1y(self, v1y: str | int | float | types.Real) -> None:
        """
        Sets `v1y`.

        Parameters:
            v1y: Ellipsoid focus #1 or center y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v1y is not None:
            if isinstance(v1y, types.Real):
                v1y = v1y
            elif isinstance(v1y, int) or isinstance(v1y, float):
                v1y = types.Real(v1y)
            elif isinstance(v1y, str):
                v1y = types.Real.from_mcnp(v1y)

        if v1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1y)

        self._v1y: types.Real = v1y

    @property
    def v1z(self) -> types.Real:
        """
        Ellipsoid focus #1 or center z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v1z

    @v1z.setter
    def v1z(self, v1z: str | int | float | types.Real) -> None:
        """
        Sets `v1z`.

        Parameters:
            v1z: Ellipsoid focus #1 or center z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v1z is not None:
            if isinstance(v1z, types.Real):
                v1z = v1z
            elif isinstance(v1z, int) or isinstance(v1z, float):
                v1z = types.Real(v1z)
            elif isinstance(v1z, str):
                v1z = types.Real.from_mcnp(v1z)

        if v1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1z)

        self._v1z: types.Real = v1z

    @property
    def v2x(self) -> types.Real:
        """
        Ellipsoid focus #2 or major axis x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v2x

    @v2x.setter
    def v2x(self, v2x: str | int | float | types.Real) -> None:
        """
        Sets `v2x`.

        Parameters:
            v2x: Ellipsoid focus #2 or major axis x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v2x is not None:
            if isinstance(v2x, types.Real):
                v2x = v2x
            elif isinstance(v2x, int) or isinstance(v2x, float):
                v2x = types.Real(v2x)
            elif isinstance(v2x, str):
                v2x = types.Real.from_mcnp(v2x)

        if v2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2x)

        self._v2x: types.Real = v2x

    @property
    def v2y(self) -> types.Real:
        """
        Ellipsoid focus #2 or major axis y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v2y

    @v2y.setter
    def v2y(self, v2y: str | int | float | types.Real) -> None:
        """
        Sets `v2y`.

        Parameters:
            v2y: Ellipsoid focus #2 or major axis y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v2y is not None:
            if isinstance(v2y, types.Real):
                v2y = v2y
            elif isinstance(v2y, int) or isinstance(v2y, float):
                v2y = types.Real(v2y)
            elif isinstance(v2y, str):
                v2y = types.Real.from_mcnp(v2y)

        if v2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2y)

        self._v2y: types.Real = v2y

    @property
    def v2z(self) -> types.Real:
        """
        Ellipsoid focus #2 or major axis z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v2z

    @v2z.setter
    def v2z(self, v2z: str | int | float | types.Real) -> None:
        """
        Sets `v2z`.

        Parameters:
            v2z: Ellipsoid focus #2 or major axis z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v2z is not None:
            if isinstance(v2z, types.Real):
                v2z = v2z
            elif isinstance(v2z, int) or isinstance(v2z, float):
                v2z = types.Real(v2z)
            elif isinstance(v2z, str):
                v2z = types.Real.from_mcnp(v2z)

        if v2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2z)

        self._v2z: types.Real = v2z

    @property
    def rm(self) -> types.Real:
        """
        Ellipsoid major/minor axis radius length

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._rm

    @rm.setter
    def rm(self, rm: str | int | float | types.Real) -> None:
        """
        Sets `rm`.

        Parameters:
            rm: Ellipsoid major/minor axis radius length.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if rm is not None:
            if isinstance(rm, types.Real):
                rm = rm
            elif isinstance(rm, int) or isinstance(rm, float):
                rm = types.Real(rm)
            elif isinstance(rm, str):
                rm = types.Real.from_mcnp(rm)

        if rm is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, rm)

        self._rm: types.Real = rm

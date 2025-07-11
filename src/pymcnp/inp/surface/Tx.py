import re

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _visualization


class Tx(_option.SurfaceOption):
    """
    Represents INP tx elements.

    Attributes:
        x: Parallel-to-x-axis tori center x component.
        y: Parallel-to-x-axis tori center y component.
        z: Parallel-to-x-axis tori center z component.
        a: Parallel-to-x-axis tori A coefficent.
        b: Parallel-to-x-axis tori B coefficent.
        c: Parallel-to-x-axis tori C coefficent.
    """

    _KEYWORD = 'tx'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'a': types.Real,
        'b': types.Real,
        'c': types.Real,
    }

    _REGEX = re.compile(
        rf'\Atx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(
        self,
        x: str | int | float | types.Real,
        y: str | int | float | types.Real,
        z: str | int | float | types.Real,
        a: str | int | float | types.Real,
        b: str | int | float | types.Real,
        c: str | int | float | types.Real,
    ):
        """
        Initializes ``Tx``.

        Parameters:
            x: Parallel-to-x-axis tori center x component.
            y: Parallel-to-x-axis tori center y component.
            z: Parallel-to-x-axis tori center z component.
            a: Parallel-to-x-axis tori A coefficent.
            b: Parallel-to-x-axis tori B coefficent.
            c: Parallel-to-x-axis tori C coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z
        self.a: types.Real = a
        self.b: types.Real = b
        self.c: types.Real = c

    @property
    def x(self) -> types.Real:
        """
        Gets ``x``.

        Returns:
            ``x``.
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets ``x``.

        Parameters:
            x: Parallel-to-x-axis tori center x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int):
                x = types.Real(x)
            elif isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)
            else:
                raise TypeError

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Real = x

    @property
    def y(self) -> types.Real:
        """
        Gets ``y``.

        Returns:
            ``y``.
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets ``y``.

        Parameters:
            y: Parallel-to-x-axis tori center y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int):
                y = types.Real(y)
            elif isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)
            else:
                raise TypeError

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.Real = y

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
            z: Parallel-to-x-axis tori center z component.

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
    def a(self) -> types.Real:
        """
        Gets ``a``.

        Returns:
            ``a``.
        """

        return self._a

    @a.setter
    def a(self, a: str | int | float | types.Real) -> None:
        """
        Sets ``a``.

        Parameters:
            a: Parallel-to-x-axis tori A coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if a is not None:
            if isinstance(a, types.Real):
                a = a
            elif isinstance(a, int):
                a = types.Real(a)
            elif isinstance(a, float):
                a = types.Real(a)
            elif isinstance(a, str):
                a = types.Real.from_mcnp(a)
            else:
                raise TypeError

        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a)

        self._a: types.Real = a

    @property
    def b(self) -> types.Real:
        """
        Gets ``b``.

        Returns:
            ``b``.
        """

        return self._b

    @b.setter
    def b(self, b: str | int | float | types.Real) -> None:
        """
        Sets ``b``.

        Parameters:
            b: Parallel-to-x-axis tori B coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if b is not None:
            if isinstance(b, types.Real):
                b = b
            elif isinstance(b, int):
                b = types.Real(b)
            elif isinstance(b, float):
                b = types.Real(b)
            elif isinstance(b, str):
                b = types.Real.from_mcnp(b)
            else:
                raise TypeError

        if b is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, b)

        self._b: types.Real = b

    @property
    def c(self) -> types.Real:
        """
        Gets ``c``.

        Returns:
            ``c``.
        """

        return self._c

    @c.setter
    def c(self, c: str | int | float | types.Real) -> None:
        """
        Sets ``c``.

        Parameters:
            c: Parallel-to-x-axis tori C coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if c is not None:
            if isinstance(c, types.Real):
                c = c
            elif isinstance(c, int):
                c = types.Real(c)
            elif isinstance(c, float):
                c = types.Real(c)
            elif isinstance(c, str):
                c = types.Real.from_mcnp(c)
            else:
                raise TypeError

        if c is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self._c: types.Real = c

    def draw(self):
        """
        Generates ``Visualization`` from ``Tx``.

        Returns:
            ``pyvista.PolyData`` for ``Tx``
        """

        vis = _visualization.Visualization.get_torus(float(self.b), float(self.c), float(self.a))
        vis = vis.add_rotation(_visualization.Vector(0, 1, 0), 90, (0, 0, 0))
        vis = vis.add_translation(_visualization.Vector(self.x, self.y, self.z))

        return vis

import re

import numpy

from . import _option
from ... import types
from ... import errors


class K_x(_option.SurfaceOption):
    """
    Represents INP `k/x` elements.
    """

    _KEYWORD = 'k/x'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ak/x( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        x: str | int | float | types.Real,
        y: str | int | float | types.Real,
        z: str | int | float | types.Real,
        t_squared: str | int | float | types.Real,
        plusminus_1: str | int | float | types.Real,
    ):
        """
        Initializes `K_x`.

        Parameters:
            x: Parallel-to-x-axis cone center x component.
            y: Parallel-to-x-axis cone center y component.
            z: Parallel-to-x-axis cone center z component.
            t_squared: Parallel-to-x-axis cone t^2 coefficent.
            plusminus_1: Parallel-to-x-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z
        self.t_squared: types.Real = t_squared
        self.plusminus_1: types.Real = plusminus_1

    @property
    def x(self) -> types.Real:
        """
        Parallel-to-x-axis cone center x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets `x`.

        Parameters:
            x: Parallel-to-x-axis cone center x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int) or isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Real = x

    @property
    def y(self) -> types.Real:
        """
        Parallel-to-x-axis cone center y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets `y`.

        Parameters:
            y: Parallel-to-x-axis cone center y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int) or isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.Real = y

    @property
    def z(self) -> types.Real:
        """
        Parallel-to-x-axis cone center z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets `z`.

        Parameters:
            z: Parallel-to-x-axis cone center z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z is not None:
            if isinstance(z, types.Real):
                z = z
            elif isinstance(z, int) or isinstance(z, float):
                z = types.Real(z)
            elif isinstance(z, str):
                z = types.Real.from_mcnp(z)

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self._z: types.Real = z

    @property
    def t_squared(self) -> types.Real:
        """
        Parallel-to-x-axis cone t^2 coefficent

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._t_squared

    @t_squared.setter
    def t_squared(self, t_squared: str | int | float | types.Real) -> None:
        """
        Sets `t_squared`.

        Parameters:
            t_squared: Parallel-to-x-axis cone t^2 coefficent.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if t_squared is not None:
            if isinstance(t_squared, types.Real):
                t_squared = t_squared
            elif isinstance(t_squared, int) or isinstance(t_squared, float):
                t_squared = types.Real(t_squared)
            elif isinstance(t_squared, str):
                t_squared = types.Real.from_mcnp(t_squared)

        if t_squared is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, t_squared)

        self._t_squared: types.Real = t_squared

    @property
    def plusminus_1(self) -> types.Real:
        """
        Parallel-to-x-axis cone sheet selector

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._plusminus_1

    @plusminus_1.setter
    def plusminus_1(self, plusminus_1: str | int | float | types.Real) -> None:
        """
        Sets `plusminus_1`.

        Parameters:
            plusminus_1: Parallel-to-x-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if plusminus_1 is not None:
            if isinstance(plusminus_1, types.Real):
                plusminus_1 = plusminus_1
            elif isinstance(plusminus_1, int) or isinstance(plusminus_1, float):
                plusminus_1 = types.Real(plusminus_1)
            elif isinstance(plusminus_1, str):
                plusminus_1 = types.Real.from_mcnp(plusminus_1)

        if plusminus_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, plusminus_1)

        self._plusminus_1: types.Real = plusminus_1

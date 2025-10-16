import re

import numpy

from . import _option
from ... import types
from ... import errors


class Kx(_option.SurfaceOption):
    """
    Represents INP `kx` elements.
    """

    _KEYWORD = 'kx'

    _ATTRS = {
        'x': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(rf'\Akx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, x: str | int | float | types.Real, t_squared: str | int | float | types.Real, plusminus_1: str | int | float | types.Real):
        """
        Initializes `Kx`.

        Parameters:
            x: On-x-axis cone center x component.
            t_squared: On-x-axis cone t^2 coefficent.
            plusminus_1: On-x-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.t_squared: types.Real = t_squared
        self.plusminus_1: types.Real = plusminus_1

    @property
    def x(self) -> types.Real:
        """
        On-x-axis cone center x component

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
            x: On-x-axis cone center x component.

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
    def t_squared(self) -> types.Real:
        """
        On-x-axis cone t^2 coefficent

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
            t_squared: On-x-axis cone t^2 coefficent.

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
        On-x-axis cone sheet selector

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
            plusminus_1: On-x-axis cone sheet selector.

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

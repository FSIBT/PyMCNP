import re

import numpy

from . import _option
from ... import types
from ... import errors


class Ky(_option.SurfaceOption):
    """
    Represents INP `ky` elements.
    """

    _KEYWORD = 'ky'

    _ATTRS = {
        'y': types.Real,
        't_squared': types.Real,
        'plusminus_1': types.Real,
    }

    _REGEX = re.compile(rf'\Aky( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, y: str | int | float | types.Real, t_squared: str | int | float | types.Real, plusminus_1: str | int | float | types.Real):
        """
        Initializes `Ky`.

        Parameters:
            y: On-y-axis cone center y component.
            t_squared: On-y-axis cone t^2 coefficent.
            plusminus_1: On-y-axis cone sheet selector.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.y: types.Real = y
        self.t_squared: types.Real = t_squared
        self.plusminus_1: types.Real = plusminus_1

    @property
    def y(self) -> types.Real:
        """
        On-y-axis cone center y component

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
            y: On-y-axis cone center y component.

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
    def t_squared(self) -> types.Real:
        """
        On-y-axis cone t^2 coefficent

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
            t_squared: On-y-axis cone t^2 coefficent.

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
        On-y-axis cone sheet selector

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
            plusminus_1: On-y-axis cone sheet selector.

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

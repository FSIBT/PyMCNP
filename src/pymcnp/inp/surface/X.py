import re

from . import _option
from ... import types
from ... import errors


class X(_option.SurfaceOption):
    """
    Represents INP `x` elements.
    """

    _KEYWORD = 'x'

    _ATTRS = {
        'x1': types.Real,
        'r1': types.Real,
        'x2': types.Real,
        'r2': types.Real,
        'x3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ax( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        x1: str | int | float | types.Real,
        r1: str | int | float | types.Real,
        x2: str | int | float | types.Real = None,
        r2: str | int | float | types.Real = None,
        x3: str | int | float | types.Real = None,
        r3: str | int | float | types.Real = None,
    ):
        """
        Initializes `X`.

        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.
            r1: X-axisymmetric point-defined surface point #1 radius.
            x2: X-axisymmetric point-defined surface point #2 x component.
            r2: X-axisymmetric point-defined surface point #2 radius.
            x3: X-axisymmetric point-defined surface point #3 x component.
            r3: X-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x1: types.Real = x1
        self.r1: types.Real = r1
        self.x2: types.Real = x2
        self.r2: types.Real = r2
        self.x3: types.Real = x3
        self.r3: types.Real = r3

    @property
    def x1(self) -> types.Real:
        """
        X-axisymmetric point-defined surface point #1 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x1

    @x1.setter
    def x1(self, x1: str | int | float | types.Real) -> None:
        """
        Sets `x1`.

        Parameters:
            x1: X-axisymmetric point-defined surface point #1 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x1 is not None:
            if isinstance(x1, types.Real):
                x1 = x1
            elif isinstance(x1, int) or isinstance(x1, float):
                x1 = types.Real(x1)
            elif isinstance(x1, str):
                x1 = types.Real.from_mcnp(x1)

        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x1)

        self._x1: types.Real = x1

    @property
    def r1(self) -> types.Real:
        """
        X-axisymmetric point-defined surface point #1 radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r1

    @r1.setter
    def r1(self, r1: str | int | float | types.Real) -> None:
        """
        Sets `r1`.

        Parameters:
            r1: X-axisymmetric point-defined surface point #1 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r1 is not None:
            if isinstance(r1, types.Real):
                r1 = r1
            elif isinstance(r1, int) or isinstance(r1, float):
                r1 = types.Real(r1)
            elif isinstance(r1, str):
                r1 = types.Real.from_mcnp(r1)

        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)

        self._r1: types.Real = r1

    @property
    def x2(self) -> types.Real:
        """
        X-axisymmetric point-defined surface point #2 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x2

    @x2.setter
    def x2(self, x2: str | int | float | types.Real) -> None:
        """
        Sets `x2`.

        Parameters:
            x2: X-axisymmetric point-defined surface point #2 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x2 is not None:
            if isinstance(x2, types.Real):
                x2 = x2
            elif isinstance(x2, int) or isinstance(x2, float):
                x2 = types.Real(x2)
            elif isinstance(x2, str):
                x2 = types.Real.from_mcnp(x2)

        self._x2: types.Real = x2

    @property
    def r2(self) -> types.Real:
        """
        X-axisymmetric point-defined surface point #2 radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r2

    @r2.setter
    def r2(self, r2: str | int | float | types.Real) -> None:
        """
        Sets `r2`.

        Parameters:
            r2: X-axisymmetric point-defined surface point #2 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r2 is not None:
            if isinstance(r2, types.Real):
                r2 = r2
            elif isinstance(r2, int) or isinstance(r2, float):
                r2 = types.Real(r2)
            elif isinstance(r2, str):
                r2 = types.Real.from_mcnp(r2)

        self._r2: types.Real = r2

    @property
    def x3(self) -> types.Real:
        """
        X-axisymmetric point-defined surface point #3 x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x3

    @x3.setter
    def x3(self, x3: str | int | float | types.Real) -> None:
        """
        Sets `x3`.

        Parameters:
            x3: X-axisymmetric point-defined surface point #3 x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x3 is not None:
            if isinstance(x3, types.Real):
                x3 = x3
            elif isinstance(x3, int) or isinstance(x3, float):
                x3 = types.Real(x3)
            elif isinstance(x3, str):
                x3 = types.Real.from_mcnp(x3)

        self._x3: types.Real = x3

    @property
    def r3(self) -> types.Real:
        """
        X-axisymmetric point-defined surface point #3 radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r3

    @r3.setter
    def r3(self, r3: str | int | float | types.Real) -> None:
        """
        Sets `r3`.

        Parameters:
            r3: X-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r3 is not None:
            if isinstance(r3, types.Real):
                r3 = r3
            elif isinstance(r3, int) or isinstance(r3, float):
                r3 = types.Real(r3)
            elif isinstance(r3, str):
                r3 = types.Real.from_mcnp(r3)

        self._r3: types.Real = r3

import re

from . import _option
from ... import types
from ... import errors


class Y(_option.SurfaceOption):
    """
    Represents INP `y` elements.
    """

    _KEYWORD = 'y'

    _ATTRS = {
        'y1': types.Real,
        'r1': types.Real,
        'y2': types.Real,
        'r2': types.Real,
        'y3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ay( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        y1: str | int | float | types.Real,
        r1: str | int | float | types.Real,
        y2: str | int | float | types.Real = None,
        r2: str | int | float | types.Real = None,
        y3: str | int | float | types.Real = None,
        r3: str | int | float | types.Real = None,
    ):
        """
        Initializes `Y`.

        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.
            r1: Y-axisymmetric point-defined surface point #1 radius.
            y2: Y-axisymmetric point-defined surface point #2 y component.
            r2: Y-axisymmetric point-defined surface point #2 radius.
            y3: Y-axisymmetric point-defined surface point #3 y component.
            r3: Y-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.y1: types.Real = y1
        self.r1: types.Real = r1
        self.y2: types.Real = y2
        self.r2: types.Real = r2
        self.y3: types.Real = y3
        self.r3: types.Real = r3

    @property
    def y1(self) -> types.Real:
        """
        Y-axisymmetric point-defined surface point #1 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y1

    @y1.setter
    def y1(self, y1: str | int | float | types.Real) -> None:
        """
        Sets `y1`.

        Parameters:
            y1: Y-axisymmetric point-defined surface point #1 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y1 is not None:
            if isinstance(y1, types.Real):
                y1 = y1
            elif isinstance(y1, int) or isinstance(y1, float):
                y1 = types.Real(y1)
            elif isinstance(y1, str):
                y1 = types.Real.from_mcnp(y1)

        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y1)

        self._y1: types.Real = y1

    @property
    def r1(self) -> types.Real:
        """
        Y-axisymmetric point-defined surface point #1 radius

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
            r1: Y-axisymmetric point-defined surface point #1 radius.

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
    def y2(self) -> types.Real:
        """
        Y-axisymmetric point-defined surface point #2 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y2

    @y2.setter
    def y2(self, y2: str | int | float | types.Real) -> None:
        """
        Sets `y2`.

        Parameters:
            y2: Y-axisymmetric point-defined surface point #2 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y2 is not None:
            if isinstance(y2, types.Real):
                y2 = y2
            elif isinstance(y2, int) or isinstance(y2, float):
                y2 = types.Real(y2)
            elif isinstance(y2, str):
                y2 = types.Real.from_mcnp(y2)

        self._y2: types.Real = y2

    @property
    def r2(self) -> types.Real:
        """
        Y-axisymmetric point-defined surface point #2 radius

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
            r2: Y-axisymmetric point-defined surface point #2 radius.

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
    def y3(self) -> types.Real:
        """
        Y-axisymmetric point-defined surface point #3 y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y3

    @y3.setter
    def y3(self, y3: str | int | float | types.Real) -> None:
        """
        Sets `y3`.

        Parameters:
            y3: Y-axisymmetric point-defined surface point #3 y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y3 is not None:
            if isinstance(y3, types.Real):
                y3 = y3
            elif isinstance(y3, int) or isinstance(y3, float):
                y3 = types.Real(y3)
            elif isinstance(y3, str):
                y3 = types.Real.from_mcnp(y3)

        self._y3: types.Real = y3

    @property
    def r3(self) -> types.Real:
        """
        Y-axisymmetric point-defined surface point #3 radius

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
            r3: Y-axisymmetric point-defined surface point #3 radius.

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

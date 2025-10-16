import re

from . import _option
from ... import types
from ... import errors


class Z(_option.SurfaceOption):
    """
    Represents INP `z` elements.
    """

    _KEYWORD = 'z'

    _ATTRS = {
        'z1': types.Real,
        'r1': types.Real,
        'z2': types.Real,
        'r2': types.Real,
        'z3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Az( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        z1: str | int | float | types.Real,
        r1: str | int | float | types.Real,
        z2: str | int | float | types.Real = None,
        r2: str | int | float | types.Real = None,
        z3: str | int | float | types.Real = None,
        r3: str | int | float | types.Real = None,
    ):
        """
        Initializes `Z`.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.
            r1: Z-axisymmetric point-defined surface point #1 radius.
            z2: Z-axisymmetric point-defined surface point #2 z component.
            r2: Z-axisymmetric point-defined surface point #2 radius.
            z3: Z-axisymmetric point-defined surface point #3 z component.
            r3: Z-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.z1: types.Real = z1
        self.r1: types.Real = r1
        self.z2: types.Real = z2
        self.r2: types.Real = r2
        self.z3: types.Real = z3
        self.r3: types.Real = r3

    @property
    def z1(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #1 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z1

    @z1.setter
    def z1(self, z1: str | int | float | types.Real) -> None:
        """
        Sets `z1`.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z1 is not None:
            if isinstance(z1, types.Real):
                z1 = z1
            elif isinstance(z1, int) or isinstance(z1, float):
                z1 = types.Real(z1)
            elif isinstance(z1, str):
                z1 = types.Real.from_mcnp(z1)

        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z1)

        self._z1: types.Real = z1

    @property
    def r1(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #1 radius

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
            r1: Z-axisymmetric point-defined surface point #1 radius.

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
    def z2(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #2 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z2

    @z2.setter
    def z2(self, z2: str | int | float | types.Real) -> None:
        """
        Sets `z2`.

        Parameters:
            z2: Z-axisymmetric point-defined surface point #2 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z2 is not None:
            if isinstance(z2, types.Real):
                z2 = z2
            elif isinstance(z2, int) or isinstance(z2, float):
                z2 = types.Real(z2)
            elif isinstance(z2, str):
                z2 = types.Real.from_mcnp(z2)

        self._z2: types.Real = z2

    @property
    def r2(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #2 radius

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
            r2: Z-axisymmetric point-defined surface point #2 radius.

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
    def z3(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #3 z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z3

    @z3.setter
    def z3(self, z3: str | int | float | types.Real) -> None:
        """
        Sets `z3`.

        Parameters:
            z3: Z-axisymmetric point-defined surface point #3 z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z3 is not None:
            if isinstance(z3, types.Real):
                z3 = z3
            elif isinstance(z3, int) or isinstance(z3, float):
                z3 = types.Real(z3)
            elif isinstance(z3, str):
                z3 = types.Real.from_mcnp(z3)

        self._z3: types.Real = z3

    @property
    def r3(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #3 radius

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
            r3: Z-axisymmetric point-defined surface point #3 radius.

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

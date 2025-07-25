import re

from . import _option
from ... import types
from ... import errors


class Fic(_option.DataOption):
    """
    Represents INP fic elements.
    """

    _KEYWORD = 'fic'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'x1': types.Real,
        'y1': types.Real,
        'z1': types.Real,
        'ro': types.Real,
        'x2': types.Real,
        'y2': types.Real,
        'z2': types.Real,
        'f1': types.Real,
        'f2': types.Real,
        'f3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Afic(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        suffix: str | int | types.Integer,
        designator: str | types.Designator,
        x1: str | int | float | types.Real,
        y1: str | int | float | types.Real,
        z1: str | int | float | types.Real,
        ro: str | int | float | types.Real,
        x2: str | int | float | types.Real,
        y2: str | int | float | types.Real,
        z2: str | int | float | types.Real,
        f1: str | int | float | types.Real,
        f2: str | int | float | types.Real,
        f3: str | int | float | types.Real,
    ):
        """
        Initializes ``Fic``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            x1: Cylindrical grid center x-coordinate.
            y1: Cylindrical grid center y-coordinate.
            z1: Cylindrical grid center z-coordinate.
            ro: Cylindrical grid exclusion radius.
            x2: Reference direction x-coordinate.
            y2: Reference direction y-coordinate.
            z2: Reference direction z-coordinate.
            f1: Source contributions on/off.
            f2: Radial view of field.
            f3: Contribution offset setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.x1: types.Real = x1
        self.y1: types.Real = y1
        self.z1: types.Real = z1
        self.ro: types.Real = ro
        self.x2: types.Real = x2
        self.y2: types.Real = y2
        self.z2: types.Real = z2
        self.f1: types.Real = f1
        self.f2: types.Real = f2
        self.f3: types.Real = f3

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets ``designator``.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

    @property
    def x1(self) -> types.Real:
        """
        Cylindrical grid center x-coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x1

    @x1.setter
    def x1(self, x1: str | int | float | types.Real) -> None:
        """
        Sets ``x1``.

        Parameters:
            x1: Cylindrical grid center x-coordinate.

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
    def y1(self) -> types.Real:
        """
        Cylindrical grid center y-coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y1

    @y1.setter
    def y1(self, y1: str | int | float | types.Real) -> None:
        """
        Sets ``y1``.

        Parameters:
            y1: Cylindrical grid center y-coordinate.

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
    def z1(self) -> types.Real:
        """
        Cylindrical grid center z-coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z1

    @z1.setter
    def z1(self, z1: str | int | float | types.Real) -> None:
        """
        Sets ``z1``.

        Parameters:
            z1: Cylindrical grid center z-coordinate.

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
    def ro(self) -> types.Real:
        """
        Cylindrical grid exclusion radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ro

    @ro.setter
    def ro(self, ro: str | int | float | types.Real) -> None:
        """
        Sets ``ro``.

        Parameters:
            ro: Cylindrical grid exclusion radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ro is not None:
            if isinstance(ro, types.Real):
                ro = ro
            elif isinstance(ro, int) or isinstance(ro, float):
                ro = types.Real(ro)
            elif isinstance(ro, str):
                ro = types.Real.from_mcnp(ro)

        if ro is None or not (ro == 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ro)

        self._ro: types.Real = ro

    @property
    def x2(self) -> types.Real:
        """
        Reference direction x-coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x2

    @x2.setter
    def x2(self, x2: str | int | float | types.Real) -> None:
        """
        Sets ``x2``.

        Parameters:
            x2: Reference direction x-coordinate.

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

        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x2)

        self._x2: types.Real = x2

    @property
    def y2(self) -> types.Real:
        """
        Reference direction y-coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y2

    @y2.setter
    def y2(self, y2: str | int | float | types.Real) -> None:
        """
        Sets ``y2``.

        Parameters:
            y2: Reference direction y-coordinate.

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

        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y2)

        self._y2: types.Real = y2

    @property
    def z2(self) -> types.Real:
        """
        Reference direction z-coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z2

    @z2.setter
    def z2(self, z2: str | int | float | types.Real) -> None:
        """
        Sets ``z2``.

        Parameters:
            z2: Reference direction z-coordinate.

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

        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z2)

        self._z2: types.Real = z2

    @property
    def f1(self) -> types.Real:
        """
        Source contributions on/off

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._f1

    @f1.setter
    def f1(self, f1: str | int | float | types.Real) -> None:
        """
        Sets ``f1``.

        Parameters:
            f1: Source contributions on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if f1 is not None:
            if isinstance(f1, types.Real):
                f1 = f1
            elif isinstance(f1, int) or isinstance(f1, float):
                f1 = types.Real(f1)
            elif isinstance(f1, str):
                f1 = types.Real.from_mcnp(f1)

        if f1 is None or f1 not in {0, -1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f1)

        self._f1: types.Real = f1

    @property
    def f2(self) -> types.Real:
        """
        Radial view of field

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._f2

    @f2.setter
    def f2(self, f2: str | int | float | types.Real) -> None:
        """
        Sets ``f2``.

        Parameters:
            f2: Radial view of field.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if f2 is not None:
            if isinstance(f2, types.Real):
                f2 = f2
            elif isinstance(f2, int) or isinstance(f2, float):
                f2 = types.Real(f2)
            elif isinstance(f2, str):
                f2 = types.Real.from_mcnp(f2)

        if f2 is None or not (f2 != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f2)

        self._f2: types.Real = f2

    @property
    def f3(self) -> types.Real:
        """
        Contribution offset setting

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._f3

    @f3.setter
    def f3(self, f3: str | int | float | types.Real) -> None:
        """
        Sets ``f3``.

        Parameters:
            f3: Contribution offset setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if f3 is not None:
            if isinstance(f3, types.Real):
                f3 = f3
            elif isinstance(f3, int) or isinstance(f3, float):
                f3 = types.Real(f3)
            elif isinstance(f3, str):
                f3 = types.Real.from_mcnp(f3)

        if f3 is None or f3 not in {0, -1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f3)

        self._f3: types.Real = f3

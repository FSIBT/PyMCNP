import re

from . import _card
from .. import _show
from .. import types
from .. import errors


class Rpp(_card.Card):
    """
    Represents INP `rpp` surface cards.
    """

    _KEYWORD = 'rpp'

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'xmin': types.Real,
        'xmax': types.Real,
        'ymin': types.Real,
        'ymax': types.Real,
        'zmin': types.Real,
        'zmax': types.Real,
    }

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rpp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        xmin: str | int | float | types.Real,
        xmax: str | int | float | types.Real,
        ymin: str | int | float | types.Real,
        ymax: str | int | float | types.Real,
        zmin: str | int | float | types.Real = None,
        zmax: str | int | float | types.Real = None,
        number: types.Integer = None,
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes `Rpp`.

        Parameters:
            xmin: Parallelepiped x termini minimum.
            xmax: Parallelepiped x termini maximum.
            ymin: Parallelepiped y termini minimum.
            ymax: Parallelepiped y termini maximum.
            zmin: Parallelepiped z termini minimum.
            zmax: Parallelepiped z termini maximum.
            number: surface number.
            transform: surface transformation.
            prefix: surface whitebody flag.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None:
            number = next(_card.NUMBER)

        self.xmin: types.Real = xmin
        self.xmax: types.Real = xmax
        self.ymin: types.Real = ymin
        self.ymax: types.Real = ymax
        self.zmin: types.Real = zmin
        self.zmax: types.Real = zmax
        self.transform: types.Integer = transform
        self.number: types.Integer = number
        self.prefix: types.String = prefix

    @property
    def xmin(self) -> types.Real:
        """
        Parallelepiped x termini minimum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xmin

    @xmin.setter
    def xmin(self, xmin: str | int | float | types.Real) -> None:
        """
        Sets `xmin`.

        Parameters:
            xmin: Parallelepiped x termini minimum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xmin is not None:
            if isinstance(xmin, types.Real):
                xmin = xmin
            elif isinstance(xmin, int) or isinstance(xmin, float):
                xmin = types.Real(xmin)
            elif isinstance(xmin, str):
                xmin = types.Real.from_mcnp(xmin)

        if xmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmin)

        self._xmin: types.Real = xmin

    @property
    def xmax(self) -> types.Real:
        """
        Parallelepiped x termini maximum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xmax

    @xmax.setter
    def xmax(self, xmax: str | int | float | types.Real) -> None:
        """
        Sets `xmax`.

        Parameters:
            xmax: Parallelepiped x termini maximum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xmax is not None:
            if isinstance(xmax, types.Real):
                xmax = xmax
            elif isinstance(xmax, int) or isinstance(xmax, float):
                xmax = types.Real(xmax)
            elif isinstance(xmax, str):
                xmax = types.Real.from_mcnp(xmax)

        if xmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmax)

        self._xmax: types.Real = xmax

    @property
    def ymin(self) -> types.Real:
        """
        Parallelepiped y termini minimum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ymin

    @ymin.setter
    def ymin(self, ymin: str | int | float | types.Real) -> None:
        """
        Sets `ymin`.

        Parameters:
            ymin: Parallelepiped y termini minimum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ymin is not None:
            if isinstance(ymin, types.Real):
                ymin = ymin
            elif isinstance(ymin, int) or isinstance(ymin, float):
                ymin = types.Real(ymin)
            elif isinstance(ymin, str):
                ymin = types.Real.from_mcnp(ymin)

        if ymin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ymin)

        self._ymin: types.Real = ymin

    @property
    def ymax(self) -> types.Real:
        """
        Parallelepiped y termini maximum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ymax

    @ymax.setter
    def ymax(self, ymax: str | int | float | types.Real) -> None:
        """
        Sets `ymax`.

        Parameters:
            ymax: Parallelepiped y termini maximum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ymax is not None:
            if isinstance(ymax, types.Real):
                ymax = ymax
            elif isinstance(ymax, int) or isinstance(ymax, float):
                ymax = types.Real(ymax)
            elif isinstance(ymax, str):
                ymax = types.Real.from_mcnp(ymax)

        if ymax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ymax)

        self._ymax: types.Real = ymax

    @property
    def zmin(self) -> types.Real:
        """
        Parallelepiped z termini minimum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zmin

    @zmin.setter
    def zmin(self, zmin: str | int | float | types.Real) -> None:
        """
        Sets `zmin`.

        Parameters:
            zmin: Parallelepiped z termini minimum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zmin is not None:
            if isinstance(zmin, types.Real):
                zmin = zmin
            elif isinstance(zmin, int) or isinstance(zmin, float):
                zmin = types.Real(zmin)
            elif isinstance(zmin, str):
                zmin = types.Real.from_mcnp(zmin)

        self._zmin: types.Real = zmin

    @property
    def zmax(self) -> types.Real:
        """
        Parallelepiped z termini maximum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zmax

    @zmax.setter
    def zmax(self, zmax: str | int | float | types.Real) -> None:
        """
        Sets `zmax`.

        Parameters:
            zmax: Parallelepiped z termini maximum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zmax is not None:
            if isinstance(zmax, types.Real):
                zmax = zmax
            elif isinstance(zmax, int) or isinstance(zmax, float):
                zmax = types.Real(zmax)
            elif isinstance(zmax, str):
                zmax = types.Real.from_mcnp(zmax)

        self._zmax: types.Real = zmax

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rpp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rpp`
        """

        vis = shapes.Parallelipiped(
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
        )

        return vis

    def __and__(a, b):
        """
        Unites `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` union.
        """

        return types.Geometry.from_mcnp(f'{a.number}:{b.number}')

    def __or__(a, b):
        """
        Intersects `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` intersection.
        """

        return types.Geometry.from_mcnp(f'{a.number} {b.number}')

    def __neg__(self):
        """
        Negatives `Surface`.

        Returns:
            `Surface` negative.
        """

        return types.Geometry.from_mcnp(f'-{self.number}')

    def __pos__(self):
        """
        Positives `Surface`.

        Returns:
            `Surface` positive.
        """

        return types.Geometry.from_mcnp(f'+{self.number}')

    def __invert__(self):
        """
        Inverts `Surface`.

        Returns:
            `Surface` complement.
        """

        return types.Geometry.from_mcnp(f'#{self.number}')

    @property
    def number(self) -> types.Integer:
        """
        Surface number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Surface number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)

        if number is None or not (1 <= number <= (99_999_999 if not self.transform else 999)):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)

        self._number: types.Integer = number

    @property
    def transform(self) -> types.Integer:
        """
        Surface transform.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._transform

    @transform.setter
    def transform(self, transform: str | int | types.Integer = None) -> None:
        """
        Sets `transform`.

        Parameters:
            transform: Surface transform.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if transform is not None:
            if isinstance(transform, types.Integer):
                transform = transform
            elif isinstance(transform, int):
                transform = types.Integer(transform)
            elif isinstance(transform, str):
                transform = types.Integer.from_mcnp(transform)

        if transform is not None and not (0 <= transform <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, transform)

        self._transform: types.Integer = transform

    @property
    def prefix(self) -> types.String:
        """
        Surface whitebody/reflecting flag.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Surface whitebody/reflecting flag.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

    def to_mcnp(self):
        """
        Generates INP from `Rpp`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.xmin} {self.xmax} {self.ymin} {self.ymax} {self.zmin if self.zmin is not None else ""} {self.zmax if self.zmax is not None else ""}'
        source = _card.Card._postprocess(source)

        return source

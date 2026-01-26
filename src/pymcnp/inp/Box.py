import re

import numpy

from . import _card
from .. import _show
from .. import types
from .. import errors


class Box(_card.Card):
    """
    Represents INP `box` surface cards.
    """

    _KEYWORD = 'box'

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'a1x': types.Real,
        'a1y': types.Real,
        'a1z': types.Real,
        'a2x': types.Real,
        'a2y': types.Real,
        'a2z': types.Real,
        'a3x': types.Real,
        'a3y': types.Real,
        'a3z': types.Real,
    }

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? box( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        vx: str | int | float | types.Real,
        vy: str | int | float | types.Real,
        vz: str | int | float | types.Real,
        a1x: str | int | float | types.Real,
        a1y: str | int | float | types.Real,
        a1z: str | int | float | types.Real,
        a2x: str | int | float | types.Real,
        a2y: str | int | float | types.Real,
        a2z: str | int | float | types.Real,
        a3x: str | int | float | types.Real,
        a3y: str | int | float | types.Real,
        a3z: str | int | float | types.Real,
        number: types.Integer = None,
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes `Box`.

        Parameters:
            vx: Box macrobody position vector x component.
            vy: Box macrobody position vector y component.
            vz: Box macrobody position vector z component.
            a1x: Box macrobody vector #1 x component.
            a1y: Box macrobody vector #1 y component.
            a1z: Box macrobody vector #1 z component.
            a2x: Box macrobody vector #2 x component.
            a2y: Box macrobody vector #2 y component.
            a2z: Box macrobody vector #2 z component.
            a3x: Box macrobody vector #3 x component.
            a3y: Box macrobody vector #3 y component.
            a3z: Box macrobody vector #3 z component.
            number: surface number.
            transform: surface transformation.
            prefix: surface whitebody flag.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None:
            number = next(_card.NUMBER)

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
        self.a1x: types.Real = a1x
        self.a1y: types.Real = a1y
        self.a1z: types.Real = a1z
        self.a2x: types.Real = a2x
        self.a2y: types.Real = a2y
        self.a2z: types.Real = a2z
        self.a3x: types.Real = a3x
        self.a3y: types.Real = a3y
        self.a3z: types.Real = a3z
        self.transform: types.Integer = transform
        self.number: types.Integer = number
        self.prefix: types.String = prefix

    @property
    def vx(self) -> types.Real:
        """
        Box macrobody position vector x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._vx

    @vx.setter
    def vx(self, vx: str | int | float | types.Real) -> None:
        """
        Sets `vx`.

        Parameters:
            vx: Box macrobody position vector x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if vx is not None:
            if isinstance(vx, types.Real):
                vx = vx
            elif isinstance(vx, int) or isinstance(vx, float):
                vx = types.Real(vx)
            elif isinstance(vx, str):
                vx = types.Real.from_mcnp(vx)

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)

        self._vx: types.Real = vx

    @property
    def vy(self) -> types.Real:
        """
        Box macrobody position vector y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._vy

    @vy.setter
    def vy(self, vy: str | int | float | types.Real) -> None:
        """
        Sets `vy`.

        Parameters:
            vy: Box macrobody position vector y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if vy is not None:
            if isinstance(vy, types.Real):
                vy = vy
            elif isinstance(vy, int) or isinstance(vy, float):
                vy = types.Real(vy)
            elif isinstance(vy, str):
                vy = types.Real.from_mcnp(vy)

        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)

        self._vy: types.Real = vy

    @property
    def vz(self) -> types.Real:
        """
        Box macrobody position vector z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._vz

    @vz.setter
    def vz(self, vz: str | int | float | types.Real) -> None:
        """
        Sets `vz`.

        Parameters:
            vz: Box macrobody position vector z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if vz is not None:
            if isinstance(vz, types.Real):
                vz = vz
            elif isinstance(vz, int) or isinstance(vz, float):
                vz = types.Real(vz)
            elif isinstance(vz, str):
                vz = types.Real.from_mcnp(vz)

        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)

        self._vz: types.Real = vz

    @property
    def a1x(self) -> types.Real:
        """
        Box macrobody vector #1 x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a1x

    @a1x.setter
    def a1x(self, a1x: str | int | float | types.Real) -> None:
        """
        Sets `a1x`.

        Parameters:
            a1x: Box macrobody vector #1 x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a1x is not None:
            if isinstance(a1x, types.Real):
                a1x = a1x
            elif isinstance(a1x, int) or isinstance(a1x, float):
                a1x = types.Real(a1x)
            elif isinstance(a1x, str):
                a1x = types.Real.from_mcnp(a1x)

        if a1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1x)

        self._a1x: types.Real = a1x

    @property
    def a1y(self) -> types.Real:
        """
        Box macrobody vector #1 y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a1y

    @a1y.setter
    def a1y(self, a1y: str | int | float | types.Real) -> None:
        """
        Sets `a1y`.

        Parameters:
            a1y: Box macrobody vector #1 y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a1y is not None:
            if isinstance(a1y, types.Real):
                a1y = a1y
            elif isinstance(a1y, int) or isinstance(a1y, float):
                a1y = types.Real(a1y)
            elif isinstance(a1y, str):
                a1y = types.Real.from_mcnp(a1y)

        if a1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1y)

        self._a1y: types.Real = a1y

    @property
    def a1z(self) -> types.Real:
        """
        Box macrobody vector #1 z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a1z

    @a1z.setter
    def a1z(self, a1z: str | int | float | types.Real) -> None:
        """
        Sets `a1z`.

        Parameters:
            a1z: Box macrobody vector #1 z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a1z is not None:
            if isinstance(a1z, types.Real):
                a1z = a1z
            elif isinstance(a1z, int) or isinstance(a1z, float):
                a1z = types.Real(a1z)
            elif isinstance(a1z, str):
                a1z = types.Real.from_mcnp(a1z)

        if a1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a1z)

        self._a1z: types.Real = a1z

    @property
    def a2x(self) -> types.Real:
        """
        Box macrobody vector #2 x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a2x

    @a2x.setter
    def a2x(self, a2x: str | int | float | types.Real) -> None:
        """
        Sets `a2x`.

        Parameters:
            a2x: Box macrobody vector #2 x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a2x is not None:
            if isinstance(a2x, types.Real):
                a2x = a2x
            elif isinstance(a2x, int) or isinstance(a2x, float):
                a2x = types.Real(a2x)
            elif isinstance(a2x, str):
                a2x = types.Real.from_mcnp(a2x)

        if a2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2x)

        self._a2x: types.Real = a2x

    @property
    def a2y(self) -> types.Real:
        """
        Box macrobody vector #2 y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a2y

    @a2y.setter
    def a2y(self, a2y: str | int | float | types.Real) -> None:
        """
        Sets `a2y`.

        Parameters:
            a2y: Box macrobody vector #2 y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a2y is not None:
            if isinstance(a2y, types.Real):
                a2y = a2y
            elif isinstance(a2y, int) or isinstance(a2y, float):
                a2y = types.Real(a2y)
            elif isinstance(a2y, str):
                a2y = types.Real.from_mcnp(a2y)

        if a2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2y)

        self._a2y: types.Real = a2y

    @property
    def a2z(self) -> types.Real:
        """
        Box macrobody vector #2 z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a2z

    @a2z.setter
    def a2z(self, a2z: str | int | float | types.Real) -> None:
        """
        Sets `a2z`.

        Parameters:
            a2z: Box macrobody vector #2 z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a2z is not None:
            if isinstance(a2z, types.Real):
                a2z = a2z
            elif isinstance(a2z, int) or isinstance(a2z, float):
                a2z = types.Real(a2z)
            elif isinstance(a2z, str):
                a2z = types.Real.from_mcnp(a2z)

        if a2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a2z)

        self._a2z: types.Real = a2z

    @property
    def a3x(self) -> types.Real:
        """
        Box macrobody vector #3 x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a3x

    @a3x.setter
    def a3x(self, a3x: str | int | float | types.Real) -> None:
        """
        Sets `a3x`.

        Parameters:
            a3x: Box macrobody vector #3 x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a3x is not None:
            if isinstance(a3x, types.Real):
                a3x = a3x
            elif isinstance(a3x, int) or isinstance(a3x, float):
                a3x = types.Real(a3x)
            elif isinstance(a3x, str):
                a3x = types.Real.from_mcnp(a3x)

        if a3x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3x)

        self._a3x: types.Real = a3x

    @property
    def a3y(self) -> types.Real:
        """
        Box macrobody vector #3 y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a3y

    @a3y.setter
    def a3y(self, a3y: str | int | float | types.Real) -> None:
        """
        Sets `a3y`.

        Parameters:
            a3y: Box macrobody vector #3 y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a3y is not None:
            if isinstance(a3y, types.Real):
                a3y = a3y
            elif isinstance(a3y, int) or isinstance(a3y, float):
                a3y = types.Real(a3y)
            elif isinstance(a3y, str):
                a3y = types.Real.from_mcnp(a3y)

        if a3y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3y)

        self._a3y: types.Real = a3y

    @property
    def a3z(self) -> types.Real:
        """
        Box macrobody vector #3 z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a3z

    @a3z.setter
    def a3z(self, a3z: str | int | float | types.Real) -> None:
        """
        Sets `a3z`.

        Parameters:
            a3z: Box macrobody vector #3 z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a3z is not None:
            if isinstance(a3z, types.Real):
                a3z = a3z
            elif isinstance(a3z, int) or isinstance(a3z, float):
                a3z = types.Real(a3z)
            elif isinstance(a3z, str):
                a3z = types.Real.from_mcnp(a3z)

        if a3z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, a3z)

        self._a3z: types.Real = a3z

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Box`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Box`.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))
        a3 = numpy.array((float(self.a3x), float(self.a3y), float(self.a3z)))

        cross = numpy.cross(numpy.array((1, 0, 0)), a1)
        angle = numpy.degrees(numpy.arccos(a1[0] / numpy.linalg.norm(a1)))

        vis = shapes.Box(numpy.linalg.norm(a1), numpy.linalg.norm(a2), numpy.linalg.norm(a3))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v + 0.5 * (a1 + a2 + a3))

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
        Generates INP from `Box`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.vx} {self.vy} {self.vz} {self.a1x} {self.a1y} {self.a1z} {self.a2x} {self.a2y} {self.a2z} {self.a3x} {self.a3y} {self.a3z}'
        source = _card.Card._postprocess(source)

        return source

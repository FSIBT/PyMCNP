import re

import numpy

from . import _card
from .. import _show
from .. import types
from .. import errors


class Ell(_card.Card):
    """
    Represents INP `ell` surface cards.
    """

    _KEYWORD = 'ell'

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
        'rm': types.Real,
    }

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? ell( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        v1x: str | int | float | types.Real,
        v1y: str | int | float | types.Real,
        v1z: str | int | float | types.Real,
        v2x: str | int | float | types.Real,
        v2y: str | int | float | types.Real,
        v2z: str | int | float | types.Real,
        rm: str | int | float | types.Real,
        number: types.Integer = None,
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes `Ell`.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.
            v1y: Ellipsoid focus #1 or center y component.
            v1z: Ellipsoid focus #1 or center z component.
            v2x: Ellipsoid focus #2 or major axis x component.
            v2y: Ellipsoid focus #2 or major axis y component.
            v2z: Ellipsoid focus #2 or major axis z component.
            rm: Ellipsoid major/minor axis radius length.
            number: surface number.
            transform: surface transformation.
            prefix: surface whitebody flag.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None:
            number = next(_card.NUMBER)

        self.v1x: types.Real = v1x
        self.v1y: types.Real = v1y
        self.v1z: types.Real = v1z
        self.v2x: types.Real = v2x
        self.v2y: types.Real = v2y
        self.v2z: types.Real = v2z
        self.rm: types.Real = rm
        self.transform: types.Integer = transform
        self.number: types.Integer = number
        self.prefix: types.String = prefix

    @property
    def v1x(self) -> types.Real:
        """
        Ellipsoid focus #1 or center x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._v1x

    @v1x.setter
    def v1x(self, v1x: str | int | float | types.Real) -> None:
        """
        Sets `v1x`.

        Parameters:
            v1x: Ellipsoid focus #1 or center x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if v1x is not None:
            if isinstance(v1x, types.Real):
                v1x = v1x
            elif isinstance(v1x, int) or isinstance(v1x, float):
                v1x = types.Real(v1x)
            elif isinstance(v1x, str):
                v1x = types.Real.from_mcnp(v1x)

        if v1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1x)

        self._v1x: types.Real = v1x

    @property
    def v1y(self) -> types.Real:
        """
        Ellipsoid focus #1 or center y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._v1y

    @v1y.setter
    def v1y(self, v1y: str | int | float | types.Real) -> None:
        """
        Sets `v1y`.

        Parameters:
            v1y: Ellipsoid focus #1 or center y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if v1y is not None:
            if isinstance(v1y, types.Real):
                v1y = v1y
            elif isinstance(v1y, int) or isinstance(v1y, float):
                v1y = types.Real(v1y)
            elif isinstance(v1y, str):
                v1y = types.Real.from_mcnp(v1y)

        if v1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1y)

        self._v1y: types.Real = v1y

    @property
    def v1z(self) -> types.Real:
        """
        Ellipsoid focus #1 or center z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._v1z

    @v1z.setter
    def v1z(self, v1z: str | int | float | types.Real) -> None:
        """
        Sets `v1z`.

        Parameters:
            v1z: Ellipsoid focus #1 or center z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if v1z is not None:
            if isinstance(v1z, types.Real):
                v1z = v1z
            elif isinstance(v1z, int) or isinstance(v1z, float):
                v1z = types.Real(v1z)
            elif isinstance(v1z, str):
                v1z = types.Real.from_mcnp(v1z)

        if v1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1z)

        self._v1z: types.Real = v1z

    @property
    def v2x(self) -> types.Real:
        """
        Ellipsoid focus #2 or major axis x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._v2x

    @v2x.setter
    def v2x(self, v2x: str | int | float | types.Real) -> None:
        """
        Sets `v2x`.

        Parameters:
            v2x: Ellipsoid focus #2 or major axis x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if v2x is not None:
            if isinstance(v2x, types.Real):
                v2x = v2x
            elif isinstance(v2x, int) or isinstance(v2x, float):
                v2x = types.Real(v2x)
            elif isinstance(v2x, str):
                v2x = types.Real.from_mcnp(v2x)

        if v2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2x)

        self._v2x: types.Real = v2x

    @property
    def v2y(self) -> types.Real:
        """
        Ellipsoid focus #2 or major axis y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._v2y

    @v2y.setter
    def v2y(self, v2y: str | int | float | types.Real) -> None:
        """
        Sets `v2y`.

        Parameters:
            v2y: Ellipsoid focus #2 or major axis y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if v2y is not None:
            if isinstance(v2y, types.Real):
                v2y = v2y
            elif isinstance(v2y, int) or isinstance(v2y, float):
                v2y = types.Real(v2y)
            elif isinstance(v2y, str):
                v2y = types.Real.from_mcnp(v2y)

        if v2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2y)

        self._v2y: types.Real = v2y

    @property
    def v2z(self) -> types.Real:
        """
        Ellipsoid focus #2 or major axis z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._v2z

    @v2z.setter
    def v2z(self, v2z: str | int | float | types.Real) -> None:
        """
        Sets `v2z`.

        Parameters:
            v2z: Ellipsoid focus #2 or major axis z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if v2z is not None:
            if isinstance(v2z, types.Real):
                v2z = v2z
            elif isinstance(v2z, int) or isinstance(v2z, float):
                v2z = types.Real(v2z)
            elif isinstance(v2z, str):
                v2z = types.Real.from_mcnp(v2z)

        if v2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2z)

        self._v2z: types.Real = v2z

    @property
    def rm(self) -> types.Real:
        """
        Ellipsoid major/minor axis radius length

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._rm

    @rm.setter
    def rm(self, rm: str | int | float | types.Real) -> None:
        """
        Sets `rm`.

        Parameters:
            rm: Ellipsoid major/minor axis radius length.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if rm is not None:
            if isinstance(rm, types.Real):
                rm = rm
            elif isinstance(rm, int) or isinstance(rm, float):
                rm = types.Real(rm)
            elif isinstance(rm, str):
                rm = types.Real.from_mcnp(rm)

        if rm is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, rm)

        self._rm: types.Real = rm

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ell`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ell`.
        """

        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        if self.rm > 0:
            center = numpy.array(((v2 - v1)[0] / 2 + v1[0], (v2 - v1)[1] / 2 + v1[1], (v2 - v1)[2] / 2 + v1[2]))
            major_length = float(self.rm)
            minor_length = 2 * (((major_length / 2) ** 2 - (numpy.linalg.norm(v2 - v1) / 2) ** 2) ** 0.5)

            if numpy.linalg.norm(v2 - v1):
                cross = numpy.cross(v2 - v1, numpy.array((1, 0, 0)))
                angle = numpy.degrees(numpy.arccos((v2 - v1)[0] / numpy.linalg.norm(v2 - v1)))
            else:
                cross = None
                angle = 0
        if self.rm < 0:
            center = v1
            major_length = numpy.linalg.norm(v2)
            minor_length = -float(self.rm)
            cross = numpy.cross(v2, numpy.array((1, 0, 0)))
            angle = numpy.degrees(numpy.arccos(v2[0] / numpy.linalg.norm(v2)))

        vis = shapes.Ellipsoid(major_length, minor_length)
        if cross is not None:
            vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(center)

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
        Generates INP from `Ell`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.v1x} {self.v1y} {self.v1z} {self.v2x} {self.v2y} {self.v2z} {self.rm}'
        source = _card.Card._postprocess(source)

        return source

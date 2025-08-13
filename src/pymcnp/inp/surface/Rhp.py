import re
import math

import numpy

from . import _option
from ... import _show
from ... import types
from ... import errors


class Rhp(_option.SurfaceOption):
    """
    Represents INP `rhp` elements.
    """

    _KEYWORD = 'rhp'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'r1': types.Real,
        'r2': types.Real,
        'r3': types.Real,
        's1': types.Real,
        's2': types.Real,
        's3': types.Real,
        't1': types.Real,
        't2': types.Real,
        't3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arhp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        vx: str | int | float | types.Real,
        vy: str | int | float | types.Real,
        vz: str | int | float | types.Real,
        hx: str | int | float | types.Real,
        hy: str | int | float | types.Real,
        hz: str | int | float | types.Real,
        r1: str | int | float | types.Real,
        r2: str | int | float | types.Real,
        r3: str | int | float | types.Real,
        s1: str | int | float | types.Real = None,
        s2: str | int | float | types.Real = None,
        s3: str | int | float | types.Real = None,
        t1: str | int | float | types.Real = None,
        t2: str | int | float | types.Real = None,
        t3: str | int | float | types.Real = None,
    ):
        """
        Initializes `Rhp`.

        Parameters:
            vx: Hexagonal prism position vector x component.
            vy: Hexagonal prism position vector y component.
            vz: Hexagonal prism position vector z component.
            hx: Hexagonal prism height vector x component.
            hy: Hexagonal prism height vector y component.
            hz: Hexagonal prism height vector z component.
            r1: Hexagonal prism facet #1 vector x component.
            r2: Hexagonal prism facet #1 vector y component.
            r3: Hexagonal prism facet #1 vector z component.
            s1: Hexagonal prism facet #2 vector x component.
            s2: Hexagonal prism facet #2 vector y component.
            s3: Hexagonal prism facet #2 vector z component.
            t1: Hexagonal prism facet #3 vector x component.
            t2: Hexagonal prism facet #3 vector y component.
            t3: Hexagonal prism facet #3 vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
        self.hx: types.Real = hx
        self.hy: types.Real = hy
        self.hz: types.Real = hz
        self.r1: types.Real = r1
        self.r2: types.Real = r2
        self.r3: types.Real = r3
        self.s1: types.Real = s1
        self.s2: types.Real = s2
        self.s3: types.Real = s3
        self.t1: types.Real = t1
        self.t2: types.Real = t2
        self.t3: types.Real = t3

    @property
    def vx(self) -> types.Real:
        """
        Hexagonal prism position vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vx

    @vx.setter
    def vx(self, vx: str | int | float | types.Real) -> None:
        """
        Sets `vx`.

        Parameters:
            vx: Hexagonal prism position vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
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
        Hexagonal prism position vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vy

    @vy.setter
    def vy(self, vy: str | int | float | types.Real) -> None:
        """
        Sets `vy`.

        Parameters:
            vy: Hexagonal prism position vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
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
        Hexagonal prism position vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vz

    @vz.setter
    def vz(self, vz: str | int | float | types.Real) -> None:
        """
        Sets `vz`.

        Parameters:
            vz: Hexagonal prism position vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
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
    def hx(self) -> types.Real:
        """
        Hexagonal prism height vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hx

    @hx.setter
    def hx(self, hx: str | int | float | types.Real) -> None:
        """
        Sets `hx`.

        Parameters:
            hx: Hexagonal prism height vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hx is not None:
            if isinstance(hx, types.Real):
                hx = hx
            elif isinstance(hx, int) or isinstance(hx, float):
                hx = types.Real(hx)
            elif isinstance(hx, str):
                hx = types.Real.from_mcnp(hx)

        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)

        self._hx: types.Real = hx

    @property
    def hy(self) -> types.Real:
        """
        Hexagonal prism height vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hy

    @hy.setter
    def hy(self, hy: str | int | float | types.Real) -> None:
        """
        Sets `hy`.

        Parameters:
            hy: Hexagonal prism height vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hy is not None:
            if isinstance(hy, types.Real):
                hy = hy
            elif isinstance(hy, int) or isinstance(hy, float):
                hy = types.Real(hy)
            elif isinstance(hy, str):
                hy = types.Real.from_mcnp(hy)

        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)

        self._hy: types.Real = hy

    @property
    def hz(self) -> types.Real:
        """
        Hexagonal prism height vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hz

    @hz.setter
    def hz(self, hz: str | int | float | types.Real) -> None:
        """
        Sets `hz`.

        Parameters:
            hz: Hexagonal prism height vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hz is not None:
            if isinstance(hz, types.Real):
                hz = hz
            elif isinstance(hz, int) or isinstance(hz, float):
                hz = types.Real(hz)
            elif isinstance(hz, str):
                hz = types.Real.from_mcnp(hz)

        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)

        self._hz: types.Real = hz

    @property
    def r1(self) -> types.Real:
        """
        Hexagonal prism facet #1 vector x component

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
            r1: Hexagonal prism facet #1 vector x component.

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
    def r2(self) -> types.Real:
        """
        Hexagonal prism facet #1 vector y component

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
            r2: Hexagonal prism facet #1 vector y component.

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

        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r2)

        self._r2: types.Real = r2

    @property
    def r3(self) -> types.Real:
        """
        Hexagonal prism facet #1 vector z component

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
            r3: Hexagonal prism facet #1 vector z component.

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

        if r3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r3)

        self._r3: types.Real = r3

    @property
    def s1(self) -> types.Real:
        """
        Hexagonal prism facet #2 vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._s1

    @s1.setter
    def s1(self, s1: str | int | float | types.Real) -> None:
        """
        Sets `s1`.

        Parameters:
            s1: Hexagonal prism facet #2 vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if s1 is not None:
            if isinstance(s1, types.Real):
                s1 = s1
            elif isinstance(s1, int) or isinstance(s1, float):
                s1 = types.Real(s1)
            elif isinstance(s1, str):
                s1 = types.Real.from_mcnp(s1)

        self._s1: types.Real = s1

    @property
    def s2(self) -> types.Real:
        """
        Hexagonal prism facet #2 vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._s2

    @s2.setter
    def s2(self, s2: str | int | float | types.Real) -> None:
        """
        Sets `s2`.

        Parameters:
            s2: Hexagonal prism facet #2 vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if s2 is not None:
            if isinstance(s2, types.Real):
                s2 = s2
            elif isinstance(s2, int) or isinstance(s2, float):
                s2 = types.Real(s2)
            elif isinstance(s2, str):
                s2 = types.Real.from_mcnp(s2)

        self._s2: types.Real = s2

    @property
    def s3(self) -> types.Real:
        """
        Hexagonal prism facet #2 vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._s3

    @s3.setter
    def s3(self, s3: str | int | float | types.Real) -> None:
        """
        Sets `s3`.

        Parameters:
            s3: Hexagonal prism facet #2 vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if s3 is not None:
            if isinstance(s3, types.Real):
                s3 = s3
            elif isinstance(s3, int) or isinstance(s3, float):
                s3 = types.Real(s3)
            elif isinstance(s3, str):
                s3 = types.Real.from_mcnp(s3)

        self._s3: types.Real = s3

    @property
    def t1(self) -> types.Real:
        """
        Hexagonal prism facet #3 vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._t1

    @t1.setter
    def t1(self, t1: str | int | float | types.Real) -> None:
        """
        Sets `t1`.

        Parameters:
            t1: Hexagonal prism facet #3 vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if t1 is not None:
            if isinstance(t1, types.Real):
                t1 = t1
            elif isinstance(t1, int) or isinstance(t1, float):
                t1 = types.Real(t1)
            elif isinstance(t1, str):
                t1 = types.Real.from_mcnp(t1)

        self._t1: types.Real = t1

    @property
    def t2(self) -> types.Real:
        """
        Hexagonal prism facet #3 vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._t2

    @t2.setter
    def t2(self, t2: str | int | float | types.Real) -> None:
        """
        Sets `t2`.

        Parameters:
            t2: Hexagonal prism facet #3 vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if t2 is not None:
            if isinstance(t2, types.Real):
                t2 = t2
            elif isinstance(t2, int) or isinstance(t2, float):
                t2 = types.Real(t2)
            elif isinstance(t2, str):
                t2 = types.Real.from_mcnp(t2)

        self._t2: types.Real = t2

    @property
    def t3(self) -> types.Real:
        """
        Hexagonal prism facet #3 vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._t3

    @t3.setter
    def t3(self, t3: str | int | float | types.Real) -> None:
        """
        Sets `t3`.

        Parameters:
            t3: Hexagonal prism facet #3 vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if t3 is not None:
            if isinstance(t3, types.Real):
                t3 = t3
            elif isinstance(t3, int) or isinstance(t3, float):
                t3 = types.Real(t3)
            elif isinstance(t3, str):
                t3 = types.Real.from_mcnp(t3)

        self._t3: types.Real = t3

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rhp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rhp`
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))
        r = numpy.array((float(self.r1), float(self.r2), float(self.r3)))
        s = numpy.array((float(self.s1), float(self.s2), float(self.s3)))
        t = numpy.array((float(self.t1), float(self.t2), float(self.t3)))

        cross = numpy.cross(v, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(v[2] / numpy.linalg.norm(v)))
        apothem_r = numpy.linalg.norm(r) * 2 / math.sqrt(3)
        apothem_s = numpy.linalg.norm(s) * 2 / math.sqrt(3)
        apothem_t = numpy.linalg.norm(t) * 2 / math.sqrt(3)

        vis = shapes.CylinderHexagonal(numpy.linalg.norm(h), apothem_r, apothem_s, apothem_t)
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v)

        return vis

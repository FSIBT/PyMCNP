import numpy

import pymcnp
from .... import classes


class Test_Geometry(classes.Test_FromMcnp):
    element = pymcnp.inp.literal.Geometry
    EXAMPLES_FROM_MCNP_VALID = [
        '7.6(6:((+1 #2):(+3:-4) #5))',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    def test___invert__(self, geometry_a: pymcnp.inp.literal.Geometry) -> None:
        assert str(~geometry_a) == '#(1:(3 #(4 5 6):(6:7) #6))'

    def test_and_intersects_and_or_unites(self) -> None:
        a, _ = pymcnp.inp.literal.Geometry.from_mcnp('-1')
        b, _ = pymcnp.inp.literal.Geometry.from_mcnp('+2')
        c, _ = pymcnp.inp.literal.Geometry.from_mcnp('-3')

        assert str(a & b) == '-1 +2'
        assert str(a | b) == '(-1:+2)'
        assert str((a | b) & c) == '(-1:+2) -3'
        assert str(a & (b | c)) == '-1 (+2:-3)'
        assert str(a | (b & c)) == '(-1:+2 -3)'

        # A top-level union is parenthesized before intersecting.
        d, _ = pymcnp.inp.literal.Geometry.from_mcnp('1:2')
        assert str(d & a) == '(1:2) -1'
        assert str(a & d) == '-1 (1:2)'


POINTS = numpy.array([[0, 0, 0], [1.5, 0, 0], [3, 0, 0]])


def _mask(geometry: str) -> list[bool]:
    # Surface 1 is a sphere of radius 1, surface 2 one of radius 2, and cell 1 is ``-1``.
    one, two = pymcnp.inp.literal.Integer('1'), pymcnp.inp.literal.Integer('2')
    surfaces = {one: pymcnp._show.pyvista.Sphere(1), two: pymcnp._show.pyvista.Sphere(2)}
    cells = {one: surfaces[one]}
    return pymcnp.inp.literal.Geometry.from_mcnp(geometry)[0].to_show(surfaces, cells).cell(POINTS).tolist()


def test_to_show_without_complement() -> None:
    assert _mask('-2') == [True, True, False]
    assert _mask('-1') == [True, False, False]


def test_to_show_complements_cells() -> None:
    assert _mask('-2 #1') == [False, True, False]


def test_to_show_complements_regions() -> None:
    assert _mask('-2 #(-1)') == [False, True, False]
    assert _mask('#(-2)') == [False, False, True]

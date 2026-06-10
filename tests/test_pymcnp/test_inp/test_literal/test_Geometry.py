import pymcnp
from .... import classes


class Test_Geometry(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Geometry
    EXAMPLES_VALID = [
        '7.6(6:((+1 #2):(+3:-4) #5))',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]

    def test___and__(self, geometry_a: pymcnp.inp.literal.Geometry, geometry_b: pymcnp.inp.literal.Geometry) -> None:
        geometry_a & geometry_b

    def test___or__(self, geometry_a: pymcnp.inp.literal.Geometry, geometry_b: pymcnp.inp.literal.Geometry) -> None:
        geometry_a | geometry_b

    def test___invert__(self, geometry_a: pymcnp.inp.literal.Geometry) -> None:
        ~geometry_a

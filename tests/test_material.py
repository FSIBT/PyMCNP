import pymcnp


def test_material():
    material_string = 'M10   48106     -0.0125        $ Cd\n      48108     -0.0089\n      48110     -0.1249\n      48111     -0.128\n      48112     -0.2413\n      48113     -0.1222\n      48114     -0.2873\n      48116     -0.0749'

    mat = pymcnp.inp.M.from_mcnp(material_string)

    assert mat.ident == 'm10'
    assert mat.comment[0] == 'cd'
    assert int(mat.suffix) == 10
    assert str(mat.substances[0].zaid) == '048106'
    assert mat.substances[0].fraction == -0.0125

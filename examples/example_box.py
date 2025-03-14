import pymcnp


def get_inp(radius_air, radius_shield, radius_lead):
    inp = pymcnp.InpBuilder(title='Box Example')

    geometry_air = pymcnp.GeometryBuilder('11')
    geometry_shield = pymcnp.GeometryBuilder('12')
    geometry_lead = pymcnp.GeometryBuilder('13')
    geometry_world = pymcnp.GeometryBuilder('14')

    cell_air = pymcnp.CellBuilder(number=1, material=21, density=0.5, geometry=geometry_air)

    cell_shield = pymcnp.CellBuilder(
        number=2, material=22, density=0.5, geometry=geometry_shield & geometry_air
    )

    cell_lead = pymcnp.CellBuilder(
        number=3, material=23, density=0.5, geometry=geometry_lead & geometry_shield
    )

    cell_world = pymcnp.CellBuilder(number=4, material=0, geometry=geometry_world)

    inp.append(cell_air)
    inp.append(cell_shield)
    inp.append(cell_lead)
    inp.append(cell_world)

    surface_air = pymcnp.SurfaceBuilder(
        number=11,
        mnemonic='rpp',
        parameter=f'{-radius_air} {radius_air} {-radius_air} {radius_air} {-radius_air} {radius_air}',
    )
    surface_shield = pymcnp.SurfaceBuilder(
        number=12,
        mnemonic='rpp',
        parameter=f'{-radius_shield} {radius_shield} {-radius_shield} {radius_shield} {-radius_shield} {radius_shield}',
    )
    surface_lead = pymcnp.SurfaceBuilder(
        number=13,
        mnemonic='rpp',
        parameter=f'{-radius_lead} {radius_lead} {-radius_lead} {radius_lead} {-radius_lead} {radius_lead}',
    )
    surface_world = pymcnp.SurfaceBuilder(
        number=14,
        mnemonic='so',
        parameter=f'{radius_air + radius_shield + radius_lead + 1}',
    )

    inp.append(surface_air)
    inp.append(surface_shield)
    inp.append(surface_lead)
    inp.append(surface_world)

    material_air = pymcnp.DataBuilder.unbuild(
        pymcnp.inp.Data(pymcnp.inp.data.M.from_formula(21, {'N2': 0.8, 'O2': 0.2}))
    )
    material_shield = pymcnp.DataBuilder.unbuild(
        pymcnp.inp.Data(pymcnp.inp.data.M.from_formula(22, {'TiO2': 0.5, 'PbO': 0.5}))
    )
    material_lead = pymcnp.DataBuilder.unbuild(
        pymcnp.inp.Data(pymcnp.inp.data.M.from_formula(23, {'Pb': 1}))
    )

    sdef = pymcnp.DataBuilder(
        mnemonic='sdef',
        parameter='x=0 y=0 z=0 erg=2.2',
    )

    inp.append(material_air)
    inp.append(material_shield)
    inp.append(material_lead)
    inp.append(sdef)

    return inp.build()


inp = get_inp(60, 15, 1)
print(inp)

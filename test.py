import pymcnp


g = pymcnp.GeometryEntryBuilder('2')
co = pymcnp.CellOptionBuilder(mnemonic='imp', designator='n,p', parameter='3.0')
c = pymcnp.CellBuilder(number = 1, material = 0, geometry = g, options=(co,))

s = pymcnp.SurfaceBuilder(number = 2, mnemonic='so', parameter='20')

d = pymcnp.DataBuilder(mnemonic='m', suffix='1', parameter='001001 1')

i = pymcnp.InpBuilder(title='HELLO')
i.append(c)
i.append(s)
i.append(d)

print(i.build().to_mcnp())

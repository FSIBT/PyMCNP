import pymcnp

cell = pymcnp.inp.Cell.from_mcnp('1 2 0.5 +999 imp:p=1')
new_cell = pymcnp.modify(cell, {'number.value': 3})
print(new_cell.to_mcnp())

surface = pymcnp.inp.Surface.from_mcnp('2 SO 4')
new_surface = pymcnp.modify(surface, {'number': pymcnp.utils.types.McnpInteger(4)})
print(new_surface.to_mcnp())

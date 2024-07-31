"""
'strategies'
"""


from typing import *

import hypothesis as hy
import hypothesis.strategies as st 


@st.composite
def fortran_integers(draw, condition = lambda _: True):
	"""
	'fortran_integers'
	"""

	return str(draw(st.integers().filter(condition)))


@st.composite
def fortran_reals(draw, condition = lambda _: True):
	"""
	'fortran_reals'
	"""

	return str(draw(st.floats(allow_nan = False, allow_infinity = False).filter(condition)))


@st.composite
def mcnp_designator(draw, condition = lambda _: True) -> str:
	"""
	'mcnp_designator'
	"""

	return draw(st.sampled_from(DESIGNATORS).filter(condition))


@st.composite
def mcnp_geometries(draw, identifiers, depth = None) -> str:
	"""
	'mcnp_geometries'
	"""

	rule = draw(st.randoms()).randint(0, 5)
	next_depth = depth + 1 if depth is not None else None

	if depth and depth >= 20:
		return f"{draw(identifiers)}"
	elif rule == 0:
		# E -> Terminal
		return f"+{draw(identifiers)}"
	elif rule == 1:
		# E -> Terminal
		return f"-{draw(identifiers)}"
	elif rule == 2:
		# E -> Terminal
		return f"{draw(identifiers)}"
	elif rule == 3:
		# E -> E '#'
		return f"#({draw(mcnp_geometries(identifiers), next_depth)})"
	elif rule == 4:
		# E -> E E ':'
		return f"({draw(mcnp_geometries(identifiers), next_depth)}:{draw(mcnp_geometries(identifiers), next_depth)})"
	elif rule == 5:
		# E -> E E ' '
		return f"({draw(mcnp_geometries(identifiers), next_depth)} {draw(mcnp_geometries(identifiers), next_depth)})"
	else:
		assert False


@st.composite
def mcnp_cells(draw, has_void_material = False):
	"""
	'mcnp_cells'
	"""

	if not has_void_material:
		return (
			draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)), 
			draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)), 
			draw(fortran_reals(lambda f: f != 0)), 
			draw(mcnp_geometries(fortran_integers(lambda i: 1 <= i <= 99_999_999)))
		)
	else:
		return (
			draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)), 
			draw(fortran_integers(lambda i: 0 <= i <= 99_999_999)), 
			draw(fortran_reals(lambda f: f != 0)), 
			draw(mcnp_geometries(fortran_integers(lambda i: 1 <= i <= 99_999_999)))
		)

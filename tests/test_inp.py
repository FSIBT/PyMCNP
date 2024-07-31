"""
'test_inp' tests the INP subpackage.
"""


from typing import *

import pytest
import hypothesis as hy
import hypothesis.strategies as st 

from pymcnp.files.inp.cell import Cell
from pymcnp.files.inp.errors import *
from pymcnp.files.types import *
 
from strategies import *


class TestCell:
	"""
	'TestCell'
	"""
	

	class TestfromMcnp:
		"""
		'TestfromMcnp'
		"""


		@hy.given(cell = mcnp_cells())
		def test_valid(self, cell):
			"""
			'test_valid'
			"""

			number, material, density, geometry = cell

			if material == 0:
				print(f"{number} 0 {geometry}")
			else:
				print(f"{number} {material} {density} {geometry}")	

			inp = Cell().from_mcnp(f"{number} {material} {density} {geometry}" if material else f"{number} 0 {geometry}")

			assert inp.number == int(number)
			assert inp.id == int(number)
			assert inp.material == int(material)
			assert inp.density == (float(density) if int(material) != 0 else None)


		@hy.given(cell = mcnp_cells(has_void_material = False), number = fortran_integers(lambda i: i < 1 or i > 99_999_999))
		def test_invalid_number(self, cell, number: str):
			"""
			'test_invalid_number_range'
			"""

			_, valid_material, valid_density, valid_geometry = cell

			with pytest.raises(INPValueError) as err:
				inp = Cell().from_mcnp(f"{number} {valid_material} {valid_density} {valid_geometry}")

			assert err.value.code == INPValueError.Codes.INVALID_CELL_NUMBER


		@hy.given(cell = mcnp_cells(has_void_material = False), material = fortran_integers(lambda i: i < 0 or i > 99_999_999))
		def test_invalid_material(self, cell, material: str):
			"""
			'test_invalid_material_range'
			"""

			valid_number, _, valid_density, valid_geometry = cell

			with pytest.raises(INPValueError) as err:
				inp = Cell().from_mcnp(f"{valid_number} {material} {valid_density} {valid_geometry}")

			assert err.value.code == INPValueError.Codes.INVALID_CELL_MATERIAL


		@hy.given(cell = mcnp_cells(has_void_material = False), density = st.just(0.0))
		def test_invalid_density(self, cell, density: str):
			"""
			'test_invalid_density'
			"""

			valid_number, valid_material, _, valid_geometry = cell

			with pytest.raises(INPValueError) as err:
				inp = Cell().from_mcnp(f"{valid_number} {valid_material} {density} {valid_geometry}")

			assert err.value.code == INPValueError.Codes.INVALID_CELL_DENSITY


		@hy.given(cell = mcnp_cells(has_void_material = False), geometry=mcnp_geometries(fortran_integers(lambda i: i > 99_999_999), depth = 0))
		def test_invalid_geometry(self, cell, geometry: str):
			"""
			'test_invalid_geometry'
			"""

			valid_number, valid_material, valid_density, _ = cell

			with pytest.raises(INPValueError) as err:
				inp = Cell().from_mcnp(f"{valid_number} {valid_material} {valid_density} {geometry}")

			assert err.value.code == INPValueError.Codes.INVALID_CELL_GEOMETRY


		def test_fuzz(self):
			"""
			'test_fuzz'
			"""

			JUST = (
				# MCNP6 User's Manual [1-9]
				"1 1 -0.9914 -7 imp:n=1",
				"1 0 -7 imp:n=1",
				"1 1 -0.0014 -7",
				"2 2 -7.86 -8",
				"3 3 -1.60 1 -2 -3 4 -5 6 7 8",
				"4 0 -1:2:3:-4:5:-6",
				# MCNP6 User's Manual [3-6]
				"3 0 -1 2 4",
				"5 0 #3",
				"5 0 #(-1 2 -4)",
				"5 0 (+1:-2:+4)",
				# MCNP6 User's Manual [5-2]
				"1 0 -2 1 -3",
				"2 0 -4 3 -5",
				"1 0 -1:-2",
				"2 0 1 2",
				# MCNP6 User's Manual [5-4]
				"1 0 -1 2",
				"2 0 -2 1",
				"3 0 -3 1 2 : -2 -1",
				"4 0 3",
				"3 0 (-3 1 2) : (-2 -1)",
				# MCNP6 User's Manual [5-5]
				"1 0 -1",
				"2 0 -2 1",
				# MCNP6 User's Manual [5-8]
				"3 0 -3 2 (-4:5:-6:7:8:-9)",
				"4 0 3",
				"5 0 4 -5 6 -7 -8 9",
				"3 0 -3 2 #(4 -5 6 -7 -8 9)",
				"3 0 -3 2 #5",
				"3 0 -3 2 (-4:5:-6:7:8:-9)",
				"5 0 -4",
				# MCNP6 User's Manual [5-9]
				"1 0 -2 -3 4 1 5 -6",
				"2 0 -7 -8 9 10 11 -12\n     (2 : 3 : -4 : -1 : -5 : 6)",
				"3 0 -13 -14 15 16 17 -18\n     (7 : 8:-9 : -10 : -11:12)",
				"4 0 13:14:-15 : -16 : -17 : 18",
				"1 0 -1 4",
				"2 0 -2 (1 : -4)",
				"3 0 2",
				"1 0 -1 : -4",
				"2 0 -2 1 4",
				"3 0 2",
				# MCNP6 User's Manual [5-10]
				"9 0 -3 -2 4 1 8 -9",
				"17 0 -5 (3 : -4 : -1 : 2 : 9 -8) : -6 : -7",
				"22 0 5 6 7",
				"9 0 -3 -2 4 1 8 -9",
				"17 0 -5 (3 : -4 : -1 : 2 : 9 : -8) : -6 -7",
				"22 0 5 (6 : 7)",
				# MCNP6 User's Manual [5-11]
				"1 0 1 2 -3 (-4 : -5) -6 7",
				"2 0 -1 : -2 : 3 : 4 5 : 6 : -7",
				"2 0 #1",
				"1 0 -1 2 3 (-4 : -16) 5 -6 (12 : 13 : -14)\n     (10 : -9 : -11 : -7 : 8) 15",
				"2 0 -10 9 11 7 -8 -1 : 2 -12 14 -6 -13 3",
				"3 0 -17 (1 : -2 : -5 : 6 : -3 : -15 : 16 4)",
				"4 0 17",
				# MCNP6 User's Manual [5-13]
				"1 0 (2 -1 -5 (7:8:-6)):(4 -3 5(-6:8:7))",
				"2 0 -8 -6 7",
				"3 0 (-2:1:5) (-4:3:-5)",
				"1 0 (2 -1 -5:4 -3 5) (-6:8:7)",
				# MCNP6 User's Manual [5-14]
				"1 0 1 -2 -23",
				"2 0 -3 25 -24 2",
				"3 0 3 -5 12 -15 16 -11",
				"4 0 5 -6 12 -17 18 -11",
				"5 0 6 -8 12 -13 -19 20",
				"6 0 8 -9 -26",
				"7 0 -12 4 -7 -27",
				"8 0 -12 7 -10 14 -21 22",
				"9 0 2 -3 -25",
				"10 0 (-1:2:23) (3:-25:24:-2)\n     (-3:5:-12:15:-16:11)\n     (-5:6:-12:17:-18:11)\n     (-6:8:-12:13:19:-20)\n     (-8:9:26) (12:-4:7:27)\n     (12:-7:10:-14:21:-22)\n     (-2:3:25) -28",
				"10 0 #1 #2 #3 #4 #5 #6 #7 #8 #9 -28",
			)

			for test in JUST:
				inp = Cell().from_mcnp(test)


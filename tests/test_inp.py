"""
'test_inp' tests the INP subpackage.
"""

import math

import pytest
import hypothesis as hy

from pymcnp.files.inp.cell import Cell
from pymcnp.files.inp.surface import Surface
from pymcnp.files.utils import errors
from pymcnp.files.utils import types

import _strategies as _st

# Test Sizes (HH:MM:SS)
# HY_TRIALS = 1      # 00:00:00
# HY_TRIALS = 10     # 00:00:01
# HY_TRIALS = 100    # 00:00:05
# HY_TRIALS = 1000   # 00:01:00
# HY_TRIALS = 10000  # 00:15:00
# HY_TRIALS = 100000 # ??:??:??

HY_TRIALS = 2000


class TestCell:
    """
    'TestCell'
    """

    class TestfromMcnp:
        """
        'TestfromMcnp'
        """

        @hy.settings(max_examples=math.ceil(HY_TRIALS / 18))
        @hy.given(cell=_st.mcnp_cells(True, True, True, True, True))
        def test_valid(self, cell):
            """
            'test_valid'
            """

            number, material, density, geometry, parameters = cell

            for parameter in parameters:
                keyword, suffix, designator, value = parameter

                parameter_str = keyword

                if suffix is not None:
                    parameter_str += suffix

                if designator is not None:
                    parameter_str += ":" + designator

                parameter_str += "=" + value

                if material != "0":
                    inp = Cell().from_mcnp(f"{number} {material} {density} {geometry} {parameter_str}")
                else:
                    inp = Cell().from_mcnp(f"{number} {material} {geometry} {parameter_str}")

                assert inp.number == int(number)
                assert inp.id == int(number)
                assert inp.material == int(material)
                assert inp.density == (float(density) if int(material) != 0 else None)
                assert inp.options[0].keyword == Cell.CellOption.CellKeyword(keyword)
                assert float(inp.options[0].value) == float(value)

                if suffix is not None:
                    assert inp.options[0].suffix == int(suffix)

                if designator is not None:
                    assert inp.options[0].designator[0] == types.Designator(designator)

        @hy.settings(max_examples=HY_TRIALS)
        @hy.given(cell=_st.mcnp_cells(False, True, True, True, True))
        def test_invalid_number(self, cell):
            """
            'test_invalid_number'
            """

            number, material, density, geometry, parameters = cell

            with pytest.raises(errors.MCNPSemanticError) as err:
                if material != "0":
                    Cell().from_mcnp(f"{number} {material} {density} {geometry}")
                else:
                    Cell().from_mcnp(f"{number} {material} {geometry}")

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_NUMBER

        @hy.settings(max_examples=HY_TRIALS)
        @hy.given(cell=_st.mcnp_cells(True, False, True, True, True))
        def test_invalid_material(self, cell):
            """
            'test_invalid_material'
            """

            number, material, density, geometry, parameters = cell

            with pytest.raises(errors.MCNPSemanticError) as err:
                if material != "0":
                    Cell().from_mcnp(f"{number} {material} {density} {geometry}")
                else:
                    Cell().from_mcnp(f"{number} {material} {geometry}")

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL

        @hy.settings(max_examples=HY_TRIALS)
        @hy.given(cell=_st.mcnp_cells(True, True, False, True, True))
        def test_invalid_density(self, cell):
            """
            'test_invalid_density'
            """

            number, material, density, geometry, parameters = cell

            # Asserting non-void material
            material = str(min(int(material) + 1, 99_999_999))

            with pytest.raises(errors.MCNPSemanticError) as err:
                Cell().from_mcnp(f"{number} {material} {density} {geometry}")

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_DENSITY

        @hy.settings(max_examples=HY_TRIALS)
        @hy.given(cell=_st.mcnp_cells(True, True, True, False, True))
        def test_invalid_geometry(self, cell):
            """
            'test_invalid_geometry'
            """

            number, material, density, geometry, parameters = cell

            with pytest.raises(errors.MCNPSemanticError) as err:
                if material != "0":
                    Cell().from_mcnp(f"{number} {material} {density} {geometry}")
                else:
                    Cell().from_mcnp(f"{number} {material} {geometry}")

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY

        def test_fuzz(self):
            """
            'test_fuzz'
            """

            JUST = (
                # MCNP6 User's Manual [1-7]
                "1 0 -7",
                "2 0 -8",
                # MCNP6 User's Manual [1-8]
                "3 0 1 -2 -3 4 -5 6 7 8",
                "4 0 -1 : 2 : 3 : -4 : 5 : -6",
                # MCNP6 User's Manual [1-10]
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
                # MCNP6 User's Manual [3-14]
                "1 0 1 -2 3",
                # MCNP6 User's Manual [3-23]
                # "3 0 -1.2 -1.1 1.4 -1.5 -1.6 99",
                # "4 0 1.1 -2001.1 -5.3 -5.5 -5.6 -5.4",
                "5 0 -5",
                "1 0 -1",
                # "2 like 1 but trcl = (2 0 0)",
                # "9 0 (-5.1:1.3:2001.1:-99:5.5:5.6) #5",
                # "3 0 5.1 -1.1 -5.3 -5.5 -5.6 99",
                # "3 0 5.1 -1.1 1.4 -5.5 -5.6 -5.4",
                # "3 0 -1.2 -1.1 -5.3 -5.5 -5.6 -5.4",
                # MCNP6 User's Manual [3-30]
                "1 0 -17",
                # "21 like 1 but *trcl=(20 0 0 45 -45 90 135 45 90 90 90 0)",
                # MCNP6 User's Manual [3-33]
                "1 0 1 -2 -3 4 -5 6 fill=1",
                "2 0 -7 1 -3 8 u=1 fill=2 lat=1",
                "3 0 -11 u=-2",
                "4 0 11 u=2",
                "5 0 -1:2:3:-4:5:-6",
                # MCNP6 User's Manual [3-52]
                # "11 1 -18.0 0 u=e10 imp:n=1",
                # "12 0 0 u=e10 imp:n=1",
                # "20 2 -0.001 -2 fill=e10 imp:n=1",
                "21 0 2 imp:n=0",
                # MCNP6 User's Manual [3-53]
                # "10 1 -2.03 0 u=2",
                # "11 1 -2.03 0 u=2",
                # "12 1 -2.03 0 u=2",
                # "13 1 -2.03 0 u=2",
                # "14 1 -2.03 0 u=2",
                # "15 1 -2.03 0 u=2",
                # "21 0 0 u=2",
                "30 0 -99 fill=2",
                "40 0 99",
                # MCNP6 User's Manual [3-?]
                "1 1 -18.7 -1 imp:n=1",
                "2 0 1 imp:n=0",
                # MCNP6 User's Manual [3-108]/[3-111]
                "1 1 -16.654 -1 2 -3",
                "2 0 -4 (1:-2:3)",
                "3 0 4",
                # MCNP6 User's Manual [3-149]
                "999 0 -999",
                # MCNP6 User's Manual [3-195]
                "11 0 -31 u=1 imp:p=1",
                "12 0 31 u=1 imp:p=1",
                "16 0 -32 u=2 imp:p=1",
                "17 0 -33 fill=2 imp:p=1",
                "18 0 33 imp:p=0",
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
                "2 0 -7 -8 9 10 11 -12\n" "     (2 : 3 : -4 : -1 : -5 : 6)",
                "3 0 -13 -14 15 16 17 -18\n" "     (7 : 8:-9 : -10 : -11:12)",
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
                "1 0 -1 2 3 (-4 : -16) 5 -6 (12 : 13 : -14)\n" "     (10 : -9 : -11 : -7 : 8) 15",
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
                "10 0 (-1:2:23) (3:-25:24:-2)\n"
                "     (-3:5:-12:15:-16:11)\n"
                "     (-5:6:-12:17:-18:11)\n"
                "     (-6:8:-12:13:19:-20)\n"
                "     (-8:9:26) (12:-4:7:27)\n"
                "     (12:-7:10:-14:21:-22)\n"
                "     (-2:3:25) -28",
                "10 0 #1 #2 #3 #4 #5 #6 #7 #8 #9 -28",
            )

            for test in JUST:
                Cell().from_mcnp(test)


class TestSurface:
    """
    'TestSurface'
    """

    class TestfromMcnp:
        """
        'TestfromMcnp'
        """

        @hy.settings(max_examples=math.ceil(HY_TRIALS / 78))
        @hy.given(surfaces=_st.mcnp_surfaces(True, True, True))
        def test_valid(self, surfaces):
            """
            'test_valid'
            """

            for surface in surfaces:
                number, transform, mnemonic, entries = surface

                inp = Surface().from_mcnp(f"{number} {mnemonic} {' '.join(entries)}")

                assert inp.number == int(number)
                assert inp.mnemonic == mnemonic

                for param, entry in zip(inp.parameters.values(), entries):
                    assert param == pytest.approx(float(entry), 0.0001)

        @hy.settings(max_examples=math.ceil(HY_TRIALS / 78))
        @hy.given(surfaces=_st.mcnp_surfaces(False, True, True))
        def test_invalid_number(self, surfaces):
            """
            'test_invalid_number'
            """

            for surface in surfaces:
                number, transform, mnemonic, entries = surface

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface().from_mcnp(f"{number} {mnemonic} {' '.join(entries)}")

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER

        @hy.settings(max_examples=math.ceil(HY_TRIALS / 78))
        @hy.given(surfaces=_st.mcnp_surfaces(True, False, True))
        def test_invalid_transformPeriodic(self, surfaces):
            """
            'test_invalid_transformPeriodic'
            """

            for surface in surfaces:
                number, transform, mnemonic, entries = surface

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface().from_mcnp(f"{number} {transform} {mnemonic} {' '.join(entries)}")

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC

        @hy.settings(max_examples=math.ceil(HY_TRIALS / 78))
        @hy.given(surfaces=_st.mcnp_surfaces(True, True, False))
        def test_invalid_mnemonic(self, surfaces):
            """
            'test_invalid_mnemonic'
            """

            for surface in surfaces:
                number, transform, mnemonic, entries = surface

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface().from_mcnp(f"{number} {mnemonic} {' '.join(entries)}")

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC

        def test_fuzz(self):
            """
            'test_fuzz'
            """

            JUST = (
                # MCNP6 User's Manual [1-11/17]
                "1 pz -5",
                "2 pz 5",
                "3 py 5",
                "4 py -5",
                "5 px 5",
                "6 px -5",
                "7 S 0 -4 -2.5 0.5",
                "8 S 0 4 4 0.5",
                # MCNP6 User's Manual [3-11]
                "1 py 3",
                "3 k/y 0 0 2 0.25 1",
                # MCNP6 User's Manual [3-12]
                "11 gq 1 0.25 0.75 0 -0.866\n" "     0 -12 -2 3.464 39",
                "11 7 CX 1",
                # MCNP6 User's Manual [3-13]
                "12 X 7 5 3 2 4 3",
                "12 SQ -0.083333333 1 1 0 0 0 68.52083 -26.5 0 0",
                "12 Y 1 2 1 3 3 4",
                "12 Y 3 0 4 1 5 0",
                "12 Z 1 0 2 1 3 4",
                "12 Z 2 1 3 4 5 9.380832",
                # MCNP6 User's Manual [3-14]
                "1 Y -3 2 3 1",
                "2 Y 2 3 3 3 4 2",
                "3 Y 2 1 3 1 4 2",
                # MCNP6 User's Manual [3-16]
                "7 BOX -1 -1 -1 2 0 0 0 2 0 0 0 2",
                "7 RPP -1 1 -1 1 -1 1",
                # MCNP6 User's Manual [3-17]
                "7 RCC 0 -5 0 0 10 0 4",
                # MCNP6 User's Manual [3-18]
                "7 RHP 0 0 -4 0 0 8 0 2 0",
                "7 REC 0 -5 0 0 10 0 4 0 0 2",
                # MCNP6 User's Manual [3-19]
                "7 TRC -5 0 0 10 0 0 4 2",
                "7 ELL 0 0 -2 0 0 2 6",
                "7 ELL 0 0 0 0 0 3 -2",
                # MCNP6 User's Manual [3-20]
                "7 WED 0 0 -6 4 0 0 0 3 0 0 0 12",
                # MCNP6 User's Manual [3-21]
                "7 ARB -5 -10 -5 -5 -10 5 5 -10 -5 5 -10 5 &\n"
                "     0 12 0 0 0 0 0 0 0 0 0 0 &\n"
                "     1234 1250 1350 2450 3450 0",
                # MCNP6 User's Manual [3-23]
                "5 rpp -2 0 -2 0 -1 1",
                "1 rpp 0 2 0 2 -1 1",
                "99 py -2",
                # MCNP6 User's Manual [3-28]
                "17 4 RCC 0 0 0 0 12 0 5",
                "11 4 px 5",
                # MCNP6 User's Manual [3-29]
                "11 py 4.1",
                # MCNP6 User's Manual [3-33]
                "1 px 0",
                "2 px 50",
                "3 py 10",
                "4 py -10",
                "5 pz 5",
                "6 pz -5",
                "7 px 10",
                "8 py 0",
                "10 py 10",
                "11 s 5 5 0 4",
                # MCNP6 User's Manual [3-34]/[3-36]
                "20 rpp 0 50 -10 10 -5 5",
                # "30 rpp 0 10 0 10",
                "11 s 5 5 0 4",
                # MCNP6 User's Manual [3-45]
                "1 rpp -10 10 -10 10 -10 10",
                # MCNP6 User's Manual [3-52]
                "2 so 17.4",
                # MCNP6 User's Manual [3-52]
                "99 sph 0. 0. 3. 10.",
                # MCNP6 User's Manual [3-108]
                "1 cz 4.0",
                "2 pz -1.0",
                "3 pz 1.0",
                "4 so 50.0",
                # MCNP6 User's Manual [3-149]
                "999 sq 25 100 0 0 0 0 -4 0 0 0",
                # MCNP6 User's Manual [3-195]
                "31 sph 0 0 0 .5",
                "32 rpp -1 1 -1 1 -1 1",
                "33 rpp -21 21 -21 21 -21 21",
            )

            for test in JUST:
                Surface().from_mcnp(test)

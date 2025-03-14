import pymcnp
import _utils


class Test_Surface:
    """
    Tests ``Surface``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``Surface.from_mcnp``.
        """

        element = pymcnp.inp.Surface
        EXAMPLES_VALID = [
            '1 PY 3',
            '3 K/Y 0 0 2 0.25 1',
            '11 GQ 1 0.25 0.75 0 -0.866 0 -12 -2 3.464 39',
            '11 7 CX 1',
            '12 X 7 5 3 2 4 3',
            '12 Y 1 2 1 3 3 4',
            '12 Y 3 0 4 1 5 0',
            '12 Z 1 0 2 1 3 4',
            '12 Z 2 1 3 4 5 9.380832',
            '5 rpp -2 0 -2 0 -1 1',
            '1 rpp 0 2 0 2 -1 1',
            '99 py -2',
            '17 4 RCC 0 0 0 0 12 0 5',
            '11 4 PX 5',
            '11 PY 4.1',
            '1 px 0',
            '2 px 50',
            '3 py 10',
            '4 py -10',
            '5 pz 5',
            '6 pz -5',
            '7 px 10',
            '8 py 0',
            '10 py 10',
            '11 s 5 5 0 4',
            '11 s 5 5 0 4',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceP_0:
    """
    Tests ``SurfaceP_0``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceP_0.from_mcnp``.
        """

        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceP_1:
    """
    Tests ``SurfaceP_1``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceP_1.from_mcnp``.
        """

        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfacePx:
    """
    Tests ``SurfacePx``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfacePx.from_mcnp``.
        """

        element = pymcnp.inp.surface.Px
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfacePy:
    """
    Tests ``SurfacePy``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfacePy.from_mcnp``.
        """

        element = pymcnp.inp.surface.Py
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfacePz:
    """
    Tests ``SurfacePz``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfacePz.from_mcnp``.
        """

        element = pymcnp.inp.surface.Pz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceSo:
    """
    Tests ``SurfaceSo``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceSo.from_mcnp``.
        """

        element = pymcnp.inp.surface.So
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceS:
    """
    Tests ``SurfaceS``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceS.from_mcnp``.
        """

        element = pymcnp.inp.surface.S
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceSx:
    """
    Tests ``SurfaceSx``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceSx.from_mcnp``.
        """

        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceSy:
    """
    Tests ``SurfaceSy``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceSy.from_mcnp``.
        """

        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceSz:
    """
    Tests ``SurfaceSz``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceSz.from_mcnp``.
        """

        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceC_x:
    """
    Tests ``SurfaceC_x``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceC_x.from_mcnp``.
        """

        element = pymcnp.inp.surface.C_x
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceC_y:
    """
    Tests ``SurfaceC_y``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceC_y.from_mcnp``.
        """

        element = pymcnp.inp.surface.C_y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceC_z:
    """
    Tests ``SurfaceC_z``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceC_z.from_mcnp``.
        """

        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceCx:
    """
    Tests ``SurfaceCx``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceCx.from_mcnp``.
        """

        element = pymcnp.inp.surface.Cx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceCy:
    """
    Tests ``SurfaceCy``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceCy.from_mcnp``.
        """

        element = pymcnp.inp.surface.Cy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceCz:
    """
    Tests ``SurfaceCz``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceCz.from_mcnp``.
        """

        element = pymcnp.inp.surface.Cz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceK_x:
    """
    Tests ``SurfaceK_x``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceK_x.from_mcnp``.
        """

        element = pymcnp.inp.surface.K_x
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceK_y:
    """
    Tests ``SurfaceK_y``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceK_y.from_mcnp``.
        """

        element = pymcnp.inp.surface.K_y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceK_z:
    """
    Tests ``SurfaceK_z``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceK_z.from_mcnp``.
        """

        element = pymcnp.inp.surface.K_z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceKx:
    """
    Tests ``SurfaceKx``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceKx.from_mcnp``.
        """

        element = pymcnp.inp.surface.Kx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceKy:
    """
    Tests ``SurfaceKy``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceKy.from_mcnp``.
        """

        element = pymcnp.inp.surface.Ky
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceKz:
    """
    Tests ``SurfaceKz``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceKz.from_mcnp``.
        """

        element = pymcnp.inp.surface.Kz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceSq:
    """
    Tests ``SurfaceSq``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceSq.from_mcnp``.
        """

        element = pymcnp.inp.surface.Sq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceGq:
    """
    Tests ``SurfaceGq``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceGq.from_mcnp``.
        """

        element = pymcnp.inp.surface.Gq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceTx:
    """
    Tests ``SurfaceTx``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceTx.from_mcnp``.
        """

        element = pymcnp.inp.surface.Tx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceTy:
    """
    Tests ``SurfaceTy``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceTy.from_mcnp``.
        """

        element = pymcnp.inp.surface.Ty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceTz:
    """
    Tests ``SurfaceTz``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceTz.from_mcnp``.
        """

        element = pymcnp.inp.surface.Tz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceX:
    """
    Tests ``SurfaceX``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceX.from_mcnp``.
        """

        element = pymcnp.inp.surface.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceY:
    """
    Tests ``SurfaceY``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceY.from_mcnp``.
        """

        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceZ:
    """
    Tests ``SurfaceZ``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceZ.from_mcnp``.
        """

        element = pymcnp.inp.surface.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceBox:
    """
    Tests ``SurfaceBox``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceBox.from_mcnp``.
        """

        element = pymcnp.inp.surface.Box
        EXAMPLES_VALID = [
            'BOX -1 -1 -1 2 0 0 0 2 0 0 0 2',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceRpp:
    """
    Tests ``SurfaceRpp``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceRpp.from_mcnp``.
        """

        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = [
            'RPP -1 1 -1 1 -1 1',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceSph:
    """
    Tests ``SurfaceSph``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceSph.from_mcnp``.
        """

        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceRcc:
    """
    Tests ``SurfaceRcc``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceRcc.from_mcnp``.
        """

        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = [
            'RCC 0 -5 0 0 10 0 4',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceRhp:
    """
    Tests ``SurfaceRhp``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceRhp.from_mcnp``.
        """

        element = pymcnp.inp.surface.Rhp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceRec:
    """
    Tests ``SurfaceRec``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceRec.from_mcnp``.
        """

        element = pymcnp.inp.surface.Rec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SurfaceTrc:
    """
    Tests ``SurfaceTrc``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceTrc.from_mcnp``.
        """

        element = pymcnp.inp.surface.Trc
        EXAMPLES_VALID = [
            'TRC -5 0 0 10 0 0 4 2',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceEll:
    """
    Tests ``SurfaceEll``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceEll.from_mcnp``.
        """

        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = [
            'ELL 0. 0. -2.236068 0. 0. 2.236068 3.',
            'ELL 0. 0. 0. 0. 0. 3. -2',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceWed:
    """
    Tests ``SurfaceWed``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceWed.from_mcnp``.
        """

        element = pymcnp.inp.surface.Wed
        EXAMPLES_VALID = [
            'WED 0 0 -6 4 0 0 0 3 0 0 0 12',
        ]
        EXAMPLES_INVALID = []


class Test_SurfaceArb:
    """
    Tests ``SurfaceArb``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        """
        Tests ``SurfaceArb.from_mcnp``.
        """

        element = pymcnp.inp.surface.Arb
        EXAMPLES_VALID = [
            'ARB -5 -10 -5 -5 -10 5 5 -10 -5 5 -10 5 &\n     0 12 0 0 0 0 0 0 0 0 0 0 &\n     1234 1250 1350 2450 3450 0',
        ]
        EXAMPLES_INVALID = []

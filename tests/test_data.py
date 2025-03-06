import pymcnp

import pytest


class _Test_FromMcnp:
    """
    Tests ``McnpElement_.from_mcnp``.
    """

    element: pymcnp.utils._object.McnpElement_
    EXAMPLE_VALID: list[str]
    EXAMPLE_INVALID: list[str]

    def test_valid(self):
        """
        Tests ``EXAMPLES_VALID``.
        """

        for example in self.EXAMPLES_VALID:
            self.element.from_mcnp(example)

    def test_invalid(self):
        """
        Tests ``EXAMPLES_INVALID``.
        """

        for example in self.EXAMPLES_INVALID:
            with pytest.raises(pymcnp.utils.errors.InpError):
                self.element.from_mcnp(example)


class Test_Data:
    """
    Tests ``Data``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``Data.from_mcnp``.
        """

        element = pymcnp.inp.Data
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataVol:
    """
    Tests ``DataVol``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataVol.from_mcnp``.
        """

        element = pymcnp.inp.data.Vol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataArea:
    """
    Tests ``DataArea``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataArea.from_mcnp``.
        """

        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTr:
    """
    Tests ``DataTr``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataTr.from_mcnp``.
        """

        element = pymcnp.inp.data.Tr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataU:
    """
    Tests ``DataU``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataU.from_mcnp``.
        """

        element = pymcnp.inp.data.U
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLat:
    """
    Tests ``DataLat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLat.from_mcnp``.
        """

        element = pymcnp.inp.data.Lat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFill:
    """
    Tests ``DataFill``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFill.from_mcnp``.
        """

        element = pymcnp.inp.data.Fill
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataUran:
    """
    Tests ``DataUran``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataUran.from_mcnp``.
        """

        element = pymcnp.inp.data.Uran
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDm:
    """
    Tests ``DataDm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDm.from_mcnp``.
        """

        element = pymcnp.inp.data.Dm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDawwg:
    """
    Tests ``DataDawwg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDawwg.from_mcnp``.
        """

        element = pymcnp.inp.data.Dawwg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DawwgPoints:
    """
    Tests ``DawwgPoints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DawwgPoints.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.Points
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DawwgXsec:
    """
    Tests ``DawwgXsec``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DawwgXsec.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.Xsec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DawwgBlock:
    """
    Tests ``DawwgBlock``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DawwgBlock.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.Block
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNgroup:
    """
    Tests ``BlockNgroup``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNgroup.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ngroup
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIsn:
    """
    Tests ``BlockIsn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIsn.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Isn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNiso:
    """
    Tests ``BlockNiso``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNiso.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Niso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockMt:
    """
    Tests ``BlockMt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockMt.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIquad:
    """
    Tests ``BlockIquad``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIquad.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Iquad
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFmmix:
    """
    Tests ``BlockFmmix``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockFmmix.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Fmmix
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNosolv:
    """
    Tests ``BlockNosolv``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNosolv.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Nosolv
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoedit:
    """
    Tests ``BlockNoedit``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNoedit.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Noedit
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNogeod:
    """
    Tests ``BlockNogeod``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNogeod.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Nogeod
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNomix:
    """
    Tests ``BlockNomix``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNomix.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Nomix
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoasg:
    """
    Tests ``BlockNoasg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNoasg.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Noasg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNomacr:
    """
    Tests ``BlockNomacr``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNomacr.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Nomacr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoslnp:
    """
    Tests ``BlockNoslnp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNoslnp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Noslnp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoedtt:
    """
    Tests ``BlockNoedtt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNoedtt.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Noedtt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoadjm:
    """
    Tests ``BlockNoadjm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNoadjm.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Noadjm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockLib:
    """
    Tests ``BlockLib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockLib.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Lib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockLibname:
    """
    Tests ``BlockLibname``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockLibname.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFissneut:
    """
    Tests ``BlockFissneut``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockFissneut.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Fissneut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockLng:
    """
    Tests ``BlockLng``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockLng.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Lng
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockBalxs:
    """
    Tests ``BlockBalxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockBalxs.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Balxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNtichi:
    """
    Tests ``BlockNtichi``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNtichi.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ntichi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIevt:
    """
    Tests ``BlockIevt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIevt.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ievt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIsct:
    """
    Tests ``BlockIsct``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIsct.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Isct
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIth:
    """
    Tests ``BlockIth``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIth.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ith
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTrcor:
    """
    Tests ``BlockTrcor``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockTrcor.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Trcor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbl:
    """
    Tests ``BlockIbl``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIbl.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ibl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbr:
    """
    Tests ``BlockIbr``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIbr.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ibr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbt:
    """
    Tests ``BlockIbt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIbt.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ibt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbb:
    """
    Tests ``BlockIbb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIbb.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ibb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbfrnt:
    """
    Tests ``BlockIbfrnt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIbfrnt.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ibfrnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbback:
    """
    Tests ``BlockIbback``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockIbback.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ibback
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockEpsi:
    """
    Tests ``BlockEpsi``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockEpsi.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Epsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockOitm:
    """
    Tests ``BlockOitm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockOitm.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Oitm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNosigf:
    """
    Tests ``BlockNosigf``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNosigf.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Nosigf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockSrcacc:
    """
    Tests ``BlockSrcacc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockSrcacc.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Srcacc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockDiffsol:
    """
    Tests ``BlockDiffsol``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockDiffsol.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Diffsol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsasn:
    """
    Tests ``BlockTsasn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockTsasn.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Tsasn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsaepsi:
    """
    Tests ``BlockTsaepsi``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockTsaepsi.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Tsaepsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsaits:
    """
    Tests ``BlockTsaits``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockTsaits.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Tsaits
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsabeta:
    """
    Tests ``BlockTsabeta``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockTsabeta.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Tsabeta
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockPtconv:
    """
    Tests ``BlockPtconv``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockPtconv.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ptconv
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNorm:
    """
    Tests ``BlockNorm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockNorm.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Norm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockXsectp:
    """
    Tests ``BlockXsectp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockXsectp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Xsectp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFissrp:
    """
    Tests ``BlockFissrp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockFissrp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Fissrp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockSourcp:
    """
    Tests ``BlockSourcp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockSourcp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Sourcp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAngp:
    """
    Tests ``BlockAngp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAngp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Angp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockBalp:
    """
    Tests ``BlockBalp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockBalp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Balp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRaflux:
    """
    Tests ``BlockRaflux``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockRaflux.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Raflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRmflux:
    """
    Tests ``BlockRmflux``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockRmflux.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Rmflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAvatar:
    """
    Tests ``BlockAvatar``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAvatar.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Avatar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsleft:
    """
    Tests ``BlockAsleft``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAsleft.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Asleft
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsrite:
    """
    Tests ``BlockAsrite``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAsrite.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Asrite
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsbott:
    """
    Tests ``BlockAsbott``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAsbott.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Asbott
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAstop:
    """
    Tests ``BlockAstop``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAstop.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Astop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsfrnt:
    """
    Tests ``BlockAsfrnt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAsfrnt.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Asfrnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsback:
    """
    Tests ``BlockAsback``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAsback.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Asback
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockMassed:
    """
    Tests ``BlockMassed``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockMassed.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Massed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockPted:
    """
    Tests ``BlockPted``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockPted.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Pted
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockZned:
    """
    Tests ``BlockZned``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockZned.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Zned
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRzflux:
    """
    Tests ``BlockRzflux``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockRzflux.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Rzflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRzmflux:
    """
    Tests ``BlockRzmflux``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockRzmflux.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Rzmflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockEdoutf:
    """
    Tests ``BlockEdoutf``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockEdoutf.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Edoutf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockByvolp:
    """
    Tests ``BlockByvolp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockByvolp.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Byvolp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAjed:
    """
    Tests ``BlockAjed``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockAjed.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Ajed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFluxone:
    """
    Tests ``BlockFluxone``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BlockFluxone.from_mcnp``.
        """

        element = pymcnp.inp.data.dawwg.block.Fluxone
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbed:
    """
    Tests ``DataEmbed``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbed.from_mcnp``.
        """

        element = pymcnp.inp.data.Embed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedBackground:
    """
    Tests ``EmbedBackground``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedBackground.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Background
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMeshgeo:
    """
    Tests ``EmbedMeshgeo``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedMeshgeo.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Meshgeo
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMgeoin:
    """
    Tests ``EmbedMgeoin``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedMgeoin.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Mgeoin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMeeout:
    """
    Tests ``EmbedMeeout``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedMeeout.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMeein:
    """
    Tests ``EmbedMeein``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedMeein.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Meein
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedCalcvols:
    """
    Tests ``EmbedCalcvols``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedCalcvols.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Calcvols
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedDebug:
    """
    Tests ``EmbedDebug``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedDebug.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Debug
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedFiletype:
    """
    Tests ``EmbedFiletype``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedFiletype.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedGmvfile:
    """
    Tests ``EmbedGmvfile``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedGmvfile.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Gmvfile
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedLength:
    """
    Tests ``EmbedLength``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedLength.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Length
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMcnpumfile:
    """
    Tests ``EmbedMcnpumfile``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbedMcnpumfile.from_mcnp``.
        """

        element = pymcnp.inp.data.embed.Mcnpumfile
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbee:
    """
    Tests ``DataEmbee``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbee.from_mcnp``.
        """

        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeEmbed:
    """
    Tests ``EmbeeEmbed``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeEmbed.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Embed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeEnergy:
    """
    Tests ``EmbeeEnergy``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeEnergy.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Energy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeTime:
    """
    Tests ``EmbeeTime``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeTime.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Time
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeAtom:
    """
    Tests ``EmbeeAtom``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeAtom.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Atom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeFactor:
    """
    Tests ``EmbeeFactor``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeFactor.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeList:
    """
    Tests ``EmbeeList``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeList.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.List
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeMat:
    """
    Tests ``EmbeeMat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeMat.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeMtype:
    """
    Tests ``EmbeeMtype``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``EmbeeMtype.from_mcnp``.
        """

        element = pymcnp.inp.data.embee.Mtype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbeb:
    """
    Tests ``DataEmbeb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbeb.from_mcnp``.
        """

        element = pymcnp.inp.data.Embeb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbem:
    """
    Tests ``DataEmbem``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbem.from_mcnp``.
        """

        element = pymcnp.inp.data.Embem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbtb:
    """
    Tests ``DataEmbtb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbtb.from_mcnp``.
        """

        element = pymcnp.inp.data.Embtb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbtm:
    """
    Tests ``DataEmbtm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbtm.from_mcnp``.
        """

        element = pymcnp.inp.data.Embtm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbdb:
    """
    Tests ``DataEmbdb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbdb.from_mcnp``.
        """

        element = pymcnp.inp.data.Embdb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbdf:
    """
    Tests ``DataEmbdf``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEmbdf.from_mcnp``.
        """

        element = pymcnp.inp.data.Embdf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataM:
    """
    Tests ``DataM``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataM.from_mcnp``.
        """

        element = pymcnp.inp.data.M
        EXAMPLES_VALID = [
            'M10   48106     -0.0125        $ Cd\n      48108     -0.0089\n      48110     -0.1249\n      48111     -0.128\n      48112     -0.2413\n      48113     -0.1222\n      48114     -0.2873\n      48116     -0.0749',
            'm1 001001 -0.999885 001002 -0.000115',
        ]
        EXAMPLES_INVALID = []


class Test_MGas:
    """
    Tests ``MGas``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MGas.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Gas
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MEstep:
    """
    Tests ``MEstep``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MEstep.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Estep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MHstep:
    """
    Tests ``MHstep``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MHstep.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Hstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MNlib:
    """
    Tests ``MNlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MNlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Nlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MPlib:
    """
    Tests ``MPlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MPlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Plib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MPnlib:
    """
    Tests ``MPnlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MPnlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Pnlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MElib:
    """
    Tests ``MElib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MElib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Elib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MHlib:
    """
    Tests ``MHlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MHlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Hlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MAlib:
    """
    Tests ``MAlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MAlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Alib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MSlib:
    """
    Tests ``MSlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MSlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Slib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MTlib:
    """
    Tests ``MTlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MTlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Tlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MDlib:
    """
    Tests ``MDlib``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MDlib.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Dlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MCond:
    """
    Tests ``MCond``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MCond.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Cond
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MRefi:
    """
    Tests ``MRefi``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MRefi.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Refi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MRefc:
    """
    Tests ``MRefc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MRefc.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Refc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MRefs:
    """
    Tests ``MRefs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MRefs.from_mcnp``.
        """

        element = pymcnp.inp.data.m.Refs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMt:
    """
    Tests ``DataMt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataMt.from_mcnp``.
        """

        element = pymcnp.inp.data.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMx:
    """
    Tests ``DataMx``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataMx.from_mcnp``.
        """

        element = pymcnp.inp.data.Mx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataOtfdb:
    """
    Tests ``DataOtfdb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataOtfdb.from_mcnp``.
        """

        element = pymcnp.inp.data.Otfdb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTotnu:
    """
    Tests ``DataTotnu``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataTotnu.from_mcnp``.
        """

        element = pymcnp.inp.data.Totnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataNonu:
    """
    Tests ``DataNonu``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataNonu.from_mcnp``.
        """

        element = pymcnp.inp.data.Nonu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataAwtab:
    """
    Tests ``DataAwtab``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataAwtab.from_mcnp``.
        """

        element = pymcnp.inp.data.Awtab
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataXs:
    """
    Tests ``DataXs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataXs.from_mcnp``.
        """

        element = pymcnp.inp.data.Xs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataVoid:
    """
    Tests ``DataVoid``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataVoid.from_mcnp``.
        """

        element = pymcnp.inp.data.Void
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMgopt:
    """
    Tests ``DataMgopt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataMgopt.from_mcnp``.
        """

        element = pymcnp.inp.data.Mgopt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDrxs:
    """
    Tests ``DataDrxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDrxs.from_mcnp``.
        """

        element = pymcnp.inp.data.Drxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMode:
    """
    Tests ``DataMode``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataMode.from_mcnp``.
        """

        element = pymcnp.inp.data.Mode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_0:
    """
    Tests ``DataPhys_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPhys_0.from_mcnp``.
        """

        element = pymcnp.inp.data.Phys_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_1:
    """
    Tests ``DataPhys_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPhys_1.from_mcnp``.
        """

        element = pymcnp.inp.data.Phys_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_2:
    """
    Tests ``DataPhys_2``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPhys_2.from_mcnp``.
        """

        element = pymcnp.inp.data.Phys_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_3:
    """
    Tests ``DataPhys_3``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPhys_3.from_mcnp``.
        """

        element = pymcnp.inp.data.Phys_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_4:
    """
    Tests ``DataPhys_4``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPhys_4.from_mcnp``.
        """

        element = pymcnp.inp.data.Phys_4
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataAct:
    """
    Tests ``DataAct``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataAct.from_mcnp``.
        """

        element = pymcnp.inp.data.Act
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActFission:
    """
    Tests ``ActFission``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActFission.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActNonfiss:
    """
    Tests ``ActNonfiss``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActNonfiss.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Nonfiss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDn:
    """
    Tests ``ActDn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActDn.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Dn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDg:
    """
    Tests ``ActDg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActDg.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActThresh:
    """
    Tests ``ActThresh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActThresh.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Thresh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDnbais:
    """
    Tests ``ActDnbais``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActDnbais.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Dnbais
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActNap:
    """
    Tests ``ActNap``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActNap.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Nap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDneb:
    """
    Tests ``ActDneb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActDneb.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Dneb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDgeb:
    """
    Tests ``ActDgeb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActDgeb.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Dgeb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActPecut:
    """
    Tests ``ActPecut``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActPecut.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Pecut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActHlcut:
    """
    Tests ``ActHlcut``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActHlcut.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Hlcut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActSample:
    """
    Tests ``ActSample``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``ActSample.from_mcnp``.
        """

        element = pymcnp.inp.data.act.Sample
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCut:
    """
    Tests ``DataCut``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataCut.from_mcnp``.
        """

        element = pymcnp.inp.data.Cut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataElpt:
    """
    Tests ``DataElpt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataElpt.from_mcnp``.
        """

        element = pymcnp.inp.data.Elpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataThtme:
    """
    Tests ``DataThtme``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataThtme.from_mcnp``.
        """

        element = pymcnp.inp.data.Thtme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMphys:
    """
    Tests ``DataMphys``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataMphys.from_mcnp``.
        """

        element = pymcnp.inp.data.Mphys
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLca:
    """
    Tests ``DataLca``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLca.from_mcnp``.
        """

        element = pymcnp.inp.data.Lca
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLcb:
    """
    Tests ``DataLcb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLcb.from_mcnp``.
        """

        element = pymcnp.inp.data.Lcb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLcc:
    """
    Tests ``DataLcc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLcc.from_mcnp``.
        """

        element = pymcnp.inp.data.Lcc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLea:
    """
    Tests ``DataLea``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLea.from_mcnp``.
        """

        element = pymcnp.inp.data.Lea
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLeb:
    """
    Tests ``DataLeb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLeb.from_mcnp``.
        """

        element = pymcnp.inp.data.Leb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFmult:
    """
    Tests ``DataFmult``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFmult.from_mcnp``.
        """

        element = pymcnp.inp.data.Fmult
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultSfnu:
    """
    Tests ``FmultSfnu``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultSfnu.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Sfnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultWidth:
    """
    Tests ``FmultWidth``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultWidth.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Width
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultSfyield:
    """
    Tests ``FmultSfyield``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultSfyield.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Sfyield
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultWatt:
    """
    Tests ``FmultWatt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultWatt.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Watt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultMethod:
    """
    Tests ``FmultMethod``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultMethod.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Method
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultData:
    """
    Tests ``FmultData``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultData.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Data
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultShift:
    """
    Tests ``FmultShift``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmultShift.from_mcnp``.
        """

        element = pymcnp.inp.data.fmult.Shift
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTropt:
    """
    Tests ``DataTropt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataTropt.from_mcnp``.
        """

        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptMcscat:
    """
    Tests ``TroptMcscat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``TroptMcscat.from_mcnp``.
        """

        element = pymcnp.inp.data.tropt.Mcscat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptEloss:
    """
    Tests ``TroptEloss``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``TroptEloss.from_mcnp``.
        """

        element = pymcnp.inp.data.tropt.Eloss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptNreact:
    """
    Tests ``TroptNreact``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``TroptNreact.from_mcnp``.
        """

        element = pymcnp.inp.data.tropt.Nreact
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptNescat:
    """
    Tests ``TroptNescat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``TroptNescat.from_mcnp``.
        """

        element = pymcnp.inp.data.tropt.Nescat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptGenxs:
    """
    Tests ``TroptGenxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``TroptGenxs.from_mcnp``.
        """

        element = pymcnp.inp.data.tropt.Genxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataUnc:
    """
    Tests ``DataUnc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataUnc.from_mcnp``.
        """

        element = pymcnp.inp.data.Unc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCosyp:
    """
    Tests ``DataCosyp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataCosyp.from_mcnp``.
        """

        element = pymcnp.inp.data.Cosyp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCosy:
    """
    Tests ``DataCosy``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataCosy.from_mcnp``.
        """

        element = pymcnp.inp.data.Cosy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataBfld:
    """
    Tests ``DataBfld``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataBfld.from_mcnp``.
        """

        element = pymcnp.inp.data.Bfld
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldField:
    """
    Tests ``BfldField``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldField.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Field
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldVec:
    """
    Tests ``BfldVec``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldVec.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldMaxdeflc:
    """
    Tests ``BfldMaxdeflc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldMaxdeflc.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Maxdeflc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldMaxstep:
    """
    Tests ``BfldMaxstep``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldMaxstep.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Maxstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldAxs:
    """
    Tests ``BfldAxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldAxs.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldFfedges:
    """
    Tests ``BfldFfedges``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldFfedges.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Ffedges
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldRefpnt:
    """
    Tests ``BfldRefpnt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``BfldRefpnt.from_mcnp``.
        """

        element = pymcnp.inp.data.bfld.Refpnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataBflcl:
    """
    Tests ``DataBflcl``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataBflcl.from_mcnp``.
        """

        element = pymcnp.inp.data.Bflcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSdef:
    """
    Tests ``DataSdef``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSdef.from_mcnp``.
        """

        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefCel:
    """
    Tests ``SdefCel``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefCel.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefSur:
    """
    Tests ``SdefSur``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefSur.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Sur
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefErg:
    """
    Tests ``SdefErg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefErg.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTme_0:
    """
    Tests ``SdefTme_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefTme_0.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Tme_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTme_1:
    """
    Tests ``SdefTme_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefTme_1.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefDir:
    """
    Tests ``SdefDir``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefDir.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Dir
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefVec:
    """
    Tests ``SdefVec``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefVec.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefNrm:
    """
    Tests ``SdefNrm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefNrm.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefPos:
    """
    Tests ``SdefPos``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefPos.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Pos
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefRad:
    """
    Tests ``SdefRad``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefRad.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Rad
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefExt:
    """
    Tests ``SdefExt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefExt.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefAxs:
    """
    Tests ``SdefAxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefAxs.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefX:
    """
    Tests ``SdefX``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefX.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefY:
    """
    Tests ``SdefY``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefY.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefZ:
    """
    Tests ``SdefZ``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefZ.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefCcc:
    """
    Tests ``SdefCcc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefCcc.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Ccc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefAra:
    """
    Tests ``SdefAra``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefAra.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Ara
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefWgt:
    """
    Tests ``SdefWgt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefWgt.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Wgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTr_0:
    """
    Tests ``SdefTr_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefTr_0.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTr_1:
    """
    Tests ``SdefTr_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefTr_1.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefEff:
    """
    Tests ``SdefEff``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefEff.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Eff
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefPar:
    """
    Tests ``SdefPar``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefPar.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Par
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefDat:
    """
    Tests ``SdefDat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefDat.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Dat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefLoc:
    """
    Tests ``SdefLoc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefLoc.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefBem:
    """
    Tests ``SdefBem``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefBem.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefBap:
    """
    Tests ``SdefBap``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SdefBap.from_mcnp``.
        """

        element = pymcnp.inp.data.sdef.Bap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSi_0:
    """
    Tests ``DataSi_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSi_0.from_mcnp``.
        """

        element = pymcnp.inp.data.Si_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSi_1:
    """
    Tests ``DataSi_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSi_1.from_mcnp``.
        """

        element = pymcnp.inp.data.Si_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSp_0:
    """
    Tests ``DataSp_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSp_0.from_mcnp``.
        """

        element = pymcnp.inp.data.Sp_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSp_1:
    """
    Tests ``DataSp_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSp_1.from_mcnp``.
        """

        element = pymcnp.inp.data.Sp_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSb_0:
    """
    Tests ``DataSb_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSb_0.from_mcnp``.
        """

        element = pymcnp.inp.data.Sb_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSb_1:
    """
    Tests ``DataSb_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSb_1.from_mcnp``.
        """

        element = pymcnp.inp.data.Sb_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDs_0:
    """
    Tests ``DataDs_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDs_0.from_mcnp``.
        """

        element = pymcnp.inp.data.Ds_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDs_1:
    """
    Tests ``DataDs_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDs_1.from_mcnp``.
        """

        element = pymcnp.inp.data.Ds_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDs_2:
    """
    Tests ``DataDs_2``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDs_2.from_mcnp``.
        """

        element = pymcnp.inp.data.Ds_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSc:
    """
    Tests ``DataSc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSc.from_mcnp``.
        """

        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSsw:
    """
    Tests ``DataSsw``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSsw.from_mcnp``.
        """

        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SswSym:
    """
    Tests ``SswSym``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SswSym.from_mcnp``.
        """

        element = pymcnp.inp.data.ssw.Sym
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SswPty:
    """
    Tests ``SswPty``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SswPty.from_mcnp``.
        """

        element = pymcnp.inp.data.ssw.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SswCel:
    """
    Tests ``SswCel``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SswCel.from_mcnp``.
        """

        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSsr:
    """
    Tests ``DataSsr``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSsr.from_mcnp``.
        """

        element = pymcnp.inp.data.Ssr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrOld:
    """
    Tests ``SsrOld``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrOld.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Old
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrCel:
    """
    Tests ``SsrCel``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrCel.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrNew:
    """
    Tests ``SsrNew``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrNew.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.New
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrPty:
    """
    Tests ``SsrPty``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrPty.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrCol:
    """
    Tests ``SsrCol``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrCol.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Col
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrWgt:
    """
    Tests ``SsrWgt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrWgt.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Wgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrTr_0:
    """
    Tests ``SsrTr_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrTr_0.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrTr_1:
    """
    Tests ``SsrTr_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrTr_1.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrPsc:
    """
    Tests ``SsrPsc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrPsc.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Psc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrAxs:
    """
    Tests ``SsrAxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrAxs.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrExt:
    """
    Tests ``SsrExt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrExt.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrPoa:
    """
    Tests ``SsrPoa``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrPoa.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Poa
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrBcw:
    """
    Tests ``SsrBcw``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``SsrBcw.from_mcnp``.
        """

        element = pymcnp.inp.data.ssr.Bcw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKcode:
    """
    Tests ``DataKcode``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataKcode.from_mcnp``.
        """

        element = pymcnp.inp.data.Kcode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKsrc:
    """
    Tests ``DataKsrc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataKsrc.from_mcnp``.
        """

        element = pymcnp.inp.data.Ksrc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKopts:
    """
    Tests ``DataKopts``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataKopts.from_mcnp``.
        """

        element = pymcnp.inp.data.Kopts
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsBlocksize:
    """
    Tests ``KoptsBlocksize``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsBlocksize.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Blocksize
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsKinetics:
    """
    Tests ``KoptsKinetics``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsKinetics.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Kinetics
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsPrecursor:
    """
    Tests ``KoptsPrecursor``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsPrecursor.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Precursor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsKsental:
    """
    Tests ``KoptsKsental``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsKsental.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmat:
    """
    Tests ``KoptsFmat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmat.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatskpt:
    """
    Tests ``KoptsFmatskpt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatskpt.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatskpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatncyc:
    """
    Tests ``KoptsFmatncyc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatncyc.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatncyc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatspace:
    """
    Tests ``KoptsFmatspace``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatspace.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatspace
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmataccel:
    """
    Tests ``KoptsFmataccel``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmataccel.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmataccel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatreduce:
    """
    Tests ``KoptsFmatreduce``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatreduce.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatreduce
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatnx:
    """
    Tests ``KoptsFmatnx``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatnx.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatnx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatny:
    """
    Tests ``KoptsFmatny``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatny.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatny
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatnz:
    """
    Tests ``KoptsFmatnz``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KoptsFmatnz.from_mcnp``.
        """

        element = pymcnp.inp.data.kopts.Fmatnz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataHsrc:
    """
    Tests ``DataHsrc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataHsrc.from_mcnp``.
        """

        element = pymcnp.inp.data.Hsrc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_0:
    """
    Tests ``DataF_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataF_0.from_mcnp``.
        """

        element = pymcnp.inp.data.F_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_1:
    """
    Tests ``DataF_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataF_1.from_mcnp``.
        """

        element = pymcnp.inp.data.F_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_2:
    """
    Tests ``DataF_2``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataF_2.from_mcnp``.
        """

        element = pymcnp.inp.data.F_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFip:
    """
    Tests ``DataFip``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFip.from_mcnp``.
        """

        element = pymcnp.inp.data.Fip
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFir:
    """
    Tests ``DataFir``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFir.from_mcnp``.
        """

        element = pymcnp.inp.data.Fir
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFic:
    """
    Tests ``DataFic``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFic.from_mcnp``.
        """

        element = pymcnp.inp.data.Fic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_3:
    """
    Tests ``DataF_3``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataF_3.from_mcnp``.
        """

        element = pymcnp.inp.data.F_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFc:
    """
    Tests ``DataFc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFc.from_mcnp``.
        """

        element = pymcnp.inp.data.Fc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataE:
    """
    Tests ``DataE``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataE.from_mcnp``.
        """

        element = pymcnp.inp.data.E
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataT_0:
    """
    Tests ``DataT_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataT_0.from_mcnp``.
        """

        element = pymcnp.inp.data.T_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataT_1:
    """
    Tests ``DataT_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataT_1.from_mcnp``.
        """

        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cbeg:
    """
    Tests ``T_1Cbeg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``T_1Cbeg.from_mcnp``.
        """

        element = pymcnp.inp.data.t_1.Cbeg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cfrq:
    """
    Tests ``T_1Cfrq``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``T_1Cfrq.from_mcnp``.
        """

        element = pymcnp.inp.data.t_1.Cfrq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cofi:
    """
    Tests ``T_1Cofi``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``T_1Cofi.from_mcnp``.
        """

        element = pymcnp.inp.data.t_1.Cofi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Coni:
    """
    Tests ``T_1Coni``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``T_1Coni.from_mcnp``.
        """

        element = pymcnp.inp.data.t_1.Coni
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Csub:
    """
    Tests ``T_1Csub``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``T_1Csub.from_mcnp``.
        """

        element = pymcnp.inp.data.t_1.Csub
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cend:
    """
    Tests ``T_1Cend``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``T_1Cend.from_mcnp``.
        """

        element = pymcnp.inp.data.t_1.Cend
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataC_0:
    """
    Tests ``DataC_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataC_0.from_mcnp``.
        """

        element = pymcnp.inp.data.C_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataC_1:
    """
    Tests ``DataC_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataC_1.from_mcnp``.
        """

        element = pymcnp.inp.data.C_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFq:
    """
    Tests ``DataFq``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFq.from_mcnp``.
        """

        element = pymcnp.inp.data.Fq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDe:
    """
    Tests ``DataDe``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDe.from_mcnp``.
        """

        element = pymcnp.inp.data.De
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDf_0:
    """
    Tests ``DataDf_0``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDf_0.from_mcnp``.
        """

        element = pymcnp.inp.data.Df_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDf_1:
    """
    Tests ``DataDf_1``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDf_1.from_mcnp``.
        """

        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Iu:
    """
    Tests ``Df_1Iu``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``Df_1Iu.from_mcnp``.
        """

        element = pymcnp.inp.data.df_1.Iu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Fac:
    """
    Tests ``Df_1Fac``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``Df_1Fac.from_mcnp``.
        """

        element = pymcnp.inp.data.df_1.Fac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Ic:
    """
    Tests ``Df_1Ic``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``Df_1Ic.from_mcnp``.
        """

        element = pymcnp.inp.data.df_1.Ic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Int:
    """
    Tests ``Df_1Int``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``Df_1Int.from_mcnp``.
        """

        element = pymcnp.inp.data.df_1.Int
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEm:
    """
    Tests ``DataEm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEm.from_mcnp``.
        """

        element = pymcnp.inp.data.Em
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTm:
    """
    Tests ``DataTm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataTm.from_mcnp``.
        """

        element = pymcnp.inp.data.Tm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCm:
    """
    Tests ``DataCm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataCm.from_mcnp``.
        """

        element = pymcnp.inp.data.Cm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCf:
    """
    Tests ``DataCf``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataCf.from_mcnp``.
        """

        element = pymcnp.inp.data.Cf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSf:
    """
    Tests ``DataSf``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSf.from_mcnp``.
        """

        element = pymcnp.inp.data.Sf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFs:
    """
    Tests ``DataFs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFs.from_mcnp``.
        """

        element = pymcnp.inp.data.Fs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSd:
    """
    Tests ``DataSd``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSd.from_mcnp``.
        """

        element = pymcnp.inp.data.Sd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFu:
    """
    Tests ``DataFu``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFu.from_mcnp``.
        """

        element = pymcnp.inp.data.Fu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataNotrn:
    """
    Tests ``DataNotrn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataNotrn.from_mcnp``.
        """

        element = pymcnp.inp.data.Notrn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPert:
    """
    Tests ``DataPert``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPert.from_mcnp``.
        """

        element = pymcnp.inp.data.Pert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertCell:
    """
    Tests ``PertCell``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PertCell.from_mcnp``.
        """

        element = pymcnp.inp.data.pert.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertMat:
    """
    Tests ``PertMat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PertMat.from_mcnp``.
        """

        element = pymcnp.inp.data.pert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertRho:
    """
    Tests ``PertRho``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PertRho.from_mcnp``.
        """

        element = pymcnp.inp.data.pert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertMethod:
    """
    Tests ``PertMethod``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PertMethod.from_mcnp``.
        """

        element = pymcnp.inp.data.pert.Method
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertErg:
    """
    Tests ``PertErg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PertErg.from_mcnp``.
        """

        element = pymcnp.inp.data.pert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertRxn:
    """
    Tests ``PertRxn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PertRxn.from_mcnp``.
        """

        element = pymcnp.inp.data.pert.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKpert:
    """
    Tests ``DataKpert``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataKpert.from_mcnp``.
        """

        element = pymcnp.inp.data.Kpert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertCell:
    """
    Tests ``KpertCell``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertCell.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertMat:
    """
    Tests ``KpertMat``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertMat.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertRho:
    """
    Tests ``KpertRho``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertRho.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertIso:
    """
    Tests ``KpertIso``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertIso.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertRxn:
    """
    Tests ``KpertRxn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertRxn.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertErg:
    """
    Tests ``KpertErg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertErg.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertLinear:
    """
    Tests ``KpertLinear``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KpertLinear.from_mcnp``.
        """

        element = pymcnp.inp.data.kpert.Linear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKsen:
    """
    Tests ``DataKsen``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataKsen.from_mcnp``.
        """

        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenIso:
    """
    Tests ``KsenIso``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenIso.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenRxn:
    """
    Tests ``KsenRxn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenRxn.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenMt:
    """
    Tests ``KsenMt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenMt.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenErg:
    """
    Tests ``KsenErg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenErg.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenEin:
    """
    Tests ``KsenEin``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenEin.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Ein
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenLegendre:
    """
    Tests ``KsenLegendre``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenLegendre.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Legendre
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenCos:
    """
    Tests ``KsenCos``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenCos.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Cos
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenConstrain:
    """
    Tests ``KsenConstrain``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``KsenConstrain.from_mcnp``.
        """

        element = pymcnp.inp.data.ksen.Constrain
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFmesh:
    """
    Tests ``DataFmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.Fmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshGeom:
    """
    Tests ``FmeshGeom``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshGeom.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshOrigin:
    """
    Tests ``FmeshOrigin``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshOrigin.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Origin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshAxs:
    """
    Tests ``FmeshAxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshAxs.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshVec:
    """
    Tests ``FmeshVec``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshVec.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshImesh:
    """
    Tests ``FmeshImesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshImesh.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshIints:
    """
    Tests ``FmeshIints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshIints.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Iints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshJmesh:
    """
    Tests ``FmeshJmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshJmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshJints:
    """
    Tests ``FmeshJints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshJints.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshKmesh:
    """
    Tests ``FmeshKmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshKmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Kmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshKints:
    """
    Tests ``FmeshKints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshKints.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Kints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshEmesh:
    """
    Tests ``FmeshEmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshEmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Emesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshEints:
    """
    Tests ``FmeshEints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshEints.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Eints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshEnorm:
    """
    Tests ``FmeshEnorm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshEnorm.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Enorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTmesh:
    """
    Tests ``FmeshTmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshTmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Tmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTints:
    """
    Tests ``FmeshTints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshTints.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Tints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTnorm:
    """
    Tests ``FmeshTnorm``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshTnorm.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Tnorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshFactor:
    """
    Tests ``FmeshFactor``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshFactor.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshOut:
    """
    Tests ``FmeshOut``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshOut.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTr:
    """
    Tests ``FmeshTr``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshTr.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Tr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshInc:
    """
    Tests ``FmeshInc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshInc.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Inc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshType:
    """
    Tests ``FmeshType``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshType.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshKclear:
    """
    Tests ``FmeshKclear``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``FmeshKclear.from_mcnp``.
        """

        element = pymcnp.inp.data.fmesh.Kclear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSpdtl:
    """
    Tests ``DataSpdtl``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataSpdtl.from_mcnp``.
        """

        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataImp:
    """
    Tests ``DataImp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataImp.from_mcnp``.
        """

        element = pymcnp.inp.data.Imp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataVar:
    """
    Tests ``DataVar``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataVar.from_mcnp``.
        """

        element = pymcnp.inp.data.Var
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_VarRr:
    """
    Tests ``VarRr``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``VarRr.from_mcnp``.
        """

        element = pymcnp.inp.data.var.Rr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwe:
    """
    Tests ``DataWwe``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwe.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwe
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwt:
    """
    Tests ``DataWwt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwt.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwn:
    """
    Tests ``DataWwn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwn.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwp:
    """
    Tests ``DataWwp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwp.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwg:
    """
    Tests ``DataWwg``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwg.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwge:
    """
    Tests ``DataWwge``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwge.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwge
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwgt:
    """
    Tests ``DataWwgt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataWwgt.from_mcnp``.
        """

        element = pymcnp.inp.data.Wwgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMesh:
    """
    Tests ``DataMesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataMesh.from_mcnp``.
        """

        element = pymcnp.inp.data.Mesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshGeom:
    """
    Tests ``MeshGeom``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshGeom.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshRef:
    """
    Tests ``MeshRef``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshRef.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Ref
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshOrigin:
    """
    Tests ``MeshOrigin``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshOrigin.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Origin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshAxs:
    """
    Tests ``MeshAxs``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshAxs.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshVec:
    """
    Tests ``MeshVec``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshVec.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshImesh:
    """
    Tests ``MeshImesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshImesh.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshIints:
    """
    Tests ``MeshIints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshIints.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Iints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshJmesh:
    """
    Tests ``MeshJmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshJmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshJints:
    """
    Tests ``MeshJints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshJints.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshKmesh:
    """
    Tests ``MeshKmesh``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshKmesh.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Kmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshKints:
    """
    Tests ``MeshKints``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``MeshKints.from_mcnp``.
        """

        element = pymcnp.inp.data.mesh.Kints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEsplt:
    """
    Tests ``DataEsplt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataEsplt.from_mcnp``.
        """

        element = pymcnp.inp.data.Esplt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTsplt:
    """
    Tests ``DataTsplt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataTsplt.from_mcnp``.
        """

        element = pymcnp.inp.data.Tsplt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataExt:
    """
    Tests ``DataExt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataExt.from_mcnp``.
        """

        element = pymcnp.inp.data.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFcl:
    """
    Tests ``DataFcl``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFcl.from_mcnp``.
        """

        element = pymcnp.inp.data.Fcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDxt:
    """
    Tests ``DataDxt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDxt.from_mcnp``.
        """

        element = pymcnp.inp.data.Dxt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDd:
    """
    Tests ``DataDd``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDd.from_mcnp``.
        """

        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPd:
    """
    Tests ``DataPd``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPd.from_mcnp``.
        """

        element = pymcnp.inp.data.Pd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDxc:
    """
    Tests ``DataDxc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDxc.from_mcnp``.
        """

        element = pymcnp.inp.data.Dxc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataBbrem:
    """
    Tests ``DataBbrem``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataBbrem.from_mcnp``.
        """

        element = pymcnp.inp.data.Bbrem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPikmt:
    """
    Tests ``DataPikmt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPikmt.from_mcnp``.
        """

        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPwt:
    """
    Tests ``DataPwt``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPwt.from_mcnp``.
        """

        element = pymcnp.inp.data.Pwt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataNps:
    """
    Tests ``DataNps``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataNps.from_mcnp``.
        """

        element = pymcnp.inp.data.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCtme:
    """
    Tests ``DataCtme``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataCtme.from_mcnp``.
        """

        element = pymcnp.inp.data.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataStop:
    """
    Tests ``DataStop``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataStop.from_mcnp``.
        """

        element = pymcnp.inp.data.Stop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_StopNps:
    """
    Tests ``StopNps``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``StopNps.from_mcnp``.
        """

        element = pymcnp.inp.data.stop.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_StopCtme:
    """
    Tests ``StopCtme``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``StopCtme.from_mcnp``.
        """

        element = pymcnp.inp.data.stop.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_StopFk:
    """
    Tests ``StopFk``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``StopFk.from_mcnp``.
        """

        element = pymcnp.inp.data.stop.Fk
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPrint:
    """
    Tests ``DataPrint``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPrint.from_mcnp``.
        """

        element = pymcnp.inp.data.Print
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTalnp:
    """
    Tests ``DataTalnp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataTalnp.from_mcnp``.
        """

        element = pymcnp.inp.data.Talnp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPrdmp:
    """
    Tests ``DataPrdmp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPrdmp.from_mcnp``.
        """

        element = pymcnp.inp.data.Prdmp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPtrac:
    """
    Tests ``DataPtrac``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataPtrac.from_mcnp``.
        """

        element = pymcnp.inp.data.Ptrac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracBuffer:
    """
    Tests ``PtracBuffer``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracBuffer.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Buffer
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracFile:
    """
    Tests ``PtracFile``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracFile.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracMax:
    """
    Tests ``PtracMax``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracMax.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Max
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracMeph:
    """
    Tests ``PtracMeph``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracMeph.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Meph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracWrite:
    """
    Tests ``PtracWrite``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracWrite.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Write
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracConic:
    """
    Tests ``PtracConic``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracConic.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Conic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracEvent:
    """
    Tests ``PtracEvent``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracEvent.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Event
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracFilter:
    """
    Tests ``PtracFilter``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracFilter.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Filter
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracType:
    """
    Tests ``PtracType``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracType.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracNps:
    """
    Tests ``PtracNps``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracNps.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracCell:
    """
    Tests ``PtracCell``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracCell.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracSurface:
    """
    Tests ``PtracSurface``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracSurface.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Surface
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracTally:
    """
    Tests ``PtracTally``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracTally.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Tally
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracValue:
    """
    Tests ``PtracValue``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``PtracValue.from_mcnp``.
        """

        element = pymcnp.inp.data.ptrac.Value
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataHistp:
    """
    Tests ``DataHistp``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataHistp.from_mcnp``.
        """

        element = pymcnp.inp.data.Histp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataRand:
    """
    Tests ``DataRand``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataRand.from_mcnp``.
        """

        element = pymcnp.inp.data.Rand
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandGen:
    """
    Tests ``RandGen``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``RandGen.from_mcnp``.
        """

        element = pymcnp.inp.data.rand.Gen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandSeed:
    """
    Tests ``RandSeed``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``RandSeed.from_mcnp``.
        """

        element = pymcnp.inp.data.rand.Seed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandStride:
    """
    Tests ``RandStride``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``RandStride.from_mcnp``.
        """

        element = pymcnp.inp.data.rand.Stride
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandHist:
    """
    Tests ``RandHist``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``RandHist.from_mcnp``.
        """

        element = pymcnp.inp.data.rand.Hist
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDbcn:
    """
    Tests ``DataDbcn``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataDbcn.from_mcnp``.
        """

        element = pymcnp.inp.data.Dbcn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLost:
    """
    Tests ``DataLost``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataLost.from_mcnp``.
        """

        element = pymcnp.inp.data.Lost
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataIdum:
    """
    Tests ``DataIdum``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataIdum.from_mcnp``.
        """

        element = pymcnp.inp.data.Idum
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataRdum:
    """
    Tests ``DataRdum``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataRdum.from_mcnp``.
        """

        element = pymcnp.inp.data.Rdum
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZa:
    """
    Tests ``DataZa``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataZa.from_mcnp``.
        """

        element = pymcnp.inp.data.Za
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZb:
    """
    Tests ``DataZb``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataZb.from_mcnp``.
        """

        element = pymcnp.inp.data.Zb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZc:
    """
    Tests ``DataZc``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataZc.from_mcnp``.
        """

        element = pymcnp.inp.data.Zc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZd:
    """
    Tests ``DataZd``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataZd.from_mcnp``.
        """

        element = pymcnp.inp.data.Zd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFiles:
    """
    Tests ``DataFiles``.
    """

    class Test_FromMcnp(_Test_FromMcnp):
        """
        Tests ``DataFiles.from_mcnp``.
        """

        element = pymcnp.inp.data.Files
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

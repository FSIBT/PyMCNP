import pymcnp
import _utils


class Test_Data:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Data
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataVol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Vol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataArea:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTr_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTr_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTr_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tr_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTr_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tr_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTr_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tr_4
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataU:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.U
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFill:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fill
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataUran:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Uran
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDawwg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dawwg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DawwgPoints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Points
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DawwgXsec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Xsec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DawwgBlock:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.Block
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNgroup:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ngroup
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIsn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Isn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNiso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Niso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockMt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIquad:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Iquad
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFmmix:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fmmix
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNosolv:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nosolv
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoedit:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noedit
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNogeod:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nogeod
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNomix:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nomix
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoasg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noasg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNomacr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nomacr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoslnp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noslnp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoedtt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noedtt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNoadjm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noadjm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockLib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Lib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockLibname:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFissneut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fissneut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockLng:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Lng
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockBalxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Balxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNtichi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ntichi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIevt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ievt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIsct:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Isct
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIth:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ith
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTrcor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Trcor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbfrnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibfrnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockIbback:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibback
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockEpsi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Epsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockOitm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Oitm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNosigf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nosigf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockSrcacc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Srcacc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockDiffsol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Diffsol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsasn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsasn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsaepsi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsaepsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsaits:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsaits
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockTsabeta:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsabeta
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockPtconv:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ptconv
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockNorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Norm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockXsectp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Xsectp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFissrp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fissrp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockSourcp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Sourcp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAngp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Angp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockBalp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Balp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRaflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Raflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRmflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Rmflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAvatar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Avatar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsleft:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asleft
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsrite:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asrite
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsbott:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asbott
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAstop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Astop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsfrnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asfrnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAsback:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asback
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockMassed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Massed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockPted:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Pted
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockZned:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Zned
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRzflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Rzflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockRzmflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Rzmflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockEdoutf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Edoutf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockByvolp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Byvolp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockAjed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ajed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BlockFluxone:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fluxone
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedBackground:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Background
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMeshgeo:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meshgeo
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMgeoin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Mgeoin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMeeout:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMeein:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meein
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedCalcvols:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Calcvols
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedDebug:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Debug
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedFiletype:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedGmvfile:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Gmvfile
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedLength:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Length
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbedMcnpumfile:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Mcnpumfile
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbee:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeEmbed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Embed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeEnergy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Energy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeTime:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Time
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeAtom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Atom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeFactor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeList:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.List
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeMat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_EmbeeMtype:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embee.Mtype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbeb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embeb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbem:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbtb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embtb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbtm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embtm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbdb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embdb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEmbdf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embdf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataM_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.M_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Gas:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Gas
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Estep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Estep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Hstep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Hstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Nlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Nlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Plib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Plib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Pnlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Pnlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Elib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Elib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Hlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Hlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Alib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Alib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Slib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Slib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Tlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Tlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Dlib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Dlib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Cond:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Cond
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Refi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Refc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_M_0Refs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.m_0.Refs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataM_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.M_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataOtfdb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Otfdb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTotnu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Totnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataNonu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Nonu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataAwtab:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Awtab
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataXs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Xs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataVoid:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Void
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMgopt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mgopt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDrxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Drxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMode:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPhys_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Phys_4
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataAct:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Act
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActFission:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActNonfiss:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Nonfiss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActThresh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Thresh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDnbais:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dnbais
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActNap:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Nap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDneb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dneb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActDgeb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Dgeb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActPecut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Pecut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActHlcut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Hlcut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ActSample:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Sample
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataElpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Elpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataThtme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Thtme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMphys:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mphys
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLca:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lca
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLcb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lcb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLcc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lcc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLea:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lea
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLeb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Leb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFmult:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fmult
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultSfnu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Sfnu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultWidth:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Width
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultSfyield:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Sfyield
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultWatt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Watt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultMethod:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Method
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultData:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Data
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmultShift:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmult.Shift
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTropt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptMcscat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Mcscat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptEloss:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Eloss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptNreact:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Nreact
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptNescat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Nescat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_TroptGenxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Genxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataUnc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Unc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCosyp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cosyp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCosy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cosy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataBfld:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Bfld
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldField:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Field
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldVec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldMaxdeflc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Maxdeflc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldMaxstep:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Maxstep
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldAxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldFfedges:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Ffedges
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_BfldRefpnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Refpnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataBflcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Bflcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSdef:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefCel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefSur:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Sur
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefErg_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Erg_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefErg_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Erg_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTme_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tme_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTme_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefDir_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dir_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefDir_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dir_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefVec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefNrm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefPos:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Pos
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefRad_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Rad_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefRad_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Rad_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefExt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefAxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefX:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefY:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefZ:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefCcc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ccc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefAra:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Ara
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefWgt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Wgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTr_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefTr_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefEff:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Eff
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefPar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Par
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefDat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefLoc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefBem:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SdefBap:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Bap
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSi_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Si_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSi_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Si_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSp_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sp_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSp_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sp_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSb_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sb_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSb_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sb_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDs_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ds_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDs_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ds_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDs_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ds_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSsw:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SswSym:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Sym
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SswPty:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SswCel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSsr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ssr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrOld:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Old
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrCel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Cel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrNew:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.New
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrPty:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrCol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Col
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrWgt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Wgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrTr_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Tr_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrTr_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Tr_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrPsc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Psc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrAxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrExt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrPoa:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Poa
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_SsrBcw:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ssr.Bcw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKcode:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Kcode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKsrc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ksrc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKopts:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Kopts
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsBlocksize:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Blocksize
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsKinetics:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Kinetics
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsPrecursor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Precursor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsKsental:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatskpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatskpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatncyc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatncyc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatspace:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatspace
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmataccel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmataccel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatreduce:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatreduce
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatnx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatnx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatny:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatny
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KoptsFmatnz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatnz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataHsrc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Hsrc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFip:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fip
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFir:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fir
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataF_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.F_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataE:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.E
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataT_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.T_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataT_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.T_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cbeg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cbeg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cfrq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cfrq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cofi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cofi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Coni:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Coni
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Csub:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Csub
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_T_1Cend:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.t_1.Cend
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataC_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.C_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataC_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.C_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDe:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.De
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDf_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Df_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDf_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Iu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Iu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Fac:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Fac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Ic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Ic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Log:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Log
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_Df_1Lin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Lin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Em
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fu
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ft
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataNotrn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Notrn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPert:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Pert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertCell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertMat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertRho:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertMethod:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Method
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertErg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PertRxn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKpert:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Kpert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertCell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertMat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertRho:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertIso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertRxn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertErg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KpertLinear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Linear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataKsen:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenIso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Iso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenRxn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenMt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenErg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenEin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Ein
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenLegendre:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Legendre
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenCos:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Cos
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_KsenConstrain:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Constrain
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshGeom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshOrigin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Origin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshAxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshVec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshImesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshIints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Iints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshJmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshJints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshKmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshKints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshEmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Emesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshEints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Eints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshEnorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Enorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTnorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tnorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshFactor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshOut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshTr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Tr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshInc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Inc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshType:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FmeshKclear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kclear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataSpdtl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataImp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Imp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataVar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Var
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_VarRr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.var.Rr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwe:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwe
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwge:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwge
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataWwgt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwgt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshGeom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshRef:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Ref
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshOrigin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Origin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshAxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Axs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshVec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Vec
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshImesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Imesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshIints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Iints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshJmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Jmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshJints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshKmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Kmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MeshKints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Kints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataEsplt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Esplt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTsplt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Tsplt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataExt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDxt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dxt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Pd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDxc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dxc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataBbrem:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Bbrem
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPikmt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPwt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Pwt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataNps:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataCtme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataStop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Stop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_StopNps:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_StopCtme:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Ctme
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_StopFk:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.stop.Fk
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPrint:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Print
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataTalnp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Talnp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPrdmp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Prdmp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataPtrac:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ptrac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracBuffer:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Buffer
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracFile:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracMax:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Max
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracMeph:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Meph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracWrite:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Write
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracConic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Conic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracEvent:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Event
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracFilter:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Filter
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracType:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Type
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracNps:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Nps
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracCell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracSurface:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Surface
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracTally:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Tally
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_PtracValue:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.Value
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataMplot:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mplot
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotTerm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Term
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFile:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotCoplot:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Coplot
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFreq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Freq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotReturn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Return
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPlot:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Plot
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPause:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Pause
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotEnd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.End
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotOptions:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Options
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotHelp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Help
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotStatus:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Status
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPrintal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Printal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotIptal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Iptal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPrintpts:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Printpts
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotRuntpe:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Runtpe
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotDump:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Dump
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotWmctal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Wmctal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotRmctal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Rmctal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotTally:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tally
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPert:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Pert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLethargy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Lethargy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotNonorm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Nonorm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFactor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotReset:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Reset
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotTitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Title
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotBelow:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Below
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotSubtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Subtitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotXtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xtitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotYtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ytitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotZtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ztitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLabel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Label
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFree:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Free
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FreeAll:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.free.All
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_FreeNoall:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.free.Noall
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFixed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotSet:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Set
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotTfc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tfc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotKcode:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Kcode
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotXs_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotXs_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotXs_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotMt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Par
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLinlin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Linlin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLinlog:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Linlog
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLoglin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Loglin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLoglog:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Loglog
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotXlims:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xlims
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotYlims:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ylims
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotScales:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Scales
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotHist:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Hist
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotPlinear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Plinear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotSpline:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Spline
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotBar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Bar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotNoerrbar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Noerrbar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotThick:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Thick
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotThin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Thin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotLegend:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Legend
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotContour:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Contour
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourPct:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Pct
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourLin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Lin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourLog:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Log
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourAll:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.All
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourNoall:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Noall
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourLine:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Line
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourNoline:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Noline
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourColor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Color
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_ContourNocolor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.contour.Nocolor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotWash:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFmesh:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fmesh
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotFmrelerr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Fmrelerr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotZlev:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Zlev
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotEbin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Ebin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotTbin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tbin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotCop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Cop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_MplotTal:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Tal
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataHistp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Histp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataRand:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Rand
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandGen:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Gen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandSeed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Seed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandStride:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Stride
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_RandHist:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.rand.Hist
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataDbcn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dbcn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataLost:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lost
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataIdum:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Idum
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataRdum:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Rdum
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZa:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Za
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Zb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Zc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataZd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Zd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_DataFiles:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Files
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

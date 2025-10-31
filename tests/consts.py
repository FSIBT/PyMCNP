import pathlib

import pymcnp


class string:
    INP = (pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'valid_10.inp').read_text()
    OUTP = (pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'valid_38.outp').read_text()
    PTRAC = (pathlib.Path(__file__).parent.parent / 'files' / 'ptrac' / 'valid_27.ptrac').read_text()
    MESHTAL = (pathlib.Path(__file__).parent.parent / 'files' / 'meshtal' / 'valid_40.meshtal').read_text()

    class types:
        GEOMETRY = '1 (2:(+3 -4) #5)'
        LATTICE = '2<3[-3:+3 -2:3 0:0]<(4<7)'
        REPEAT = '10r'
        INSERT = '10i'
        MULTIPLY = '10m'
        JUMP = '10j'
        LOG = '10log'
        INTEGER = '1'
        REAL = '3.1'
        STRING = 'none'
        DISTRIBUTION = 'd1'
        EMBEDDEDDISTRIBUTION = 'd1'
        ZAID = '001001'
        DESIGNATOR = 'n,#'
        SUBSTANCE = '001001 0.5'
        TRANSFORMATION_0 = '1 1 1 2 2 2 3 3 3 4 4 4'
        TRANSFORMATION_1 = '1 1 1 2 2 2 3 3 3'
        TRANSFORMATION_2 = '1 1 1 2 2 2 3 3'
        TRANSFORMATION_3 = '1 1 1 2 2 2'
        TRANSFORMATION_4 = '1 1 1'
        INDEX = '1:2'
        TUPLE = '0.5 3.1'

    class inp:
        CELL = '1 1 3.1 1 (2:(+3 -4) #5) imp:@=1'
        LIKE = '2 like 1 but imp:@=2'
        SURFACE = '1 SO 1'
        DATA = 'vol no 3.1 3.1 3.1'
        COMMENT = 'c hello'
        VOL = 'vol no 3.1 3.1 3.1'
        AREA = 'area 3.1 3.1 3.1'
        TR_0 = '*tr1 1 1 1 2 2 2 3 3 3 4 4 4'
        TR_1 = '*tr1 1 1 1 2 2 2 3 3 3'
        TR_2 = '*tr1 1 1 1 2 2 2 3 3'
        TR_3 = '*tr1 1 1 1 2 2 2'
        TR_4 = '*tr1 1 1 1'
        U = 'u 1 1 1'
        LAT = 'lat 1 1 1'
        FILL = 'fill 1 1 1'
        URAN = 'uran 1 3.1 3.1 3.1 1 3.1 3.1 3.1'
        DM = 'dm1 001001 001001 001001'
        DAWWG = 'dawwg points=1'
        EMBED = 'embed1 background=1'
        EMBEE = 'embee1:@ embed=1'
        EMBEB = 'embeb1 3.1 3.1 3.1'
        EMBEM = 'embem1 3.1 3.1 3.1'
        EMBTB = 'embtb1 3.1 3.1 3.1'
        EMBTM = 'embtm1 3.1 3.1 3.1'
        EMBDB = 'embdb1 3.1 3.1 3.1'
        EMBDF = 'embdf1 3.1 3.1 3.1'
        M_0 = 'm1 001001 0.5 001001 0.5 gas=yes'
        M_1 = 'm1 hello'
        MT = 'mt1 hello hello hello'
        MX = 'mx1:@ 001001 001001 001001'
        OTFDB = 'otfdb 001001 001001 001001'
        TOTNU = 'totnu no'
        NONU = 'nonu 1 1 1'
        AWTAB = 'awtab 001001 0.5 001001 0.5 001001 0.5'
        XS = 'xs1 001001 0.5 001001 0.5 001001 0.5'
        VOID = 'void 1 1 1'
        MGOPT = 'mgopt f 1 1 1 1 3.1 3.1'
        DRXS = 'drxs 001001 001001 001001'
        MODE = 'mode @ @ @'
        PHYS_0 = 'phys:n 3.1 3.1 1 3.1 1 1 1 1'
        PHYS_1 = 'phys:p 3.1 1 1 1 1 1'
        PHYS_2 = 'phys:e 3.1 1 1 1 1 3.1 3.1 1 1 1 -1 j j 0.8 3.1 0.8'
        PHYS_3 = 'phys:h 3.1 3.1 3.1 1 0.8 1 1 -1 0.8 0.8 3.1'
        PHYS_4 = 'phys:@ 3.1 1 1 3.1 1 1 -1 0.8 0.8 3.1'
        ACT = 'act fission none'
        CUT = 'cut:@ 3.1 3.1 3.1 3.1 3.1'
        ELPT = 'elpt 3.1 3.1 3.1'
        TMP = 'tmp1 3.1 3.1 3.1'
        THTME = 'thtme 3.1 3.1 3.1'
        MPHYS = 'mphys on'
        LCA = 'lca 1 1 1 1 1 1 1 1 1 1 1'
        LCB = 'lcb 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1'
        LCC = 'lcc 3.1 3.1 3.1 1 1 3.1 3.1 3.1'
        LEA = 'lea 1 1 1 1 1 1 1'
        LEB = 'leb 3.1 3.1 3.1 3.1'
        FMULT = 'fmult 001001 sfnu=3.1 3.1 3.1'
        TROPT = 'tropt mcscat=off'
        UNC = 'unc:@ 1 1 1'
        COSYP = 'cosyp 1 1 1 3.1 3.1 3.1'
        COSY = 'cosy 1 1 1'
        BFLD = 'bfld1 const field=3.1'
        BFLCL = 'bflcl 1 1 1'
        SDEF = 'sdef cel=1'
        SI_0 = 'si1 h d1 d1 d1'
        SI_1 = 'si1 h 3.1 3.1 3.1'
        SI_2 = 'si1 h @ @ @'
        SP_0 = 'sp1 d 3.1'
        SP_1 = 'sp -2 3.1 3.1'
        SB_0 = 'sb1 d 3.1 3.1 3.1'
        SB_1 = 'sb -2 3.1 3.1'
        DS_0 = 'ds1 h 3.1 3.1 3.1'
        DS_1 = 'ds1 t 3.1 3.1 3.1 3.1 3.1 3.1'
        DS_2 = 'ds1 q d1 3.1 d2 3.1 d3 3.1'
        DS_3 = 'ds1 s d1 0 0 d2'
        SC = 'sc1 hello hello hello'
        SSW = 'ssw 1 1 1 1 1 1 sym=1'
        SSR = 'ssr old 1 1 1'
        KCODE = 'kcode 1 3.1 1 1 1 1 1 1'
        KSRC = 'ksrc 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1'
        KOPTS = 'kopts blocksize=2'
        HSRC = 'hsrc 1 3.1 3.1 1 3.1 3.1 1 3.1 3.1'
        F_0 = '+f1:@ 1 1 1 t'
        F_1 = '+f5:@ 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 nd'
        F_2 = '+f5x:@ 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 nd'
        F_3 = '+f8:@ 1 1 1 t'
        F_4 = '+f4:@ 2<3'
        FIP = 'fip5:@ 3.1 3.1 3.1 0 3.1 3.1 3.1 3.1 3.1 3.1'
        FIR = 'fir5:@ 3.1 3.1 3.1 0 3.1 3.1 3.1 1 3.1 1'
        FIC = 'fic5:@ 3.1 3.1 3.1 0 3.1 3.1 3.1 -1 3.1 -1'
        FC = 'fc1 hello'
        E = 'e1 3.1 3.1 3.1 nt c'
        T_0 = 't1 3.1 3.1 3.1 nt c'
        T_1 = 't1 cbeg 3.1'
        C = '*c1 3.1 3.1 3.1 t c'
        FQ = 'fq1 f f f f f f f '
        FM = '*fm1 hello'
        DE = 'de1 log 3.1 3.1 3.1'
        DF_0 = 'df1 log 3.1 3.1 3.1'
        DF_1 = 'df1 iu=1'
        EM = 'em1 3.1 3.1 3.1'
        TM = 'tm1 3.1 3.1 3.1'
        CM = 'cm1 3.1 3.1 3.1'
        CF = 'cf1 1 1 1'
        SF = 'sf1 1 1 1'
        FS = 'fs1 1 1 1 t c'
        SD = 'sd1 3.1 3.1 3.1'
        FU = 'fu1 3.1 3.1 3.1 nt c'
        FT = 'ft1 hello'
        TF_0 = 'tf1 1 1 1 1 1 1 1 1'
        TF_1 = 'tf1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
        NOTRN = 'notrn'
        PERT = 'pert1:@ cell=1 1 1'
        KPERT = 'kpert1 cell=1 1 1'
        KSEN = 'ksen1 hello iso=001001 002001 003001'
        FMESH = 'fmesh1:@ geom=xyz'
        SPDTL = 'spdtl force'
        IMP = 'imp:@ 3.1 3.1 3.1'
        VAR = 'var rr=no'
        WWE = 'wwe:@ 3.1 3.1 3.1'
        WWT = 'wwt:@ 3.1 3.1 3.1'
        WWN = 'wwn1:@ 3.1 3.1 3.1 '
        WWP = 'wwp:@ 3.1 3.1 3.1 1 3.1 1 3.1 1 3.1 3.1'
        WWG = 'wwg 1 1 3.1 1'
        WWGE = 'wwge:@ 3.1 3.1 3.1'
        WWGT = 'wwgt:@ 3.1 3.1 3.1'
        MESH = 'mesh geom=xyz'
        ESPLT = 'esplt:@ 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1'
        TSPLT = 'tsplt:@ 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1'
        EXT = 'ext:@ hello hello hello'
        FCL = 'fcl:@ 3.1 3.1 3.1'
        DXT = 'dxt:@ 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1 1 1 3.1 3.1 3.1'
        DD = 'dd1 3.1 3.1 3.1 3.1 3.1 3.1'
        PD = 'pd1:@ 3.1 3.1 3.1'
        DXC = 'dxc1:@ 3.1 3.1 3.1'
        BBREM = 'bbrem 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 3.1 1 1 1'
        PIKMT = 'pikmt 001001 1 001001 1 001001 1'
        PWT = 'pwt 3.1 3.1 3.1'
        NPS = 'nps 1 1'
        CTME = 'ctme 1'
        STOP = 'stop nps=1 1'
        PRINT = 'print 1 1 1'
        TALNP = 'talnp 1 1 1'
        PRDMP = 'prdmp 1 1 1 1 1'
        PTRAC = 'ptrac buffer=1'
        MPLOT = 'mplot term=1'
        HISTP = 'histp 1 1 1 1'
        RAND = 'rand gen=1'
        DBCN = 'dbcn 1 1 1 1 1 56 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
        LOST = 'lost 1 1'
        IDUM = 'idum 1 1 1'
        RDUM = 'rdum 3.1 3.1 3.1'
        ZA = 'za hello'
        ZB = 'zb hello'
        ZC = 'zc hello'
        ZD = 'zd hello'
        FILES = 'files 1 1 s f 1 1 1 s f 1 1 1 s f 1'

        class dd:
            DIAGNOSTIC = '3.1 4.1'

        class ds_1:
            VARIABLES = '3.1 4.1'

        class ds_2:
            VARIABLES = 'd1 4.1'

        class dxt:
            SHELL = '3.1 4.1 5.9 1 2'

        class f_1:
            SPHERE = '3.1 4.1 5.9 2.6'

        class f_2:
            RING = '3.1 4.1 5.9'

        class files:
            FILE = '1 2 s f 3'

        class ksrc:
            LOCATION = '3.1 4.1 5.9'

        class pikmt:
            PHOTONBIAS = '001001 1'

        class uran:
            STOCHASTIC = '1 3.1 4.1 5.9'

        class dawwg:
            POINTS = 'points 1'
            XSEC = 'xsec hello'
            BLOCK = 'block 1'

            class block:
                NGROUP = 'ngroup 1'
                ISN = 'isn 1'
                NISO = 'niso 1'
                MT = 'mt 1'
                IQUAD = 'iquad 1'
                FMMIX = 'fmmix 1'
                NOSOLV = 'nosolv 1'
                NOEDIT = 'noedit 1'
                NOGEOD = 'nogeod 1'
                NOMIX = 'nomix 1'
                NOASG = 'noasg 1'
                NOMACR = 'nomacr 1'
                NOSLNP = 'noslnp 1'
                NOEDTT = 'noedtt 1'
                NOADJM = 'noadjm 1'
                LIB = 'lib hello'
                LIBNAME = 'libname hello'
                FISSNEUT = 'fissneut 1'
                LNG = 'lng 1'
                BALXS = 'balxs 1'
                NTICHI = 'ntichi 1'
                IEVT = 'ievt 1'
                ISCT = 'isct 1'
                ITH = 'ith 1'
                TRCOR = 'trcor diag'
                IBL = 'ibl 1'
                IBR = 'ibr 1'
                IBT = 'ibt 1'
                IBB = 'ibb 1'
                IBFRNT = 'ibfrnt 1'
                IBBACK = 'ibback 1'
                EPSI = 'epsi 3.1'
                OITM = 'oitm 1'
                NOSIGF = 'nosigf 1'
                SRCACC = 'srcacc dsa'
                DIFFSOL = 'diffsol hello'
                TSASN = 'tsasn 1'
                TSAEPSI = 'tsaepsi 3.1'
                TSAITS = 'tsaits 1'
                TSABETA = 'tsabeta 1'
                PTCONV = 'ptconv 1'
                NORM = 'norm 3.1'
                XSECTP = 'xsectp 1'
                FISSRP = 'fissrp 1'
                SOURCP = 'sourcp 1'
                ANGP = 'angp 1'
                BALP = 'balp 1'
                RAFLUX = 'raflux 1'
                RMFLUX = 'rmflux 1'
                AVATAR = 'avatar 1'
                ASLEFT = 'asleft 1'
                ASRITE = 'asrite 1'
                ASBOTT = 'asbott 1'
                ASTOP = 'astop 1'
                ASFRNT = 'asfrnt 1'
                ASBACK = 'asback 1'
                MASSED = 'massed 1'
                PTED = 'pted 1'
                ZNED = 'zned 1'
                RZFLUX = 'rzflux 1'
                RZMFLUX = 'rzmflux 1'
                EDOUTF = 'edoutf 1'
                BYVOLP = 'byvolp 1'
                AJED = 'ajed 1'
                FLUXONE = 'fluxone 1'

        class embed:
            BACKGROUND = 'background 3.1'
            MATCELL = 'matcell 1 2 1 2 1 2'
            MESHGEO = 'meshgeo lnk3dnt'
            MGEOIN = 'mgeoin hello'
            MEEOUT = 'meeout hello'
            MEEIN = 'meein hello'
            CALCVOLS = 'calc_vols yes'
            DEBUG = 'debug echomesh'
            FILETYPE = 'filetype ascii'
            GMVFILE = 'gmvfile hello'
            LENGTH = 'length 3.1'
            MCNPUMFILE = 'mcnpumfile hello'

            class matcell:
                ENTRY = '1 2'

        class embee:
            EMBED = 'embed 1'
            ENERGY = 'energy 3.1'
            TIME = 'time 3.1'
            ATOM = 'atom yes'
            FACTOR = 'factor 3.1'
            LIST = 'list 3.1'
            MAT = 'mat 1'
            MTYPE = 'mtype flux'

        class m_0:
            GAS = 'gas yes'
            ESTEP = 'estep 1'
            HSTEP = 'hstep 1'
            NLIB = 'nlib hello'
            PLIB = 'plib hello'
            PNLIB = 'pnlib hello'
            ELIB = 'elib hello'
            HLIB = 'hlib hello'
            ALIB = 'alib hello'
            SLIB = 'slib hello'
            TLIB = 'tlib hello'
            DLIB = 'dlib hello'
            COND = 'cond 3.1'
            REFI = 'refi 3.1'
            REFC = 'refc 3.1 3.1 3.1'
            REFS = 'refs 3.1 3.1 3.1'

        class act:
            FISSION = 'fission none'
            NONFISS = 'nonfiss none'
            DN = 'dn model'
            DG = 'dg none'
            THRESH = 'thresh 0.8'
            DNBAIS = 'dnbais 1'
            NAP = 'nap 1'
            DNEB = 'dneb 3.1 3.1 3.1 3.1 3.1 3.1'
            DGEB = 'dgeb 3.1 3.1 3.1 3.1 3.1 3.1'
            PECUT = 'pecut 3.1'
            HLCUT = 'hlcut 3.1'
            SAMPLE = 'sample correlate'

            class dgeb:
                BIAS = '3.1 4.1'

            class dneb:
                BIAS = '3.1 4.1'

        class fmult:
            SFNU = 'sfnu 3.1 3.1 3.1'
            WIDTH = 'width 3.1'
            SFYIELD = 'sfyield 3.1'
            WATT = 'watt 3.1 3.1'
            METHOD = 'method 1'
            DATA = 'data 1'
            SHIFT = 'shift 1'

        class tropt:
            MCSCAT = 'mcscat off'
            ELOSS = 'eloss off'
            NREACT = 'nreact off'
            NESCAT = 'nescat off'
            GENXS = 'genxs hello'

        class bfld:
            FIELD = 'field 3.1'
            VEC = 'vec 3.1 3.1 3.1'
            MAXDEFLC = 'maxdeflc 3.1'
            MAXSTEP = 'maxstep 3.1'
            AXS = 'axs 3.1 3.1 3.1'
            FFEDGES = 'ffedges 3.1 3.1 3.1'
            REFPNT = 'refpnt 3.1 3.1 3.1'

        class sdef:
            CEL_0 = 'cel 1'
            CEL_1 = 'cel d1'
            CEL_2 = 'cel fara d1'
            SUR_0 = 'sur 1'
            SUR_1 = 'sur fara d1'
            ERG_0 = 'erg 3.1'
            ERG_1 = 'erg d1'
            ERG_2 = 'erg fara d1'
            TME_0 = 'tme 3.1'
            TME_1 = 'tme d1'
            TME_2 = 'tme fara d1'
            DIR_0 = 'dir 3.1'
            DIR_1 = 'dir d1'
            DIR_2 = 'dir fara d1'
            VEC_0 = 'vec 3.1 3.1 3.1'
            VEC_1 = 'vec fara d1'
            NRM_0 = 'nrm 1'
            NRM_1 = 'nrm fara d1'
            POS_0 = 'pos 3.1 3.1 3.1'
            POS_1 = 'pos d1'
            POS_2 = 'pos fara d1'
            RAD_0 = 'rad 3.1'
            RAD_1 = 'rad d1'
            RAD_2 = 'rad fara d1'
            EXT_0 = 'ext 3.1'
            EXT_1 = 'ext d1'
            EXT_2 = 'ext fara d1'
            AXS_0 = 'axs 3.1 3.1 3.1'
            AXS_1 = 'axs fara d1'
            X_0 = 'x 3.1'
            X_1 = 'x d1'
            X_2 = 'x fara d1'
            Y_0 = 'y 3.1'
            Y_1 = 'y d1'
            Y_2 = 'y fara d1'
            Z_0 = 'z 3.1'
            Z_1 = 'z d1'
            Z_2 = 'z fara d1'
            CCC_0 = 'ccc 1'
            CCC_1 = 'ccc fara d1'
            ARA_0 = 'ara 3.1'
            ARA_1 = 'ara fara d1'
            WGT_0 = 'wgt 3.1'
            WGT_1 = 'wgt fara d1'
            TR_0 = 'tr 1'
            TR_1 = 'tr d1'
            TR_2 = 'tr fara d1'
            EFF_0 = 'eff 3.1'
            EFF_1 = 'eff fara d1'
            PAR_0 = 'par hello'
            PAR_1 = 'par fara d1'
            DAT_0 = 'dat 1 1 1'
            DAT_1 = 'dat fara d1'
            LOC_0 = 'loc 3.1 3.1 3.1'
            LOC_1 = 'loc fara d1'
            BEM_0 = 'bem 3.1 3.1 3.1'
            BEM_1 = 'bem fara d1'
            BAP_0 = 'bap 3.1 3.1 3.1'
            BAP_1 = 'bap fara d1'

            class f:
                FCEL = 'fcel d1'
                FSUR = 'fsur d1'
                FERG = 'ferg d1'
                FTME = 'ftme d1'
                FDIR = 'fdir d1'
                FVEC = 'fvec d1'
                FNRM = 'fnrm d1'
                FPOS = 'fpos d1'
                FRAD = 'frad d1'
                FEXT = 'fext d1'
                FAXS = 'faxs d1'
                FX = 'fx d1'
                FY = 'fy d1'
                FZ = 'fz d1'
                FCCC = 'fccc d1'
                FARA = 'fara d1'
                FWGT = 'fwgt d1'
                FTR = 'ftr d1'
                FEFF = 'feff d1'
                FPAR = 'fpar d1'
                FDAT = 'fdat d1'
                FLOC = 'floc d1'
                FBEM = 'fbem d1'
                FBAP = 'fbap d1'

            class tme_1:
                EMBEDDED = 'd1 < d2'

        class ssw:
            SYM = 'sym 1'
            PTY = 'pty @ @ @'
            CEL = 'cel 1 1 1'

        class ssr:
            OLD = 'old 1 1 1'
            CEL = 'cel 1 1 1'
            NEW = 'new 1 1 1'
            PTY = 'pty @ @ @'
            COL = 'col 1'
            WGT = 'wgt 3.1'
            TR_0 = 'tr d1'
            TR_1 = 'tr 1'
            PSC = 'psc 3.1'
            AXS = 'axs 3.1 3.1 3.1'
            EXT = 'ext d1'
            POA = 'poa 3.1'
            BCW = 'bcw 3.1 0.8 3.1'

        class kopts:
            BLOCKSIZE = 'blocksize 2'
            KINETICS = 'kinetics yes'
            PRECURSOR = 'precursor yes'
            KSENTAL = 'ksental mctal'
            FMAT = 'fmat yes'
            FMATSKPT = 'fmatskpt 3.1'
            FMATNCYC = 'fmatncyc 3.1'
            FMATSPACE = 'fmatspace 3.1'
            FMATACCEL = 'fmataccel yes'
            FMATREDUCE = 'fmatreduce yes'
            FMATNX = 'fmatnx 3.1'
            FMATNY = 'fmatny 3.1'
            FMATNZ = 'fmatnz 3.1'

        class t_1:
            CBEG = 'cbeg 3.1'
            CFRQ = 'cfrq 3.1'
            COFI = 'cofi 3.1'
            CONI = 'coni 3.1'
            CSUB = 'csub 1'
            CEND = 'cend 3.1'

        class df_1:
            IU = 'iu 1'
            FAC = 'fac 1'
            IC = 'ic 10'
            LOG = 'log'
            LIN = 'lin'

        class pert:
            CELL = 'cell 1 1 1'
            MAT = 'mat 1'
            RHO = 'rho 3.1'
            METHOD = 'method 1'
            ERG = 'erg 3.1 3.1'
            RXN = 'rxn 1 1 1'

        class kpert:
            CELL = 'cell 1 1 1'
            MAT = 'mat 1 1 1'
            RHO = 'rho 3.1 3.1 3.1'
            ISO = 'iso 001001 001001 001001'
            RXN = 'rxn 1 1 1'
            ERG = 'erg 3.1 3.1 3.1'
            LINEAR = 'linear yes'

        class ksen:
            ISO = 'iso 001001 001001 001001'
            RXN = 'rxn 1 1 1'
            MT = 'mt 1 1 1'
            ERG = 'erg 3.1 3.1 3.1'
            EIN = 'ein 3.1 3.1 3.1'
            LEGENDRE = 'legendre 1'
            COS = 'cos 3.1 3.1 3.1'
            CONSTRAIN = 'constrain yes'

        class fmesh:
            GEOM = 'geom xyz'
            ORIGIN = 'origin 3.1 3.1 3.1'
            AXS = 'axs 3.1 3.1 3.1'
            VEC = 'vec 3.1 3.1 3.1'
            IMESH = 'imesh 3.1 3.1 3.1'
            IINTS = 'iints 1 1 1'
            JMESH = 'jmesh 3.1 3.1 3.1'
            JINTS = 'jints 1 1 1'
            KMESH = 'kmesh 3.1 3.1 3.1'
            KINTS = 'kints 1 1 1'
            EMESH = 'emesh 3.1'
            EINTS = 'eints 1'
            ENORM = 'enorm yes'
            TMESH = 'tmesh 3.1'
            TINTS = 'tints 1'
            TNORM = 'tnorm yes'
            FACTOR = 'factor 3.1'
            OUT = 'out col'
            TR = 'tr 1'
            INC = 'inc 3.1 3.1'
            TYPE = 'type flux'
            KCLEAR = 'kclear 1'

        class var:
            RR = 'rr no'

        class mesh:
            GEOM = 'geom xyz'
            REF = 'ref 3.1 3.1 3.1'
            ORIGIN = 'origin 3.1 3.1 3.1'
            AXS = 'axs 3.1 3.1 3.1'
            VEC = 'vec 3.1 3.1 3.1'
            IMESH = 'imesh 3.1 3.1 3.1'
            IINTS = 'iints 1 1 1'
            JMESH = 'jmesh 3.1 3.1 3.1'
            JINTS = 'jints 1 1 1'
            KMESH = 'kmesh 3.1 3.1 3.1'
            KINTS = 'kints 1 1 1'

        class stop:
            NPS = 'nps 1 1'
            CTME = 'ctme 3.1'
            F = 'f1 1'

        class ptrac:
            BUFFER = 'buffer 1'
            FILE = 'file asc'
            MAX = 'max 1'
            MEPH = 'meph 1'
            WRITE = 'write pos'
            CONIC = 'conic col'
            EVENT = 'event hello hello hello'
            FILTER = 'filter 3.1,hello,3.1 3.1,hello,3.1 3.1,hello,3.1'
            TYPE = 'type @ @ @'
            NPS = 'nps 1 1 1'
            CELL = 'cell 1 1 1'
            SURFACE = 'surface 1 1 1'
            TALLY = 'tally 1 1 1'
            VALUE = 'value 3.1'

            class filter:
                ENTRY = '3.1,hello,4.1'

        class mplot:
            TERM = 'term 1'
            FILE = 'file all'
            COPLOT = 'coplot'
            FREQ = 'freq 1'
            RETURN = 'return'
            PLOT = 'plot'
            PAUSE = 'pause 1'
            END = 'end'
            OPTIONS = 'options'
            HELP = 'help'
            STATUS = 'status'
            PRINTAL = 'printal'
            IPTAL = 'iptal'
            PRINTPTS = 'printpts'
            RUNTPE = 'runtpe hello 1'
            DUMP = 'dump 1'
            WMCTAL = 'wmctal hello'
            RMCTAL = 'rmctal hello'
            TALLY = 'tally 1'
            PERT = 'pert 1'
            LETHARGY = 'lethargy'
            NONORM = 'nonorm'
            FACTOR = 'factor x 3.1 3.1'
            RESET = 'reset all'
            TITLE = 'title 1 "hello"'
            BELOW = 'below'
            SUBTITLE = 'subtitle 1 1 "hello"'
            XTITLE = 'xtitle "hello"'
            YTITLE = 'ytitle "hello"'
            ZTITLE = 'ztitle "hello"'
            LABEL = 'label "hello"'
            FREE = 'free f f all'
            FIXED = 'fixed f 1'
            SET = 'set 1 1 1 1 1 1 1 1'
            TFC = 'tfc hello'
            KCODE = 'kcode 1'
            XS_0 = 'xs 1'
            XS_1 = 'xs 001001'
            XS_2 = 'xs ?'
            MT = 'mt 1'
            PAR = 'par @'
            LINLIN = 'linlin'
            LINLOG = 'linlog'
            LOGLIN = 'loglin'
            LOGLOG = 'loglog'
            XLIMS = 'xlims 0.8 3.1 3.1'
            YLIMS = 'ylims 0.8 3.1 3.1'
            SCALES = 'scales 1'
            HIST = 'hist'
            PLINEAR = 'plinear'
            SPLINE = 'spline 3.1'
            BAR = 'bar'
            NOERRBAR = 'noerrbar'
            THICK = 'thick 3.1'
            THIN = 'thin'
            LEGEND = 'legend 3.1 3.1'
            CONTOUR = 'contour 3.1 3.1 3.1 pct'
            WASH = 'wash on'
            FMESH = 'fmesh 1'
            FMRELERR = 'fmrelerr 1'
            ZLEV = 'zlev hello hello hello'
            EBIN = 'ebin 1'
            TBIN = 'tbin 1'
            COP = 'cop'
            TAL = 'tal 1'

            class free:
                ALL = 'all'
                NOALL = 'noall'

            class contour:
                PCT = 'pct'
                LIN = 'lin'
                LOG = 'log'
                ALL = 'all'
                NOALL = 'noall'
                LINE = 'line'
                NOLINE = 'noline'
                COLOR = 'color'
                NOCOLOR = 'nocolor'

        class rand:
            GEN = 'gen 1'
            SEED = 'seed 1'
            STRIDE = 'stride 1'
            HIST = 'hist 1'

        class cell:
            IMP = 'imp:@=1'
            VOL = 'vol=1'
            PWT = 'pwt=3.1'
            EXT = 'ext:@=hello'
            FCL = 'fcl:@=0.8'
            WWN = 'wwn1:@=3.1'
            DXC = 'dxc1:@=0.8'
            NONU = 'nonu=1'
            PD = 'pd1=0.8'
            U = 'u=3.1'
            TRCL_0 = 'trcl=1'
            TRCL_1 = 'trcl=1 1 1 2 2 2 3 3 3 4 4 4'
            TRCL_2 = 'trcl=1 1 1 2 2 2 3 3 3'
            TRCL_3 = 'trcl=1 1 1 2 2 2 3 3'
            TRCL_4 = 'trcl=1 1 1 2 2 2'
            TRCL_5 = 'trcl=1 1 1'
            LAT = 'lat=1'
            FILL_0 = '*fill=1:2 1:2 1:2 1 1 1 1 1 1 1'
            FILL_1 = '*fill=1 1 1 1 2 2 2 3 3 3 4 4 4'
            FILL_2 = '*fill=1 1 1 1 2 2 2 3 3 3'
            FILL_3 = '*fill=1 1 1 1 2 2 2 3 3'
            FILL_4 = '*fill=1 1 1 1 2 2 2'
            FILL_5 = '*fill=1 1 1 1'
            FILL_6 = '*fill=1 1'
            ELPT = 'elpt:@=3.1'
            TMP = 'tmp1=3.1 3.1 3.1'
            COSY = 'cosy=1'
            BFLCL = 'bflcl=1'
            UNC = 'unc:@=1'

        class like:
            IMP = 'imp:@=1'
            VOL = 'vol=1'
            PWT = 'pwt=3.1'
            EXT = 'ext:@=hello'
            FCL = 'fcl:@=0.8'
            WWN = 'wwn1:@=3.1'
            DXC = 'dxc1:@=0.8'
            NONU = 'nonu=1'
            PD = 'pd1=0.8'
            U = 'u=3.1'
            TRCL_0 = 'trcl=1'
            TRCL_1 = 'trcl=1 1 1 2 2 2 3 3 3 4 4 4'
            TRCL_2 = 'trcl=1 1 1 2 2 2 3 3 3'
            TRCL_3 = 'trcl=1 1 1 2 2 2 3 3'
            TRCL_4 = 'trcl=1 1 1 2 2 2'
            TRCL_5 = 'trcl=1 1 1'
            LAT = 'lat=1'
            FILL_0 = '*fill=1:2 1:2 1:2 1 1 1 1 1 1 1'
            FILL_1 = '*fill=1 1 1 1 2 2 2 3 3 3 4 4 4'
            FILL_2 = '*fill=1 1 1 1 2 2 2 3 3 3'
            FILL_3 = '*fill=1 1 1 1 2 2 2 3 3'
            FILL_4 = '*fill=1 1 1 1 2 2 2'
            FILL_5 = '*fill=1 1 1 1'
            FILL_6 = '*fill=1 1'
            ELPT = 'elpt:@=3.1'
            TMP = 'tmp1=3.1 3.1 3.1'
            COSY = 'cosy=1'
            BFLCL = 'bflcl=1'
            UNC = 'unc:@=1'
            MAT = 'mat 1'
            RHO = 'rho -9'

        class surface:
            P_0 = 'p 1 1 1 1'
            P_1 = 'p 1 0 0 0 1 0 0 0 1'
            PX = 'px 1'
            PY = 'py 1'
            PZ = 'pz 1'
            SO = 'so 1'
            S = 's 1 1 1 1'
            SX = 'sx 1 1'
            SY = 'sy 1 1'
            SZ = 'sz 1 1'
            C_X = 'c/x 1 1 1'
            C_Y = 'c/y 1 1 1'
            C_Z = 'c/z 1 1 1'
            CX = 'cx 1'
            CY = 'cy 1'
            CZ = 'cz 1'
            K_X = 'k/x 1 1 1 1 1'
            K_Y = 'k/y 1 1 1 1 1'
            K_Z = 'k/z 1 1 1 1 1'
            KX = 'kx 1 1 1'
            KY = 'ky 1 1 1'
            KZ = 'kz 1 1 1'
            SQ = 'sq 1 1 1 1 1 1 1 1 1 1'
            GQ = 'gq 1 1 1 1 1 1 1 1 1 1'
            TX = 'tx 1 1 1 1 1 1'
            TY = 'ty 1 1 1 1 1 1'
            TZ = 'tz 1 1 1 1 1 1'
            X = 'x 1 1 1 1 1 1'
            Y = 'y 1 1 1 1 1 1'
            Z = 'z 1 1 1 1 1 1'
            BOX = 'box 1 1 1 1 1 1 1 1 1 1 1 1'
            RPP = 'rpp 1 1 1 1 1 1'
            SPH = 'sph 1 1 1 1'
            RCC = 'rcc 1 1 1 1 1 1 1'
            RHP = 'rhp 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
            REC = 'rec 1 1 1 1 1 1 1 1 1 1 1 1'
            TRC = 'trc 1 1 1 1 1 1 1 1'
            ELL = 'ell 1 1 1 1 1 1 1'
            WED = 'wed 1 1 1 1 1 1 1 1 1 1 1 1'
            ARB = 'arb 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'

    class outp:
        ANALYSIS_TALLY_FLUCTUATION = """
1analysis of the results in the tally fluctuation chart bin (tfc) for tally 1 with nps = 1000000             print table 160


 normed average tally per history  = 1.13338E-04          unnormed average tally per history  = 1.13338E-04
 estimated tally relative error    = 0.0981               estimated variance of the variance  = 0.0121
 relative error from zero tallies  = 0.0962               relative error from nonzero scores  = 0.0192

 number of nonzero history tallies =         108          efficiency for the nonzero tallies  = 0.0001
 history number of largest  tally  =      112938          largest  unnormalized history tally = 2.00000E+00
 (largest  tally)/(average tally)  = 1.76463E+04          (largest  tally)/(avg nonzero tally)= 1.90580E+00

 (confidence interval shift)/mean  = 0.0051               shifted confidence interval center  = 1.13921E-04


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.13338E-04             1.15338E-04                     0.017645
      relative error                  9.81244E-02             9.79695E-02                    -0.001578
      variance of the variance        1.20537E-02             1.22915E-02                     0.019724
      shifted center                  1.13921E-04             1.13934E-04                     0.000115
      figure of merit                 1.35377E+02             1.35805E+02                     0.003164

 there is not enough information in the largest  history scores (usually less than 500 scores) for a reliable estimate of the slope.
 the empirical history score probability density function appears to be increasing at the largest  history scores:
 please examine. see print table 161.
 the history score probability density function appears to have an unsampled region at the largest  history scores:
 please examine. see print table 161.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (1.303E+06)*( 1.019E-02)**2 = (1.303E+06)*(1.039E-04) = 1.354E+02
"""[1:]
        HEADER = """
          Code Name & Version = MCNP_6.20, 6.2.0
  
     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ 
    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        
   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     
  _/      _/      _/             _/    _/_/       _/           _/    _/    
 _/      _/        _/_/_/       _/      _/       _/             _/_/       
  
  +-----------------------------------------------------------------------+
  | Copyright (2018).  Los Alamos National Security, LLC.  All rights     !
  | reserved.                                                             !
  |  This material was produced under U.S. Government contract            !
  | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is        !
  | operated by Los Alamos National Security, LLC for the U.S.            !
  | Department of Energy. The Government is granted for itself and        !
  | others acting on its behalf a paid-up, nonexclusive, irrevocable      !
  | worldwide license in this material to reproduce, prepare derivative   !
  | works, and perform publicly and display publicly. Beginning five (5)  !
  | years after February 14, 2018, subject to additional five-year        !
  | worldwide renewals, the Government is granted for itself and others   !
  | acting on its behalf a paid-up, nonexclusive, irrevocable worldwide   !
  | license in this material to reproduce, prepare derivative works,      !
  | distribute copies to the public, perform publicly and display         !
  | publicly, and to permit others to do so. NEITHER THE UNITED STATES    !
  | NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL   !
  | SECURITY, LLC, NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY,        !
  | EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY  !
  | FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF ANY INFORMATION,     !
  | APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE  !
  | WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS.                            !
  +-----------------------------------------------------------------------+
  
"""[1:]
        MCNP = """
1mcnp     version 6     ld=02/20/18                     10/21/24 12:25:31 
 *************************************************************************                 probid =  10/21/24 12:25:31 
 i=F1.i o=F1.o

 
  comment.  Physics models disabled.
         1-       Isotropic neutron source over lunar regolith with two gamma detectors
         2-       c ============================================================
         3-       c                        cell cards
         4-       c ============================================================
         5-       100 100 -1.54 -1                          IMP:P,N=1 $ surface
         6-       200 300 -5.06 -2                          IMP:P,N=1 $ LaBr3
         7-       201 200 -5.1  -3                          IMP:P,N=1 $ CeBr3
         8-       777 900 -1e-6 1 2 3 -99                   IMP:P,N=1 $ Air
         9-       999 0 99                                  IMP:P,N=0 $ Graveyard
        10-       
        11-       c ============================================================
        12-       c                       surface cards
        13-       c ============================================================
        14-       1 RPP -300 300 -300 300 -150 -50       $ surface
        15-       2 RCC 50 0 0 0 0 7.62 3.81             $ 3-inch LaBr3 crystal
        16-       3 RCC -50 0 0 0 0 5.08 2.54            $ 2-inch CeBr3 crystal
        17-       99 SO 600                              $ World
        18-       
        19-       c ============================================================
        20-       c                      material cards
        21-       c ============================================================
        22-       c Lunar Highlands:
        23-       M100   13027      -0.1701            $ Al-027
        24-              20040      -0.131742819       $ Ca-040
        25-              20042      -0.000879273       $ Ca-042
        26-              20044      -0.002834874       $ Ca-044
        27-              26054      -0.00086506        $ Fe-054
        28-              26056      -0.013579592       $ Fe-056
        29-              26057      -0.000313612       $ Fe-057
        30-              8016       -0.45489192        $ O-016
        31-              19039      -0.0001865162      $ K-039
        32-              19041      -1.34604e-05       $ K-041
        33-              12024      -0.00402849        $ Mg-024
        34-              12025      -0.00051           $ Mg-025
        35-              12026      -0.00056151        $ Mg-026
        36-              11023      -0.0045            $ Na-023
        37-              14028      -0.190532718       $ Si-028
        38-              14029      -0.00967921        $ Si-029
        39-              14030      -0.006388072       $ Si-030
        40-              90232      -0.006             $ Th-232
        41-              22046      -6.6e-05           $ Ti-046
        42-              22047      -5.952e-05         $ Ti-047
        43-              22048      -0.00058976        $ Ti-048
        44-              22049      -4.328e-05         $ Ti-049
        45-              22050      -4.144e-05         $ Ti-050
        46-       c CeBr3:
        47-       M200   35079      -0.3199072536      $ Br-079
        48-              35081      -0.3111980011      $ Br-081
        49-              58140      -0.3262874023      $ Ce-140
        50-              58142      -0.040998962       $ Ce-142
        51-       c LaBr3:
        52-       M300   35079      -0.3209300771      $ Br-079
        53-              35081      -0.3121929789      $ Br-081
        54-              57139      -0.3665511205      $ La-139
        55-       c Air:
        56-       M900   8016      -0.2094897          $ O-016
        57-              7014      -0.7771608          $ N-014
        58-              18040     -0.00996035         $ Ar-040
        59-       c
        60-       c ============================================================
        61-       c                      source cards
        62-       c ============================================================
        63-       mode n p
  comment.  photonuclear physics may be needed (phys:p).
        64-       nps 1e6
        65-       c rand seed = 71129329235055
        66-       c source definition
        67-       sdef par=n erg=14.05
        68-       c tally information
        69-       c
        70-       F1:p 2.1 2.2 2.3 $ body, base, top
        71-       *C1 90 0
        72-       E1 0.1 511I 10
        73-       F21:p 3.1 3.2 3.3 $ body, base, top
        74-       *C21 90 0
        75-       E21 0.1 511I 10
        76-       c
        77-       c end of file

 ***************************************************
 * Random Number Generator  =                    1 *
 * Random Number Seed       =       19073486328125 *
 * Random Number Multiplier =       19073486328125 *
 * Random Number Adder      =                    0 *
 * Random Number Bits Used  =                   48 *
 * Random Number Stride     =               152917 *
 ***************************************************

 
  comment.  total nubar used if fissionable isotopes are present.

 surface        2.3 and surface        3.3 are the same.        3.3 will be deleted.
 
  comment.           1 surfaces were deleted for being the same as others.
 
  warning.  replacing eliminated surface with facet        2.3 in tally       21.
 
  warning.    4 materials had unnormalized fractions. print table 40.
"""[1:]
        NEUTRON_ACTIVITY = """
1neutron  activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1        1       10076        10000            2    2.0000E-04   1.3819E+01   1.3933E+01   9.9945E-01   1.1942E+04
        2        2           3            3            1    7.9710E-05   1.2184E+01   1.3180E+01   9.8234E-01   4.4652E+00
        3        3       10079        10000         5357    5.2183E-01   9.6845E+00   1.2274E+01   9.7811E-01   9.3059E+00

           total         20158        20003         5360    5.2211E-01
"""[1:-1]
        PHOTON_ACTIVITY = """
1photon   activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1      100          52      1116266      5140537    5.1841E+00   1.6803E+00   1.6803E+00   1.0080E+00   1.0659E+01
        2      200         316          512          860    8.6800E-04   2.1401E+00   2.1401E+00   1.0052E+00   3.5814E+00
        3      201         140          244          351    3.6137E-04   1.8982E+00   1.8982E+00   1.0191E+00   3.3707E+00
        4      777      236156       235894            8    8.0491E-06   2.2608E+00   2.2608E+00   1.0083E+00   2.0885E+07

           total        236664      1352916      5141756    5.1854E+00
"""[1:-1]
        PROBLEM_SUMMARY = """
1problem summary                                                                                                           

      run terminated when    10000000  particle histories were done.
+                                                                                                    10/23/24 18:49:52 

 =====>      71.59 M histories/hr    (based on wall-clock time in mcrun)


      Isotropic neutron source over lunar regolith with two gamma detectors     probid =  10/23/24 18:41:28 

 neutron creation    tracks      weight        energy            neutron loss        tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source            10000000    1.0000E+00    1.4050E+01          escape             8340143    8.3401E-01    8.8893E+00
 nucl. interaction        0    0.            0.                  energy cutoff            0    0.            0.        
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    0.            0.                  weight cutoff            0    0.            0.        
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 upscattering             0    0.            2.7739E-09          downscattering           0    0.            3.1523E+00
 photonuclear             0    0.            0.                  capture            1709465    1.7095E-01    1.9574E+00
 (n,xn)               91097    9.1097E-03    1.1649E-02          loss to (n,xn)       44874    4.4874E-03    6.2132E-02
 prompt fission        4686    4.6860E-04    8.9758E-04          loss to fission       1356    1.3560E-04    1.4918E-03
 delayed fission         55    5.5000E-06    2.7253E-06          nucl. interaction        0    0.            0.        
 prompt photofis          0    0.            0.                  particle decay           0    0.            0.        
 tabular boundary         0    0.            0.                  tabular boundary         0    0.            0.        
 tabular sampling         0    0.            0.                  elastic scatter          0    0.            0.        
     total         10095838    1.0096E+00    1.4063E+01              total         10095838    1.0096E+00    1.4063E+01

   number of neutrons banked                   49608        average time of (shakes)              cutoffs
   neutron tracks per source particle     1.0096E+00          escape            5.8041E+03          tco   1.0000E+33
   neutron collisions per source particle 9.2106E+00          capture           3.9507E+03          eco   0.0000E+00
   total neutron collisions                 92105606          capture or escape 5.4888E+03          wc1   0.0000E+00
   net multiplication              1.0050E+00 0.0000          any termination   5.4637E+03          wc2   0.0000E+00

 photon creation     tracks      weight        energy            photon loss         tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source                   0    0.            0.                  escape             2376525    2.3765E-01    5.3734E-01
 nucl. interaction        0    0.            0.                  energy cutoff            2    1.9887E-07    6.4567E-05
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    0.            0.                  weight cutoff            0    0.            0.        
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 from neutrons      6704145    6.7040E-01    2.1970E+00          compton scatter          0    0.            1.4052E+00
 bremsstrahlung     3206266    3.2062E-01    3.4894E-02          capture           10551627    1.0551E+00    7.2990E-02
 p-annihilation      991806    9.9180E-02    5.0682E-02          pair production     495903    4.9590E-02    2.7765E-01
 photonuclear             0    0.            0.                  photonuclear abs         0    0.            0.        
 electron x-rays          0    0.            0.                  loss to photofis         0    0.            0.        
 compton fluores          0    0.            0.                                                                        
 muon capt fluores        0    0.            0.                                                                        
 1st fluorescence   2194184    2.1941E-01    1.0173E-02                                                                
 2nd fluorescence    327656    3.2765E-02    4.6203E-04                                                                
 cerenkov                 0    0.            0.                                                                        
 (gamma,xgamma)           0    0.            0.                                                                        
 tabular sampling         0    0.            0.                                                                        
 prompt photofis          0    0.            0.                                                                        
     total         13424057    1.3424E+00    2.2932E+00              total         13424057    1.3424E+00    2.2932E+00

   number of photons banked                 11229871        average time of (shakes)              cutoffs
   photon tracks per source particle      1.3424E+00          escape            8.8021E+02          tco   1.0000E+33
   photon collisions per source particle  5.1783E+00          capture           2.4146E+03          eco   1.0000E-03
   total photon collisions                  51782677          capture or escape 2.1325E+03          wc1   0.0000E+00
                                                              any termination   2.1263E+03          wc2   0.0000E+00

 computer time so far in this run     3.99 minutes            maximum number ever in bank        26
 computer time in mcrun               3.98 minutes            bank overflows to backup file       0
 source particles per minute            2.5151E+06
 random numbers generated               1765025087            most random numbers used was       12077 in history     1159964

 range of sampled source weights = 1.0000E+00 to 1.0000E+00
"""[1:]
        STARTING_MCRUN = """
1starting mcrun.      cp0 =  0.00                                                                       print table 110

      lattice example 18                                                              


     nps    x          y          z          cell       surf     u          v          w        energy     weight      time
 
      1 -1.933E+00 -4.878E+00  2.138E+00        5            -9.600E-02  9.907E-01  9.642E-02  6.632E+00  3.500E-01  0.000E+00
        -1.498E-01 -1.272E+00  1.138E+00       10            -7.104E-01  6.972E-01  9.642E-02                                 
        -2.498E-01 -3.724E-01  1.138E+00       15          0 -7.104E-01  6.972E-01  9.642E-02                                 
 warning.  tally not scored beyond last energy bin.                    
 nps =       40899     nrn =                  67 tal =    4     erg = 1.3903E+01      
"""[1:]
        TALLY_1A = """
1tally        1        nps =    10000000
           tally type 1    number of particles crossing a surface.                             
           particle(s): photons  
 
 surface  2.1                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   8.29996E-06 0.1098
    1.1934E-01   3.80440E-06 0.1622
    1.3867E-01   2.70000E-06 0.1924
      total      1.49149E-04 0.0259
 
 surface  2.1                                                                                                                          
 angle  bin:   0.90000E+02 to  0.00000E+00 degrees                                                                                     
      energy   
    1.0000E-01   1.50000E-06 0.2749
    1.1934E-01   8.99962E-07 0.3333
    1.3867E-01   9.00000E-07 0.3333
      total      1.13262E-04 0.0319
 
 surface  2.2                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   0.00000E+00 0.0000
    1.1934E-01   0.00000E+00 0.0000
    1.3867E-01   0.00000E+00 0.0000
      total      0.00000E+00 0.0000
 
 surface  2.2                                                                                                                          
 angle  bin:   0.90000E+02 to  0.00000E+00 degrees                                                                                     
      energy   
    1.0000E-01   3.99999E-07 0.5000
    1.1934E-01   4.00000E-07 0.5000
    1.3867E-01   0.00000E+00 0.0000
      total      5.93995E-05 0.0423
 
 surface  2.3                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   9.09998E-06 0.1048
    1.1934E-01   5.69996E-06 0.1325
    1.3867E-01   4.69996E-06 0.1459
      total      1.98462E-04 0.0225
 
 surface  2.3                                                                                                                          
 angle  bin:   0.90000E+02 to  0.00000E+00 degrees                                                                                     
      energy   
    1.0000E-01   9.99999E-07 0.3162
    1.1934E-01   3.99999E-07 0.5000
    1.3867E-01   6.00000E-07 0.4082
      total      1.75999E-05 0.0762


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        1

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.03      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.0972E-04 to 1.1695E-04; 1.0610E-04 to 1.2056E-04; 1.0249E-04 to 1.2417E-04
 estimated  symmetric confidence interval(1,2,3 sigma): 1.0965E-04 to 1.1687E-04; 1.0604E-04 to 1.2049E-04; 1.0243E-04 to 1.2410E-04

"""[1:-1]
        TALLY_1B = """
1tally        1        nps =     1000000
           tally type 1    number of particles crossing a surface.                             
           particle(s): photons  
 
 surface  2.1                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   1.03581E-05 0.3177
    1.1934E-01   3.00000E-06 0.5773
    1.3867E-01   5.02454E-06 0.4472
      total      1.61175E-04 0.0791
 
 surface  2.1                                                                                                                          
 angle  bin:   0.90000E+02 to  0.00000E+00 degrees                                                                                     
      energy   
    1.0000E-01   3.11418E-06 0.5781
    1.1934E-01   0.00000E+00 0.0000
    1.3867E-01   1.99999E-06 0.7071
      total      1.13338E-04 0.0981
 
 surface  2.2                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   0.00000E+00 0.0000
    1.1934E-01   0.00000E+00 0.0000
    1.3867E-01   0.00000E+00 0.0000
      total      0.00000E+00 0.0000
 
 surface  2.2                                                                                                                          
 angle  bin:   0.90000E+02 to  0.00000E+00 degrees                                                                                     
      energy   
    1.0000E-01   0.00000E+00 0.0000
    1.1934E-01   0.00000E+00 0.0000
    1.3867E-01   0.00000E+00 0.0000
      total      7.22900E-05 0.1179
 
 surface  2.3                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   1.50736E-05 0.2582
    1.1934E-01   8.04909E-06 0.3536
    1.3867E-01   9.04909E-06 0.3333
      total      2.18636E-04 0.0682
 
 surface  2.3                                                                                                                          
 angle  bin:   0.90000E+02 to  0.00000E+00 degrees                                                                                     
      energy   
    1.0000E-01   5.00000E-06 0.4472
    1.1934E-01   0.00000E+00 0.0000
    1.3867E-01   0.00000E+00 0.0000
      total      2.13311E-05 0.2185


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        1

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.10      yes          yes            0.01      yes         yes            constant    random       0.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes          no

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

"""[1:-1]
        TALLY_2 = """
1tally        2        nps =      100000
           tally type 2    particle flux averaged over a surface.       units   1/cm**2        
           particle(s): neutrons 

           areas   
                surface:       8                                                                                   
                         1.25664E+01
 
      surface:           8                                                                                         
        time   
    0.0000E+00   0.00000E+00 0.0000
    1.0000E+02   7.79859E-05 0.1010
    2.0000E+02   8.51479E-05 0.0966
      total      7.95775E-02 0.0000


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        2

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed    constant       0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 7.9577E-02 to 7.9577E-02; 7.9577E-02 to 7.9577E-02; 7.9577E-02 to 7.9577E-02
 estimated  symmetric confidence interval(1,2,3 sigma): 7.9577E-02 to 7.9577E-02; 7.9577E-02 to 7.9577E-02; 7.9577E-02 to 7.9577E-02

"""[1:-1]
        TALLY_4 = """
1tally       14        nps =  1000000000
           tally type 4    track length estimate of particle flux.      units   1/cm**2        
           particle(s): photons  

           volumes 
                   cell:      12                                                                                   
                         2.86848E+03
 
 cell  12                                                                                                                              
      energy   
    1.0000E-01   3.62214E-07 0.0025
    1.9099E+00   4.26948E-09 0.0228
    1.9198E+00   4.10659E-09 0.0231
      total      6.83312E-06 0.0008


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally       14

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.00      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 6.8273E-06 to 6.8389E-06; 6.8215E-06 to 6.8447E-06; 6.8157E-06 to 6.8505E-06
 estimated  symmetric confidence interval(1,2,3 sigma): 6.8273E-06 to 6.8389E-06; 6.8215E-06 to 6.8447E-06; 6.8157E-06 to 6.8505E-06

"""[1:-1]
        TALLY_8A = """
1tally       18        nps =    10000000
           tally type 8    pulse height distribution.                   units   number         
           particle(s): photons  
 
 cell  200                                                                                                                             
      energy   
    1.0000E-01   1.08900E-04 0.0303
    1.1934E-01   8.30000E-06 0.1098
    1.3867E-01   7.80000E-06 0.1132
      total      2.89500E-04 0.0186


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally       18

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.02      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 2.8417E-04 to 2.9493E-04; 2.7879E-04 to 3.0031E-04; 2.7341E-04 to 3.0569E-04
 estimated  symmetric confidence interval(1,2,3 sigma): 2.8412E-04 to 2.9488E-04; 2.7874E-04 to 3.0026E-04; 2.7336E-04 to 3.0564E-04

"""[1:-1]
        TALLY_8B = """
1tally       18        nps =    10000000
           tally type 8    pulse height distribution.                   units   number         
           particle(s): photons  
 
 cell  200                                                                                                                             
      energy   
    1.0000E-01   1.08900E-04 0.0303
    1.1934E-01   8.30000E-06 0.1098
    1.3867E-01   7.80000E-06 0.1132
      total      2.89500E-04 0.0186


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally       18

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.02      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass  1 of the 10 statistical checks.

"""[1:-1]
        UNNORMED_TALLY_DENSITY = """
1unnormed tally density for tally 4          nonzero tally mean(m) = 5.406E+00   nps = 1000000               print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 5.7)
  tally  number num den log den:d------------------d-------------------d--------------------d-------------------d-------------------
 7.94-04      1 6.12-03  -2.213 *******************|*******************|********************|*******************|*******************
 1.00-03      0 0.00+00   0.000                    |                   |                    |                   |                   
 1.58-02      2 6.14-04  -3.212 *******************|*******************|********************|*******************|                   
  total    2313 2.31-03         d------------------d-------------------d--------------------d-------------------d-------------------
"""[1:-1]

        class tally:
            SUBTALLY_1 = """
 surface  2.1                                                                                                                          
 angle  bin:  180.0        to  0.90000E+02 degrees                                                                                     
      energy   
    1.0000E-01   8.29996E-06 0.1098
    1.1934E-01   3.80440E-06 0.1622
    1.3867E-01   2.70000E-06 0.1924
      total      1.49149E-04 0.0259

"""[1:]
            SUBTALLY_2 = """
      surface:           8                                                                                         
        time   
    0.0000E+00   0.00000E+00 0.0000
    1.0000E+02   7.79859E-05 0.1010
    2.0000E+02   8.51479E-05 0.0966
      total      7.95775E-02 0.0000

"""[1:]
            SUBTALLY_4 = """
 cell  12                                                                                                                              
      energy   
    1.0000E-01   3.62214E-07 0.0025
    1.9099E+00   4.26948E-09 0.0228
    1.9198E+00   4.10659E-09 0.0231
      total      6.83312E-06 0.0008

"""[1:]

            class subtally:
                LINE = '    1.0000E-01   3.62214E-07 0.0025\n'

    class ptrac:
        HEADER = """
   -1
mcnp    6                        05/08/13 01/08/25 08:25:00 
Pulsed neutron source over lunar regolith with a neutron detector               
   1.4000E+01  1.0000E+00  1.0000E+02  0.0000E+00  1.0000E+00  2.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  1.0000E+00
   1.0000E+09  0.0000E+00  0.0000E+00  0.0000E+00  2.0000E+00 -1.0000E+00 -2.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00
   1.0000E+00  2.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00
     4    6    9    7    9    7    9    7    9    7    9    1    4    0    0    0    0    0    0    0
    1   2   5   6   7   8   9  17  18  19  20  21  22  23  24  25  26  27  28   7   8  10  11  17  18  19  20  21  22  23
   24  25  26  27  28   7   8  12  13  17  18  19  20  21  22  23  24  25  26  27  28   7   8  10  11  17  18  19  20  21
   22  23  24  25  26  27  28   7   8  14  15  17  18  19  20  21  22  23  24  25  26  27  28
"""[1:]
        HISTORY = """
       7496      2007        24  4.05973E-02
       9000         3     14030         2       100         1         3
  -0.19401E+02 -0.35503E+01 -0.10317E+03 -0.53898E+00 -0.84167E+00 -0.33130E-01  0.95589E+00  0.63221E+00  0.21010E+01
"""[1:]

        class header:
            V = """
   1.4000E+01  1.0000E+00  1.0000E+02  0.0000E+00  1.0000E+00  2.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00  1.0000E+00
   1.0000E+09  0.0000E+00  0.0000E+00  0.0000E+00  2.0000E+00 -1.0000E+00 -2.0000E+00  1.0000E+00  1.0000E+00  0.0000E+00
   1.0000E+00  2.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00
"""[1:]
            N = '     4    6    9    7    9    7    9    7    9    7    9    1    4    0    0    0    0    0    0    0\n'
            L = """
    1   2   5   6   7   8   9  17  18  19  20  21  22  23  24  25  26  27  28   7   8  10  11  17  18  19  20  21  22  23
   24  25  26  27  28   7   8  12  13  17  18  19  20  21  22  23  24  25  26  27  28   7   8  10  11  17  18  19  20  21
   22  23  24  25  26  27  28   7   8  14  15  17  18  19  20  21  22  23  24  25  26  27  28
"""[1:]

        class history:
            I = '       7496      2007        24  4.05973E-02'
            EVENT = """
       9000         3     14030         2       100         1         3
  -0.19401E+02 -0.35503E+01 -0.10317E+03 -0.53898E+00 -0.84167E+00 -0.33130E-01  0.95589E+00  0.63221E+00  0.21010E+01
"""[1:]

            class event:
                J_0 = '       9000         3     14030         2       100'
                J_1 = '       9000         3     14030         2       100         1'
                J_2 = '       9000         3     14030         2       100         1'
                J_3 = '       9000         3     14030         2       100         1         3'
                J_4 = '       9000         3     14030         2       100         1'
                J_5 = '       9000         3     14030         2       100         1         3'
                J_6 = '       9000         3     14030         2       100         1         3'
                J_7 = '       9000         3     14030         2       100         1         3         4'
                P_0 = '  -0.19401E+02 -0.35503E+01 -0.10317E+03'
                P_1 = '  -0.19401E+02 -0.35503E+01 -0.10317E+03 -0.53898E+00 -0.84167E+00 -0.33130E-01  0.95589E+00  0.63221E+00  0.21010E+01'

                class j:
                    EVENT_TYPE = '9000'

    class meshtal:
        HEADER = """
mcnp   version 6     ld=02/20/18  probid =  11/01/24 10:26:01 
 Isotropic neutron source over lunar regolith with two gamma detectors
 Number of histories used for normalizing tallies =      10000000.00

 Mesh Tally Number         4
 neutron  mesh tally.

 Tally bin boundaries:
    X direction:   -100.00    -80.00    -60.00    -40.00    -20.00      0.00     20.00     40.00     60.00     80.00    100.00
    Y direction:   -100.00    -80.00    -60.00    -40.00    -20.00      0.00     20.00     40.00     60.00     80.00    100.00
    Z direction:   -150.00   -149.00   -148.00   -147.00   -146.00   -145.00   -144.00   -143.00   -142.00   -141.00   -140.00   -139.00   -138.00   -137.00   -136.00   -135.00   -134.00   -133.00   -132.00   -131.00   -130.00   -129.00   -128.00   -127.00   -126.00   -125.00   -124.00   -123.00   -122.00   -121.00   -120.00   -119.00   -118.00   -117.00   -116.00   -115.00   -114.00   -113.00   -112.00   -111.00   -110.00   -109.00   -108.00   -107.00   -106.00   -105.00   -104.00   -103.00   -102.00   -101.00   -100.00    -99.00    -98.00    -97.00    -96.00    -95.00    -94.00    -93.00    -92.00    -91.00    -90.00    -89.00    -88.00    -87.00    -86.00    -85.00    -84.00    -83.00    -82.00    -81.00    -80.00    -79.00    -78.00    -77.00    -76.00    -75.00    -74.00    -73.00    -72.00    -71.00    -70.00    -69.00    -68.00    -67.00    -66.00    -65.00    -64.00    -63.00    -62.00    -61.00    -60.00    -59.00    -58.00    -57.00    -56.00    -55.00    -54.00    -53.00    -52.00    -51.00    -50.00
    Energy bin boundaries: 0.00E+00 1.00E+36

        X         Y         Z     Result     Rel Error
"""[1:]
        TALLY = '    -90.000   -90.000  -149.500 3.99211E+00 3.16463E-02'


class ast:
    INP = pymcnp.Inp.from_mcnp(string.INP)
    OUTP = pymcnp.Outp.from_mcnp(string.OUTP)
    PTRAC = pymcnp.Ptrac.from_mcnp(string.PTRAC)
    MESHTAL = pymcnp.Meshtal.from_mcnp(string.MESHTAL)

    class _show:
        class pyvista:
            BOX = pymcnp._show.pyvista.Box(0.5, 0.5, 0.5)
            EMPTY = pymcnp._show.pyvista.Empty()
            CONETRUNCATED = pymcnp._show.pyvista.ConeTruncated(0.5, 0.5, 0.5)
            CONEUNBOUNDED = pymcnp._show.pyvista.ConeUnbounded(0.5, 1)
            CYLINDERCIRCULAR = pymcnp._show.pyvista.CylinderCircular(0.5, 0.5)
            CYLINDERELLIPTICAL = pymcnp._show.pyvista.CylinderElliptical(0.5, 0.5, 0.5)
            CYLINDERHEXAGONAL = pymcnp._show.pyvista.CylinderHexagonal(0.5, 0.5, 0.5, 0.5)
            CYLINDERUNBOUNDED = pymcnp._show.pyvista.CylinderUnbounded(0.5)
            ELLIPSOID = pymcnp._show.pyvista.Ellipsoid(0.5, 0.5)
            PARALLELIPIPED = pymcnp._show.pyvista.Parallelipiped(0.5, 0.5, 0.5, 0.5, 0.5, 0.5)
            PLANE = pymcnp._show.pyvista.Plane(0.5, 0.5, 0.5, 0.5)
            SPHERE = pymcnp._show.pyvista.Sphere(0.5)
            TORUS = pymcnp._show.pyvista.Torus(0.5, 0.5, 0.5)
            WEDGE = pymcnp._show.pyvista.Wedge(0.5, 0.5, 0.5)

    class types:
        LATTICE = pymcnp.types.Lattice.from_mcnp(string.types.LATTICE)
        GEOMETRY = pymcnp.types.Geometry.from_mcnp(string.types.GEOMETRY)
        REPEAT = pymcnp.types.Repeat.from_mcnp(string.types.REPEAT)
        INSERT = pymcnp.types.Insert.from_mcnp(string.types.INSERT)
        MULTIPLY = pymcnp.types.Multiply.from_mcnp(string.types.MULTIPLY)
        JUMP = pymcnp.types.Jump.from_mcnp(string.types.JUMP)
        LOG = pymcnp.types.Log.from_mcnp(string.types.LOG)
        INTEGER = pymcnp.types.Integer.from_mcnp(string.types.INTEGER)
        REAL = pymcnp.types.Real.from_mcnp(string.types.REAL)
        STRING = pymcnp.types.String.from_mcnp(string.types.STRING)
        DISTRIBUTION = pymcnp.types.Distribution.from_mcnp(string.types.DISTRIBUTION)
        ZAID = pymcnp.types.Zaid.from_mcnp(string.types.ZAID)
        DESIGNATOR = pymcnp.types.Designator.from_mcnp(string.types.DESIGNATOR)
        SUBSTANCE = pymcnp.types.Substance.from_mcnp(string.types.SUBSTANCE)
        TRANSFORMATION_0 = pymcnp.types.Transformation_0.from_mcnp(string.types.TRANSFORMATION_0)
        TRANSFORMATION_1 = pymcnp.types.Transformation_1.from_mcnp(string.types.TRANSFORMATION_1)
        TRANSFORMATION_2 = pymcnp.types.Transformation_2.from_mcnp(string.types.TRANSFORMATION_2)
        TRANSFORMATION_3 = pymcnp.types.Transformation_3.from_mcnp(string.types.TRANSFORMATION_3)
        TRANSFORMATION_4 = pymcnp.types.Transformation_4.from_mcnp(string.types.TRANSFORMATION_4)
        INDEX = pymcnp.types.Index.from_mcnp(string.types.INDEX)

    class inp:
        CELL = pymcnp.inp.Cell.from_mcnp(string.inp.CELL)
        LIKE = pymcnp.inp.Like.from_mcnp(string.inp.LIKE)
        SURFACE = pymcnp.inp.Surface.from_mcnp(string.inp.SURFACE)
        COMMENT = pymcnp.inp.Comment.from_mcnp(string.inp.COMMENT)
        VOL = pymcnp.inp.Vol.from_mcnp(string.inp.VOL)
        AREA = pymcnp.inp.Area.from_mcnp(string.inp.AREA)
        TR_0 = pymcnp.inp.Tr_0.from_mcnp(string.inp.TR_0)
        TR_1 = pymcnp.inp.Tr_1.from_mcnp(string.inp.TR_1)
        TR_2 = pymcnp.inp.Tr_2.from_mcnp(string.inp.TR_2)
        TR_3 = pymcnp.inp.Tr_3.from_mcnp(string.inp.TR_3)
        TR_4 = pymcnp.inp.Tr_4.from_mcnp(string.inp.TR_4)
        U = pymcnp.inp.U.from_mcnp(string.inp.U)
        LAT = pymcnp.inp.Lat.from_mcnp(string.inp.LAT)
        FILL = pymcnp.inp.Fill.from_mcnp(string.inp.FILL)
        URAN = pymcnp.inp.Uran.from_mcnp(string.inp.URAN)
        DM = pymcnp.inp.Dm.from_mcnp(string.inp.DM)
        DAWWG = pymcnp.inp.Dawwg.from_mcnp(string.inp.DAWWG)
        EMBED = pymcnp.inp.Embed.from_mcnp(string.inp.EMBED)
        EMBEE = pymcnp.inp.Embee.from_mcnp(string.inp.EMBEE)
        EMBEB = pymcnp.inp.Embeb.from_mcnp(string.inp.EMBEB)
        EMBEM = pymcnp.inp.Embem.from_mcnp(string.inp.EMBEM)
        EMBTB = pymcnp.inp.Embtb.from_mcnp(string.inp.EMBTB)
        EMBTM = pymcnp.inp.Embtm.from_mcnp(string.inp.EMBTM)
        EMBDB = pymcnp.inp.Embdb.from_mcnp(string.inp.EMBDB)
        EMBDF = pymcnp.inp.Embdf.from_mcnp(string.inp.EMBDF)
        M_0 = pymcnp.inp.M_0.from_mcnp(string.inp.M_0)
        M_1 = pymcnp.inp.M_1.from_mcnp(string.inp.M_1)
        MT = pymcnp.inp.Mt.from_mcnp(string.inp.MT)
        MX = pymcnp.inp.Mx.from_mcnp(string.inp.MX)
        OTFDB = pymcnp.inp.Otfdb.from_mcnp(string.inp.OTFDB)
        TOTNU = pymcnp.inp.Totnu.from_mcnp(string.inp.TOTNU)
        NONU = pymcnp.inp.Nonu.from_mcnp(string.inp.NONU)
        AWTAB = pymcnp.inp.Awtab.from_mcnp(string.inp.AWTAB)
        XS = pymcnp.inp.Xs.from_mcnp(string.inp.XS)
        VOID = pymcnp.inp.Void.from_mcnp(string.inp.VOID)
        MGOPT = pymcnp.inp.Mgopt.from_mcnp(string.inp.MGOPT)
        DRXS = pymcnp.inp.Drxs.from_mcnp(string.inp.DRXS)
        MODE = pymcnp.inp.Mode.from_mcnp(string.inp.MODE)
        PHYS_0 = pymcnp.inp.Phys_0.from_mcnp(string.inp.PHYS_0)
        PHYS_1 = pymcnp.inp.Phys_1.from_mcnp(string.inp.PHYS_1)
        PHYS_2 = pymcnp.inp.Phys_2.from_mcnp(string.inp.PHYS_2)
        PHYS_3 = pymcnp.inp.Phys_3.from_mcnp(string.inp.PHYS_3)
        PHYS_4 = pymcnp.inp.Phys_4.from_mcnp(string.inp.PHYS_4)
        ACT = pymcnp.inp.Act.from_mcnp(string.inp.ACT)
        CUT = pymcnp.inp.Cut.from_mcnp(string.inp.CUT)
        ELPT = pymcnp.inp.Elpt.from_mcnp(string.inp.ELPT)
        TMP = pymcnp.inp.Tmp.from_mcnp(string.inp.TMP)
        THTME = pymcnp.inp.Thtme.from_mcnp(string.inp.THTME)
        MPHYS = pymcnp.inp.Mphys.from_mcnp(string.inp.MPHYS)
        LCA = pymcnp.inp.Lca.from_mcnp(string.inp.LCA)
        LCB = pymcnp.inp.Lcb.from_mcnp(string.inp.LCB)
        LCC = pymcnp.inp.Lcc.from_mcnp(string.inp.LCC)
        LEA = pymcnp.inp.Lea.from_mcnp(string.inp.LEA)
        LEB = pymcnp.inp.Leb.from_mcnp(string.inp.LEB)
        FMULT = pymcnp.inp.Fmult.from_mcnp(string.inp.FMULT)
        TROPT = pymcnp.inp.Tropt.from_mcnp(string.inp.TROPT)
        UNC = pymcnp.inp.Unc.from_mcnp(string.inp.UNC)
        COSYP = pymcnp.inp.Cosyp.from_mcnp(string.inp.COSYP)
        COSY = pymcnp.inp.Cosy.from_mcnp(string.inp.COSY)
        BFLD = pymcnp.inp.Bfld.from_mcnp(string.inp.BFLD)
        BFLCL = pymcnp.inp.Bflcl.from_mcnp(string.inp.BFLCL)
        SDEF = pymcnp.inp.Sdef.from_mcnp(string.inp.SDEF)
        SI_0 = pymcnp.inp.Si_0.from_mcnp(string.inp.SI_0)
        SI_1 = pymcnp.inp.Si_1.from_mcnp(string.inp.SI_1)
        SI_2 = pymcnp.inp.Si_2.from_mcnp(string.inp.SI_2)
        SP_0 = pymcnp.inp.Sp_0.from_mcnp(string.inp.SP_0)
        SP_1 = pymcnp.inp.Sp_1.from_mcnp(string.inp.SP_1)
        SB_0 = pymcnp.inp.Sb_0.from_mcnp(string.inp.SB_0)
        SB_1 = pymcnp.inp.Sb_1.from_mcnp(string.inp.SB_1)
        DS_0 = pymcnp.inp.Ds_0.from_mcnp(string.inp.DS_0)
        DS_1 = pymcnp.inp.Ds_1.from_mcnp(string.inp.DS_1)
        DS_2 = pymcnp.inp.Ds_2.from_mcnp(string.inp.DS_2)
        DS_3 = pymcnp.inp.Ds_3.from_mcnp(string.inp.DS_3)
        SC = pymcnp.inp.Sc.from_mcnp(string.inp.SC)
        SSW = pymcnp.inp.Ssw.from_mcnp(string.inp.SSW)
        SSR = pymcnp.inp.Ssr.from_mcnp(string.inp.SSR)
        KCODE = pymcnp.inp.Kcode.from_mcnp(string.inp.KCODE)
        KSRC = pymcnp.inp.Ksrc.from_mcnp(string.inp.KSRC)
        KOPTS = pymcnp.inp.Kopts.from_mcnp(string.inp.KOPTS)
        HSRC = pymcnp.inp.Hsrc.from_mcnp(string.inp.HSRC)
        F_0 = pymcnp.inp.F_0.from_mcnp(string.inp.F_0)
        F_1 = pymcnp.inp.F_1.from_mcnp(string.inp.F_1)
        F_2 = pymcnp.inp.F_2.from_mcnp(string.inp.F_2)
        F_3 = pymcnp.inp.F_3.from_mcnp(string.inp.F_3)
        F_4 = pymcnp.inp.F_4.from_mcnp(string.inp.F_4)
        FIP = pymcnp.inp.Fip.from_mcnp(string.inp.FIP)
        FIR = pymcnp.inp.Fir.from_mcnp(string.inp.FIR)
        FIC = pymcnp.inp.Fic.from_mcnp(string.inp.FIC)
        FC = pymcnp.inp.Fc.from_mcnp(string.inp.FC)
        E = pymcnp.inp.E.from_mcnp(string.inp.E)
        T_0 = pymcnp.inp.T_0.from_mcnp(string.inp.T_0)
        T_1 = pymcnp.inp.T_1.from_mcnp(string.inp.T_1)
        C = pymcnp.inp.C.from_mcnp(string.inp.C)
        FQ = pymcnp.inp.Fq.from_mcnp(string.inp.FQ)
        FM = pymcnp.inp.Fm.from_mcnp(string.inp.FM)
        DE = pymcnp.inp.De.from_mcnp(string.inp.DE)
        DF_0 = pymcnp.inp.Df_0.from_mcnp(string.inp.DF_0)
        DF_1 = pymcnp.inp.Df_1.from_mcnp(string.inp.DF_1)
        EM = pymcnp.inp.Em.from_mcnp(string.inp.EM)
        TM = pymcnp.inp.Tm.from_mcnp(string.inp.TM)
        CM = pymcnp.inp.Cm.from_mcnp(string.inp.CM)
        CF = pymcnp.inp.Cf.from_mcnp(string.inp.CF)
        SF = pymcnp.inp.Sf.from_mcnp(string.inp.SF)
        FS = pymcnp.inp.Fs.from_mcnp(string.inp.FS)
        SD = pymcnp.inp.Sd.from_mcnp(string.inp.SD)
        FU = pymcnp.inp.Fu.from_mcnp(string.inp.FU)
        FT = pymcnp.inp.Ft.from_mcnp(string.inp.FT)
        TF_0 = pymcnp.inp.Tf_0.from_mcnp(string.inp.TF_0)
        TF_1 = pymcnp.inp.Tf_1.from_mcnp(string.inp.TF_1)
        NOTRN = pymcnp.inp.Notrn.from_mcnp(string.inp.NOTRN)
        PERT = pymcnp.inp.Pert.from_mcnp(string.inp.PERT)
        KPERT = pymcnp.inp.Kpert.from_mcnp(string.inp.KPERT)
        KSEN = pymcnp.inp.Ksen.from_mcnp(string.inp.KSEN)
        FMESH = pymcnp.inp.Fmesh.from_mcnp(string.inp.FMESH)
        SPDTL = pymcnp.inp.Spdtl.from_mcnp(string.inp.SPDTL)
        IMP = pymcnp.inp.Imp.from_mcnp(string.inp.IMP)
        VAR = pymcnp.inp.Var.from_mcnp(string.inp.VAR)
        WWE = pymcnp.inp.Wwe.from_mcnp(string.inp.WWE)
        WWT = pymcnp.inp.Wwt.from_mcnp(string.inp.WWT)
        WWN = pymcnp.inp.Wwn.from_mcnp(string.inp.WWN)
        WWP = pymcnp.inp.Wwp.from_mcnp(string.inp.WWP)
        WWG = pymcnp.inp.Wwg.from_mcnp(string.inp.WWG)
        WWGE = pymcnp.inp.Wwge.from_mcnp(string.inp.WWGE)
        WWGT = pymcnp.inp.Wwgt.from_mcnp(string.inp.WWGT)
        MESH = pymcnp.inp.Mesh.from_mcnp(string.inp.MESH)
        ESPLT = pymcnp.inp.Esplt.from_mcnp(string.inp.ESPLT)
        TSPLT = pymcnp.inp.Tsplt.from_mcnp(string.inp.TSPLT)
        EXT = pymcnp.inp.Ext.from_mcnp(string.inp.EXT)
        FCL = pymcnp.inp.Fcl.from_mcnp(string.inp.FCL)
        DXT = pymcnp.inp.Dxt.from_mcnp(string.inp.DXT)
        DD = pymcnp.inp.Dd.from_mcnp(string.inp.DD)
        PD = pymcnp.inp.Pd.from_mcnp(string.inp.PD)
        DXC = pymcnp.inp.Dxc.from_mcnp(string.inp.DXC)
        BBREM = pymcnp.inp.Bbrem.from_mcnp(string.inp.BBREM)
        PIKMT = pymcnp.inp.Pikmt.from_mcnp(string.inp.PIKMT)
        PWT = pymcnp.inp.Pwt.from_mcnp(string.inp.PWT)
        NPS = pymcnp.inp.Nps.from_mcnp(string.inp.NPS)
        CTME = pymcnp.inp.Ctme.from_mcnp(string.inp.CTME)
        STOP = pymcnp.inp.Stop.from_mcnp(string.inp.STOP)
        PRINT = pymcnp.inp.Print.from_mcnp(string.inp.PRINT)
        TALNP = pymcnp.inp.Talnp.from_mcnp(string.inp.TALNP)
        PRDMP = pymcnp.inp.Prdmp.from_mcnp(string.inp.PRDMP)
        PTRAC = pymcnp.inp.Ptrac.from_mcnp(string.inp.PTRAC)
        MPLOT = pymcnp.inp.Mplot.from_mcnp(string.inp.MPLOT)
        HISTP = pymcnp.inp.Histp.from_mcnp(string.inp.HISTP)
        RAND = pymcnp.inp.Rand.from_mcnp(string.inp.RAND)
        DBCN = pymcnp.inp.Dbcn.from_mcnp(string.inp.DBCN)
        LOST = pymcnp.inp.Lost.from_mcnp(string.inp.LOST)
        IDUM = pymcnp.inp.Idum.from_mcnp(string.inp.IDUM)
        RDUM = pymcnp.inp.Rdum.from_mcnp(string.inp.RDUM)
        ZA = pymcnp.inp.Za.from_mcnp(string.inp.ZA)
        ZB = pymcnp.inp.Zb.from_mcnp(string.inp.ZB)
        ZC = pymcnp.inp.Zc.from_mcnp(string.inp.ZC)
        ZD = pymcnp.inp.Zd.from_mcnp(string.inp.ZD)
        FILES = pymcnp.inp.Files.from_mcnp(string.inp.FILES)

        class dd:
            DIAGNOSTIC = pymcnp.inp.dd.Diagnostic.from_mcnp(string.inp.dd.DIAGNOSTIC)

        class ds_1:
            VARIABLES = pymcnp.inp.ds_1.Variables.from_mcnp(string.inp.ds_1.VARIABLES)

        class ds_2:
            VARIABLES = pymcnp.inp.ds_2.Variables.from_mcnp(string.inp.ds_2.VARIABLES)

        class dxt:
            SHELL = pymcnp.inp.dxt.Shell.from_mcnp(string.inp.dxt.SHELL)

        class f_1:
            SPHERE = pymcnp.inp.f_1.Sphere.from_mcnp(string.inp.f_1.SPHERE)

        class f_2:
            RING = pymcnp.inp.f_2.Ring.from_mcnp(string.inp.f_2.RING)

        class files:
            FILE = pymcnp.inp.files.File.from_mcnp(string.inp.files.FILE)

        class ksrc:
            LOCATION = pymcnp.inp.ksrc.Location.from_mcnp(string.inp.ksrc.LOCATION)

        class pikmt:
            PHOTONBIAS = pymcnp.inp.pikmt.Photonbias.from_mcnp(string.inp.pikmt.PHOTONBIAS)

        class uran:
            STOCHASTIC = pymcnp.inp.uran.Stochastic.from_mcnp(string.inp.uran.STOCHASTIC)

        class dawwg:
            POINTS = pymcnp.inp.dawwg.Points.from_mcnp(string.inp.dawwg.POINTS)
            XSEC = pymcnp.inp.dawwg.Xsec.from_mcnp(string.inp.dawwg.XSEC)
            BLOCK = pymcnp.inp.dawwg.Block.from_mcnp(string.inp.dawwg.BLOCK)

            class block:
                NGROUP = pymcnp.inp.dawwg.block.Ngroup.from_mcnp(string.inp.dawwg.block.NGROUP)
                ISN = pymcnp.inp.dawwg.block.Isn.from_mcnp(string.inp.dawwg.block.ISN)
                NISO = pymcnp.inp.dawwg.block.Niso.from_mcnp(string.inp.dawwg.block.NISO)
                MT = pymcnp.inp.dawwg.block.Mt.from_mcnp(string.inp.dawwg.block.MT)
                IQUAD = pymcnp.inp.dawwg.block.Iquad.from_mcnp(string.inp.dawwg.block.IQUAD)
                FMMIX = pymcnp.inp.dawwg.block.Fmmix.from_mcnp(string.inp.dawwg.block.FMMIX)
                NOSOLV = pymcnp.inp.dawwg.block.Nosolv.from_mcnp(string.inp.dawwg.block.NOSOLV)
                NOEDIT = pymcnp.inp.dawwg.block.Noedit.from_mcnp(string.inp.dawwg.block.NOEDIT)
                NOGEOD = pymcnp.inp.dawwg.block.Nogeod.from_mcnp(string.inp.dawwg.block.NOGEOD)
                NOMIX = pymcnp.inp.dawwg.block.Nomix.from_mcnp(string.inp.dawwg.block.NOMIX)
                NOASG = pymcnp.inp.dawwg.block.Noasg.from_mcnp(string.inp.dawwg.block.NOASG)
                NOMACR = pymcnp.inp.dawwg.block.Nomacr.from_mcnp(string.inp.dawwg.block.NOMACR)
                NOSLNP = pymcnp.inp.dawwg.block.Noslnp.from_mcnp(string.inp.dawwg.block.NOSLNP)
                NOEDTT = pymcnp.inp.dawwg.block.Noedtt.from_mcnp(string.inp.dawwg.block.NOEDTT)
                NOADJM = pymcnp.inp.dawwg.block.Noadjm.from_mcnp(string.inp.dawwg.block.NOADJM)
                LIB = pymcnp.inp.dawwg.block.Lib.from_mcnp(string.inp.dawwg.block.LIB)
                LIBNAME = pymcnp.inp.dawwg.block.Libname.from_mcnp(string.inp.dawwg.block.LIBNAME)
                FISSNEUT = pymcnp.inp.dawwg.block.Fissneut.from_mcnp(string.inp.dawwg.block.FISSNEUT)
                LNG = pymcnp.inp.dawwg.block.Lng.from_mcnp(string.inp.dawwg.block.LNG)
                BALXS = pymcnp.inp.dawwg.block.Balxs.from_mcnp(string.inp.dawwg.block.BALXS)
                NTICHI = pymcnp.inp.dawwg.block.Ntichi.from_mcnp(string.inp.dawwg.block.NTICHI)
                IEVT = pymcnp.inp.dawwg.block.Ievt.from_mcnp(string.inp.dawwg.block.IEVT)
                ISCT = pymcnp.inp.dawwg.block.Isct.from_mcnp(string.inp.dawwg.block.ISCT)
                ITH = pymcnp.inp.dawwg.block.Ith.from_mcnp(string.inp.dawwg.block.ITH)
                TRCOR = pymcnp.inp.dawwg.block.Trcor.from_mcnp(string.inp.dawwg.block.TRCOR)
                IBL = pymcnp.inp.dawwg.block.Ibl.from_mcnp(string.inp.dawwg.block.IBL)
                IBR = pymcnp.inp.dawwg.block.Ibr.from_mcnp(string.inp.dawwg.block.IBR)
                IBT = pymcnp.inp.dawwg.block.Ibt.from_mcnp(string.inp.dawwg.block.IBT)
                IBB = pymcnp.inp.dawwg.block.Ibb.from_mcnp(string.inp.dawwg.block.IBB)
                IBFRNT = pymcnp.inp.dawwg.block.Ibfrnt.from_mcnp(string.inp.dawwg.block.IBFRNT)
                IBBACK = pymcnp.inp.dawwg.block.Ibback.from_mcnp(string.inp.dawwg.block.IBBACK)
                EPSI = pymcnp.inp.dawwg.block.Epsi.from_mcnp(string.inp.dawwg.block.EPSI)
                OITM = pymcnp.inp.dawwg.block.Oitm.from_mcnp(string.inp.dawwg.block.OITM)
                NOSIGF = pymcnp.inp.dawwg.block.Nosigf.from_mcnp(string.inp.dawwg.block.NOSIGF)
                SRCACC = pymcnp.inp.dawwg.block.Srcacc.from_mcnp(string.inp.dawwg.block.SRCACC)
                DIFFSOL = pymcnp.inp.dawwg.block.Diffsol.from_mcnp(string.inp.dawwg.block.DIFFSOL)
                TSASN = pymcnp.inp.dawwg.block.Tsasn.from_mcnp(string.inp.dawwg.block.TSASN)
                TSAEPSI = pymcnp.inp.dawwg.block.Tsaepsi.from_mcnp(string.inp.dawwg.block.TSAEPSI)
                TSAITS = pymcnp.inp.dawwg.block.Tsaits.from_mcnp(string.inp.dawwg.block.TSAITS)
                TSABETA = pymcnp.inp.dawwg.block.Tsabeta.from_mcnp(string.inp.dawwg.block.TSABETA)
                PTCONV = pymcnp.inp.dawwg.block.Ptconv.from_mcnp(string.inp.dawwg.block.PTCONV)
                NORM = pymcnp.inp.dawwg.block.Norm.from_mcnp(string.inp.dawwg.block.NORM)
                XSECTP = pymcnp.inp.dawwg.block.Xsectp.from_mcnp(string.inp.dawwg.block.XSECTP)
                FISSRP = pymcnp.inp.dawwg.block.Fissrp.from_mcnp(string.inp.dawwg.block.FISSRP)
                SOURCP = pymcnp.inp.dawwg.block.Sourcp.from_mcnp(string.inp.dawwg.block.SOURCP)
                ANGP = pymcnp.inp.dawwg.block.Angp.from_mcnp(string.inp.dawwg.block.ANGP)
                BALP = pymcnp.inp.dawwg.block.Balp.from_mcnp(string.inp.dawwg.block.BALP)
                RAFLUX = pymcnp.inp.dawwg.block.Raflux.from_mcnp(string.inp.dawwg.block.RAFLUX)
                RMFLUX = pymcnp.inp.dawwg.block.Rmflux.from_mcnp(string.inp.dawwg.block.RMFLUX)
                AVATAR = pymcnp.inp.dawwg.block.Avatar.from_mcnp(string.inp.dawwg.block.AVATAR)
                ASLEFT = pymcnp.inp.dawwg.block.Asleft.from_mcnp(string.inp.dawwg.block.ASLEFT)
                ASRITE = pymcnp.inp.dawwg.block.Asrite.from_mcnp(string.inp.dawwg.block.ASRITE)
                ASBOTT = pymcnp.inp.dawwg.block.Asbott.from_mcnp(string.inp.dawwg.block.ASBOTT)
                ASTOP = pymcnp.inp.dawwg.block.Astop.from_mcnp(string.inp.dawwg.block.ASTOP)
                ASFRNT = pymcnp.inp.dawwg.block.Asfrnt.from_mcnp(string.inp.dawwg.block.ASFRNT)
                ASBACK = pymcnp.inp.dawwg.block.Asback.from_mcnp(string.inp.dawwg.block.ASBACK)
                MASSED = pymcnp.inp.dawwg.block.Massed.from_mcnp(string.inp.dawwg.block.MASSED)
                PTED = pymcnp.inp.dawwg.block.Pted.from_mcnp(string.inp.dawwg.block.PTED)
                ZNED = pymcnp.inp.dawwg.block.Zned.from_mcnp(string.inp.dawwg.block.ZNED)
                RZFLUX = pymcnp.inp.dawwg.block.Rzflux.from_mcnp(string.inp.dawwg.block.RZFLUX)
                RZMFLUX = pymcnp.inp.dawwg.block.Rzmflux.from_mcnp(string.inp.dawwg.block.RZMFLUX)
                EDOUTF = pymcnp.inp.dawwg.block.Edoutf.from_mcnp(string.inp.dawwg.block.EDOUTF)
                BYVOLP = pymcnp.inp.dawwg.block.Byvolp.from_mcnp(string.inp.dawwg.block.BYVOLP)
                AJED = pymcnp.inp.dawwg.block.Ajed.from_mcnp(string.inp.dawwg.block.AJED)
                FLUXONE = pymcnp.inp.dawwg.block.Fluxone.from_mcnp(string.inp.dawwg.block.FLUXONE)

        class embed:
            BACKGROUND = pymcnp.inp.embed.Background.from_mcnp(string.inp.embed.BACKGROUND)
            MATCELL = pymcnp.inp.embed.Matcell.from_mcnp(string.inp.embed.MATCELL)
            MESHGEO = pymcnp.inp.embed.Meshgeo.from_mcnp(string.inp.embed.MESHGEO)
            MGEOIN = pymcnp.inp.embed.Mgeoin.from_mcnp(string.inp.embed.MGEOIN)
            MEEOUT = pymcnp.inp.embed.Meeout.from_mcnp(string.inp.embed.MEEOUT)
            MEEIN = pymcnp.inp.embed.Meein.from_mcnp(string.inp.embed.MEEIN)
            CALCVOLS = pymcnp.inp.embed.Calcvols.from_mcnp(string.inp.embed.CALCVOLS)
            DEBUG = pymcnp.inp.embed.Debug.from_mcnp(string.inp.embed.DEBUG)
            FILETYPE = pymcnp.inp.embed.Filetype.from_mcnp(string.inp.embed.FILETYPE)
            GMVFILE = pymcnp.inp.embed.Gmvfile.from_mcnp(string.inp.embed.GMVFILE)
            LENGTH = pymcnp.inp.embed.Length.from_mcnp(string.inp.embed.LENGTH)
            MCNPUMFILE = pymcnp.inp.embed.Mcnpumfile.from_mcnp(string.inp.embed.MCNPUMFILE)

            class matcell:
                ENTRY = pymcnp.inp.embed.matcell.Entry.from_mcnp(string.inp.embed.matcell.ENTRY)

        class embee:
            EMBED = pymcnp.inp.embee.Embed.from_mcnp(string.inp.embee.EMBED)
            ENERGY = pymcnp.inp.embee.Energy.from_mcnp(string.inp.embee.ENERGY)
            TIME = pymcnp.inp.embee.Time.from_mcnp(string.inp.embee.TIME)
            ATOM = pymcnp.inp.embee.Atom.from_mcnp(string.inp.embee.ATOM)
            FACTOR = pymcnp.inp.embee.Factor.from_mcnp(string.inp.embee.FACTOR)
            LIST = pymcnp.inp.embee.List.from_mcnp(string.inp.embee.LIST)
            MAT = pymcnp.inp.embee.Mat.from_mcnp(string.inp.embee.MAT)
            MTYPE = pymcnp.inp.embee.Mtype.from_mcnp(string.inp.embee.MTYPE)

        class m_0:
            GAS = pymcnp.inp.m_0.Gas.from_mcnp(string.inp.m_0.GAS)
            ESTEP = pymcnp.inp.m_0.Estep.from_mcnp(string.inp.m_0.ESTEP)
            HSTEP = pymcnp.inp.m_0.Hstep.from_mcnp(string.inp.m_0.HSTEP)
            NLIB = pymcnp.inp.m_0.Nlib.from_mcnp(string.inp.m_0.NLIB)
            PLIB = pymcnp.inp.m_0.Plib.from_mcnp(string.inp.m_0.PLIB)
            PNLIB = pymcnp.inp.m_0.Pnlib.from_mcnp(string.inp.m_0.PNLIB)
            ELIB = pymcnp.inp.m_0.Elib.from_mcnp(string.inp.m_0.ELIB)
            HLIB = pymcnp.inp.m_0.Hlib.from_mcnp(string.inp.m_0.HLIB)
            ALIB = pymcnp.inp.m_0.Alib.from_mcnp(string.inp.m_0.ALIB)
            SLIB = pymcnp.inp.m_0.Slib.from_mcnp(string.inp.m_0.SLIB)
            TLIB = pymcnp.inp.m_0.Tlib.from_mcnp(string.inp.m_0.TLIB)
            DLIB = pymcnp.inp.m_0.Dlib.from_mcnp(string.inp.m_0.DLIB)
            COND = pymcnp.inp.m_0.Cond.from_mcnp(string.inp.m_0.COND)
            REFI = pymcnp.inp.m_0.Refi.from_mcnp(string.inp.m_0.REFI)
            REFC = pymcnp.inp.m_0.Refc.from_mcnp(string.inp.m_0.REFC)
            REFS = pymcnp.inp.m_0.Refs.from_mcnp(string.inp.m_0.REFS)

        class act:
            FISSION = pymcnp.inp.act.Fission.from_mcnp(string.inp.act.FISSION)
            NONFISS = pymcnp.inp.act.Nonfiss.from_mcnp(string.inp.act.NONFISS)
            DN = pymcnp.inp.act.Dn.from_mcnp(string.inp.act.DN)
            DG = pymcnp.inp.act.Dg.from_mcnp(string.inp.act.DG)
            THRESH = pymcnp.inp.act.Thresh.from_mcnp(string.inp.act.THRESH)
            DNBAIS = pymcnp.inp.act.Dnbais.from_mcnp(string.inp.act.DNBAIS)
            NAP = pymcnp.inp.act.Nap.from_mcnp(string.inp.act.NAP)
            DNEB = pymcnp.inp.act.Dneb.from_mcnp(string.inp.act.DNEB)
            DGEB = pymcnp.inp.act.Dgeb.from_mcnp(string.inp.act.DGEB)
            PECUT = pymcnp.inp.act.Pecut.from_mcnp(string.inp.act.PECUT)
            HLCUT = pymcnp.inp.act.Hlcut.from_mcnp(string.inp.act.HLCUT)
            SAMPLE = pymcnp.inp.act.Sample.from_mcnp(string.inp.act.SAMPLE)

            class dgeb:
                BIAS = pymcnp.inp.act.dgeb.Bias.from_mcnp(string.inp.act.dgeb.BIAS)

            class dneb:
                BIAS = pymcnp.inp.act.dneb.Bias.from_mcnp(string.inp.act.dneb.BIAS)

        class fmult:
            SFNU = pymcnp.inp.fmult.Sfnu.from_mcnp(string.inp.fmult.SFNU)
            WIDTH = pymcnp.inp.fmult.Width.from_mcnp(string.inp.fmult.WIDTH)
            SFYIELD = pymcnp.inp.fmult.Sfyield.from_mcnp(string.inp.fmult.SFYIELD)
            WATT = pymcnp.inp.fmult.Watt.from_mcnp(string.inp.fmult.WATT)
            METHOD = pymcnp.inp.fmult.Method.from_mcnp(string.inp.fmult.METHOD)
            DATA = pymcnp.inp.fmult.Data.from_mcnp(string.inp.fmult.DATA)
            SHIFT = pymcnp.inp.fmult.Shift.from_mcnp(string.inp.fmult.SHIFT)

        class tropt:
            MCSCAT = pymcnp.inp.tropt.Mcscat.from_mcnp(string.inp.tropt.MCSCAT)
            ELOSS = pymcnp.inp.tropt.Eloss.from_mcnp(string.inp.tropt.ELOSS)
            NREACT = pymcnp.inp.tropt.Nreact.from_mcnp(string.inp.tropt.NREACT)
            NESCAT = pymcnp.inp.tropt.Nescat.from_mcnp(string.inp.tropt.NESCAT)
            GENXS = pymcnp.inp.tropt.Genxs.from_mcnp(string.inp.tropt.GENXS)

        class bfld:
            FIELD = pymcnp.inp.bfld.Field.from_mcnp(string.inp.bfld.FIELD)
            VEC = pymcnp.inp.bfld.Vec.from_mcnp(string.inp.bfld.VEC)
            MAXDEFLC = pymcnp.inp.bfld.Maxdeflc.from_mcnp(string.inp.bfld.MAXDEFLC)
            MAXSTEP = pymcnp.inp.bfld.Maxstep.from_mcnp(string.inp.bfld.MAXSTEP)
            AXS = pymcnp.inp.bfld.Axs.from_mcnp(string.inp.bfld.AXS)
            FFEDGES = pymcnp.inp.bfld.Ffedges.from_mcnp(string.inp.bfld.FFEDGES)
            REFPNT = pymcnp.inp.bfld.Refpnt.from_mcnp(string.inp.bfld.REFPNT)

        class sdef:
            CEL_0 = pymcnp.inp.sdef.Cel_0.from_mcnp(string.inp.sdef.CEL_0)
            CEL_1 = pymcnp.inp.sdef.Cel_1.from_mcnp(string.inp.sdef.CEL_1)
            CEL_2 = pymcnp.inp.sdef.Cel_2.from_mcnp(string.inp.sdef.CEL_2)
            SUR_0 = pymcnp.inp.sdef.Sur_0.from_mcnp(string.inp.sdef.SUR_0)
            SUR_1 = pymcnp.inp.sdef.Sur_1.from_mcnp(string.inp.sdef.SUR_1)
            ERG_0 = pymcnp.inp.sdef.Erg_0.from_mcnp(string.inp.sdef.ERG_0)
            ERG_1 = pymcnp.inp.sdef.Erg_1.from_mcnp(string.inp.sdef.ERG_1)
            ERG_2 = pymcnp.inp.sdef.Erg_2.from_mcnp(string.inp.sdef.ERG_2)
            TME_0 = pymcnp.inp.sdef.Tme_0.from_mcnp(string.inp.sdef.TME_0)
            TME_1 = pymcnp.inp.sdef.Tme_1.from_mcnp(string.inp.sdef.TME_1)
            TME_2 = pymcnp.inp.sdef.Tme_2.from_mcnp(string.inp.sdef.TME_2)
            DIR_0 = pymcnp.inp.sdef.Dir_0.from_mcnp(string.inp.sdef.DIR_0)
            DIR_1 = pymcnp.inp.sdef.Dir_1.from_mcnp(string.inp.sdef.DIR_1)
            DIR_2 = pymcnp.inp.sdef.Dir_2.from_mcnp(string.inp.sdef.DIR_2)
            VEC_0 = pymcnp.inp.sdef.Vec_0.from_mcnp(string.inp.sdef.VEC_0)
            VEC_1 = pymcnp.inp.sdef.Vec_1.from_mcnp(string.inp.sdef.VEC_1)
            NRM_0 = pymcnp.inp.sdef.Nrm_0.from_mcnp(string.inp.sdef.NRM_0)
            NRM_1 = pymcnp.inp.sdef.Nrm_1.from_mcnp(string.inp.sdef.NRM_1)
            POS_0 = pymcnp.inp.sdef.Pos_0.from_mcnp(string.inp.sdef.POS_0)
            POS_1 = pymcnp.inp.sdef.Pos_1.from_mcnp(string.inp.sdef.POS_1)
            POS_2 = pymcnp.inp.sdef.Pos_2.from_mcnp(string.inp.sdef.POS_2)
            RAD_0 = pymcnp.inp.sdef.Rad_0.from_mcnp(string.inp.sdef.RAD_0)
            RAD_1 = pymcnp.inp.sdef.Rad_1.from_mcnp(string.inp.sdef.RAD_1)
            RAD_2 = pymcnp.inp.sdef.Rad_2.from_mcnp(string.inp.sdef.RAD_2)
            EXT_0 = pymcnp.inp.sdef.Ext_0.from_mcnp(string.inp.sdef.EXT_0)
            EXT_1 = pymcnp.inp.sdef.Ext_1.from_mcnp(string.inp.sdef.EXT_1)
            EXT_2 = pymcnp.inp.sdef.Ext_2.from_mcnp(string.inp.sdef.EXT_2)
            AXS_0 = pymcnp.inp.sdef.Axs_0.from_mcnp(string.inp.sdef.AXS_0)
            AXS_1 = pymcnp.inp.sdef.Axs_1.from_mcnp(string.inp.sdef.AXS_1)
            X_0 = pymcnp.inp.sdef.X_0.from_mcnp(string.inp.sdef.X_0)
            X_1 = pymcnp.inp.sdef.X_1.from_mcnp(string.inp.sdef.X_1)
            X_2 = pymcnp.inp.sdef.X_2.from_mcnp(string.inp.sdef.X_2)
            Y_0 = pymcnp.inp.sdef.Y_0.from_mcnp(string.inp.sdef.Y_0)
            Y_1 = pymcnp.inp.sdef.Y_1.from_mcnp(string.inp.sdef.Y_1)
            Y_2 = pymcnp.inp.sdef.Y_2.from_mcnp(string.inp.sdef.Y_2)
            Z_0 = pymcnp.inp.sdef.Z_0.from_mcnp(string.inp.sdef.Z_0)
            Z_1 = pymcnp.inp.sdef.Z_1.from_mcnp(string.inp.sdef.Z_1)
            Z_2 = pymcnp.inp.sdef.Z_2.from_mcnp(string.inp.sdef.Z_2)
            CCC_0 = pymcnp.inp.sdef.Ccc_0.from_mcnp(string.inp.sdef.CCC_0)
            CCC_1 = pymcnp.inp.sdef.Ccc_1.from_mcnp(string.inp.sdef.CCC_1)
            ARA_0 = pymcnp.inp.sdef.Ara_0.from_mcnp(string.inp.sdef.ARA_0)
            ARA_1 = pymcnp.inp.sdef.Ara_1.from_mcnp(string.inp.sdef.ARA_1)
            WGT_0 = pymcnp.inp.sdef.Wgt_0.from_mcnp(string.inp.sdef.WGT_0)
            WGT_1 = pymcnp.inp.sdef.Wgt_1.from_mcnp(string.inp.sdef.WGT_1)
            TR_0 = pymcnp.inp.sdef.Tr_0.from_mcnp(string.inp.sdef.TR_0)
            TR_1 = pymcnp.inp.sdef.Tr_1.from_mcnp(string.inp.sdef.TR_1)
            TR_2 = pymcnp.inp.sdef.Tr_2.from_mcnp(string.inp.sdef.TR_2)
            EFF_0 = pymcnp.inp.sdef.Eff_0.from_mcnp(string.inp.sdef.EFF_0)
            EFF_1 = pymcnp.inp.sdef.Eff_1.from_mcnp(string.inp.sdef.EFF_1)
            PAR_0 = pymcnp.inp.sdef.Par_0.from_mcnp(string.inp.sdef.PAR_0)
            PAR_1 = pymcnp.inp.sdef.Par_1.from_mcnp(string.inp.sdef.PAR_1)
            DAT_0 = pymcnp.inp.sdef.Dat_0.from_mcnp(string.inp.sdef.DAT_0)
            DAT_1 = pymcnp.inp.sdef.Dat_1.from_mcnp(string.inp.sdef.DAT_1)
            LOC_0 = pymcnp.inp.sdef.Loc_0.from_mcnp(string.inp.sdef.LOC_0)
            LOC_1 = pymcnp.inp.sdef.Loc_1.from_mcnp(string.inp.sdef.LOC_1)
            BEM_0 = pymcnp.inp.sdef.Bem_0.from_mcnp(string.inp.sdef.BEM_0)
            BEM_1 = pymcnp.inp.sdef.Bem_1.from_mcnp(string.inp.sdef.BEM_1)
            BAP_0 = pymcnp.inp.sdef.Bap_0.from_mcnp(string.inp.sdef.BAP_0)
            BAP_1 = pymcnp.inp.sdef.Bap_1.from_mcnp(string.inp.sdef.BAP_1)

            class f:
                FCEL = pymcnp.inp.sdef.f.Fcel.from_mcnp(string.inp.sdef.f.FCEL)
                FSUR = pymcnp.inp.sdef.f.Fsur.from_mcnp(string.inp.sdef.f.FSUR)
                FERG = pymcnp.inp.sdef.f.Ferg.from_mcnp(string.inp.sdef.f.FERG)
                FTME = pymcnp.inp.sdef.f.Ftme.from_mcnp(string.inp.sdef.f.FTME)
                FDIR = pymcnp.inp.sdef.f.Fdir.from_mcnp(string.inp.sdef.f.FDIR)
                FVEC = pymcnp.inp.sdef.f.Fvec.from_mcnp(string.inp.sdef.f.FVEC)
                FNRM = pymcnp.inp.sdef.f.Fnrm.from_mcnp(string.inp.sdef.f.FNRM)
                FPOS = pymcnp.inp.sdef.f.Fpos.from_mcnp(string.inp.sdef.f.FPOS)
                FRAD = pymcnp.inp.sdef.f.Frad.from_mcnp(string.inp.sdef.f.FRAD)
                FEXT = pymcnp.inp.sdef.f.Fext.from_mcnp(string.inp.sdef.f.FEXT)
                FAXS = pymcnp.inp.sdef.f.Faxs.from_mcnp(string.inp.sdef.f.FAXS)
                FX = pymcnp.inp.sdef.f.Fx.from_mcnp(string.inp.sdef.f.FX)
                FY = pymcnp.inp.sdef.f.Fy.from_mcnp(string.inp.sdef.f.FY)
                FZ = pymcnp.inp.sdef.f.Fz.from_mcnp(string.inp.sdef.f.FZ)
                FCCC = pymcnp.inp.sdef.f.Fccc.from_mcnp(string.inp.sdef.f.FCCC)
                FARA = pymcnp.inp.sdef.f.Fara.from_mcnp(string.inp.sdef.f.FARA)
                FWGT = pymcnp.inp.sdef.f.Fwgt.from_mcnp(string.inp.sdef.f.FWGT)
                FTR = pymcnp.inp.sdef.f.Ftr.from_mcnp(string.inp.sdef.f.FTR)
                FEFF = pymcnp.inp.sdef.f.Feff.from_mcnp(string.inp.sdef.f.FEFF)
                FPAR = pymcnp.inp.sdef.f.Fpar.from_mcnp(string.inp.sdef.f.FPAR)
                FDAT = pymcnp.inp.sdef.f.Fdat.from_mcnp(string.inp.sdef.f.FDAT)
                FLOC = pymcnp.inp.sdef.f.Floc.from_mcnp(string.inp.sdef.f.FLOC)
                FBEM = pymcnp.inp.sdef.f.Fbem.from_mcnp(string.inp.sdef.f.FBEM)
                FBAP = pymcnp.inp.sdef.f.Fbap.from_mcnp(string.inp.sdef.f.FBAP)

            class tme_1:
                EMBEDDED = pymcnp.inp.sdef.tme_1.Embedded.from_mcnp(string.inp.sdef.tme_1.EMBEDDED)

        class ssw:
            SYM = pymcnp.inp.ssw.Sym.from_mcnp(string.inp.ssw.SYM)
            PTY = pymcnp.inp.ssw.Pty.from_mcnp(string.inp.ssw.PTY)
            CEL = pymcnp.inp.ssw.Cel.from_mcnp(string.inp.ssw.CEL)

        class ssr:
            OLD = pymcnp.inp.ssr.Old.from_mcnp(string.inp.ssr.OLD)
            CEL = pymcnp.inp.ssr.Cel.from_mcnp(string.inp.ssr.CEL)
            NEW = pymcnp.inp.ssr.New.from_mcnp(string.inp.ssr.NEW)
            PTY = pymcnp.inp.ssr.Pty.from_mcnp(string.inp.ssr.PTY)
            COL = pymcnp.inp.ssr.Col.from_mcnp(string.inp.ssr.COL)
            WGT = pymcnp.inp.ssr.Wgt.from_mcnp(string.inp.ssr.WGT)
            TR_0 = pymcnp.inp.ssr.Tr_0.from_mcnp(string.inp.ssr.TR_0)
            TR_1 = pymcnp.inp.ssr.Tr_1.from_mcnp(string.inp.ssr.TR_1)
            PSC = pymcnp.inp.ssr.Psc.from_mcnp(string.inp.ssr.PSC)
            AXS = pymcnp.inp.ssr.Axs.from_mcnp(string.inp.ssr.AXS)
            EXT = pymcnp.inp.ssr.Ext.from_mcnp(string.inp.ssr.EXT)
            POA = pymcnp.inp.ssr.Poa.from_mcnp(string.inp.ssr.POA)
            BCW = pymcnp.inp.ssr.Bcw.from_mcnp(string.inp.ssr.BCW)

        class kopts:
            BLOCKSIZE = pymcnp.inp.kopts.Blocksize.from_mcnp(string.inp.kopts.BLOCKSIZE)
            KINETICS = pymcnp.inp.kopts.Kinetics.from_mcnp(string.inp.kopts.KINETICS)
            PRECURSOR = pymcnp.inp.kopts.Precursor.from_mcnp(string.inp.kopts.PRECURSOR)
            KSENTAL = pymcnp.inp.kopts.Ksental.from_mcnp(string.inp.kopts.KSENTAL)
            FMAT = pymcnp.inp.kopts.Fmat.from_mcnp(string.inp.kopts.FMAT)
            FMATSKPT = pymcnp.inp.kopts.Fmatskpt.from_mcnp(string.inp.kopts.FMATSKPT)
            FMATNCYC = pymcnp.inp.kopts.Fmatncyc.from_mcnp(string.inp.kopts.FMATNCYC)
            FMATSPACE = pymcnp.inp.kopts.Fmatspace.from_mcnp(string.inp.kopts.FMATSPACE)
            FMATACCEL = pymcnp.inp.kopts.Fmataccel.from_mcnp(string.inp.kopts.FMATACCEL)
            FMATREDUCE = pymcnp.inp.kopts.Fmatreduce.from_mcnp(string.inp.kopts.FMATREDUCE)
            FMATNX = pymcnp.inp.kopts.Fmatnx.from_mcnp(string.inp.kopts.FMATNX)
            FMATNY = pymcnp.inp.kopts.Fmatny.from_mcnp(string.inp.kopts.FMATNY)
            FMATNZ = pymcnp.inp.kopts.Fmatnz.from_mcnp(string.inp.kopts.FMATNZ)

        class t_1:
            CBEG = pymcnp.inp.t_1.Cbeg.from_mcnp(string.inp.t_1.CBEG)
            CFRQ = pymcnp.inp.t_1.Cfrq.from_mcnp(string.inp.t_1.CFRQ)
            COFI = pymcnp.inp.t_1.Cofi.from_mcnp(string.inp.t_1.COFI)
            CONI = pymcnp.inp.t_1.Coni.from_mcnp(string.inp.t_1.CONI)
            CSUB = pymcnp.inp.t_1.Csub.from_mcnp(string.inp.t_1.CSUB)
            CEND = pymcnp.inp.t_1.Cend.from_mcnp(string.inp.t_1.CEND)

        class df_1:
            IU = pymcnp.inp.df_1.Iu.from_mcnp(string.inp.df_1.IU)
            FAC = pymcnp.inp.df_1.Fac.from_mcnp(string.inp.df_1.FAC)
            IC = pymcnp.inp.df_1.Ic.from_mcnp(string.inp.df_1.IC)
            LOG = pymcnp.inp.df_1.Log.from_mcnp(string.inp.df_1.LOG)
            LIN = pymcnp.inp.df_1.Lin.from_mcnp(string.inp.df_1.LIN)

        class pert:
            CELL = pymcnp.inp.pert.Cell.from_mcnp(string.inp.pert.CELL)
            MAT = pymcnp.inp.pert.Mat.from_mcnp(string.inp.pert.MAT)
            RHO = pymcnp.inp.pert.Rho.from_mcnp(string.inp.pert.RHO)
            METHOD = pymcnp.inp.pert.Method.from_mcnp(string.inp.pert.METHOD)
            ERG = pymcnp.inp.pert.Erg.from_mcnp(string.inp.pert.ERG)
            RXN = pymcnp.inp.pert.Rxn.from_mcnp(string.inp.pert.RXN)

        class kpert:
            CELL = pymcnp.inp.kpert.Cell.from_mcnp(string.inp.kpert.CELL)
            MAT = pymcnp.inp.kpert.Mat.from_mcnp(string.inp.kpert.MAT)
            RHO = pymcnp.inp.kpert.Rho.from_mcnp(string.inp.kpert.RHO)
            ISO = pymcnp.inp.kpert.Iso.from_mcnp(string.inp.kpert.ISO)
            RXN = pymcnp.inp.kpert.Rxn.from_mcnp(string.inp.kpert.RXN)
            ERG = pymcnp.inp.kpert.Erg.from_mcnp(string.inp.kpert.ERG)
            LINEAR = pymcnp.inp.kpert.Linear.from_mcnp(string.inp.kpert.LINEAR)

        class ksen:
            ISO = pymcnp.inp.ksen.Iso.from_mcnp(string.inp.ksen.ISO)
            RXN = pymcnp.inp.ksen.Rxn.from_mcnp(string.inp.ksen.RXN)
            MT = pymcnp.inp.ksen.Mt.from_mcnp(string.inp.ksen.MT)
            ERG = pymcnp.inp.ksen.Erg.from_mcnp(string.inp.ksen.ERG)
            EIN = pymcnp.inp.ksen.Ein.from_mcnp(string.inp.ksen.EIN)
            LEGENDRE = pymcnp.inp.ksen.Legendre.from_mcnp(string.inp.ksen.LEGENDRE)
            COS = pymcnp.inp.ksen.Cos.from_mcnp(string.inp.ksen.COS)
            CONSTRAIN = pymcnp.inp.ksen.Constrain.from_mcnp(string.inp.ksen.CONSTRAIN)

        class fmesh:
            GEOM = pymcnp.inp.fmesh.Geom.from_mcnp(string.inp.fmesh.GEOM)
            ORIGIN = pymcnp.inp.fmesh.Origin.from_mcnp(string.inp.fmesh.ORIGIN)
            AXS = pymcnp.inp.fmesh.Axs.from_mcnp(string.inp.fmesh.AXS)
            VEC = pymcnp.inp.fmesh.Vec.from_mcnp(string.inp.fmesh.VEC)
            IMESH = pymcnp.inp.fmesh.Imesh.from_mcnp(string.inp.fmesh.IMESH)
            IINTS = pymcnp.inp.fmesh.Iints.from_mcnp(string.inp.fmesh.IINTS)
            JMESH = pymcnp.inp.fmesh.Jmesh.from_mcnp(string.inp.fmesh.JMESH)
            JINTS = pymcnp.inp.fmesh.Jints.from_mcnp(string.inp.fmesh.JINTS)
            KMESH = pymcnp.inp.fmesh.Kmesh.from_mcnp(string.inp.fmesh.KMESH)
            KINTS = pymcnp.inp.fmesh.Kints.from_mcnp(string.inp.fmesh.KINTS)
            EMESH = pymcnp.inp.fmesh.Emesh.from_mcnp(string.inp.fmesh.EMESH)
            EINTS = pymcnp.inp.fmesh.Eints.from_mcnp(string.inp.fmesh.EINTS)
            ENORM = pymcnp.inp.fmesh.Enorm.from_mcnp(string.inp.fmesh.ENORM)
            TMESH = pymcnp.inp.fmesh.Tmesh.from_mcnp(string.inp.fmesh.TMESH)
            TINTS = pymcnp.inp.fmesh.Tints.from_mcnp(string.inp.fmesh.TINTS)
            TNORM = pymcnp.inp.fmesh.Tnorm.from_mcnp(string.inp.fmesh.TNORM)
            FACTOR = pymcnp.inp.fmesh.Factor.from_mcnp(string.inp.fmesh.FACTOR)
            OUT = pymcnp.inp.fmesh.Out.from_mcnp(string.inp.fmesh.OUT)
            TR = pymcnp.inp.fmesh.Tr.from_mcnp(string.inp.fmesh.TR)
            INC = pymcnp.inp.fmesh.Inc.from_mcnp(string.inp.fmesh.INC)
            TYPE = pymcnp.inp.fmesh.Type.from_mcnp(string.inp.fmesh.TYPE)
            KCLEAR = pymcnp.inp.fmesh.Kclear.from_mcnp(string.inp.fmesh.KCLEAR)

        class var:
            RR = pymcnp.inp.var.Rr.from_mcnp(string.inp.var.RR)

        class mesh:
            GEOM = pymcnp.inp.mesh.Geom.from_mcnp(string.inp.mesh.GEOM)
            REF = pymcnp.inp.mesh.Ref.from_mcnp(string.inp.mesh.REF)
            ORIGIN = pymcnp.inp.mesh.Origin.from_mcnp(string.inp.mesh.ORIGIN)
            AXS = pymcnp.inp.mesh.Axs.from_mcnp(string.inp.mesh.AXS)
            VEC = pymcnp.inp.mesh.Vec.from_mcnp(string.inp.mesh.VEC)
            IMESH = pymcnp.inp.mesh.Imesh.from_mcnp(string.inp.mesh.IMESH)
            IINTS = pymcnp.inp.mesh.Iints.from_mcnp(string.inp.mesh.IINTS)
            JMESH = pymcnp.inp.mesh.Jmesh.from_mcnp(string.inp.mesh.JMESH)
            JINTS = pymcnp.inp.mesh.Jints.from_mcnp(string.inp.mesh.JINTS)
            KMESH = pymcnp.inp.mesh.Kmesh.from_mcnp(string.inp.mesh.KMESH)
            KINTS = pymcnp.inp.mesh.Kints.from_mcnp(string.inp.mesh.KINTS)

        class stop:
            NPS = pymcnp.inp.stop.Nps.from_mcnp(string.inp.stop.NPS)
            CTME = pymcnp.inp.stop.Ctme.from_mcnp(string.inp.stop.CTME)
            F = pymcnp.inp.stop.F.from_mcnp(string.inp.stop.F)

        class ptrac:
            BUFFER = pymcnp.inp.ptrac.Buffer.from_mcnp(string.inp.ptrac.BUFFER)
            FILE = pymcnp.inp.ptrac.File.from_mcnp(string.inp.ptrac.FILE)
            MAX = pymcnp.inp.ptrac.Max.from_mcnp(string.inp.ptrac.MAX)
            MEPH = pymcnp.inp.ptrac.Meph.from_mcnp(string.inp.ptrac.MEPH)
            WRITE = pymcnp.inp.ptrac.Write.from_mcnp(string.inp.ptrac.WRITE)
            CONIC = pymcnp.inp.ptrac.Conic.from_mcnp(string.inp.ptrac.CONIC)
            EVENT = pymcnp.inp.ptrac.Event.from_mcnp(string.inp.ptrac.EVENT)
            FILTER = pymcnp.inp.ptrac.Filter.from_mcnp(string.inp.ptrac.FILTER)
            TYPE = pymcnp.inp.ptrac.Type.from_mcnp(string.inp.ptrac.TYPE)
            NPS = pymcnp.inp.ptrac.Nps.from_mcnp(string.inp.ptrac.NPS)
            CELL = pymcnp.inp.ptrac.Cell.from_mcnp(string.inp.ptrac.CELL)
            SURFACE = pymcnp.inp.ptrac.Surface.from_mcnp(string.inp.ptrac.SURFACE)
            TALLY = pymcnp.inp.ptrac.Tally.from_mcnp(string.inp.ptrac.TALLY)
            VALUE = pymcnp.inp.ptrac.Value.from_mcnp(string.inp.ptrac.VALUE)

            class filter:
                ENTRY = pymcnp.inp.ptrac.filter.Entry.from_mcnp(string.inp.ptrac.filter.ENTRY)

        class mplot:
            TERM = pymcnp.inp.mplot.Term.from_mcnp(string.inp.mplot.TERM)
            FILE = pymcnp.inp.mplot.File.from_mcnp(string.inp.mplot.FILE)
            COPLOT = pymcnp.inp.mplot.Coplot.from_mcnp(string.inp.mplot.COPLOT)
            FREQ = pymcnp.inp.mplot.Freq.from_mcnp(string.inp.mplot.FREQ)
            RETURN = pymcnp.inp.mplot.Return.from_mcnp(string.inp.mplot.RETURN)
            PLOT = pymcnp.inp.mplot.Plot.from_mcnp(string.inp.mplot.PLOT)
            PAUSE = pymcnp.inp.mplot.Pause.from_mcnp(string.inp.mplot.PAUSE)
            END = pymcnp.inp.mplot.End.from_mcnp(string.inp.mplot.END)
            OPTIONS = pymcnp.inp.mplot.Options.from_mcnp(string.inp.mplot.OPTIONS)
            HELP = pymcnp.inp.mplot.Help.from_mcnp(string.inp.mplot.HELP)
            STATUS = pymcnp.inp.mplot.Status.from_mcnp(string.inp.mplot.STATUS)
            PRINTAL = pymcnp.inp.mplot.Printal.from_mcnp(string.inp.mplot.PRINTAL)
            IPTAL = pymcnp.inp.mplot.Iptal.from_mcnp(string.inp.mplot.IPTAL)
            PRINTPTS = pymcnp.inp.mplot.Printpts.from_mcnp(string.inp.mplot.PRINTPTS)
            RUNTPE = pymcnp.inp.mplot.Runtpe.from_mcnp(string.inp.mplot.RUNTPE)
            DUMP = pymcnp.inp.mplot.Dump.from_mcnp(string.inp.mplot.DUMP)
            WMCTAL = pymcnp.inp.mplot.Wmctal.from_mcnp(string.inp.mplot.WMCTAL)
            RMCTAL = pymcnp.inp.mplot.Rmctal.from_mcnp(string.inp.mplot.RMCTAL)
            TALLY = pymcnp.inp.mplot.Tally.from_mcnp(string.inp.mplot.TALLY)
            PERT = pymcnp.inp.mplot.Pert.from_mcnp(string.inp.mplot.PERT)
            LETHARGY = pymcnp.inp.mplot.Lethargy.from_mcnp(string.inp.mplot.LETHARGY)
            NONORM = pymcnp.inp.mplot.Nonorm.from_mcnp(string.inp.mplot.NONORM)
            FACTOR = pymcnp.inp.mplot.Factor.from_mcnp(string.inp.mplot.FACTOR)
            RESET = pymcnp.inp.mplot.Reset.from_mcnp(string.inp.mplot.RESET)
            TITLE = pymcnp.inp.mplot.Title.from_mcnp(string.inp.mplot.TITLE)
            BELOW = pymcnp.inp.mplot.Below.from_mcnp(string.inp.mplot.BELOW)
            SUBTITLE = pymcnp.inp.mplot.Subtitle.from_mcnp(string.inp.mplot.SUBTITLE)
            XTITLE = pymcnp.inp.mplot.Xtitle.from_mcnp(string.inp.mplot.XTITLE)
            YTITLE = pymcnp.inp.mplot.Ytitle.from_mcnp(string.inp.mplot.YTITLE)
            ZTITLE = pymcnp.inp.mplot.Ztitle.from_mcnp(string.inp.mplot.ZTITLE)
            LABEL = pymcnp.inp.mplot.Label.from_mcnp(string.inp.mplot.LABEL)
            FREE = pymcnp.inp.mplot.Free.from_mcnp(string.inp.mplot.FREE)
            FIXED = pymcnp.inp.mplot.Fixed.from_mcnp(string.inp.mplot.FIXED)
            SET = pymcnp.inp.mplot.Set.from_mcnp(string.inp.mplot.SET)
            TFC = pymcnp.inp.mplot.Tfc.from_mcnp(string.inp.mplot.TFC)
            KCODE = pymcnp.inp.mplot.Kcode.from_mcnp(string.inp.mplot.KCODE)
            XS_0 = pymcnp.inp.mplot.Xs_0.from_mcnp(string.inp.mplot.XS_0)
            XS_1 = pymcnp.inp.mplot.Xs_1.from_mcnp(string.inp.mplot.XS_1)
            XS_2 = pymcnp.inp.mplot.Xs_2.from_mcnp(string.inp.mplot.XS_2)
            MT = pymcnp.inp.mplot.Mt.from_mcnp(string.inp.mplot.MT)
            PAR = pymcnp.inp.mplot.Par.from_mcnp(string.inp.mplot.PAR)
            LINLIN = pymcnp.inp.mplot.Linlin.from_mcnp(string.inp.mplot.LINLIN)
            LINLOG = pymcnp.inp.mplot.Linlog.from_mcnp(string.inp.mplot.LINLOG)
            LOGLIN = pymcnp.inp.mplot.Loglin.from_mcnp(string.inp.mplot.LOGLIN)
            LOGLOG = pymcnp.inp.mplot.Loglog.from_mcnp(string.inp.mplot.LOGLOG)
            XLIMS = pymcnp.inp.mplot.Xlims.from_mcnp(string.inp.mplot.XLIMS)
            YLIMS = pymcnp.inp.mplot.Ylims.from_mcnp(string.inp.mplot.YLIMS)
            SCALES = pymcnp.inp.mplot.Scales.from_mcnp(string.inp.mplot.SCALES)
            HIST = pymcnp.inp.mplot.Hist.from_mcnp(string.inp.mplot.HIST)
            PLINEAR = pymcnp.inp.mplot.Plinear.from_mcnp(string.inp.mplot.PLINEAR)
            SPLINE = pymcnp.inp.mplot.Spline.from_mcnp(string.inp.mplot.SPLINE)
            BAR = pymcnp.inp.mplot.Bar.from_mcnp(string.inp.mplot.BAR)
            NOERRBAR = pymcnp.inp.mplot.Noerrbar.from_mcnp(string.inp.mplot.NOERRBAR)
            THICK = pymcnp.inp.mplot.Thick.from_mcnp(string.inp.mplot.THICK)
            THIN = pymcnp.inp.mplot.Thin.from_mcnp(string.inp.mplot.THIN)
            LEGEND = pymcnp.inp.mplot.Legend.from_mcnp(string.inp.mplot.LEGEND)
            CONTOUR = pymcnp.inp.mplot.Contour.from_mcnp(string.inp.mplot.CONTOUR)
            WASH = pymcnp.inp.mplot.Wash.from_mcnp(string.inp.mplot.WASH)
            FMESH = pymcnp.inp.mplot.Fmesh.from_mcnp(string.inp.mplot.FMESH)
            FMRELERR = pymcnp.inp.mplot.Fmrelerr.from_mcnp(string.inp.mplot.FMRELERR)
            ZLEV = pymcnp.inp.mplot.Zlev.from_mcnp(string.inp.mplot.ZLEV)
            EBIN = pymcnp.inp.mplot.Ebin.from_mcnp(string.inp.mplot.EBIN)
            TBIN = pymcnp.inp.mplot.Tbin.from_mcnp(string.inp.mplot.TBIN)
            COP = pymcnp.inp.mplot.Cop.from_mcnp(string.inp.mplot.COP)
            TAL = pymcnp.inp.mplot.Tal.from_mcnp(string.inp.mplot.TAL)

            class free:
                ALL = pymcnp.inp.mplot.free.All.from_mcnp(string.inp.mplot.free.ALL)
                NOALL = pymcnp.inp.mplot.free.Noall.from_mcnp(string.inp.mplot.free.NOALL)

            class contour:
                PCT = pymcnp.inp.mplot.contour.Pct.from_mcnp(string.inp.mplot.contour.PCT)
                LIN = pymcnp.inp.mplot.contour.Lin.from_mcnp(string.inp.mplot.contour.LIN)
                LOG = pymcnp.inp.mplot.contour.Log.from_mcnp(string.inp.mplot.contour.LOG)
                ALL = pymcnp.inp.mplot.contour.All.from_mcnp(string.inp.mplot.contour.ALL)
                NOALL = pymcnp.inp.mplot.contour.Noall.from_mcnp(string.inp.mplot.contour.NOALL)
                LINE = pymcnp.inp.mplot.contour.Line.from_mcnp(string.inp.mplot.contour.LINE)
                NOLINE = pymcnp.inp.mplot.contour.Noline.from_mcnp(string.inp.mplot.contour.NOLINE)
                COLOR = pymcnp.inp.mplot.contour.Color.from_mcnp(string.inp.mplot.contour.COLOR)
                NOCOLOR = pymcnp.inp.mplot.contour.Nocolor.from_mcnp(string.inp.mplot.contour.NOCOLOR)

        class rand:
            GEN = pymcnp.inp.rand.Gen.from_mcnp(string.inp.rand.GEN)
            SEED = pymcnp.inp.rand.Seed.from_mcnp(string.inp.rand.SEED)
            STRIDE = pymcnp.inp.rand.Stride.from_mcnp(string.inp.rand.STRIDE)
            HIST = pymcnp.inp.rand.Hist.from_mcnp(string.inp.rand.HIST)

        class cell:
            IMP = pymcnp.inp.cell.Imp.from_mcnp(string.inp.cell.IMP)
            VOL = pymcnp.inp.cell.Vol.from_mcnp(string.inp.cell.VOL)
            PWT = pymcnp.inp.cell.Pwt.from_mcnp(string.inp.cell.PWT)
            EXT = pymcnp.inp.cell.Ext.from_mcnp(string.inp.cell.EXT)
            FCL = pymcnp.inp.cell.Fcl.from_mcnp(string.inp.cell.FCL)
            WWN = pymcnp.inp.cell.Wwn.from_mcnp(string.inp.cell.WWN)
            DXC = pymcnp.inp.cell.Dxc.from_mcnp(string.inp.cell.DXC)
            NONU = pymcnp.inp.cell.Nonu.from_mcnp(string.inp.cell.NONU)
            PD = pymcnp.inp.cell.Pd.from_mcnp(string.inp.cell.PD)
            U = pymcnp.inp.cell.U.from_mcnp(string.inp.cell.U)
            TRCL_0 = pymcnp.inp.cell.Trcl_0.from_mcnp(string.inp.cell.TRCL_0)
            TRCL_1 = pymcnp.inp.cell.Trcl_1.from_mcnp(string.inp.cell.TRCL_1)
            TRCL_2 = pymcnp.inp.cell.Trcl_2.from_mcnp(string.inp.cell.TRCL_2)
            TRCL_3 = pymcnp.inp.cell.Trcl_3.from_mcnp(string.inp.cell.TRCL_3)
            TRCL_4 = pymcnp.inp.cell.Trcl_4.from_mcnp(string.inp.cell.TRCL_4)
            TRCL_5 = pymcnp.inp.cell.Trcl_5.from_mcnp(string.inp.cell.TRCL_5)
            LAT = pymcnp.inp.cell.Lat.from_mcnp(string.inp.cell.LAT)
            FILL_0 = pymcnp.inp.cell.Fill_0.from_mcnp(string.inp.cell.FILL_0)
            FILL_1 = pymcnp.inp.cell.Fill_1.from_mcnp(string.inp.cell.FILL_1)
            FILL_2 = pymcnp.inp.cell.Fill_2.from_mcnp(string.inp.cell.FILL_2)
            FILL_3 = pymcnp.inp.cell.Fill_3.from_mcnp(string.inp.cell.FILL_3)
            FILL_4 = pymcnp.inp.cell.Fill_4.from_mcnp(string.inp.cell.FILL_4)
            FILL_5 = pymcnp.inp.cell.Fill_5.from_mcnp(string.inp.cell.FILL_5)
            FILL_6 = pymcnp.inp.cell.Fill_6.from_mcnp(string.inp.cell.FILL_6)
            ELPT = pymcnp.inp.cell.Elpt.from_mcnp(string.inp.cell.ELPT)
            TMP = pymcnp.inp.cell.Tmp.from_mcnp(string.inp.cell.TMP)
            COSY = pymcnp.inp.cell.Cosy.from_mcnp(string.inp.cell.COSY)
            BFLCL = pymcnp.inp.cell.Bflcl.from_mcnp(string.inp.cell.BFLCL)
            UNC = pymcnp.inp.cell.Unc.from_mcnp(string.inp.cell.UNC)

        class like:
            IMP = pymcnp.inp.like.Imp.from_mcnp(string.inp.like.IMP)
            VOL = pymcnp.inp.like.Vol.from_mcnp(string.inp.like.VOL)
            PWT = pymcnp.inp.like.Pwt.from_mcnp(string.inp.like.PWT)
            EXT = pymcnp.inp.like.Ext.from_mcnp(string.inp.like.EXT)
            FCL = pymcnp.inp.like.Fcl.from_mcnp(string.inp.like.FCL)
            WWN = pymcnp.inp.like.Wwn.from_mcnp(string.inp.like.WWN)
            DXC = pymcnp.inp.like.Dxc.from_mcnp(string.inp.like.DXC)
            NONU = pymcnp.inp.like.Nonu.from_mcnp(string.inp.like.NONU)
            PD = pymcnp.inp.like.Pd.from_mcnp(string.inp.like.PD)
            U = pymcnp.inp.like.U.from_mcnp(string.inp.like.U)
            TRCL_0 = pymcnp.inp.like.Trcl_0.from_mcnp(string.inp.like.TRCL_0)
            TRCL_1 = pymcnp.inp.like.Trcl_1.from_mcnp(string.inp.like.TRCL_1)
            TRCL_2 = pymcnp.inp.like.Trcl_2.from_mcnp(string.inp.like.TRCL_2)
            TRCL_3 = pymcnp.inp.like.Trcl_3.from_mcnp(string.inp.like.TRCL_3)
            TRCL_4 = pymcnp.inp.like.Trcl_4.from_mcnp(string.inp.like.TRCL_4)
            TRCL_5 = pymcnp.inp.like.Trcl_5.from_mcnp(string.inp.like.TRCL_5)
            LAT = pymcnp.inp.like.Lat.from_mcnp(string.inp.like.LAT)
            FILL_0 = pymcnp.inp.like.Fill_0.from_mcnp(string.inp.like.FILL_0)
            FILL_1 = pymcnp.inp.like.Fill_1.from_mcnp(string.inp.like.FILL_1)
            FILL_2 = pymcnp.inp.like.Fill_2.from_mcnp(string.inp.like.FILL_2)
            FILL_3 = pymcnp.inp.like.Fill_3.from_mcnp(string.inp.like.FILL_3)
            FILL_4 = pymcnp.inp.like.Fill_4.from_mcnp(string.inp.like.FILL_4)
            FILL_5 = pymcnp.inp.like.Fill_5.from_mcnp(string.inp.like.FILL_5)
            FILL_6 = pymcnp.inp.like.Fill_6.from_mcnp(string.inp.like.FILL_6)
            ELPT = pymcnp.inp.like.Elpt.from_mcnp(string.inp.like.ELPT)
            TMP = pymcnp.inp.like.Tmp.from_mcnp(string.inp.like.TMP)
            COSY = pymcnp.inp.like.Cosy.from_mcnp(string.inp.like.COSY)
            BFLCL = pymcnp.inp.like.Bflcl.from_mcnp(string.inp.like.BFLCL)
            UNC = pymcnp.inp.like.Unc.from_mcnp(string.inp.like.UNC)
            MAT = pymcnp.inp.like.Mat.from_mcnp(string.inp.like.MAT)
            RHO = pymcnp.inp.like.Rho.from_mcnp(string.inp.like.RHO)

        class surface:
            P_0 = pymcnp.inp.surface.P_0.from_mcnp(string.inp.surface.P_0)
            P_1 = pymcnp.inp.surface.P_1.from_mcnp(string.inp.surface.P_1)
            PX = pymcnp.inp.surface.Px.from_mcnp(string.inp.surface.PX)
            PY = pymcnp.inp.surface.Py.from_mcnp(string.inp.surface.PY)
            PZ = pymcnp.inp.surface.Pz.from_mcnp(string.inp.surface.PZ)
            SO = pymcnp.inp.surface.So.from_mcnp(string.inp.surface.SO)
            S = pymcnp.inp.surface.S.from_mcnp(string.inp.surface.S)
            SX = pymcnp.inp.surface.Sx.from_mcnp(string.inp.surface.SX)
            SY = pymcnp.inp.surface.Sy.from_mcnp(string.inp.surface.SY)
            SZ = pymcnp.inp.surface.Sz.from_mcnp(string.inp.surface.SZ)
            C_X = pymcnp.inp.surface.C_x.from_mcnp(string.inp.surface.C_X)
            C_Y = pymcnp.inp.surface.C_y.from_mcnp(string.inp.surface.C_Y)
            C_Z = pymcnp.inp.surface.C_z.from_mcnp(string.inp.surface.C_Z)
            CX = pymcnp.inp.surface.Cx.from_mcnp(string.inp.surface.CX)
            CY = pymcnp.inp.surface.Cy.from_mcnp(string.inp.surface.CY)
            CZ = pymcnp.inp.surface.Cz.from_mcnp(string.inp.surface.CZ)
            K_X = pymcnp.inp.surface.K_x.from_mcnp(string.inp.surface.K_X)
            K_Y = pymcnp.inp.surface.K_y.from_mcnp(string.inp.surface.K_Y)
            K_Z = pymcnp.inp.surface.K_z.from_mcnp(string.inp.surface.K_Z)
            KX = pymcnp.inp.surface.Kx.from_mcnp(string.inp.surface.KX)
            KY = pymcnp.inp.surface.Ky.from_mcnp(string.inp.surface.KY)
            KZ = pymcnp.inp.surface.Kz.from_mcnp(string.inp.surface.KZ)
            SQ = pymcnp.inp.surface.Sq.from_mcnp(string.inp.surface.SQ)
            GQ = pymcnp.inp.surface.Gq.from_mcnp(string.inp.surface.GQ)
            TX = pymcnp.inp.surface.Tx.from_mcnp(string.inp.surface.TX)
            TY = pymcnp.inp.surface.Ty.from_mcnp(string.inp.surface.TY)
            TZ = pymcnp.inp.surface.Tz.from_mcnp(string.inp.surface.TZ)
            X = pymcnp.inp.surface.X.from_mcnp(string.inp.surface.X)
            Y = pymcnp.inp.surface.Y.from_mcnp(string.inp.surface.Y)
            Z = pymcnp.inp.surface.Z.from_mcnp(string.inp.surface.Z)
            BOX = pymcnp.inp.surface.Box.from_mcnp(string.inp.surface.BOX)
            RPP = pymcnp.inp.surface.Rpp.from_mcnp(string.inp.surface.RPP)
            SPH = pymcnp.inp.surface.Sph.from_mcnp(string.inp.surface.SPH)
            RCC = pymcnp.inp.surface.Rcc.from_mcnp(string.inp.surface.RCC)
            RHP = pymcnp.inp.surface.Rhp.from_mcnp(string.inp.surface.RHP)
            REC = pymcnp.inp.surface.Rec.from_mcnp(string.inp.surface.REC)
            TRC = pymcnp.inp.surface.Trc.from_mcnp(string.inp.surface.TRC)
            ELL = pymcnp.inp.surface.Ell.from_mcnp(string.inp.surface.ELL)
            WED = pymcnp.inp.surface.Wed.from_mcnp(string.inp.surface.WED)
            ARB = pymcnp.inp.surface.Arb.from_mcnp(string.inp.surface.ARB)

    class outp:
        ANALYSIS_TALLY_FLUCTUATION = pymcnp.outp.AnalysisTallyFluctuation.from_mcnp(string.outp.ANALYSIS_TALLY_FLUCTUATION)
        HEADER = pymcnp.outp.Header.from_mcnp(string.outp.HEADER)
        MCNP = pymcnp.outp.Mcnp.from_mcnp(string.outp.MCNP)
        NEUTRON_ACTIVITY = pymcnp.outp.NeutronActivity.from_mcnp(string.outp.NEUTRON_ACTIVITY)
        PHOTON_ACTIVITY = pymcnp.outp.PhotonActivity.from_mcnp(string.outp.PHOTON_ACTIVITY)
        PROBLEM_SUMMARY = pymcnp.outp.ProblemSummary.from_mcnp(string.outp.PROBLEM_SUMMARY)
        STARTING_MCRUN = pymcnp.outp.StartingMcrun.from_mcnp(string.outp.STARTING_MCRUN)
        TALLY_1A = pymcnp.outp.Tally_1A.from_mcnp(string.outp.TALLY_1A)
        TALLY_2 = pymcnp.outp.Tally_2.from_mcnp(string.outp.TALLY_2)
        TALLY_4 = pymcnp.outp.Tally_4.from_mcnp(string.outp.TALLY_4)
        UNNORMED_TALLY_DENSITY = pymcnp.outp.UnnormedTallyDensity.from_mcnp(string.outp.UNNORMED_TALLY_DENSITY)

        class tally:
            SUBTALLY_1 = pymcnp.outp.tally.Subtally_1.from_mcnp(string.outp.tally.SUBTALLY_1)
            SUBTALLY_2 = pymcnp.outp.tally.Subtally_2.from_mcnp(string.outp.tally.SUBTALLY_2)
            SUBTALLY_4 = pymcnp.outp.tally.Subtally_4.from_mcnp(string.outp.tally.SUBTALLY_4)

            class subtally:
                LINE = pymcnp.outp.tally.subtally.Line.from_mcnp(string.outp.tally.subtally.LINE)

    class ptrac:
        HEADER = pymcnp.ptrac.Header.from_mcnp(string.ptrac.HEADER)
        HISTORY = pymcnp.ptrac.History.from_mcnp(string.ptrac.HISTORY)

        class header:
            V = pymcnp.ptrac.header.V.from_mcnp(string.ptrac.header.V)
            N = pymcnp.ptrac.header.N.from_mcnp(string.ptrac.header.N)
            L = pymcnp.ptrac.header.L.from_mcnp(string.ptrac.header.L)

        class history:
            I = pymcnp.ptrac.history.I.from_mcnp(string.ptrac.history.I)
            EVENT = pymcnp.ptrac.history.Event.from_mcnp(string.ptrac.history.EVENT)

            class event:
                J_0 = pymcnp.ptrac.history.event.J_0.from_mcnp(string.ptrac.history.event.J_0)
                J_1 = pymcnp.ptrac.history.event.J_1.from_mcnp(string.ptrac.history.event.J_1)
                J_2 = pymcnp.ptrac.history.event.J_2.from_mcnp(string.ptrac.history.event.J_2)
                J_3 = pymcnp.ptrac.history.event.J_3.from_mcnp(string.ptrac.history.event.J_3)
                J_4 = pymcnp.ptrac.history.event.J_4.from_mcnp(string.ptrac.history.event.J_4)
                J_5 = pymcnp.ptrac.history.event.J_5.from_mcnp(string.ptrac.history.event.J_5)
                J_6 = pymcnp.ptrac.history.event.J_6.from_mcnp(string.ptrac.history.event.J_6)
                J_7 = pymcnp.ptrac.history.event.J_7.from_mcnp(string.ptrac.history.event.J_7)
                P_0 = pymcnp.ptrac.history.event.P_0.from_mcnp(string.ptrac.history.event.P_0)
                P_1 = pymcnp.ptrac.history.event.P_1.from_mcnp(string.ptrac.history.event.P_1)

                class j:
                    EVENT_TYPE = pymcnp.ptrac.history.event.j.EventType.from_mcnp(string.ptrac.history.event.j.EVENT_TYPE)

    class meshtal:
        HEADER = pymcnp.meshtal.Header.from_mcnp(string.meshtal.HEADER)
        TALLY = pymcnp.meshtal.Tally.from_mcnp(string.meshtal.TALLY)

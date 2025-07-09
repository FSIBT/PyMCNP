import pymcnp


class string:
    class type:
        REPEAT = '10r'
        INSERT = '10i'
        MULTIPLY = '10m'
        JUMP = '10j'
        LOG = '10log'
        INTEGER = '1'
        REAL = '3.1'
        STRING = 'none'
        DISTRIBUTIONNUMBER = 'd1'
        EMBEDDEDDISTRIBUTIONNUMBER = 'd1'
        ZAID = '001001'
        DESIGNATOR = 'n,#'
        GEOMETRY = '1 (2:(+3 -4) #5)'
        SUBSTANCE = '001001 0.5'
        BIAS = '3.1 4.1'
        TRANSFORMATION_0 = '1 1 1 2 2 2 3 3 3 4 4 4'
        TRANSFORMATION_1 = '1 1 1 2 2 2 3 3 3'
        TRANSFORMATION_2 = '1 1 1 2 2 2 3 3'
        TRANSFORMATION_3 = '1 1 1 2 2 2'
        TRANSFORMATION_4 = '1 1 1'
        STOCHASTIC = '1 3.1 4.1 5.9'
        INDEPENDENTDEPENDENT = '3.1 4.1'
        LOCATION = '3.1 4.1 5.9'
        FILE = '1 2 s f 3'
        DIAGNOSTIC = '3.1 4.1'
        RING = '3.1 4.1 5.9'
        SPHERE = '3.1 4.1 5.9 2.6'
        SHELL = '3.1 4.1 5.9 1 2'
        REACTION = '001001 1'
        PTRACFILTER = '3.1,hello,4.1'
        PHOTONBIAS = '001001 1'
        INDEX = '1:2'
        MATCELL = '1 2'

    class inp:
        CELL = '1 1 3.1 1 (2:(+3 -4) #5) imp:@=1'
        SURFACE = '1 SO 1'
        DATA = 'vol no 3.1 3.1 3.1'
        COMMENT = 'c hello'

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

        class surface:
            P_0 = 'p 1 1 1 1'
            P_1 = 'p 1 1 1 1 1 1 1 1 1'
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

        class data:
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
            DAWWG = 'dawwg points hello'
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
            PHYS_2 = 'phys:e 3.1 1 1 1 1 3.1 3.1 1 1 1 -1 0.8 3.1 0.8'
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
            SI_0 = 'si1 hello d1 d1 d1'
            SI_1 = 'si1 hello 3.1 3.1 3.1'
            SI_2 = 'si1 hello @ @ @'
            SP_0 = 'sp1 d 3.1'
            SP_1 = 'sp -2 3.1 3.1'
            SB_0 = 'sb1 d 3.1 3.1 3.1'
            SB_1 = 'sb -2 3.1 3.1'
            DS_0 = 'ds1 h 3.1 3.1 3.1'
            DS_1 = 'ds1 t 3.1 3.1 3.1 3.1 3.1 3.1'
            DS_2 = 'ds1 q 3.1 3.1 3.1 3.1 3.1 3.1'
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
            FIP = 'fip5:@ 3.1 3.1 3.1 0 3.1 3.1 3.1 3.1 3.1 3.1'
            FIR = 'fir5:@ 3.1 3.1 3.1 0 3.1 3.1 3.1 1 3.1 1'
            FIC = 'fic5:@ 3.1 3.1 3.1 0 3.1 3.1 3.1 -1 3.1 -1'
            F_3 = '+f8:@ 1 1 1 t'
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

            class dawwg:
                POINTS = 'points hello'
                XSEC = 'xsec 1'
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
                MATCELL = 'matcell 1 1 1 1 1 1'
                MESHGEO = 'meshgeo lnk3dnt'
                MGEOIN = 'mgeoin hello'
                MEEOUT = 'meeout hello'
                MEEIN = 'meein hello'
                CALCVOLS = 'calcvols yes'
                DEBUG = 'debug echomesh'
                FILETYPE = 'filetype ascii'
                GMVFILE = 'gmvfile hello'
                LENGTH = 'length 3.1'
                MCNPUMFILE = 'mcnpumfile hello'

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
                CEL = 'cel 1'
                SUR = 'sur 1'
                ERG_0 = 'erg 3.1'
                ERG_1 = 'erg d1'
                TME_0 = 'tme 3.1'
                TME_1 = 'tme d1'
                DIR_0 = 'dir 3.1'
                DIR_1 = 'dir d1'
                VEC = 'vec 3.1 3.1 3.1'
                NRM = 'nrm 1'
                POS = 'pos 3.1 3.1 3.1'
                RAD_0 = 'rad 3.1'
                RAD_1 = 'rad d1'
                EXT = 'ext 3.1'
                AXS = 'axs 3.1 3.1 3.1'
                X = 'x 3.1'
                Y = 'y 3.1'
                Z = 'z 3.1'
                CCC = 'ccc 1'
                ARA = 'ara 3.1'
                WGT = 'wgt 3.1'
                TR_0 = 'tr 1'
                TR_1 = 'tr 1'
                EFF = 'eff 3.1'
                PAR = 'par hello'
                DAT = 'dat 1 1 1'
                LOC = 'loc 3.1 3.1 3.1'
                BEM = 'bem 3.1 3.1 3.1'
                BAP = 'bap 3.1 3.1 3.1'

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


class ast:
    class type:
        REPEAT = pymcnp.utils.types.Repeat.from_mcnp(string.type.REPEAT)
        INSERT = pymcnp.utils.types.Insert.from_mcnp(string.type.INSERT)
        MULTIPLY = pymcnp.utils.types.Multiply.from_mcnp(string.type.MULTIPLY)
        JUMP = pymcnp.utils.types.Jump.from_mcnp(string.type.JUMP)
        LOG = pymcnp.utils.types.Log.from_mcnp(string.type.LOG)
        INTEGER = pymcnp.utils.types.Integer.from_mcnp(string.type.INTEGER)
        REAL = pymcnp.utils.types.Real.from_mcnp(string.type.REAL)
        STRING = pymcnp.utils.types.String.from_mcnp(string.type.STRING)
        DISTRIBUTIONNUMBER = pymcnp.utils.types.DistributionNumber.from_mcnp(string.type.DISTRIBUTIONNUMBER)
        EMBEDDEDDISTRIBUTIONNUMBER = pymcnp.utils.types.EmbeddedDistributionNumber.from_mcnp(string.type.EMBEDDEDDISTRIBUTIONNUMBER)
        ZAID = pymcnp.utils.types.Zaid.from_mcnp(string.type.ZAID)
        DESIGNATOR = pymcnp.utils.types.Designator.from_mcnp(string.type.DESIGNATOR)
        GEOMETRY = pymcnp.utils.types.Geometry.from_mcnp(string.type.GEOMETRY)
        SUBSTANCE = pymcnp.utils.types.Substance.from_mcnp(string.type.SUBSTANCE)
        BIAS = pymcnp.utils.types.Bias.from_mcnp(string.type.BIAS)
        TRANSFORMATION_0 = pymcnp.utils.types.Transformation_0.from_mcnp(string.type.TRANSFORMATION_0)
        TRANSFORMATION_1 = pymcnp.utils.types.Transformation_1.from_mcnp(string.type.TRANSFORMATION_1)
        TRANSFORMATION_2 = pymcnp.utils.types.Transformation_2.from_mcnp(string.type.TRANSFORMATION_2)
        TRANSFORMATION_3 = pymcnp.utils.types.Transformation_3.from_mcnp(string.type.TRANSFORMATION_3)
        TRANSFORMATION_4 = pymcnp.utils.types.Transformation_4.from_mcnp(string.type.TRANSFORMATION_4)
        STOCHASTIC = pymcnp.utils.types.Stochastic.from_mcnp(string.type.STOCHASTIC)
        INDEPENDENTDEPENDENT = pymcnp.utils.types.IndependentDependent.from_mcnp(string.type.INDEPENDENTDEPENDENT)
        LOCATION = pymcnp.utils.types.Location.from_mcnp(string.type.LOCATION)
        FILE = pymcnp.utils.types.File.from_mcnp(string.type.FILE)
        DIAGNOSTIC = pymcnp.utils.types.Diagnostic.from_mcnp(string.type.DIAGNOSTIC)
        RING = pymcnp.utils.types.Ring.from_mcnp(string.type.RING)
        SPHERE = pymcnp.utils.types.Sphere.from_mcnp(string.type.SPHERE)
        SHELL = pymcnp.utils.types.Shell.from_mcnp(string.type.SHELL)
        REACTION = pymcnp.utils.types.Reaction.from_mcnp(string.type.REACTION)
        PTRACFILTER = pymcnp.utils.types.PtracFilter.from_mcnp(string.type.PTRACFILTER)
        PHOTONBIAS = pymcnp.utils.types.PhotonBias.from_mcnp(string.type.PHOTONBIAS)
        INDEX = pymcnp.utils.types.Index.from_mcnp(string.type.INDEX)
        MATCELL = pymcnp.utils.types.Matcell.from_mcnp(string.type.MATCELL)

    class inp:
        CELL = pymcnp.inp.Cell.from_mcnp(string.inp.CELL)
        SURFACE = pymcnp.inp.Surface.from_mcnp(string.inp.SURFACE)
        DATA = pymcnp.inp.Data.from_mcnp(string.inp.DATA)
        COMMENT = pymcnp.inp.Comment.from_mcnp(string.inp.COMMENT)

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

        class data:
            VOL = pymcnp.inp.data.Vol.from_mcnp(string.inp.data.VOL)
            AREA = pymcnp.inp.data.Area.from_mcnp(string.inp.data.AREA)
            TR_0 = pymcnp.inp.data.Tr_0.from_mcnp(string.inp.data.TR_0)
            TR_1 = pymcnp.inp.data.Tr_1.from_mcnp(string.inp.data.TR_1)
            TR_2 = pymcnp.inp.data.Tr_2.from_mcnp(string.inp.data.TR_2)
            TR_3 = pymcnp.inp.data.Tr_3.from_mcnp(string.inp.data.TR_3)
            TR_4 = pymcnp.inp.data.Tr_4.from_mcnp(string.inp.data.TR_4)
            U = pymcnp.inp.data.U.from_mcnp(string.inp.data.U)
            LAT = pymcnp.inp.data.Lat.from_mcnp(string.inp.data.LAT)
            FILL = pymcnp.inp.data.Fill.from_mcnp(string.inp.data.FILL)
            URAN = pymcnp.inp.data.Uran.from_mcnp(string.inp.data.URAN)
            DM = pymcnp.inp.data.Dm.from_mcnp(string.inp.data.DM)
            DAWWG = pymcnp.inp.data.Dawwg.from_mcnp(string.inp.data.DAWWG)
            EMBED = pymcnp.inp.data.Embed.from_mcnp(string.inp.data.EMBED)
            EMBEE = pymcnp.inp.data.Embee.from_mcnp(string.inp.data.EMBEE)
            EMBEB = pymcnp.inp.data.Embeb.from_mcnp(string.inp.data.EMBEB)
            EMBEM = pymcnp.inp.data.Embem.from_mcnp(string.inp.data.EMBEM)
            EMBTB = pymcnp.inp.data.Embtb.from_mcnp(string.inp.data.EMBTB)
            EMBTM = pymcnp.inp.data.Embtm.from_mcnp(string.inp.data.EMBTM)
            EMBDB = pymcnp.inp.data.Embdb.from_mcnp(string.inp.data.EMBDB)
            EMBDF = pymcnp.inp.data.Embdf.from_mcnp(string.inp.data.EMBDF)
            M_0 = pymcnp.inp.data.M_0.from_mcnp(string.inp.data.M_0)
            M_1 = pymcnp.inp.data.M_1.from_mcnp(string.inp.data.M_1)
            MT = pymcnp.inp.data.Mt.from_mcnp(string.inp.data.MT)
            MX = pymcnp.inp.data.Mx.from_mcnp(string.inp.data.MX)
            OTFDB = pymcnp.inp.data.Otfdb.from_mcnp(string.inp.data.OTFDB)
            TOTNU = pymcnp.inp.data.Totnu.from_mcnp(string.inp.data.TOTNU)
            NONU = pymcnp.inp.data.Nonu.from_mcnp(string.inp.data.NONU)
            AWTAB = pymcnp.inp.data.Awtab.from_mcnp(string.inp.data.AWTAB)
            XS = pymcnp.inp.data.Xs.from_mcnp(string.inp.data.XS)
            VOID = pymcnp.inp.data.Void.from_mcnp(string.inp.data.VOID)
            MGOPT = pymcnp.inp.data.Mgopt.from_mcnp(string.inp.data.MGOPT)
            DRXS = pymcnp.inp.data.Drxs.from_mcnp(string.inp.data.DRXS)
            MODE = pymcnp.inp.data.Mode.from_mcnp(string.inp.data.MODE)
            PHYS_0 = pymcnp.inp.data.Phys_0.from_mcnp(string.inp.data.PHYS_0)
            PHYS_1 = pymcnp.inp.data.Phys_1.from_mcnp(string.inp.data.PHYS_1)
            PHYS_2 = pymcnp.inp.data.Phys_2.from_mcnp(string.inp.data.PHYS_2)
            PHYS_3 = pymcnp.inp.data.Phys_3.from_mcnp(string.inp.data.PHYS_3)
            PHYS_4 = pymcnp.inp.data.Phys_4.from_mcnp(string.inp.data.PHYS_4)
            ACT = pymcnp.inp.data.Act.from_mcnp(string.inp.data.ACT)
            CUT = pymcnp.inp.data.Cut.from_mcnp(string.inp.data.CUT)
            ELPT = pymcnp.inp.data.Elpt.from_mcnp(string.inp.data.ELPT)
            TMP = pymcnp.inp.data.Tmp.from_mcnp(string.inp.data.TMP)
            THTME = pymcnp.inp.data.Thtme.from_mcnp(string.inp.data.THTME)
            MPHYS = pymcnp.inp.data.Mphys.from_mcnp(string.inp.data.MPHYS)
            LCA = pymcnp.inp.data.Lca.from_mcnp(string.inp.data.LCA)
            LCB = pymcnp.inp.data.Lcb.from_mcnp(string.inp.data.LCB)
            LCC = pymcnp.inp.data.Lcc.from_mcnp(string.inp.data.LCC)
            LEA = pymcnp.inp.data.Lea.from_mcnp(string.inp.data.LEA)
            LEB = pymcnp.inp.data.Leb.from_mcnp(string.inp.data.LEB)
            FMULT = pymcnp.inp.data.Fmult.from_mcnp(string.inp.data.FMULT)
            TROPT = pymcnp.inp.data.Tropt.from_mcnp(string.inp.data.TROPT)
            UNC = pymcnp.inp.data.Unc.from_mcnp(string.inp.data.UNC)
            COSYP = pymcnp.inp.data.Cosyp.from_mcnp(string.inp.data.COSYP)
            COSY = pymcnp.inp.data.Cosy.from_mcnp(string.inp.data.COSY)
            BFLD = pymcnp.inp.data.Bfld.from_mcnp(string.inp.data.BFLD)
            BFLCL = pymcnp.inp.data.Bflcl.from_mcnp(string.inp.data.BFLCL)
            SDEF = pymcnp.inp.data.Sdef.from_mcnp(string.inp.data.SDEF)
            SI_0 = pymcnp.inp.data.Si_0.from_mcnp(string.inp.data.SI_0)
            SI_1 = pymcnp.inp.data.Si_1.from_mcnp(string.inp.data.SI_1)
            SI_2 = pymcnp.inp.data.Si_2.from_mcnp(string.inp.data.SI_2)
            SP_0 = pymcnp.inp.data.Sp_0.from_mcnp(string.inp.data.SP_0)
            SP_1 = pymcnp.inp.data.Sp_1.from_mcnp(string.inp.data.SP_1)
            SB_0 = pymcnp.inp.data.Sb_0.from_mcnp(string.inp.data.SB_0)
            SB_1 = pymcnp.inp.data.Sb_1.from_mcnp(string.inp.data.SB_1)
            DS_0 = pymcnp.inp.data.Ds_0.from_mcnp(string.inp.data.DS_0)
            DS_1 = pymcnp.inp.data.Ds_1.from_mcnp(string.inp.data.DS_1)
            DS_2 = pymcnp.inp.data.Ds_2.from_mcnp(string.inp.data.DS_2)
            SC = pymcnp.inp.data.Sc.from_mcnp(string.inp.data.SC)
            SSW = pymcnp.inp.data.Ssw.from_mcnp(string.inp.data.SSW)
            SSR = pymcnp.inp.data.Ssr.from_mcnp(string.inp.data.SSR)
            KCODE = pymcnp.inp.data.Kcode.from_mcnp(string.inp.data.KCODE)
            KSRC = pymcnp.inp.data.Ksrc.from_mcnp(string.inp.data.KSRC)
            KOPTS = pymcnp.inp.data.Kopts.from_mcnp(string.inp.data.KOPTS)
            HSRC = pymcnp.inp.data.Hsrc.from_mcnp(string.inp.data.HSRC)
            F_0 = pymcnp.inp.data.F_0.from_mcnp(string.inp.data.F_0)
            F_1 = pymcnp.inp.data.F_1.from_mcnp(string.inp.data.F_1)
            F_2 = pymcnp.inp.data.F_2.from_mcnp(string.inp.data.F_2)
            FIP = pymcnp.inp.data.Fip.from_mcnp(string.inp.data.FIP)
            FIR = pymcnp.inp.data.Fir.from_mcnp(string.inp.data.FIR)
            FIC = pymcnp.inp.data.Fic.from_mcnp(string.inp.data.FIC)
            F_3 = pymcnp.inp.data.F_3.from_mcnp(string.inp.data.F_3)
            FC = pymcnp.inp.data.Fc.from_mcnp(string.inp.data.FC)
            E = pymcnp.inp.data.E.from_mcnp(string.inp.data.E)
            T_0 = pymcnp.inp.data.T_0.from_mcnp(string.inp.data.T_0)
            T_1 = pymcnp.inp.data.T_1.from_mcnp(string.inp.data.T_1)
            C = pymcnp.inp.data.C.from_mcnp(string.inp.data.C)
            FQ = pymcnp.inp.data.Fq.from_mcnp(string.inp.data.FQ)
            FM = pymcnp.inp.data.Fm.from_mcnp(string.inp.data.FM)
            DE = pymcnp.inp.data.De.from_mcnp(string.inp.data.DE)
            DF_0 = pymcnp.inp.data.Df_0.from_mcnp(string.inp.data.DF_0)
            DF_1 = pymcnp.inp.data.Df_1.from_mcnp(string.inp.data.DF_1)
            EM = pymcnp.inp.data.Em.from_mcnp(string.inp.data.EM)
            TM = pymcnp.inp.data.Tm.from_mcnp(string.inp.data.TM)
            CM = pymcnp.inp.data.Cm.from_mcnp(string.inp.data.CM)
            CF = pymcnp.inp.data.Cf.from_mcnp(string.inp.data.CF)
            SF = pymcnp.inp.data.Sf.from_mcnp(string.inp.data.SF)
            FS = pymcnp.inp.data.Fs.from_mcnp(string.inp.data.FS)
            SD = pymcnp.inp.data.Sd.from_mcnp(string.inp.data.SD)
            FU = pymcnp.inp.data.Fu.from_mcnp(string.inp.data.FU)
            FT = pymcnp.inp.data.Ft.from_mcnp(string.inp.data.FT)
            TF_0 = pymcnp.inp.data.Tf_0.from_mcnp(string.inp.data.TF_0)
            TF_1 = pymcnp.inp.data.Tf_1.from_mcnp(string.inp.data.TF_1)
            NOTRN = pymcnp.inp.data.Notrn.from_mcnp(string.inp.data.NOTRN)
            PERT = pymcnp.inp.data.Pert.from_mcnp(string.inp.data.PERT)
            KPERT = pymcnp.inp.data.Kpert.from_mcnp(string.inp.data.KPERT)
            KSEN = pymcnp.inp.data.Ksen.from_mcnp(string.inp.data.KSEN)
            FMESH = pymcnp.inp.data.Fmesh.from_mcnp(string.inp.data.FMESH)
            SPDTL = pymcnp.inp.data.Spdtl.from_mcnp(string.inp.data.SPDTL)
            IMP = pymcnp.inp.data.Imp.from_mcnp(string.inp.data.IMP)
            VAR = pymcnp.inp.data.Var.from_mcnp(string.inp.data.VAR)
            WWE = pymcnp.inp.data.Wwe.from_mcnp(string.inp.data.WWE)
            WWT = pymcnp.inp.data.Wwt.from_mcnp(string.inp.data.WWT)
            WWN = pymcnp.inp.data.Wwn.from_mcnp(string.inp.data.WWN)
            WWP = pymcnp.inp.data.Wwp.from_mcnp(string.inp.data.WWP)
            WWG = pymcnp.inp.data.Wwg.from_mcnp(string.inp.data.WWG)
            WWGE = pymcnp.inp.data.Wwge.from_mcnp(string.inp.data.WWGE)
            WWGT = pymcnp.inp.data.Wwgt.from_mcnp(string.inp.data.WWGT)
            MESH = pymcnp.inp.data.Mesh.from_mcnp(string.inp.data.MESH)
            ESPLT = pymcnp.inp.data.Esplt.from_mcnp(string.inp.data.ESPLT)
            TSPLT = pymcnp.inp.data.Tsplt.from_mcnp(string.inp.data.TSPLT)
            EXT = pymcnp.inp.data.Ext.from_mcnp(string.inp.data.EXT)
            FCL = pymcnp.inp.data.Fcl.from_mcnp(string.inp.data.FCL)
            DXT = pymcnp.inp.data.Dxt.from_mcnp(string.inp.data.DXT)
            DD = pymcnp.inp.data.Dd.from_mcnp(string.inp.data.DD)
            PD = pymcnp.inp.data.Pd.from_mcnp(string.inp.data.PD)
            DXC = pymcnp.inp.data.Dxc.from_mcnp(string.inp.data.DXC)
            BBREM = pymcnp.inp.data.Bbrem.from_mcnp(string.inp.data.BBREM)
            PIKMT = pymcnp.inp.data.Pikmt.from_mcnp(string.inp.data.PIKMT)
            PWT = pymcnp.inp.data.Pwt.from_mcnp(string.inp.data.PWT)
            NPS = pymcnp.inp.data.Nps.from_mcnp(string.inp.data.NPS)
            CTME = pymcnp.inp.data.Ctme.from_mcnp(string.inp.data.CTME)
            STOP = pymcnp.inp.data.Stop.from_mcnp(string.inp.data.STOP)
            PRINT = pymcnp.inp.data.Print.from_mcnp(string.inp.data.PRINT)
            TALNP = pymcnp.inp.data.Talnp.from_mcnp(string.inp.data.TALNP)
            PRDMP = pymcnp.inp.data.Prdmp.from_mcnp(string.inp.data.PRDMP)
            PTRAC = pymcnp.inp.data.Ptrac.from_mcnp(string.inp.data.PTRAC)
            MPLOT = pymcnp.inp.data.Mplot.from_mcnp(string.inp.data.MPLOT)
            HISTP = pymcnp.inp.data.Histp.from_mcnp(string.inp.data.HISTP)
            RAND = pymcnp.inp.data.Rand.from_mcnp(string.inp.data.RAND)
            DBCN = pymcnp.inp.data.Dbcn.from_mcnp(string.inp.data.DBCN)
            LOST = pymcnp.inp.data.Lost.from_mcnp(string.inp.data.LOST)
            IDUM = pymcnp.inp.data.Idum.from_mcnp(string.inp.data.IDUM)
            RDUM = pymcnp.inp.data.Rdum.from_mcnp(string.inp.data.RDUM)
            ZA = pymcnp.inp.data.Za.from_mcnp(string.inp.data.ZA)
            ZB = pymcnp.inp.data.Zb.from_mcnp(string.inp.data.ZB)
            ZC = pymcnp.inp.data.Zc.from_mcnp(string.inp.data.ZC)
            ZD = pymcnp.inp.data.Zd.from_mcnp(string.inp.data.ZD)
            FILES = pymcnp.inp.data.Files.from_mcnp(string.inp.data.FILES)

            class dawwg:
                POINTS = pymcnp.inp.data.dawwg.Points.from_mcnp(string.inp.data.dawwg.POINTS)
                XSEC = pymcnp.inp.data.dawwg.Xsec.from_mcnp(string.inp.data.dawwg.XSEC)
                BLOCK = pymcnp.inp.data.dawwg.Block.from_mcnp(string.inp.data.dawwg.BLOCK)

                class block:
                    NGROUP = pymcnp.inp.data.dawwg.block.Ngroup.from_mcnp(string.inp.data.dawwg.block.NGROUP)
                    ISN = pymcnp.inp.data.dawwg.block.Isn.from_mcnp(string.inp.data.dawwg.block.ISN)
                    NISO = pymcnp.inp.data.dawwg.block.Niso.from_mcnp(string.inp.data.dawwg.block.NISO)
                    MT = pymcnp.inp.data.dawwg.block.Mt.from_mcnp(string.inp.data.dawwg.block.MT)
                    IQUAD = pymcnp.inp.data.dawwg.block.Iquad.from_mcnp(string.inp.data.dawwg.block.IQUAD)
                    FMMIX = pymcnp.inp.data.dawwg.block.Fmmix.from_mcnp(string.inp.data.dawwg.block.FMMIX)
                    NOSOLV = pymcnp.inp.data.dawwg.block.Nosolv.from_mcnp(string.inp.data.dawwg.block.NOSOLV)
                    NOEDIT = pymcnp.inp.data.dawwg.block.Noedit.from_mcnp(string.inp.data.dawwg.block.NOEDIT)
                    NOGEOD = pymcnp.inp.data.dawwg.block.Nogeod.from_mcnp(string.inp.data.dawwg.block.NOGEOD)
                    NOMIX = pymcnp.inp.data.dawwg.block.Nomix.from_mcnp(string.inp.data.dawwg.block.NOMIX)
                    NOASG = pymcnp.inp.data.dawwg.block.Noasg.from_mcnp(string.inp.data.dawwg.block.NOASG)
                    NOMACR = pymcnp.inp.data.dawwg.block.Nomacr.from_mcnp(string.inp.data.dawwg.block.NOMACR)
                    NOSLNP = pymcnp.inp.data.dawwg.block.Noslnp.from_mcnp(string.inp.data.dawwg.block.NOSLNP)
                    NOEDTT = pymcnp.inp.data.dawwg.block.Noedtt.from_mcnp(string.inp.data.dawwg.block.NOEDTT)
                    NOADJM = pymcnp.inp.data.dawwg.block.Noadjm.from_mcnp(string.inp.data.dawwg.block.NOADJM)
                    LIB = pymcnp.inp.data.dawwg.block.Lib.from_mcnp(string.inp.data.dawwg.block.LIB)
                    LIBNAME = pymcnp.inp.data.dawwg.block.Libname.from_mcnp(string.inp.data.dawwg.block.LIBNAME)
                    FISSNEUT = pymcnp.inp.data.dawwg.block.Fissneut.from_mcnp(string.inp.data.dawwg.block.FISSNEUT)
                    LNG = pymcnp.inp.data.dawwg.block.Lng.from_mcnp(string.inp.data.dawwg.block.LNG)
                    BALXS = pymcnp.inp.data.dawwg.block.Balxs.from_mcnp(string.inp.data.dawwg.block.BALXS)
                    NTICHI = pymcnp.inp.data.dawwg.block.Ntichi.from_mcnp(string.inp.data.dawwg.block.NTICHI)
                    IEVT = pymcnp.inp.data.dawwg.block.Ievt.from_mcnp(string.inp.data.dawwg.block.IEVT)
                    ISCT = pymcnp.inp.data.dawwg.block.Isct.from_mcnp(string.inp.data.dawwg.block.ISCT)
                    ITH = pymcnp.inp.data.dawwg.block.Ith.from_mcnp(string.inp.data.dawwg.block.ITH)
                    TRCOR = pymcnp.inp.data.dawwg.block.Trcor.from_mcnp(string.inp.data.dawwg.block.TRCOR)
                    IBL = pymcnp.inp.data.dawwg.block.Ibl.from_mcnp(string.inp.data.dawwg.block.IBL)
                    IBR = pymcnp.inp.data.dawwg.block.Ibr.from_mcnp(string.inp.data.dawwg.block.IBR)
                    IBT = pymcnp.inp.data.dawwg.block.Ibt.from_mcnp(string.inp.data.dawwg.block.IBT)
                    IBB = pymcnp.inp.data.dawwg.block.Ibb.from_mcnp(string.inp.data.dawwg.block.IBB)
                    IBFRNT = pymcnp.inp.data.dawwg.block.Ibfrnt.from_mcnp(string.inp.data.dawwg.block.IBFRNT)
                    IBBACK = pymcnp.inp.data.dawwg.block.Ibback.from_mcnp(string.inp.data.dawwg.block.IBBACK)
                    EPSI = pymcnp.inp.data.dawwg.block.Epsi.from_mcnp(string.inp.data.dawwg.block.EPSI)
                    OITM = pymcnp.inp.data.dawwg.block.Oitm.from_mcnp(string.inp.data.dawwg.block.OITM)
                    NOSIGF = pymcnp.inp.data.dawwg.block.Nosigf.from_mcnp(string.inp.data.dawwg.block.NOSIGF)
                    SRCACC = pymcnp.inp.data.dawwg.block.Srcacc.from_mcnp(string.inp.data.dawwg.block.SRCACC)
                    DIFFSOL = pymcnp.inp.data.dawwg.block.Diffsol.from_mcnp(string.inp.data.dawwg.block.DIFFSOL)
                    TSASN = pymcnp.inp.data.dawwg.block.Tsasn.from_mcnp(string.inp.data.dawwg.block.TSASN)
                    TSAEPSI = pymcnp.inp.data.dawwg.block.Tsaepsi.from_mcnp(string.inp.data.dawwg.block.TSAEPSI)
                    TSAITS = pymcnp.inp.data.dawwg.block.Tsaits.from_mcnp(string.inp.data.dawwg.block.TSAITS)
                    TSABETA = pymcnp.inp.data.dawwg.block.Tsabeta.from_mcnp(string.inp.data.dawwg.block.TSABETA)
                    PTCONV = pymcnp.inp.data.dawwg.block.Ptconv.from_mcnp(string.inp.data.dawwg.block.PTCONV)
                    NORM = pymcnp.inp.data.dawwg.block.Norm.from_mcnp(string.inp.data.dawwg.block.NORM)
                    XSECTP = pymcnp.inp.data.dawwg.block.Xsectp.from_mcnp(string.inp.data.dawwg.block.XSECTP)
                    FISSRP = pymcnp.inp.data.dawwg.block.Fissrp.from_mcnp(string.inp.data.dawwg.block.FISSRP)
                    SOURCP = pymcnp.inp.data.dawwg.block.Sourcp.from_mcnp(string.inp.data.dawwg.block.SOURCP)
                    ANGP = pymcnp.inp.data.dawwg.block.Angp.from_mcnp(string.inp.data.dawwg.block.ANGP)
                    BALP = pymcnp.inp.data.dawwg.block.Balp.from_mcnp(string.inp.data.dawwg.block.BALP)
                    RAFLUX = pymcnp.inp.data.dawwg.block.Raflux.from_mcnp(string.inp.data.dawwg.block.RAFLUX)
                    RMFLUX = pymcnp.inp.data.dawwg.block.Rmflux.from_mcnp(string.inp.data.dawwg.block.RMFLUX)
                    AVATAR = pymcnp.inp.data.dawwg.block.Avatar.from_mcnp(string.inp.data.dawwg.block.AVATAR)
                    ASLEFT = pymcnp.inp.data.dawwg.block.Asleft.from_mcnp(string.inp.data.dawwg.block.ASLEFT)
                    ASRITE = pymcnp.inp.data.dawwg.block.Asrite.from_mcnp(string.inp.data.dawwg.block.ASRITE)
                    ASBOTT = pymcnp.inp.data.dawwg.block.Asbott.from_mcnp(string.inp.data.dawwg.block.ASBOTT)
                    ASTOP = pymcnp.inp.data.dawwg.block.Astop.from_mcnp(string.inp.data.dawwg.block.ASTOP)
                    ASFRNT = pymcnp.inp.data.dawwg.block.Asfrnt.from_mcnp(string.inp.data.dawwg.block.ASFRNT)
                    ASBACK = pymcnp.inp.data.dawwg.block.Asback.from_mcnp(string.inp.data.dawwg.block.ASBACK)
                    MASSED = pymcnp.inp.data.dawwg.block.Massed.from_mcnp(string.inp.data.dawwg.block.MASSED)
                    PTED = pymcnp.inp.data.dawwg.block.Pted.from_mcnp(string.inp.data.dawwg.block.PTED)
                    ZNED = pymcnp.inp.data.dawwg.block.Zned.from_mcnp(string.inp.data.dawwg.block.ZNED)
                    RZFLUX = pymcnp.inp.data.dawwg.block.Rzflux.from_mcnp(string.inp.data.dawwg.block.RZFLUX)
                    RZMFLUX = pymcnp.inp.data.dawwg.block.Rzmflux.from_mcnp(string.inp.data.dawwg.block.RZMFLUX)
                    EDOUTF = pymcnp.inp.data.dawwg.block.Edoutf.from_mcnp(string.inp.data.dawwg.block.EDOUTF)
                    BYVOLP = pymcnp.inp.data.dawwg.block.Byvolp.from_mcnp(string.inp.data.dawwg.block.BYVOLP)
                    AJED = pymcnp.inp.data.dawwg.block.Ajed.from_mcnp(string.inp.data.dawwg.block.AJED)
                    FLUXONE = pymcnp.inp.data.dawwg.block.Fluxone.from_mcnp(string.inp.data.dawwg.block.FLUXONE)

            class embed:
                BACKGROUND = pymcnp.inp.data.embed.Background.from_mcnp(string.inp.data.embed.BACKGROUND)
                MATCELL = pymcnp.inp.data.embed.Matcell.from_mcnp(string.inp.data.embed.MATCELL)
                MESHGEO = pymcnp.inp.data.embed.Meshgeo.from_mcnp(string.inp.data.embed.MESHGEO)
                MGEOIN = pymcnp.inp.data.embed.Mgeoin.from_mcnp(string.inp.data.embed.MGEOIN)
                MEEOUT = pymcnp.inp.data.embed.Meeout.from_mcnp(string.inp.data.embed.MEEOUT)
                MEEIN = pymcnp.inp.data.embed.Meein.from_mcnp(string.inp.data.embed.MEEIN)
                CALCVOLS = pymcnp.inp.data.embed.Calcvols.from_mcnp(string.inp.data.embed.CALCVOLS)
                DEBUG = pymcnp.inp.data.embed.Debug.from_mcnp(string.inp.data.embed.DEBUG)
                FILETYPE = pymcnp.inp.data.embed.Filetype.from_mcnp(string.inp.data.embed.FILETYPE)
                GMVFILE = pymcnp.inp.data.embed.Gmvfile.from_mcnp(string.inp.data.embed.GMVFILE)
                LENGTH = pymcnp.inp.data.embed.Length.from_mcnp(string.inp.data.embed.LENGTH)
                MCNPUMFILE = pymcnp.inp.data.embed.Mcnpumfile.from_mcnp(string.inp.data.embed.MCNPUMFILE)

            class embee:
                EMBED = pymcnp.inp.data.embee.Embed.from_mcnp(string.inp.data.embee.EMBED)
                ENERGY = pymcnp.inp.data.embee.Energy.from_mcnp(string.inp.data.embee.ENERGY)
                TIME = pymcnp.inp.data.embee.Time.from_mcnp(string.inp.data.embee.TIME)
                ATOM = pymcnp.inp.data.embee.Atom.from_mcnp(string.inp.data.embee.ATOM)
                FACTOR = pymcnp.inp.data.embee.Factor.from_mcnp(string.inp.data.embee.FACTOR)
                LIST = pymcnp.inp.data.embee.List.from_mcnp(string.inp.data.embee.LIST)
                MAT = pymcnp.inp.data.embee.Mat.from_mcnp(string.inp.data.embee.MAT)
                MTYPE = pymcnp.inp.data.embee.Mtype.from_mcnp(string.inp.data.embee.MTYPE)

            class m_0:
                GAS = pymcnp.inp.data.m_0.Gas.from_mcnp(string.inp.data.m_0.GAS)
                ESTEP = pymcnp.inp.data.m_0.Estep.from_mcnp(string.inp.data.m_0.ESTEP)
                HSTEP = pymcnp.inp.data.m_0.Hstep.from_mcnp(string.inp.data.m_0.HSTEP)
                NLIB = pymcnp.inp.data.m_0.Nlib.from_mcnp(string.inp.data.m_0.NLIB)
                PLIB = pymcnp.inp.data.m_0.Plib.from_mcnp(string.inp.data.m_0.PLIB)
                PNLIB = pymcnp.inp.data.m_0.Pnlib.from_mcnp(string.inp.data.m_0.PNLIB)
                ELIB = pymcnp.inp.data.m_0.Elib.from_mcnp(string.inp.data.m_0.ELIB)
                HLIB = pymcnp.inp.data.m_0.Hlib.from_mcnp(string.inp.data.m_0.HLIB)
                ALIB = pymcnp.inp.data.m_0.Alib.from_mcnp(string.inp.data.m_0.ALIB)
                SLIB = pymcnp.inp.data.m_0.Slib.from_mcnp(string.inp.data.m_0.SLIB)
                TLIB = pymcnp.inp.data.m_0.Tlib.from_mcnp(string.inp.data.m_0.TLIB)
                DLIB = pymcnp.inp.data.m_0.Dlib.from_mcnp(string.inp.data.m_0.DLIB)
                COND = pymcnp.inp.data.m_0.Cond.from_mcnp(string.inp.data.m_0.COND)
                REFI = pymcnp.inp.data.m_0.Refi.from_mcnp(string.inp.data.m_0.REFI)
                REFC = pymcnp.inp.data.m_0.Refc.from_mcnp(string.inp.data.m_0.REFC)
                REFS = pymcnp.inp.data.m_0.Refs.from_mcnp(string.inp.data.m_0.REFS)

            class act:
                FISSION = pymcnp.inp.data.act.Fission.from_mcnp(string.inp.data.act.FISSION)
                NONFISS = pymcnp.inp.data.act.Nonfiss.from_mcnp(string.inp.data.act.NONFISS)
                DN = pymcnp.inp.data.act.Dn.from_mcnp(string.inp.data.act.DN)
                DG = pymcnp.inp.data.act.Dg.from_mcnp(string.inp.data.act.DG)
                THRESH = pymcnp.inp.data.act.Thresh.from_mcnp(string.inp.data.act.THRESH)
                DNBAIS = pymcnp.inp.data.act.Dnbais.from_mcnp(string.inp.data.act.DNBAIS)
                NAP = pymcnp.inp.data.act.Nap.from_mcnp(string.inp.data.act.NAP)
                DNEB = pymcnp.inp.data.act.Dneb.from_mcnp(string.inp.data.act.DNEB)
                DGEB = pymcnp.inp.data.act.Dgeb.from_mcnp(string.inp.data.act.DGEB)
                PECUT = pymcnp.inp.data.act.Pecut.from_mcnp(string.inp.data.act.PECUT)
                HLCUT = pymcnp.inp.data.act.Hlcut.from_mcnp(string.inp.data.act.HLCUT)
                SAMPLE = pymcnp.inp.data.act.Sample.from_mcnp(string.inp.data.act.SAMPLE)

            class fmult:
                SFNU = pymcnp.inp.data.fmult.Sfnu.from_mcnp(string.inp.data.fmult.SFNU)
                WIDTH = pymcnp.inp.data.fmult.Width.from_mcnp(string.inp.data.fmult.WIDTH)
                SFYIELD = pymcnp.inp.data.fmult.Sfyield.from_mcnp(string.inp.data.fmult.SFYIELD)
                WATT = pymcnp.inp.data.fmult.Watt.from_mcnp(string.inp.data.fmult.WATT)
                METHOD = pymcnp.inp.data.fmult.Method.from_mcnp(string.inp.data.fmult.METHOD)
                DATA = pymcnp.inp.data.fmult.Data.from_mcnp(string.inp.data.fmult.DATA)
                SHIFT = pymcnp.inp.data.fmult.Shift.from_mcnp(string.inp.data.fmult.SHIFT)

            class tropt:
                MCSCAT = pymcnp.inp.data.tropt.Mcscat.from_mcnp(string.inp.data.tropt.MCSCAT)
                ELOSS = pymcnp.inp.data.tropt.Eloss.from_mcnp(string.inp.data.tropt.ELOSS)
                NREACT = pymcnp.inp.data.tropt.Nreact.from_mcnp(string.inp.data.tropt.NREACT)
                NESCAT = pymcnp.inp.data.tropt.Nescat.from_mcnp(string.inp.data.tropt.NESCAT)
                GENXS = pymcnp.inp.data.tropt.Genxs.from_mcnp(string.inp.data.tropt.GENXS)

            class bfld:
                FIELD = pymcnp.inp.data.bfld.Field.from_mcnp(string.inp.data.bfld.FIELD)
                VEC = pymcnp.inp.data.bfld.Vec.from_mcnp(string.inp.data.bfld.VEC)
                MAXDEFLC = pymcnp.inp.data.bfld.Maxdeflc.from_mcnp(string.inp.data.bfld.MAXDEFLC)
                MAXSTEP = pymcnp.inp.data.bfld.Maxstep.from_mcnp(string.inp.data.bfld.MAXSTEP)
                AXS = pymcnp.inp.data.bfld.Axs.from_mcnp(string.inp.data.bfld.AXS)
                FFEDGES = pymcnp.inp.data.bfld.Ffedges.from_mcnp(string.inp.data.bfld.FFEDGES)
                REFPNT = pymcnp.inp.data.bfld.Refpnt.from_mcnp(string.inp.data.bfld.REFPNT)

            class sdef:
                CEL = pymcnp.inp.data.sdef.Cel.from_mcnp(string.inp.data.sdef.CEL)
                SUR = pymcnp.inp.data.sdef.Sur.from_mcnp(string.inp.data.sdef.SUR)
                ERG_0 = pymcnp.inp.data.sdef.Erg_0.from_mcnp(string.inp.data.sdef.ERG_0)
                ERG_1 = pymcnp.inp.data.sdef.Erg_1.from_mcnp(string.inp.data.sdef.ERG_1)
                TME_0 = pymcnp.inp.data.sdef.Tme_0.from_mcnp(string.inp.data.sdef.TME_0)
                TME_1 = pymcnp.inp.data.sdef.Tme_1.from_mcnp(string.inp.data.sdef.TME_1)
                DIR_0 = pymcnp.inp.data.sdef.Dir_0.from_mcnp(string.inp.data.sdef.DIR_0)
                DIR_1 = pymcnp.inp.data.sdef.Dir_1.from_mcnp(string.inp.data.sdef.DIR_1)
                VEC = pymcnp.inp.data.sdef.Vec.from_mcnp(string.inp.data.sdef.VEC)
                NRM = pymcnp.inp.data.sdef.Nrm.from_mcnp(string.inp.data.sdef.NRM)
                POS = pymcnp.inp.data.sdef.Pos.from_mcnp(string.inp.data.sdef.POS)
                RAD_0 = pymcnp.inp.data.sdef.Rad_0.from_mcnp(string.inp.data.sdef.RAD_0)
                RAD_1 = pymcnp.inp.data.sdef.Rad_1.from_mcnp(string.inp.data.sdef.RAD_1)
                EXT = pymcnp.inp.data.sdef.Ext.from_mcnp(string.inp.data.sdef.EXT)
                AXS = pymcnp.inp.data.sdef.Axs.from_mcnp(string.inp.data.sdef.AXS)
                X = pymcnp.inp.data.sdef.X.from_mcnp(string.inp.data.sdef.X)
                Y = pymcnp.inp.data.sdef.Y.from_mcnp(string.inp.data.sdef.Y)
                Z = pymcnp.inp.data.sdef.Z.from_mcnp(string.inp.data.sdef.Z)
                CCC = pymcnp.inp.data.sdef.Ccc.from_mcnp(string.inp.data.sdef.CCC)
                ARA = pymcnp.inp.data.sdef.Ara.from_mcnp(string.inp.data.sdef.ARA)
                WGT = pymcnp.inp.data.sdef.Wgt.from_mcnp(string.inp.data.sdef.WGT)
                TR_0 = pymcnp.inp.data.sdef.Tr_0.from_mcnp(string.inp.data.sdef.TR_0)
                TR_1 = pymcnp.inp.data.sdef.Tr_1.from_mcnp(string.inp.data.sdef.TR_1)
                EFF = pymcnp.inp.data.sdef.Eff.from_mcnp(string.inp.data.sdef.EFF)
                PAR = pymcnp.inp.data.sdef.Par.from_mcnp(string.inp.data.sdef.PAR)
                DAT = pymcnp.inp.data.sdef.Dat.from_mcnp(string.inp.data.sdef.DAT)
                LOC = pymcnp.inp.data.sdef.Loc.from_mcnp(string.inp.data.sdef.LOC)
                BEM = pymcnp.inp.data.sdef.Bem.from_mcnp(string.inp.data.sdef.BEM)
                BAP = pymcnp.inp.data.sdef.Bap.from_mcnp(string.inp.data.sdef.BAP)

            class ssw:
                SYM = pymcnp.inp.data.ssw.Sym.from_mcnp(string.inp.data.ssw.SYM)
                PTY = pymcnp.inp.data.ssw.Pty.from_mcnp(string.inp.data.ssw.PTY)
                CEL = pymcnp.inp.data.ssw.Cel.from_mcnp(string.inp.data.ssw.CEL)

            class ssr:
                OLD = pymcnp.inp.data.ssr.Old.from_mcnp(string.inp.data.ssr.OLD)
                CEL = pymcnp.inp.data.ssr.Cel.from_mcnp(string.inp.data.ssr.CEL)
                NEW = pymcnp.inp.data.ssr.New.from_mcnp(string.inp.data.ssr.NEW)
                PTY = pymcnp.inp.data.ssr.Pty.from_mcnp(string.inp.data.ssr.PTY)
                COL = pymcnp.inp.data.ssr.Col.from_mcnp(string.inp.data.ssr.COL)
                WGT = pymcnp.inp.data.ssr.Wgt.from_mcnp(string.inp.data.ssr.WGT)
                TR_0 = pymcnp.inp.data.ssr.Tr_0.from_mcnp(string.inp.data.ssr.TR_0)
                TR_1 = pymcnp.inp.data.ssr.Tr_1.from_mcnp(string.inp.data.ssr.TR_1)
                PSC = pymcnp.inp.data.ssr.Psc.from_mcnp(string.inp.data.ssr.PSC)
                AXS = pymcnp.inp.data.ssr.Axs.from_mcnp(string.inp.data.ssr.AXS)
                EXT = pymcnp.inp.data.ssr.Ext.from_mcnp(string.inp.data.ssr.EXT)
                POA = pymcnp.inp.data.ssr.Poa.from_mcnp(string.inp.data.ssr.POA)
                BCW = pymcnp.inp.data.ssr.Bcw.from_mcnp(string.inp.data.ssr.BCW)

            class kopts:
                BLOCKSIZE = pymcnp.inp.data.kopts.Blocksize.from_mcnp(string.inp.data.kopts.BLOCKSIZE)
                KINETICS = pymcnp.inp.data.kopts.Kinetics.from_mcnp(string.inp.data.kopts.KINETICS)
                PRECURSOR = pymcnp.inp.data.kopts.Precursor.from_mcnp(string.inp.data.kopts.PRECURSOR)
                KSENTAL = pymcnp.inp.data.kopts.Ksental.from_mcnp(string.inp.data.kopts.KSENTAL)
                FMAT = pymcnp.inp.data.kopts.Fmat.from_mcnp(string.inp.data.kopts.FMAT)
                FMATSKPT = pymcnp.inp.data.kopts.Fmatskpt.from_mcnp(string.inp.data.kopts.FMATSKPT)
                FMATNCYC = pymcnp.inp.data.kopts.Fmatncyc.from_mcnp(string.inp.data.kopts.FMATNCYC)
                FMATSPACE = pymcnp.inp.data.kopts.Fmatspace.from_mcnp(string.inp.data.kopts.FMATSPACE)
                FMATACCEL = pymcnp.inp.data.kopts.Fmataccel.from_mcnp(string.inp.data.kopts.FMATACCEL)
                FMATREDUCE = pymcnp.inp.data.kopts.Fmatreduce.from_mcnp(string.inp.data.kopts.FMATREDUCE)
                FMATNX = pymcnp.inp.data.kopts.Fmatnx.from_mcnp(string.inp.data.kopts.FMATNX)
                FMATNY = pymcnp.inp.data.kopts.Fmatny.from_mcnp(string.inp.data.kopts.FMATNY)
                FMATNZ = pymcnp.inp.data.kopts.Fmatnz.from_mcnp(string.inp.data.kopts.FMATNZ)

            class t_1:
                CBEG = pymcnp.inp.data.t_1.Cbeg.from_mcnp(string.inp.data.t_1.CBEG)
                CFRQ = pymcnp.inp.data.t_1.Cfrq.from_mcnp(string.inp.data.t_1.CFRQ)
                COFI = pymcnp.inp.data.t_1.Cofi.from_mcnp(string.inp.data.t_1.COFI)
                CONI = pymcnp.inp.data.t_1.Coni.from_mcnp(string.inp.data.t_1.CONI)
                CSUB = pymcnp.inp.data.t_1.Csub.from_mcnp(string.inp.data.t_1.CSUB)
                CEND = pymcnp.inp.data.t_1.Cend.from_mcnp(string.inp.data.t_1.CEND)

            class df_1:
                IU = pymcnp.inp.data.df_1.Iu.from_mcnp(string.inp.data.df_1.IU)
                FAC = pymcnp.inp.data.df_1.Fac.from_mcnp(string.inp.data.df_1.FAC)
                IC = pymcnp.inp.data.df_1.Ic.from_mcnp(string.inp.data.df_1.IC)
                LOG = pymcnp.inp.data.df_1.Log.from_mcnp(string.inp.data.df_1.LOG)
                LIN = pymcnp.inp.data.df_1.Lin.from_mcnp(string.inp.data.df_1.LIN)

            class pert:
                CELL = pymcnp.inp.data.pert.Cell.from_mcnp(string.inp.data.pert.CELL)
                MAT = pymcnp.inp.data.pert.Mat.from_mcnp(string.inp.data.pert.MAT)
                RHO = pymcnp.inp.data.pert.Rho.from_mcnp(string.inp.data.pert.RHO)
                METHOD = pymcnp.inp.data.pert.Method.from_mcnp(string.inp.data.pert.METHOD)
                ERG = pymcnp.inp.data.pert.Erg.from_mcnp(string.inp.data.pert.ERG)
                RXN = pymcnp.inp.data.pert.Rxn.from_mcnp(string.inp.data.pert.RXN)

            class kpert:
                CELL = pymcnp.inp.data.kpert.Cell.from_mcnp(string.inp.data.kpert.CELL)
                MAT = pymcnp.inp.data.kpert.Mat.from_mcnp(string.inp.data.kpert.MAT)
                RHO = pymcnp.inp.data.kpert.Rho.from_mcnp(string.inp.data.kpert.RHO)
                ISO = pymcnp.inp.data.kpert.Iso.from_mcnp(string.inp.data.kpert.ISO)
                RXN = pymcnp.inp.data.kpert.Rxn.from_mcnp(string.inp.data.kpert.RXN)
                ERG = pymcnp.inp.data.kpert.Erg.from_mcnp(string.inp.data.kpert.ERG)
                LINEAR = pymcnp.inp.data.kpert.Linear.from_mcnp(string.inp.data.kpert.LINEAR)

            class ksen:
                ISO = pymcnp.inp.data.ksen.Iso.from_mcnp(string.inp.data.ksen.ISO)
                RXN = pymcnp.inp.data.ksen.Rxn.from_mcnp(string.inp.data.ksen.RXN)
                MT = pymcnp.inp.data.ksen.Mt.from_mcnp(string.inp.data.ksen.MT)
                ERG = pymcnp.inp.data.ksen.Erg.from_mcnp(string.inp.data.ksen.ERG)
                EIN = pymcnp.inp.data.ksen.Ein.from_mcnp(string.inp.data.ksen.EIN)
                LEGENDRE = pymcnp.inp.data.ksen.Legendre.from_mcnp(string.inp.data.ksen.LEGENDRE)
                COS = pymcnp.inp.data.ksen.Cos.from_mcnp(string.inp.data.ksen.COS)
                CONSTRAIN = pymcnp.inp.data.ksen.Constrain.from_mcnp(string.inp.data.ksen.CONSTRAIN)

            class fmesh:
                GEOM = pymcnp.inp.data.fmesh.Geom.from_mcnp(string.inp.data.fmesh.GEOM)
                ORIGIN = pymcnp.inp.data.fmesh.Origin.from_mcnp(string.inp.data.fmesh.ORIGIN)
                AXS = pymcnp.inp.data.fmesh.Axs.from_mcnp(string.inp.data.fmesh.AXS)
                VEC = pymcnp.inp.data.fmesh.Vec.from_mcnp(string.inp.data.fmesh.VEC)
                IMESH = pymcnp.inp.data.fmesh.Imesh.from_mcnp(string.inp.data.fmesh.IMESH)
                IINTS = pymcnp.inp.data.fmesh.Iints.from_mcnp(string.inp.data.fmesh.IINTS)
                JMESH = pymcnp.inp.data.fmesh.Jmesh.from_mcnp(string.inp.data.fmesh.JMESH)
                JINTS = pymcnp.inp.data.fmesh.Jints.from_mcnp(string.inp.data.fmesh.JINTS)
                KMESH = pymcnp.inp.data.fmesh.Kmesh.from_mcnp(string.inp.data.fmesh.KMESH)
                KINTS = pymcnp.inp.data.fmesh.Kints.from_mcnp(string.inp.data.fmesh.KINTS)
                EMESH = pymcnp.inp.data.fmesh.Emesh.from_mcnp(string.inp.data.fmesh.EMESH)
                EINTS = pymcnp.inp.data.fmesh.Eints.from_mcnp(string.inp.data.fmesh.EINTS)
                ENORM = pymcnp.inp.data.fmesh.Enorm.from_mcnp(string.inp.data.fmesh.ENORM)
                TMESH = pymcnp.inp.data.fmesh.Tmesh.from_mcnp(string.inp.data.fmesh.TMESH)
                TINTS = pymcnp.inp.data.fmesh.Tints.from_mcnp(string.inp.data.fmesh.TINTS)
                TNORM = pymcnp.inp.data.fmesh.Tnorm.from_mcnp(string.inp.data.fmesh.TNORM)
                FACTOR = pymcnp.inp.data.fmesh.Factor.from_mcnp(string.inp.data.fmesh.FACTOR)
                OUT = pymcnp.inp.data.fmesh.Out.from_mcnp(string.inp.data.fmesh.OUT)
                TR = pymcnp.inp.data.fmesh.Tr.from_mcnp(string.inp.data.fmesh.TR)
                INC = pymcnp.inp.data.fmesh.Inc.from_mcnp(string.inp.data.fmesh.INC)
                TYPE = pymcnp.inp.data.fmesh.Type.from_mcnp(string.inp.data.fmesh.TYPE)
                KCLEAR = pymcnp.inp.data.fmesh.Kclear.from_mcnp(string.inp.data.fmesh.KCLEAR)

            class var:
                RR = pymcnp.inp.data.var.Rr.from_mcnp(string.inp.data.var.RR)

            class mesh:
                GEOM = pymcnp.inp.data.mesh.Geom.from_mcnp(string.inp.data.mesh.GEOM)
                REF = pymcnp.inp.data.mesh.Ref.from_mcnp(string.inp.data.mesh.REF)
                ORIGIN = pymcnp.inp.data.mesh.Origin.from_mcnp(string.inp.data.mesh.ORIGIN)
                AXS = pymcnp.inp.data.mesh.Axs.from_mcnp(string.inp.data.mesh.AXS)
                VEC = pymcnp.inp.data.mesh.Vec.from_mcnp(string.inp.data.mesh.VEC)
                IMESH = pymcnp.inp.data.mesh.Imesh.from_mcnp(string.inp.data.mesh.IMESH)
                IINTS = pymcnp.inp.data.mesh.Iints.from_mcnp(string.inp.data.mesh.IINTS)
                JMESH = pymcnp.inp.data.mesh.Jmesh.from_mcnp(string.inp.data.mesh.JMESH)
                JINTS = pymcnp.inp.data.mesh.Jints.from_mcnp(string.inp.data.mesh.JINTS)
                KMESH = pymcnp.inp.data.mesh.Kmesh.from_mcnp(string.inp.data.mesh.KMESH)
                KINTS = pymcnp.inp.data.mesh.Kints.from_mcnp(string.inp.data.mesh.KINTS)

            class stop:
                NPS = pymcnp.inp.data.stop.Nps.from_mcnp(string.inp.data.stop.NPS)
                CTME = pymcnp.inp.data.stop.Ctme.from_mcnp(string.inp.data.stop.CTME)
                F = pymcnp.inp.data.stop.F.from_mcnp(string.inp.data.stop.F)

            class ptrac:
                BUFFER = pymcnp.inp.data.ptrac.Buffer.from_mcnp(string.inp.data.ptrac.BUFFER)
                FILE = pymcnp.inp.data.ptrac.File.from_mcnp(string.inp.data.ptrac.FILE)
                MAX = pymcnp.inp.data.ptrac.Max.from_mcnp(string.inp.data.ptrac.MAX)
                MEPH = pymcnp.inp.data.ptrac.Meph.from_mcnp(string.inp.data.ptrac.MEPH)
                WRITE = pymcnp.inp.data.ptrac.Write.from_mcnp(string.inp.data.ptrac.WRITE)
                CONIC = pymcnp.inp.data.ptrac.Conic.from_mcnp(string.inp.data.ptrac.CONIC)
                EVENT = pymcnp.inp.data.ptrac.Event.from_mcnp(string.inp.data.ptrac.EVENT)
                FILTER = pymcnp.inp.data.ptrac.Filter.from_mcnp(string.inp.data.ptrac.FILTER)
                TYPE = pymcnp.inp.data.ptrac.Type.from_mcnp(string.inp.data.ptrac.TYPE)
                NPS = pymcnp.inp.data.ptrac.Nps.from_mcnp(string.inp.data.ptrac.NPS)
                CELL = pymcnp.inp.data.ptrac.Cell.from_mcnp(string.inp.data.ptrac.CELL)
                SURFACE = pymcnp.inp.data.ptrac.Surface.from_mcnp(string.inp.data.ptrac.SURFACE)
                TALLY = pymcnp.inp.data.ptrac.Tally.from_mcnp(string.inp.data.ptrac.TALLY)
                VALUE = pymcnp.inp.data.ptrac.Value.from_mcnp(string.inp.data.ptrac.VALUE)

            class mplot:
                TERM = pymcnp.inp.data.mplot.Term.from_mcnp(string.inp.data.mplot.TERM)
                FILE = pymcnp.inp.data.mplot.File.from_mcnp(string.inp.data.mplot.FILE)
                COPLOT = pymcnp.inp.data.mplot.Coplot.from_mcnp(string.inp.data.mplot.COPLOT)
                FREQ = pymcnp.inp.data.mplot.Freq.from_mcnp(string.inp.data.mplot.FREQ)
                RETURN = pymcnp.inp.data.mplot.Return.from_mcnp(string.inp.data.mplot.RETURN)
                PLOT = pymcnp.inp.data.mplot.Plot.from_mcnp(string.inp.data.mplot.PLOT)
                PAUSE = pymcnp.inp.data.mplot.Pause.from_mcnp(string.inp.data.mplot.PAUSE)
                END = pymcnp.inp.data.mplot.End.from_mcnp(string.inp.data.mplot.END)
                OPTIONS = pymcnp.inp.data.mplot.Options.from_mcnp(string.inp.data.mplot.OPTIONS)
                HELP = pymcnp.inp.data.mplot.Help.from_mcnp(string.inp.data.mplot.HELP)
                STATUS = pymcnp.inp.data.mplot.Status.from_mcnp(string.inp.data.mplot.STATUS)
                PRINTAL = pymcnp.inp.data.mplot.Printal.from_mcnp(string.inp.data.mplot.PRINTAL)
                IPTAL = pymcnp.inp.data.mplot.Iptal.from_mcnp(string.inp.data.mplot.IPTAL)
                PRINTPTS = pymcnp.inp.data.mplot.Printpts.from_mcnp(string.inp.data.mplot.PRINTPTS)
                RUNTPE = pymcnp.inp.data.mplot.Runtpe.from_mcnp(string.inp.data.mplot.RUNTPE)
                DUMP = pymcnp.inp.data.mplot.Dump.from_mcnp(string.inp.data.mplot.DUMP)
                WMCTAL = pymcnp.inp.data.mplot.Wmctal.from_mcnp(string.inp.data.mplot.WMCTAL)
                RMCTAL = pymcnp.inp.data.mplot.Rmctal.from_mcnp(string.inp.data.mplot.RMCTAL)
                TALLY = pymcnp.inp.data.mplot.Tally.from_mcnp(string.inp.data.mplot.TALLY)
                PERT = pymcnp.inp.data.mplot.Pert.from_mcnp(string.inp.data.mplot.PERT)
                LETHARGY = pymcnp.inp.data.mplot.Lethargy.from_mcnp(string.inp.data.mplot.LETHARGY)
                NONORM = pymcnp.inp.data.mplot.Nonorm.from_mcnp(string.inp.data.mplot.NONORM)
                FACTOR = pymcnp.inp.data.mplot.Factor.from_mcnp(string.inp.data.mplot.FACTOR)
                RESET = pymcnp.inp.data.mplot.Reset.from_mcnp(string.inp.data.mplot.RESET)
                TITLE = pymcnp.inp.data.mplot.Title.from_mcnp(string.inp.data.mplot.TITLE)
                BELOW = pymcnp.inp.data.mplot.Below.from_mcnp(string.inp.data.mplot.BELOW)
                SUBTITLE = pymcnp.inp.data.mplot.Subtitle.from_mcnp(string.inp.data.mplot.SUBTITLE)
                XTITLE = pymcnp.inp.data.mplot.Xtitle.from_mcnp(string.inp.data.mplot.XTITLE)
                YTITLE = pymcnp.inp.data.mplot.Ytitle.from_mcnp(string.inp.data.mplot.YTITLE)
                ZTITLE = pymcnp.inp.data.mplot.Ztitle.from_mcnp(string.inp.data.mplot.ZTITLE)
                LABEL = pymcnp.inp.data.mplot.Label.from_mcnp(string.inp.data.mplot.LABEL)
                FREE = pymcnp.inp.data.mplot.Free.from_mcnp(string.inp.data.mplot.FREE)
                FIXED = pymcnp.inp.data.mplot.Fixed.from_mcnp(string.inp.data.mplot.FIXED)
                SET = pymcnp.inp.data.mplot.Set.from_mcnp(string.inp.data.mplot.SET)
                TFC = pymcnp.inp.data.mplot.Tfc.from_mcnp(string.inp.data.mplot.TFC)
                KCODE = pymcnp.inp.data.mplot.Kcode.from_mcnp(string.inp.data.mplot.KCODE)
                XS_0 = pymcnp.inp.data.mplot.Xs_0.from_mcnp(string.inp.data.mplot.XS_0)
                XS_1 = pymcnp.inp.data.mplot.Xs_1.from_mcnp(string.inp.data.mplot.XS_1)
                XS_2 = pymcnp.inp.data.mplot.Xs_2.from_mcnp(string.inp.data.mplot.XS_2)
                MT = pymcnp.inp.data.mplot.Mt.from_mcnp(string.inp.data.mplot.MT)
                PAR = pymcnp.inp.data.mplot.Par.from_mcnp(string.inp.data.mplot.PAR)
                LINLIN = pymcnp.inp.data.mplot.Linlin.from_mcnp(string.inp.data.mplot.LINLIN)
                LINLOG = pymcnp.inp.data.mplot.Linlog.from_mcnp(string.inp.data.mplot.LINLOG)
                LOGLIN = pymcnp.inp.data.mplot.Loglin.from_mcnp(string.inp.data.mplot.LOGLIN)
                LOGLOG = pymcnp.inp.data.mplot.Loglog.from_mcnp(string.inp.data.mplot.LOGLOG)
                XLIMS = pymcnp.inp.data.mplot.Xlims.from_mcnp(string.inp.data.mplot.XLIMS)
                YLIMS = pymcnp.inp.data.mplot.Ylims.from_mcnp(string.inp.data.mplot.YLIMS)
                SCALES = pymcnp.inp.data.mplot.Scales.from_mcnp(string.inp.data.mplot.SCALES)
                HIST = pymcnp.inp.data.mplot.Hist.from_mcnp(string.inp.data.mplot.HIST)
                PLINEAR = pymcnp.inp.data.mplot.Plinear.from_mcnp(string.inp.data.mplot.PLINEAR)
                SPLINE = pymcnp.inp.data.mplot.Spline.from_mcnp(string.inp.data.mplot.SPLINE)
                BAR = pymcnp.inp.data.mplot.Bar.from_mcnp(string.inp.data.mplot.BAR)
                NOERRBAR = pymcnp.inp.data.mplot.Noerrbar.from_mcnp(string.inp.data.mplot.NOERRBAR)
                THICK = pymcnp.inp.data.mplot.Thick.from_mcnp(string.inp.data.mplot.THICK)
                THIN = pymcnp.inp.data.mplot.Thin.from_mcnp(string.inp.data.mplot.THIN)
                LEGEND = pymcnp.inp.data.mplot.Legend.from_mcnp(string.inp.data.mplot.LEGEND)
                CONTOUR = pymcnp.inp.data.mplot.Contour.from_mcnp(string.inp.data.mplot.CONTOUR)
                WASH = pymcnp.inp.data.mplot.Wash.from_mcnp(string.inp.data.mplot.WASH)
                FMESH = pymcnp.inp.data.mplot.Fmesh.from_mcnp(string.inp.data.mplot.FMESH)
                FMRELERR = pymcnp.inp.data.mplot.Fmrelerr.from_mcnp(string.inp.data.mplot.FMRELERR)
                ZLEV = pymcnp.inp.data.mplot.Zlev.from_mcnp(string.inp.data.mplot.ZLEV)
                EBIN = pymcnp.inp.data.mplot.Ebin.from_mcnp(string.inp.data.mplot.EBIN)
                TBIN = pymcnp.inp.data.mplot.Tbin.from_mcnp(string.inp.data.mplot.TBIN)
                COP = pymcnp.inp.data.mplot.Cop.from_mcnp(string.inp.data.mplot.COP)
                TAL = pymcnp.inp.data.mplot.Tal.from_mcnp(string.inp.data.mplot.TAL)

                class free:
                    ALL = pymcnp.inp.data.mplot.free.All.from_mcnp(string.inp.data.mplot.free.ALL)
                    NOALL = pymcnp.inp.data.mplot.free.Noall.from_mcnp(string.inp.data.mplot.free.NOALL)

                class contour:
                    PCT = pymcnp.inp.data.mplot.contour.Pct.from_mcnp(string.inp.data.mplot.contour.PCT)
                    LIN = pymcnp.inp.data.mplot.contour.Lin.from_mcnp(string.inp.data.mplot.contour.LIN)
                    LOG = pymcnp.inp.data.mplot.contour.Log.from_mcnp(string.inp.data.mplot.contour.LOG)
                    ALL = pymcnp.inp.data.mplot.contour.All.from_mcnp(string.inp.data.mplot.contour.ALL)
                    NOALL = pymcnp.inp.data.mplot.contour.Noall.from_mcnp(string.inp.data.mplot.contour.NOALL)
                    LINE = pymcnp.inp.data.mplot.contour.Line.from_mcnp(string.inp.data.mplot.contour.LINE)
                    NOLINE = pymcnp.inp.data.mplot.contour.Noline.from_mcnp(string.inp.data.mplot.contour.NOLINE)
                    COLOR = pymcnp.inp.data.mplot.contour.Color.from_mcnp(string.inp.data.mplot.contour.COLOR)
                    NOCOLOR = pymcnp.inp.data.mplot.contour.Nocolor.from_mcnp(string.inp.data.mplot.contour.NOCOLOR)

            class rand:
                GEN = pymcnp.inp.data.rand.Gen.from_mcnp(string.inp.data.rand.GEN)
                SEED = pymcnp.inp.data.rand.Seed.from_mcnp(string.inp.data.rand.SEED)
                STRIDE = pymcnp.inp.data.rand.Stride.from_mcnp(string.inp.data.rand.STRIDE)
                HIST = pymcnp.inp.data.rand.Hist.from_mcnp(string.inp.data.rand.HIST)

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
        HISTORY = pymcnp.ptrac.History.from_mcnp(string.ptrac.HISTORY, HEADER)

        class header:
            V = pymcnp.ptrac.header.V.from_mcnp(string.ptrac.header.V)
            N = pymcnp.ptrac.header.N.from_mcnp(string.ptrac.header.N)
            L = pymcnp.ptrac.header.L.from_mcnp(string.ptrac.header.L)

        class history:
            I = pymcnp.ptrac.history.I.from_mcnp(string.ptrac.history.I)
            EVENT = pymcnp.ptrac.history.Event.from_mcnp(string.ptrac.history.EVENT, I.event_type, pymcnp.ptrac.Header.from_mcnp(string.ptrac.HEADER))

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


class builder:
    class type:
        GEOMETRY = pymcnp.types.GeometryBuilder.unbuild(ast.type.GEOMETRY)

    class inp:
        CELL = pymcnp.inp.CellBuilder.unbuild(ast.inp.CELL)
        SURFACE = pymcnp.inp.SurfaceBuilder.unbuild(ast.inp.SURFACE)
        DATA = pymcnp.inp.DataBuilder.unbuild(ast.inp.DATA)
        COMMENT = pymcnp.inp.CommentBuilder.unbuild(ast.inp.COMMENT)

        class cell:
            IMP = pymcnp.inp.cell.ImpBuilder.unbuild(ast.inp.cell.IMP)
            VOL = pymcnp.inp.cell.VolBuilder.unbuild(ast.inp.cell.VOL)
            PWT = pymcnp.inp.cell.PwtBuilder.unbuild(ast.inp.cell.PWT)
            EXT = pymcnp.inp.cell.ExtBuilder.unbuild(ast.inp.cell.EXT)
            FCL = pymcnp.inp.cell.FclBuilder.unbuild(ast.inp.cell.FCL)
            WWN = pymcnp.inp.cell.WwnBuilder.unbuild(ast.inp.cell.WWN)
            DXC = pymcnp.inp.cell.DxcBuilder.unbuild(ast.inp.cell.DXC)
            NONU = pymcnp.inp.cell.NonuBuilder.unbuild(ast.inp.cell.NONU)
            PD = pymcnp.inp.cell.PdBuilder.unbuild(ast.inp.cell.PD)
            U = pymcnp.inp.cell.UBuilder.unbuild(ast.inp.cell.U)
            TRCL_0 = pymcnp.inp.cell.TrclBuilder_0.unbuild(ast.inp.cell.TRCL_0)
            TRCL_1 = pymcnp.inp.cell.TrclBuilder_1.unbuild(ast.inp.cell.TRCL_1)
            TRCL_2 = pymcnp.inp.cell.TrclBuilder_2.unbuild(ast.inp.cell.TRCL_2)
            TRCL_3 = pymcnp.inp.cell.TrclBuilder_3.unbuild(ast.inp.cell.TRCL_3)
            TRCL_4 = pymcnp.inp.cell.TrclBuilder_4.unbuild(ast.inp.cell.TRCL_4)
            TRCL_5 = pymcnp.inp.cell.TrclBuilder_5.unbuild(ast.inp.cell.TRCL_5)
            LAT = pymcnp.inp.cell.LatBuilder.unbuild(ast.inp.cell.LAT)
            FILL_0 = pymcnp.inp.cell.FillBuilder_0.unbuild(ast.inp.cell.FILL_0)
            FILL_1 = pymcnp.inp.cell.FillBuilder_1.unbuild(ast.inp.cell.FILL_1)
            FILL_2 = pymcnp.inp.cell.FillBuilder_2.unbuild(ast.inp.cell.FILL_2)
            FILL_3 = pymcnp.inp.cell.FillBuilder_3.unbuild(ast.inp.cell.FILL_3)
            FILL_4 = pymcnp.inp.cell.FillBuilder_4.unbuild(ast.inp.cell.FILL_4)
            FILL_5 = pymcnp.inp.cell.FillBuilder_5.unbuild(ast.inp.cell.FILL_5)
            FILL_6 = pymcnp.inp.cell.FillBuilder_6.unbuild(ast.inp.cell.FILL_6)
            ELPT = pymcnp.inp.cell.ElptBuilder.unbuild(ast.inp.cell.ELPT)
            TMP = pymcnp.inp.cell.TmpBuilder.unbuild(ast.inp.cell.TMP)
            COSY = pymcnp.inp.cell.CosyBuilder.unbuild(ast.inp.cell.COSY)
            BFLCL = pymcnp.inp.cell.BflclBuilder.unbuild(ast.inp.cell.BFLCL)
            UNC = pymcnp.inp.cell.UncBuilder.unbuild(ast.inp.cell.UNC)

        class surface:
            P_0 = pymcnp.inp.surface.PBuilder_0.unbuild(ast.inp.surface.P_0)
            P_1 = pymcnp.inp.surface.PBuilder_1.unbuild(ast.inp.surface.P_1)
            PX = pymcnp.inp.surface.PxBuilder.unbuild(ast.inp.surface.PX)
            PY = pymcnp.inp.surface.PyBuilder.unbuild(ast.inp.surface.PY)
            PZ = pymcnp.inp.surface.PzBuilder.unbuild(ast.inp.surface.PZ)
            SO = pymcnp.inp.surface.SoBuilder.unbuild(ast.inp.surface.SO)
            S = pymcnp.inp.surface.SBuilder.unbuild(ast.inp.surface.S)
            SX = pymcnp.inp.surface.SxBuilder.unbuild(ast.inp.surface.SX)
            SY = pymcnp.inp.surface.SyBuilder.unbuild(ast.inp.surface.SY)
            SZ = pymcnp.inp.surface.SzBuilder.unbuild(ast.inp.surface.SZ)
            C_X = pymcnp.inp.surface.C_xBuilder.unbuild(ast.inp.surface.C_X)
            C_Y = pymcnp.inp.surface.C_yBuilder.unbuild(ast.inp.surface.C_Y)
            C_Z = pymcnp.inp.surface.C_zBuilder.unbuild(ast.inp.surface.C_Z)
            CX = pymcnp.inp.surface.CxBuilder.unbuild(ast.inp.surface.CX)
            CY = pymcnp.inp.surface.CyBuilder.unbuild(ast.inp.surface.CY)
            CZ = pymcnp.inp.surface.CzBuilder.unbuild(ast.inp.surface.CZ)
            K_X = pymcnp.inp.surface.K_xBuilder.unbuild(ast.inp.surface.K_X)
            K_Y = pymcnp.inp.surface.K_yBuilder.unbuild(ast.inp.surface.K_Y)
            K_Z = pymcnp.inp.surface.K_zBuilder.unbuild(ast.inp.surface.K_Z)
            KX = pymcnp.inp.surface.KxBuilder.unbuild(ast.inp.surface.KX)
            KY = pymcnp.inp.surface.KyBuilder.unbuild(ast.inp.surface.KY)
            KZ = pymcnp.inp.surface.KzBuilder.unbuild(ast.inp.surface.KZ)
            SQ = pymcnp.inp.surface.SqBuilder.unbuild(ast.inp.surface.SQ)
            GQ = pymcnp.inp.surface.GqBuilder.unbuild(ast.inp.surface.GQ)
            TX = pymcnp.inp.surface.TxBuilder.unbuild(ast.inp.surface.TX)
            TY = pymcnp.inp.surface.TyBuilder.unbuild(ast.inp.surface.TY)
            TZ = pymcnp.inp.surface.TzBuilder.unbuild(ast.inp.surface.TZ)
            X = pymcnp.inp.surface.XBuilder.unbuild(ast.inp.surface.X)
            Y = pymcnp.inp.surface.YBuilder.unbuild(ast.inp.surface.Y)
            Z = pymcnp.inp.surface.ZBuilder.unbuild(ast.inp.surface.Z)
            BOX = pymcnp.inp.surface.BoxBuilder.unbuild(ast.inp.surface.BOX)
            RPP = pymcnp.inp.surface.RppBuilder.unbuild(ast.inp.surface.RPP)
            SPH = pymcnp.inp.surface.SphBuilder.unbuild(ast.inp.surface.SPH)
            RCC = pymcnp.inp.surface.RccBuilder.unbuild(ast.inp.surface.RCC)
            RHP = pymcnp.inp.surface.RhpBuilder.unbuild(ast.inp.surface.RHP)
            REC = pymcnp.inp.surface.RecBuilder.unbuild(ast.inp.surface.REC)
            TRC = pymcnp.inp.surface.TrcBuilder.unbuild(ast.inp.surface.TRC)
            ELL = pymcnp.inp.surface.EllBuilder.unbuild(ast.inp.surface.ELL)
            WED = pymcnp.inp.surface.WedBuilder.unbuild(ast.inp.surface.WED)
            ARB = pymcnp.inp.surface.ArbBuilder.unbuild(ast.inp.surface.ARB)

        class data:
            VOL = pymcnp.inp.data.VolBuilder.unbuild(ast.inp.data.VOL)
            AREA = pymcnp.inp.data.AreaBuilder.unbuild(ast.inp.data.AREA)
            TR_0 = pymcnp.inp.data.TrBuilder_0.unbuild(ast.inp.data.TR_0)
            TR_1 = pymcnp.inp.data.TrBuilder_1.unbuild(ast.inp.data.TR_1)
            TR_2 = pymcnp.inp.data.TrBuilder_2.unbuild(ast.inp.data.TR_2)
            TR_3 = pymcnp.inp.data.TrBuilder_3.unbuild(ast.inp.data.TR_3)
            TR_4 = pymcnp.inp.data.TrBuilder_4.unbuild(ast.inp.data.TR_4)
            U = pymcnp.inp.data.UBuilder.unbuild(ast.inp.data.U)
            LAT = pymcnp.inp.data.LatBuilder.unbuild(ast.inp.data.LAT)
            FILL = pymcnp.inp.data.FillBuilder.unbuild(ast.inp.data.FILL)
            URAN = pymcnp.inp.data.UranBuilder.unbuild(ast.inp.data.URAN)
            DM = pymcnp.inp.data.DmBuilder.unbuild(ast.inp.data.DM)
            DAWWG = pymcnp.inp.data.DawwgBuilder.unbuild(ast.inp.data.DAWWG)
            EMBED = pymcnp.inp.data.EmbedBuilder.unbuild(ast.inp.data.EMBED)
            EMBEE = pymcnp.inp.data.EmbeeBuilder.unbuild(ast.inp.data.EMBEE)
            EMBEB = pymcnp.inp.data.EmbebBuilder.unbuild(ast.inp.data.EMBEB)
            EMBEM = pymcnp.inp.data.EmbemBuilder.unbuild(ast.inp.data.EMBEM)
            EMBTB = pymcnp.inp.data.EmbtbBuilder.unbuild(ast.inp.data.EMBTB)
            EMBTM = pymcnp.inp.data.EmbtmBuilder.unbuild(ast.inp.data.EMBTM)
            EMBDB = pymcnp.inp.data.EmbdbBuilder.unbuild(ast.inp.data.EMBDB)
            EMBDF = pymcnp.inp.data.EmbdfBuilder.unbuild(ast.inp.data.EMBDF)
            M_0 = pymcnp.inp.data.MBuilder_0.unbuild(ast.inp.data.M_0)
            M_1 = pymcnp.inp.data.MBuilder_1.unbuild(ast.inp.data.M_1)
            MT = pymcnp.inp.data.MtBuilder.unbuild(ast.inp.data.MT)
            MX = pymcnp.inp.data.MxBuilder.unbuild(ast.inp.data.MX)
            OTFDB = pymcnp.inp.data.OtfdbBuilder.unbuild(ast.inp.data.OTFDB)
            TOTNU = pymcnp.inp.data.TotnuBuilder.unbuild(ast.inp.data.TOTNU)
            NONU = pymcnp.inp.data.NonuBuilder.unbuild(ast.inp.data.NONU)
            AWTAB = pymcnp.inp.data.AwtabBuilder.unbuild(ast.inp.data.AWTAB)
            XS = pymcnp.inp.data.XsBuilder.unbuild(ast.inp.data.XS)
            VOID = pymcnp.inp.data.VoidBuilder.unbuild(ast.inp.data.VOID)
            MGOPT = pymcnp.inp.data.MgoptBuilder.unbuild(ast.inp.data.MGOPT)
            DRXS = pymcnp.inp.data.DrxsBuilder.unbuild(ast.inp.data.DRXS)
            MODE = pymcnp.inp.data.ModeBuilder.unbuild(ast.inp.data.MODE)
            PHYS_0 = pymcnp.inp.data.PhysBuilder_0.unbuild(ast.inp.data.PHYS_0)
            PHYS_1 = pymcnp.inp.data.PhysBuilder_1.unbuild(ast.inp.data.PHYS_1)
            PHYS_2 = pymcnp.inp.data.PhysBuilder_2.unbuild(ast.inp.data.PHYS_2)
            PHYS_3 = pymcnp.inp.data.PhysBuilder_3.unbuild(ast.inp.data.PHYS_3)
            PHYS_4 = pymcnp.inp.data.PhysBuilder_4.unbuild(ast.inp.data.PHYS_4)
            ACT = pymcnp.inp.data.ActBuilder.unbuild(ast.inp.data.ACT)
            CUT = pymcnp.inp.data.CutBuilder.unbuild(ast.inp.data.CUT)
            ELPT = pymcnp.inp.data.ElptBuilder.unbuild(ast.inp.data.ELPT)
            TMP = pymcnp.inp.data.TmpBuilder.unbuild(ast.inp.data.TMP)
            THTME = pymcnp.inp.data.ThtmeBuilder.unbuild(ast.inp.data.THTME)
            MPHYS = pymcnp.inp.data.MphysBuilder.unbuild(ast.inp.data.MPHYS)
            LCA = pymcnp.inp.data.LcaBuilder.unbuild(ast.inp.data.LCA)
            LCB = pymcnp.inp.data.LcbBuilder.unbuild(ast.inp.data.LCB)
            LCC = pymcnp.inp.data.LccBuilder.unbuild(ast.inp.data.LCC)
            LEA = pymcnp.inp.data.LeaBuilder.unbuild(ast.inp.data.LEA)
            LEB = pymcnp.inp.data.LebBuilder.unbuild(ast.inp.data.LEB)
            FMULT = pymcnp.inp.data.FmultBuilder.unbuild(ast.inp.data.FMULT)
            TROPT = pymcnp.inp.data.TroptBuilder.unbuild(ast.inp.data.TROPT)
            UNC = pymcnp.inp.data.UncBuilder.unbuild(ast.inp.data.UNC)
            COSYP = pymcnp.inp.data.CosypBuilder.unbuild(ast.inp.data.COSYP)
            COSY = pymcnp.inp.data.CosyBuilder.unbuild(ast.inp.data.COSY)
            BFLD = pymcnp.inp.data.BfldBuilder.unbuild(ast.inp.data.BFLD)
            BFLCL = pymcnp.inp.data.BflclBuilder.unbuild(ast.inp.data.BFLCL)
            SDEF = pymcnp.inp.data.SdefBuilder.unbuild(ast.inp.data.SDEF)
            SI_0 = pymcnp.inp.data.SiBuilder_0.unbuild(ast.inp.data.SI_0)
            SI_1 = pymcnp.inp.data.SiBuilder_1.unbuild(ast.inp.data.SI_1)
            SI_2 = pymcnp.inp.data.SiBuilder_2.unbuild(ast.inp.data.SI_2)
            SP_0 = pymcnp.inp.data.SpBuilder_0.unbuild(ast.inp.data.SP_0)
            SP_1 = pymcnp.inp.data.SpBuilder_1.unbuild(ast.inp.data.SP_1)
            SB_0 = pymcnp.inp.data.SbBuilder_0.unbuild(ast.inp.data.SB_0)
            SB_1 = pymcnp.inp.data.SbBuilder_1.unbuild(ast.inp.data.SB_1)
            DS_0 = pymcnp.inp.data.DsBuilder_0.unbuild(ast.inp.data.DS_0)
            DS_1 = pymcnp.inp.data.DsBuilder_1.unbuild(ast.inp.data.DS_1)
            DS_2 = pymcnp.inp.data.DsBuilder_2.unbuild(ast.inp.data.DS_2)
            SC = pymcnp.inp.data.ScBuilder.unbuild(ast.inp.data.SC)
            SSW = pymcnp.inp.data.SswBuilder.unbuild(ast.inp.data.SSW)
            SSR = pymcnp.inp.data.SsrBuilder.unbuild(ast.inp.data.SSR)
            KCODE = pymcnp.inp.data.KcodeBuilder.unbuild(ast.inp.data.KCODE)
            KSRC = pymcnp.inp.data.KsrcBuilder.unbuild(ast.inp.data.KSRC)
            KOPTS = pymcnp.inp.data.KoptsBuilder.unbuild(ast.inp.data.KOPTS)
            HSRC = pymcnp.inp.data.HsrcBuilder.unbuild(ast.inp.data.HSRC)
            F_0 = pymcnp.inp.data.FBuilder_0.unbuild(ast.inp.data.F_0)
            F_1 = pymcnp.inp.data.FBuilder_1.unbuild(ast.inp.data.F_1)
            F_2 = pymcnp.inp.data.FBuilder_2.unbuild(ast.inp.data.F_2)
            FIP = pymcnp.inp.data.FipBuilder.unbuild(ast.inp.data.FIP)
            FIR = pymcnp.inp.data.FirBuilder.unbuild(ast.inp.data.FIR)
            FIC = pymcnp.inp.data.FicBuilder.unbuild(ast.inp.data.FIC)
            F_3 = pymcnp.inp.data.FBuilder_3.unbuild(ast.inp.data.F_3)
            FC = pymcnp.inp.data.FcBuilder.unbuild(ast.inp.data.FC)
            E = pymcnp.inp.data.EBuilder.unbuild(ast.inp.data.E)
            T_0 = pymcnp.inp.data.TBuilder_0.unbuild(ast.inp.data.T_0)
            T_1 = pymcnp.inp.data.TBuilder_1.unbuild(ast.inp.data.T_1)
            C = pymcnp.inp.data.CBuilder.unbuild(ast.inp.data.C)
            FQ = pymcnp.inp.data.FqBuilder.unbuild(ast.inp.data.FQ)
            FM = pymcnp.inp.data.FmBuilder.unbuild(ast.inp.data.FM)
            DE = pymcnp.inp.data.DeBuilder.unbuild(ast.inp.data.DE)
            DF_0 = pymcnp.inp.data.DfBuilder_0.unbuild(ast.inp.data.DF_0)
            DF_1 = pymcnp.inp.data.DfBuilder_1.unbuild(ast.inp.data.DF_1)
            EM = pymcnp.inp.data.EmBuilder.unbuild(ast.inp.data.EM)
            TM = pymcnp.inp.data.TmBuilder.unbuild(ast.inp.data.TM)
            CM = pymcnp.inp.data.CmBuilder.unbuild(ast.inp.data.CM)
            CF = pymcnp.inp.data.CfBuilder.unbuild(ast.inp.data.CF)
            SF = pymcnp.inp.data.SfBuilder.unbuild(ast.inp.data.SF)
            FS = pymcnp.inp.data.FsBuilder.unbuild(ast.inp.data.FS)
            SD = pymcnp.inp.data.SdBuilder.unbuild(ast.inp.data.SD)
            FU = pymcnp.inp.data.FuBuilder.unbuild(ast.inp.data.FU)
            FT = pymcnp.inp.data.FtBuilder.unbuild(ast.inp.data.FT)
            TF_0 = pymcnp.inp.data.TfBuilder_0.unbuild(ast.inp.data.TF_0)
            TF_1 = pymcnp.inp.data.TfBuilder_1.unbuild(ast.inp.data.TF_1)
            NOTRN = pymcnp.inp.data.NotrnBuilder.unbuild(ast.inp.data.NOTRN)
            PERT = pymcnp.inp.data.PertBuilder.unbuild(ast.inp.data.PERT)
            KPERT = pymcnp.inp.data.KpertBuilder.unbuild(ast.inp.data.KPERT)
            KSEN = pymcnp.inp.data.KsenBuilder.unbuild(ast.inp.data.KSEN)
            FMESH = pymcnp.inp.data.FmeshBuilder.unbuild(ast.inp.data.FMESH)
            SPDTL = pymcnp.inp.data.SpdtlBuilder.unbuild(ast.inp.data.SPDTL)
            IMP = pymcnp.inp.data.ImpBuilder.unbuild(ast.inp.data.IMP)
            VAR = pymcnp.inp.data.VarBuilder.unbuild(ast.inp.data.VAR)
            WWE = pymcnp.inp.data.WweBuilder.unbuild(ast.inp.data.WWE)
            WWT = pymcnp.inp.data.WwtBuilder.unbuild(ast.inp.data.WWT)
            WWN = pymcnp.inp.data.WwnBuilder.unbuild(ast.inp.data.WWN)
            WWP = pymcnp.inp.data.WwpBuilder.unbuild(ast.inp.data.WWP)
            WWG = pymcnp.inp.data.WwgBuilder.unbuild(ast.inp.data.WWG)
            WWGE = pymcnp.inp.data.WwgeBuilder.unbuild(ast.inp.data.WWGE)
            WWGT = pymcnp.inp.data.WwgtBuilder.unbuild(ast.inp.data.WWGT)
            MESH = pymcnp.inp.data.MeshBuilder.unbuild(ast.inp.data.MESH)
            ESPLT = pymcnp.inp.data.EspltBuilder.unbuild(ast.inp.data.ESPLT)
            TSPLT = pymcnp.inp.data.TspltBuilder.unbuild(ast.inp.data.TSPLT)
            EXT = pymcnp.inp.data.ExtBuilder.unbuild(ast.inp.data.EXT)
            FCL = pymcnp.inp.data.FclBuilder.unbuild(ast.inp.data.FCL)
            DXT = pymcnp.inp.data.DxtBuilder.unbuild(ast.inp.data.DXT)
            DD = pymcnp.inp.data.DdBuilder.unbuild(ast.inp.data.DD)
            PD = pymcnp.inp.data.PdBuilder.unbuild(ast.inp.data.PD)
            DXC = pymcnp.inp.data.DxcBuilder.unbuild(ast.inp.data.DXC)
            BBREM = pymcnp.inp.data.BbremBuilder.unbuild(ast.inp.data.BBREM)
            PIKMT = pymcnp.inp.data.PikmtBuilder.unbuild(ast.inp.data.PIKMT)
            PWT = pymcnp.inp.data.PwtBuilder.unbuild(ast.inp.data.PWT)
            NPS = pymcnp.inp.data.NpsBuilder.unbuild(ast.inp.data.NPS)
            CTME = pymcnp.inp.data.CtmeBuilder.unbuild(ast.inp.data.CTME)
            STOP = pymcnp.inp.data.StopBuilder.unbuild(ast.inp.data.STOP)
            PRINT = pymcnp.inp.data.PrintBuilder.unbuild(ast.inp.data.PRINT)
            TALNP = pymcnp.inp.data.TalnpBuilder.unbuild(ast.inp.data.TALNP)
            PRDMP = pymcnp.inp.data.PrdmpBuilder.unbuild(ast.inp.data.PRDMP)
            PTRAC = pymcnp.inp.data.PtracBuilder.unbuild(ast.inp.data.PTRAC)
            MPLOT = pymcnp.inp.data.MplotBuilder.unbuild(ast.inp.data.MPLOT)
            HISTP = pymcnp.inp.data.HistpBuilder.unbuild(ast.inp.data.HISTP)
            RAND = pymcnp.inp.data.RandBuilder.unbuild(ast.inp.data.RAND)
            DBCN = pymcnp.inp.data.DbcnBuilder.unbuild(ast.inp.data.DBCN)
            LOST = pymcnp.inp.data.LostBuilder.unbuild(ast.inp.data.LOST)
            IDUM = pymcnp.inp.data.IdumBuilder.unbuild(ast.inp.data.IDUM)
            RDUM = pymcnp.inp.data.RdumBuilder.unbuild(ast.inp.data.RDUM)
            ZA = pymcnp.inp.data.ZaBuilder.unbuild(ast.inp.data.ZA)
            ZB = pymcnp.inp.data.ZbBuilder.unbuild(ast.inp.data.ZB)
            ZC = pymcnp.inp.data.ZcBuilder.unbuild(ast.inp.data.ZC)
            ZD = pymcnp.inp.data.ZdBuilder.unbuild(ast.inp.data.ZD)
            FILES = pymcnp.inp.data.FilesBuilder.unbuild(ast.inp.data.FILES)

            class dawwg:
                POINTS = pymcnp.inp.data.dawwg.PointsBuilder.unbuild(ast.inp.data.dawwg.POINTS)
                XSEC = pymcnp.inp.data.dawwg.XsecBuilder.unbuild(ast.inp.data.dawwg.XSEC)
                BLOCK = pymcnp.inp.data.dawwg.BlockBuilder.unbuild(ast.inp.data.dawwg.BLOCK)

                class block:
                    NGROUP = pymcnp.inp.data.dawwg.block.NgroupBuilder.unbuild(ast.inp.data.dawwg.block.NGROUP)
                    ISN = pymcnp.inp.data.dawwg.block.IsnBuilder.unbuild(ast.inp.data.dawwg.block.ISN)
                    NISO = pymcnp.inp.data.dawwg.block.NisoBuilder.unbuild(ast.inp.data.dawwg.block.NISO)
                    MT = pymcnp.inp.data.dawwg.block.MtBuilder.unbuild(ast.inp.data.dawwg.block.MT)
                    IQUAD = pymcnp.inp.data.dawwg.block.IquadBuilder.unbuild(ast.inp.data.dawwg.block.IQUAD)
                    FMMIX = pymcnp.inp.data.dawwg.block.FmmixBuilder.unbuild(ast.inp.data.dawwg.block.FMMIX)
                    NOSOLV = pymcnp.inp.data.dawwg.block.NosolvBuilder.unbuild(ast.inp.data.dawwg.block.NOSOLV)
                    NOEDIT = pymcnp.inp.data.dawwg.block.NoeditBuilder.unbuild(ast.inp.data.dawwg.block.NOEDIT)
                    NOGEOD = pymcnp.inp.data.dawwg.block.NogeodBuilder.unbuild(ast.inp.data.dawwg.block.NOGEOD)
                    NOMIX = pymcnp.inp.data.dawwg.block.NomixBuilder.unbuild(ast.inp.data.dawwg.block.NOMIX)
                    NOASG = pymcnp.inp.data.dawwg.block.NoasgBuilder.unbuild(ast.inp.data.dawwg.block.NOASG)
                    NOMACR = pymcnp.inp.data.dawwg.block.NomacrBuilder.unbuild(ast.inp.data.dawwg.block.NOMACR)
                    NOSLNP = pymcnp.inp.data.dawwg.block.NoslnpBuilder.unbuild(ast.inp.data.dawwg.block.NOSLNP)
                    NOEDTT = pymcnp.inp.data.dawwg.block.NoedttBuilder.unbuild(ast.inp.data.dawwg.block.NOEDTT)
                    NOADJM = pymcnp.inp.data.dawwg.block.NoadjmBuilder.unbuild(ast.inp.data.dawwg.block.NOADJM)
                    LIB = pymcnp.inp.data.dawwg.block.LibBuilder.unbuild(ast.inp.data.dawwg.block.LIB)
                    LIBNAME = pymcnp.inp.data.dawwg.block.LibnameBuilder.unbuild(ast.inp.data.dawwg.block.LIBNAME)
                    FISSNEUT = pymcnp.inp.data.dawwg.block.FissneutBuilder.unbuild(ast.inp.data.dawwg.block.FISSNEUT)
                    LNG = pymcnp.inp.data.dawwg.block.LngBuilder.unbuild(ast.inp.data.dawwg.block.LNG)
                    BALXS = pymcnp.inp.data.dawwg.block.BalxsBuilder.unbuild(ast.inp.data.dawwg.block.BALXS)
                    NTICHI = pymcnp.inp.data.dawwg.block.NtichiBuilder.unbuild(ast.inp.data.dawwg.block.NTICHI)
                    IEVT = pymcnp.inp.data.dawwg.block.IevtBuilder.unbuild(ast.inp.data.dawwg.block.IEVT)
                    ISCT = pymcnp.inp.data.dawwg.block.IsctBuilder.unbuild(ast.inp.data.dawwg.block.ISCT)
                    ITH = pymcnp.inp.data.dawwg.block.IthBuilder.unbuild(ast.inp.data.dawwg.block.ITH)
                    TRCOR = pymcnp.inp.data.dawwg.block.TrcorBuilder.unbuild(ast.inp.data.dawwg.block.TRCOR)
                    IBL = pymcnp.inp.data.dawwg.block.IblBuilder.unbuild(ast.inp.data.dawwg.block.IBL)
                    IBR = pymcnp.inp.data.dawwg.block.IbrBuilder.unbuild(ast.inp.data.dawwg.block.IBR)
                    IBT = pymcnp.inp.data.dawwg.block.IbtBuilder.unbuild(ast.inp.data.dawwg.block.IBT)
                    IBB = pymcnp.inp.data.dawwg.block.IbbBuilder.unbuild(ast.inp.data.dawwg.block.IBB)
                    IBFRNT = pymcnp.inp.data.dawwg.block.IbfrntBuilder.unbuild(ast.inp.data.dawwg.block.IBFRNT)
                    IBBACK = pymcnp.inp.data.dawwg.block.IbbackBuilder.unbuild(ast.inp.data.dawwg.block.IBBACK)
                    EPSI = pymcnp.inp.data.dawwg.block.EpsiBuilder.unbuild(ast.inp.data.dawwg.block.EPSI)
                    OITM = pymcnp.inp.data.dawwg.block.OitmBuilder.unbuild(ast.inp.data.dawwg.block.OITM)
                    NOSIGF = pymcnp.inp.data.dawwg.block.NosigfBuilder.unbuild(ast.inp.data.dawwg.block.NOSIGF)
                    SRCACC = pymcnp.inp.data.dawwg.block.SrcaccBuilder.unbuild(ast.inp.data.dawwg.block.SRCACC)
                    DIFFSOL = pymcnp.inp.data.dawwg.block.DiffsolBuilder.unbuild(ast.inp.data.dawwg.block.DIFFSOL)
                    TSASN = pymcnp.inp.data.dawwg.block.TsasnBuilder.unbuild(ast.inp.data.dawwg.block.TSASN)
                    TSAEPSI = pymcnp.inp.data.dawwg.block.TsaepsiBuilder.unbuild(ast.inp.data.dawwg.block.TSAEPSI)
                    TSAITS = pymcnp.inp.data.dawwg.block.TsaitsBuilder.unbuild(ast.inp.data.dawwg.block.TSAITS)
                    TSABETA = pymcnp.inp.data.dawwg.block.TsabetaBuilder.unbuild(ast.inp.data.dawwg.block.TSABETA)
                    PTCONV = pymcnp.inp.data.dawwg.block.PtconvBuilder.unbuild(ast.inp.data.dawwg.block.PTCONV)
                    NORM = pymcnp.inp.data.dawwg.block.NormBuilder.unbuild(ast.inp.data.dawwg.block.NORM)
                    XSECTP = pymcnp.inp.data.dawwg.block.XsectpBuilder.unbuild(ast.inp.data.dawwg.block.XSECTP)
                    FISSRP = pymcnp.inp.data.dawwg.block.FissrpBuilder.unbuild(ast.inp.data.dawwg.block.FISSRP)
                    SOURCP = pymcnp.inp.data.dawwg.block.SourcpBuilder.unbuild(ast.inp.data.dawwg.block.SOURCP)
                    ANGP = pymcnp.inp.data.dawwg.block.AngpBuilder.unbuild(ast.inp.data.dawwg.block.ANGP)
                    BALP = pymcnp.inp.data.dawwg.block.BalpBuilder.unbuild(ast.inp.data.dawwg.block.BALP)
                    RAFLUX = pymcnp.inp.data.dawwg.block.RafluxBuilder.unbuild(ast.inp.data.dawwg.block.RAFLUX)
                    RMFLUX = pymcnp.inp.data.dawwg.block.RmfluxBuilder.unbuild(ast.inp.data.dawwg.block.RMFLUX)
                    AVATAR = pymcnp.inp.data.dawwg.block.AvatarBuilder.unbuild(ast.inp.data.dawwg.block.AVATAR)
                    ASLEFT = pymcnp.inp.data.dawwg.block.AsleftBuilder.unbuild(ast.inp.data.dawwg.block.ASLEFT)
                    ASRITE = pymcnp.inp.data.dawwg.block.AsriteBuilder.unbuild(ast.inp.data.dawwg.block.ASRITE)
                    ASBOTT = pymcnp.inp.data.dawwg.block.AsbottBuilder.unbuild(ast.inp.data.dawwg.block.ASBOTT)
                    ASTOP = pymcnp.inp.data.dawwg.block.AstopBuilder.unbuild(ast.inp.data.dawwg.block.ASTOP)
                    ASFRNT = pymcnp.inp.data.dawwg.block.AsfrntBuilder.unbuild(ast.inp.data.dawwg.block.ASFRNT)
                    ASBACK = pymcnp.inp.data.dawwg.block.AsbackBuilder.unbuild(ast.inp.data.dawwg.block.ASBACK)
                    MASSED = pymcnp.inp.data.dawwg.block.MassedBuilder.unbuild(ast.inp.data.dawwg.block.MASSED)
                    PTED = pymcnp.inp.data.dawwg.block.PtedBuilder.unbuild(ast.inp.data.dawwg.block.PTED)
                    ZNED = pymcnp.inp.data.dawwg.block.ZnedBuilder.unbuild(ast.inp.data.dawwg.block.ZNED)
                    RZFLUX = pymcnp.inp.data.dawwg.block.RzfluxBuilder.unbuild(ast.inp.data.dawwg.block.RZFLUX)
                    RZMFLUX = pymcnp.inp.data.dawwg.block.RzmfluxBuilder.unbuild(ast.inp.data.dawwg.block.RZMFLUX)
                    EDOUTF = pymcnp.inp.data.dawwg.block.EdoutfBuilder.unbuild(ast.inp.data.dawwg.block.EDOUTF)
                    BYVOLP = pymcnp.inp.data.dawwg.block.ByvolpBuilder.unbuild(ast.inp.data.dawwg.block.BYVOLP)
                    AJED = pymcnp.inp.data.dawwg.block.AjedBuilder.unbuild(ast.inp.data.dawwg.block.AJED)
                    FLUXONE = pymcnp.inp.data.dawwg.block.FluxoneBuilder.unbuild(ast.inp.data.dawwg.block.FLUXONE)

            class embed:
                BACKGROUND = pymcnp.inp.data.embed.BackgroundBuilder.unbuild(ast.inp.data.embed.BACKGROUND)
                MATCELL = pymcnp.inp.data.embed.MatcellBuilder.unbuild(ast.inp.data.embed.MATCELL)
                MESHGEO = pymcnp.inp.data.embed.MeshgeoBuilder.unbuild(ast.inp.data.embed.MESHGEO)
                MGEOIN = pymcnp.inp.data.embed.MgeoinBuilder.unbuild(ast.inp.data.embed.MGEOIN)
                MEEOUT = pymcnp.inp.data.embed.MeeoutBuilder.unbuild(ast.inp.data.embed.MEEOUT)
                MEEIN = pymcnp.inp.data.embed.MeeinBuilder.unbuild(ast.inp.data.embed.MEEIN)
                CALCVOLS = pymcnp.inp.data.embed.CalcvolsBuilder.unbuild(ast.inp.data.embed.CALCVOLS)
                DEBUG = pymcnp.inp.data.embed.DebugBuilder.unbuild(ast.inp.data.embed.DEBUG)
                FILETYPE = pymcnp.inp.data.embed.FiletypeBuilder.unbuild(ast.inp.data.embed.FILETYPE)
                GMVFILE = pymcnp.inp.data.embed.GmvfileBuilder.unbuild(ast.inp.data.embed.GMVFILE)
                LENGTH = pymcnp.inp.data.embed.LengthBuilder.unbuild(ast.inp.data.embed.LENGTH)
                MCNPUMFILE = pymcnp.inp.data.embed.McnpumfileBuilder.unbuild(ast.inp.data.embed.MCNPUMFILE)

            class embee:
                EMBED = pymcnp.inp.data.embee.EmbedBuilder.unbuild(ast.inp.data.embee.EMBED)
                ENERGY = pymcnp.inp.data.embee.EnergyBuilder.unbuild(ast.inp.data.embee.ENERGY)
                TIME = pymcnp.inp.data.embee.TimeBuilder.unbuild(ast.inp.data.embee.TIME)
                ATOM = pymcnp.inp.data.embee.AtomBuilder.unbuild(ast.inp.data.embee.ATOM)
                FACTOR = pymcnp.inp.data.embee.FactorBuilder.unbuild(ast.inp.data.embee.FACTOR)
                LIST = pymcnp.inp.data.embee.ListBuilder.unbuild(ast.inp.data.embee.LIST)
                MAT = pymcnp.inp.data.embee.MatBuilder.unbuild(ast.inp.data.embee.MAT)
                MTYPE = pymcnp.inp.data.embee.MtypeBuilder.unbuild(ast.inp.data.embee.MTYPE)

            class m_0:
                GAS = pymcnp.inp.data.m_0.GasBuilder.unbuild(ast.inp.data.m_0.GAS)
                ESTEP = pymcnp.inp.data.m_0.EstepBuilder.unbuild(ast.inp.data.m_0.ESTEP)
                HSTEP = pymcnp.inp.data.m_0.HstepBuilder.unbuild(ast.inp.data.m_0.HSTEP)
                NLIB = pymcnp.inp.data.m_0.NlibBuilder.unbuild(ast.inp.data.m_0.NLIB)
                PLIB = pymcnp.inp.data.m_0.PlibBuilder.unbuild(ast.inp.data.m_0.PLIB)
                PNLIB = pymcnp.inp.data.m_0.PnlibBuilder.unbuild(ast.inp.data.m_0.PNLIB)
                ELIB = pymcnp.inp.data.m_0.ElibBuilder.unbuild(ast.inp.data.m_0.ELIB)
                HLIB = pymcnp.inp.data.m_0.HlibBuilder.unbuild(ast.inp.data.m_0.HLIB)
                ALIB = pymcnp.inp.data.m_0.AlibBuilder.unbuild(ast.inp.data.m_0.ALIB)
                SLIB = pymcnp.inp.data.m_0.SlibBuilder.unbuild(ast.inp.data.m_0.SLIB)
                TLIB = pymcnp.inp.data.m_0.TlibBuilder.unbuild(ast.inp.data.m_0.TLIB)
                DLIB = pymcnp.inp.data.m_0.DlibBuilder.unbuild(ast.inp.data.m_0.DLIB)
                COND = pymcnp.inp.data.m_0.CondBuilder.unbuild(ast.inp.data.m_0.COND)
                REFI = pymcnp.inp.data.m_0.RefiBuilder.unbuild(ast.inp.data.m_0.REFI)
                REFC = pymcnp.inp.data.m_0.RefcBuilder.unbuild(ast.inp.data.m_0.REFC)
                REFS = pymcnp.inp.data.m_0.RefsBuilder.unbuild(ast.inp.data.m_0.REFS)

            class act:
                FISSION = pymcnp.inp.data.act.FissionBuilder.unbuild(ast.inp.data.act.FISSION)
                NONFISS = pymcnp.inp.data.act.NonfissBuilder.unbuild(ast.inp.data.act.NONFISS)
                DN = pymcnp.inp.data.act.DnBuilder.unbuild(ast.inp.data.act.DN)
                DG = pymcnp.inp.data.act.DgBuilder.unbuild(ast.inp.data.act.DG)
                THRESH = pymcnp.inp.data.act.ThreshBuilder.unbuild(ast.inp.data.act.THRESH)
                DNBAIS = pymcnp.inp.data.act.DnbaisBuilder.unbuild(ast.inp.data.act.DNBAIS)
                NAP = pymcnp.inp.data.act.NapBuilder.unbuild(ast.inp.data.act.NAP)
                DNEB = pymcnp.inp.data.act.DnebBuilder.unbuild(ast.inp.data.act.DNEB)
                DGEB = pymcnp.inp.data.act.DgebBuilder.unbuild(ast.inp.data.act.DGEB)
                PECUT = pymcnp.inp.data.act.PecutBuilder.unbuild(ast.inp.data.act.PECUT)
                HLCUT = pymcnp.inp.data.act.HlcutBuilder.unbuild(ast.inp.data.act.HLCUT)
                SAMPLE = pymcnp.inp.data.act.SampleBuilder.unbuild(ast.inp.data.act.SAMPLE)

            class fmult:
                SFNU = pymcnp.inp.data.fmult.SfnuBuilder.unbuild(ast.inp.data.fmult.SFNU)
                WIDTH = pymcnp.inp.data.fmult.WidthBuilder.unbuild(ast.inp.data.fmult.WIDTH)
                SFYIELD = pymcnp.inp.data.fmult.SfyieldBuilder.unbuild(ast.inp.data.fmult.SFYIELD)
                WATT = pymcnp.inp.data.fmult.WattBuilder.unbuild(ast.inp.data.fmult.WATT)
                METHOD = pymcnp.inp.data.fmult.MethodBuilder.unbuild(ast.inp.data.fmult.METHOD)
                DATA = pymcnp.inp.data.fmult.DataBuilder.unbuild(ast.inp.data.fmult.DATA)
                SHIFT = pymcnp.inp.data.fmult.ShiftBuilder.unbuild(ast.inp.data.fmult.SHIFT)

            class tropt:
                MCSCAT = pymcnp.inp.data.tropt.McscatBuilder.unbuild(ast.inp.data.tropt.MCSCAT)
                ELOSS = pymcnp.inp.data.tropt.ElossBuilder.unbuild(ast.inp.data.tropt.ELOSS)
                NREACT = pymcnp.inp.data.tropt.NreactBuilder.unbuild(ast.inp.data.tropt.NREACT)
                NESCAT = pymcnp.inp.data.tropt.NescatBuilder.unbuild(ast.inp.data.tropt.NESCAT)
                GENXS = pymcnp.inp.data.tropt.GenxsBuilder.unbuild(ast.inp.data.tropt.GENXS)

            class bfld:
                FIELD = pymcnp.inp.data.bfld.FieldBuilder.unbuild(ast.inp.data.bfld.FIELD)
                VEC = pymcnp.inp.data.bfld.VecBuilder.unbuild(ast.inp.data.bfld.VEC)
                MAXDEFLC = pymcnp.inp.data.bfld.MaxdeflcBuilder.unbuild(ast.inp.data.bfld.MAXDEFLC)
                MAXSTEP = pymcnp.inp.data.bfld.MaxstepBuilder.unbuild(ast.inp.data.bfld.MAXSTEP)
                AXS = pymcnp.inp.data.bfld.AxsBuilder.unbuild(ast.inp.data.bfld.AXS)
                FFEDGES = pymcnp.inp.data.bfld.FfedgesBuilder.unbuild(ast.inp.data.bfld.FFEDGES)
                REFPNT = pymcnp.inp.data.bfld.RefpntBuilder.unbuild(ast.inp.data.bfld.REFPNT)

            class sdef:
                CEL = pymcnp.inp.data.sdef.CelBuilder.unbuild(ast.inp.data.sdef.CEL)
                SUR = pymcnp.inp.data.sdef.SurBuilder.unbuild(ast.inp.data.sdef.SUR)
                ERG_0 = pymcnp.inp.data.sdef.ErgBuilder_0.unbuild(ast.inp.data.sdef.ERG_0)
                ERG_1 = pymcnp.inp.data.sdef.ErgBuilder_1.unbuild(ast.inp.data.sdef.ERG_1)
                TME_0 = pymcnp.inp.data.sdef.TmeBuilder_0.unbuild(ast.inp.data.sdef.TME_0)
                TME_1 = pymcnp.inp.data.sdef.TmeBuilder_1.unbuild(ast.inp.data.sdef.TME_1)
                DIR_0 = pymcnp.inp.data.sdef.DirBuilder_0.unbuild(ast.inp.data.sdef.DIR_0)
                DIR_1 = pymcnp.inp.data.sdef.DirBuilder_1.unbuild(ast.inp.data.sdef.DIR_1)
                VEC = pymcnp.inp.data.sdef.VecBuilder.unbuild(ast.inp.data.sdef.VEC)
                NRM = pymcnp.inp.data.sdef.NrmBuilder.unbuild(ast.inp.data.sdef.NRM)
                POS = pymcnp.inp.data.sdef.PosBuilder.unbuild(ast.inp.data.sdef.POS)
                RAD_0 = pymcnp.inp.data.sdef.RadBuilder_0.unbuild(ast.inp.data.sdef.RAD_0)
                RAD_1 = pymcnp.inp.data.sdef.RadBuilder_1.unbuild(ast.inp.data.sdef.RAD_1)
                EXT = pymcnp.inp.data.sdef.ExtBuilder.unbuild(ast.inp.data.sdef.EXT)
                AXS = pymcnp.inp.data.sdef.AxsBuilder.unbuild(ast.inp.data.sdef.AXS)
                X = pymcnp.inp.data.sdef.XBuilder.unbuild(ast.inp.data.sdef.X)
                Y = pymcnp.inp.data.sdef.YBuilder.unbuild(ast.inp.data.sdef.Y)
                Z = pymcnp.inp.data.sdef.ZBuilder.unbuild(ast.inp.data.sdef.Z)
                CCC = pymcnp.inp.data.sdef.CccBuilder.unbuild(ast.inp.data.sdef.CCC)
                ARA = pymcnp.inp.data.sdef.AraBuilder.unbuild(ast.inp.data.sdef.ARA)
                WGT = pymcnp.inp.data.sdef.WgtBuilder.unbuild(ast.inp.data.sdef.WGT)
                TR_0 = pymcnp.inp.data.sdef.TrBuilder_0.unbuild(ast.inp.data.sdef.TR_0)
                TR_1 = pymcnp.inp.data.sdef.TrBuilder_1.unbuild(ast.inp.data.sdef.TR_1)
                EFF = pymcnp.inp.data.sdef.EffBuilder.unbuild(ast.inp.data.sdef.EFF)
                PAR = pymcnp.inp.data.sdef.ParBuilder.unbuild(ast.inp.data.sdef.PAR)
                DAT = pymcnp.inp.data.sdef.DatBuilder.unbuild(ast.inp.data.sdef.DAT)
                LOC = pymcnp.inp.data.sdef.LocBuilder.unbuild(ast.inp.data.sdef.LOC)
                BEM = pymcnp.inp.data.sdef.BemBuilder.unbuild(ast.inp.data.sdef.BEM)
                BAP = pymcnp.inp.data.sdef.BapBuilder.unbuild(ast.inp.data.sdef.BAP)

            class ssw:
                SYM = pymcnp.inp.data.ssw.SymBuilder.unbuild(ast.inp.data.ssw.SYM)
                PTY = pymcnp.inp.data.ssw.PtyBuilder.unbuild(ast.inp.data.ssw.PTY)
                CEL = pymcnp.inp.data.ssw.CelBuilder.unbuild(ast.inp.data.ssw.CEL)

            class ssr:
                OLD = pymcnp.inp.data.ssr.OldBuilder.unbuild(ast.inp.data.ssr.OLD)
                CEL = pymcnp.inp.data.ssr.CelBuilder.unbuild(ast.inp.data.ssr.CEL)
                NEW = pymcnp.inp.data.ssr.NewBuilder.unbuild(ast.inp.data.ssr.NEW)
                PTY = pymcnp.inp.data.ssr.PtyBuilder.unbuild(ast.inp.data.ssr.PTY)
                COL = pymcnp.inp.data.ssr.ColBuilder.unbuild(ast.inp.data.ssr.COL)
                WGT = pymcnp.inp.data.ssr.WgtBuilder.unbuild(ast.inp.data.ssr.WGT)
                TR_0 = pymcnp.inp.data.ssr.TrBuilder_0.unbuild(ast.inp.data.ssr.TR_0)
                TR_1 = pymcnp.inp.data.ssr.TrBuilder_1.unbuild(ast.inp.data.ssr.TR_1)
                PSC = pymcnp.inp.data.ssr.PscBuilder.unbuild(ast.inp.data.ssr.PSC)
                AXS = pymcnp.inp.data.ssr.AxsBuilder.unbuild(ast.inp.data.ssr.AXS)
                EXT = pymcnp.inp.data.ssr.ExtBuilder.unbuild(ast.inp.data.ssr.EXT)
                POA = pymcnp.inp.data.ssr.PoaBuilder.unbuild(ast.inp.data.ssr.POA)
                BCW = pymcnp.inp.data.ssr.BcwBuilder.unbuild(ast.inp.data.ssr.BCW)

            class kopts:
                BLOCKSIZE = pymcnp.inp.data.kopts.BlocksizeBuilder.unbuild(ast.inp.data.kopts.BLOCKSIZE)
                KINETICS = pymcnp.inp.data.kopts.KineticsBuilder.unbuild(ast.inp.data.kopts.KINETICS)
                PRECURSOR = pymcnp.inp.data.kopts.PrecursorBuilder.unbuild(ast.inp.data.kopts.PRECURSOR)
                KSENTAL = pymcnp.inp.data.kopts.KsentalBuilder.unbuild(ast.inp.data.kopts.KSENTAL)
                FMAT = pymcnp.inp.data.kopts.FmatBuilder.unbuild(ast.inp.data.kopts.FMAT)
                FMATSKPT = pymcnp.inp.data.kopts.FmatskptBuilder.unbuild(ast.inp.data.kopts.FMATSKPT)
                FMATNCYC = pymcnp.inp.data.kopts.FmatncycBuilder.unbuild(ast.inp.data.kopts.FMATNCYC)
                FMATSPACE = pymcnp.inp.data.kopts.FmatspaceBuilder.unbuild(ast.inp.data.kopts.FMATSPACE)
                FMATACCEL = pymcnp.inp.data.kopts.FmataccelBuilder.unbuild(ast.inp.data.kopts.FMATACCEL)
                FMATREDUCE = pymcnp.inp.data.kopts.FmatreduceBuilder.unbuild(ast.inp.data.kopts.FMATREDUCE)
                FMATNX = pymcnp.inp.data.kopts.FmatnxBuilder.unbuild(ast.inp.data.kopts.FMATNX)
                FMATNY = pymcnp.inp.data.kopts.FmatnyBuilder.unbuild(ast.inp.data.kopts.FMATNY)
                FMATNZ = pymcnp.inp.data.kopts.FmatnzBuilder.unbuild(ast.inp.data.kopts.FMATNZ)

            class t_1:
                CBEG = pymcnp.inp.data.t_1.CbegBuilder.unbuild(ast.inp.data.t_1.CBEG)
                CFRQ = pymcnp.inp.data.t_1.CfrqBuilder.unbuild(ast.inp.data.t_1.CFRQ)
                COFI = pymcnp.inp.data.t_1.CofiBuilder.unbuild(ast.inp.data.t_1.COFI)
                CONI = pymcnp.inp.data.t_1.ConiBuilder.unbuild(ast.inp.data.t_1.CONI)
                CSUB = pymcnp.inp.data.t_1.CsubBuilder.unbuild(ast.inp.data.t_1.CSUB)
                CEND = pymcnp.inp.data.t_1.CendBuilder.unbuild(ast.inp.data.t_1.CEND)

            class df_1:
                IU = pymcnp.inp.data.df_1.IuBuilder.unbuild(ast.inp.data.df_1.IU)
                FAC = pymcnp.inp.data.df_1.FacBuilder.unbuild(ast.inp.data.df_1.FAC)
                IC = pymcnp.inp.data.df_1.IcBuilder.unbuild(ast.inp.data.df_1.IC)
                LOG = pymcnp.inp.data.df_1.LogBuilder.unbuild(ast.inp.data.df_1.LOG)
                LIN = pymcnp.inp.data.df_1.LinBuilder.unbuild(ast.inp.data.df_1.LIN)

            class pert:
                CELL = pymcnp.inp.data.pert.CellBuilder.unbuild(ast.inp.data.pert.CELL)
                MAT = pymcnp.inp.data.pert.MatBuilder.unbuild(ast.inp.data.pert.MAT)
                RHO = pymcnp.inp.data.pert.RhoBuilder.unbuild(ast.inp.data.pert.RHO)
                METHOD = pymcnp.inp.data.pert.MethodBuilder.unbuild(ast.inp.data.pert.METHOD)
                ERG = pymcnp.inp.data.pert.ErgBuilder.unbuild(ast.inp.data.pert.ERG)
                RXN = pymcnp.inp.data.pert.RxnBuilder.unbuild(ast.inp.data.pert.RXN)

            class kpert:
                CELL = pymcnp.inp.data.kpert.CellBuilder.unbuild(ast.inp.data.kpert.CELL)
                MAT = pymcnp.inp.data.kpert.MatBuilder.unbuild(ast.inp.data.kpert.MAT)
                RHO = pymcnp.inp.data.kpert.RhoBuilder.unbuild(ast.inp.data.kpert.RHO)
                ISO = pymcnp.inp.data.kpert.IsoBuilder.unbuild(ast.inp.data.kpert.ISO)
                RXN = pymcnp.inp.data.kpert.RxnBuilder.unbuild(ast.inp.data.kpert.RXN)
                ERG = pymcnp.inp.data.kpert.ErgBuilder.unbuild(ast.inp.data.kpert.ERG)
                LINEAR = pymcnp.inp.data.kpert.LinearBuilder.unbuild(ast.inp.data.kpert.LINEAR)

            class ksen:
                ISO = pymcnp.inp.data.ksen.IsoBuilder.unbuild(ast.inp.data.ksen.ISO)
                RXN = pymcnp.inp.data.ksen.RxnBuilder.unbuild(ast.inp.data.ksen.RXN)
                MT = pymcnp.inp.data.ksen.MtBuilder.unbuild(ast.inp.data.ksen.MT)
                ERG = pymcnp.inp.data.ksen.ErgBuilder.unbuild(ast.inp.data.ksen.ERG)
                EIN = pymcnp.inp.data.ksen.EinBuilder.unbuild(ast.inp.data.ksen.EIN)
                LEGENDRE = pymcnp.inp.data.ksen.LegendreBuilder.unbuild(ast.inp.data.ksen.LEGENDRE)
                COS = pymcnp.inp.data.ksen.CosBuilder.unbuild(ast.inp.data.ksen.COS)
                CONSTRAIN = pymcnp.inp.data.ksen.ConstrainBuilder.unbuild(ast.inp.data.ksen.CONSTRAIN)

            class fmesh:
                GEOM = pymcnp.inp.data.fmesh.GeomBuilder.unbuild(ast.inp.data.fmesh.GEOM)
                ORIGIN = pymcnp.inp.data.fmesh.OriginBuilder.unbuild(ast.inp.data.fmesh.ORIGIN)
                AXS = pymcnp.inp.data.fmesh.AxsBuilder.unbuild(ast.inp.data.fmesh.AXS)
                VEC = pymcnp.inp.data.fmesh.VecBuilder.unbuild(ast.inp.data.fmesh.VEC)
                IMESH = pymcnp.inp.data.fmesh.ImeshBuilder.unbuild(ast.inp.data.fmesh.IMESH)
                IINTS = pymcnp.inp.data.fmesh.IintsBuilder.unbuild(ast.inp.data.fmesh.IINTS)
                JMESH = pymcnp.inp.data.fmesh.JmeshBuilder.unbuild(ast.inp.data.fmesh.JMESH)
                JINTS = pymcnp.inp.data.fmesh.JintsBuilder.unbuild(ast.inp.data.fmesh.JINTS)
                KMESH = pymcnp.inp.data.fmesh.KmeshBuilder.unbuild(ast.inp.data.fmesh.KMESH)
                KINTS = pymcnp.inp.data.fmesh.KintsBuilder.unbuild(ast.inp.data.fmesh.KINTS)
                EMESH = pymcnp.inp.data.fmesh.EmeshBuilder.unbuild(ast.inp.data.fmesh.EMESH)
                EINTS = pymcnp.inp.data.fmesh.EintsBuilder.unbuild(ast.inp.data.fmesh.EINTS)
                ENORM = pymcnp.inp.data.fmesh.EnormBuilder.unbuild(ast.inp.data.fmesh.ENORM)
                TMESH = pymcnp.inp.data.fmesh.TmeshBuilder.unbuild(ast.inp.data.fmesh.TMESH)
                TINTS = pymcnp.inp.data.fmesh.TintsBuilder.unbuild(ast.inp.data.fmesh.TINTS)
                TNORM = pymcnp.inp.data.fmesh.TnormBuilder.unbuild(ast.inp.data.fmesh.TNORM)
                FACTOR = pymcnp.inp.data.fmesh.FactorBuilder.unbuild(ast.inp.data.fmesh.FACTOR)
                OUT = pymcnp.inp.data.fmesh.OutBuilder.unbuild(ast.inp.data.fmesh.OUT)
                TR = pymcnp.inp.data.fmesh.TrBuilder.unbuild(ast.inp.data.fmesh.TR)
                INC = pymcnp.inp.data.fmesh.IncBuilder.unbuild(ast.inp.data.fmesh.INC)
                TYPE = pymcnp.inp.data.fmesh.TypeBuilder.unbuild(ast.inp.data.fmesh.TYPE)
                KCLEAR = pymcnp.inp.data.fmesh.KclearBuilder.unbuild(ast.inp.data.fmesh.KCLEAR)

            class var:
                RR = pymcnp.inp.data.var.RrBuilder.unbuild(ast.inp.data.var.RR)

            class mesh:
                GEOM = pymcnp.inp.data.mesh.GeomBuilder.unbuild(ast.inp.data.mesh.GEOM)
                REF = pymcnp.inp.data.mesh.RefBuilder.unbuild(ast.inp.data.mesh.REF)
                ORIGIN = pymcnp.inp.data.mesh.OriginBuilder.unbuild(ast.inp.data.mesh.ORIGIN)
                AXS = pymcnp.inp.data.mesh.AxsBuilder.unbuild(ast.inp.data.mesh.AXS)
                VEC = pymcnp.inp.data.mesh.VecBuilder.unbuild(ast.inp.data.mesh.VEC)
                IMESH = pymcnp.inp.data.mesh.ImeshBuilder.unbuild(ast.inp.data.mesh.IMESH)
                IINTS = pymcnp.inp.data.mesh.IintsBuilder.unbuild(ast.inp.data.mesh.IINTS)
                JMESH = pymcnp.inp.data.mesh.JmeshBuilder.unbuild(ast.inp.data.mesh.JMESH)
                JINTS = pymcnp.inp.data.mesh.JintsBuilder.unbuild(ast.inp.data.mesh.JINTS)
                KMESH = pymcnp.inp.data.mesh.KmeshBuilder.unbuild(ast.inp.data.mesh.KMESH)
                KINTS = pymcnp.inp.data.mesh.KintsBuilder.unbuild(ast.inp.data.mesh.KINTS)

            class stop:
                NPS = pymcnp.inp.data.stop.NpsBuilder.unbuild(ast.inp.data.stop.NPS)
                CTME = pymcnp.inp.data.stop.CtmeBuilder.unbuild(ast.inp.data.stop.CTME)
                F = pymcnp.inp.data.stop.FBuilder.unbuild(ast.inp.data.stop.F)

            class ptrac:
                BUFFER = pymcnp.inp.data.ptrac.BufferBuilder.unbuild(ast.inp.data.ptrac.BUFFER)
                FILE = pymcnp.inp.data.ptrac.FileBuilder.unbuild(ast.inp.data.ptrac.FILE)
                MAX = pymcnp.inp.data.ptrac.MaxBuilder.unbuild(ast.inp.data.ptrac.MAX)
                MEPH = pymcnp.inp.data.ptrac.MephBuilder.unbuild(ast.inp.data.ptrac.MEPH)
                WRITE = pymcnp.inp.data.ptrac.WriteBuilder.unbuild(ast.inp.data.ptrac.WRITE)
                CONIC = pymcnp.inp.data.ptrac.ConicBuilder.unbuild(ast.inp.data.ptrac.CONIC)
                EVENT = pymcnp.inp.data.ptrac.EventBuilder.unbuild(ast.inp.data.ptrac.EVENT)
                FILTER = pymcnp.inp.data.ptrac.FilterBuilder.unbuild(ast.inp.data.ptrac.FILTER)
                TYPE = pymcnp.inp.data.ptrac.TypeBuilder.unbuild(ast.inp.data.ptrac.TYPE)
                NPS = pymcnp.inp.data.ptrac.NpsBuilder.unbuild(ast.inp.data.ptrac.NPS)
                CELL = pymcnp.inp.data.ptrac.CellBuilder.unbuild(ast.inp.data.ptrac.CELL)
                SURFACE = pymcnp.inp.data.ptrac.SurfaceBuilder.unbuild(ast.inp.data.ptrac.SURFACE)
                TALLY = pymcnp.inp.data.ptrac.TallyBuilder.unbuild(ast.inp.data.ptrac.TALLY)
                VALUE = pymcnp.inp.data.ptrac.ValueBuilder.unbuild(ast.inp.data.ptrac.VALUE)

            class mplot:
                TERM = pymcnp.inp.data.mplot.TermBuilder.unbuild(ast.inp.data.mplot.TERM)
                FILE = pymcnp.inp.data.mplot.FileBuilder.unbuild(ast.inp.data.mplot.FILE)
                COPLOT = pymcnp.inp.data.mplot.CoplotBuilder.unbuild(ast.inp.data.mplot.COPLOT)
                FREQ = pymcnp.inp.data.mplot.FreqBuilder.unbuild(ast.inp.data.mplot.FREQ)
                RETURN = pymcnp.inp.data.mplot.ReturnBuilder.unbuild(ast.inp.data.mplot.RETURN)
                PLOT = pymcnp.inp.data.mplot.PlotBuilder.unbuild(ast.inp.data.mplot.PLOT)
                PAUSE = pymcnp.inp.data.mplot.PauseBuilder.unbuild(ast.inp.data.mplot.PAUSE)
                END = pymcnp.inp.data.mplot.EndBuilder.unbuild(ast.inp.data.mplot.END)
                OPTIONS = pymcnp.inp.data.mplot.OptionsBuilder.unbuild(ast.inp.data.mplot.OPTIONS)
                HELP = pymcnp.inp.data.mplot.HelpBuilder.unbuild(ast.inp.data.mplot.HELP)
                STATUS = pymcnp.inp.data.mplot.StatusBuilder.unbuild(ast.inp.data.mplot.STATUS)
                PRINTAL = pymcnp.inp.data.mplot.PrintalBuilder.unbuild(ast.inp.data.mplot.PRINTAL)
                IPTAL = pymcnp.inp.data.mplot.IptalBuilder.unbuild(ast.inp.data.mplot.IPTAL)
                PRINTPTS = pymcnp.inp.data.mplot.PrintptsBuilder.unbuild(ast.inp.data.mplot.PRINTPTS)
                RUNTPE = pymcnp.inp.data.mplot.RuntpeBuilder.unbuild(ast.inp.data.mplot.RUNTPE)
                DUMP = pymcnp.inp.data.mplot.DumpBuilder.unbuild(ast.inp.data.mplot.DUMP)
                WMCTAL = pymcnp.inp.data.mplot.WmctalBuilder.unbuild(ast.inp.data.mplot.WMCTAL)
                RMCTAL = pymcnp.inp.data.mplot.RmctalBuilder.unbuild(ast.inp.data.mplot.RMCTAL)
                TALLY = pymcnp.inp.data.mplot.TallyBuilder.unbuild(ast.inp.data.mplot.TALLY)
                PERT = pymcnp.inp.data.mplot.PertBuilder.unbuild(ast.inp.data.mplot.PERT)
                LETHARGY = pymcnp.inp.data.mplot.LethargyBuilder.unbuild(ast.inp.data.mplot.LETHARGY)
                NONORM = pymcnp.inp.data.mplot.NonormBuilder.unbuild(ast.inp.data.mplot.NONORM)
                FACTOR = pymcnp.inp.data.mplot.FactorBuilder.unbuild(ast.inp.data.mplot.FACTOR)
                RESET = pymcnp.inp.data.mplot.ResetBuilder.unbuild(ast.inp.data.mplot.RESET)
                TITLE = pymcnp.inp.data.mplot.TitleBuilder.unbuild(ast.inp.data.mplot.TITLE)
                BELOW = pymcnp.inp.data.mplot.BelowBuilder.unbuild(ast.inp.data.mplot.BELOW)
                SUBTITLE = pymcnp.inp.data.mplot.SubtitleBuilder.unbuild(ast.inp.data.mplot.SUBTITLE)
                XTITLE = pymcnp.inp.data.mplot.XtitleBuilder.unbuild(ast.inp.data.mplot.XTITLE)
                YTITLE = pymcnp.inp.data.mplot.YtitleBuilder.unbuild(ast.inp.data.mplot.YTITLE)
                ZTITLE = pymcnp.inp.data.mplot.ZtitleBuilder.unbuild(ast.inp.data.mplot.ZTITLE)
                LABEL = pymcnp.inp.data.mplot.LabelBuilder.unbuild(ast.inp.data.mplot.LABEL)
                FREE = pymcnp.inp.data.mplot.FreeBuilder.unbuild(ast.inp.data.mplot.FREE)
                FIXED = pymcnp.inp.data.mplot.FixedBuilder.unbuild(ast.inp.data.mplot.FIXED)
                SET = pymcnp.inp.data.mplot.SetBuilder.unbuild(ast.inp.data.mplot.SET)
                TFC = pymcnp.inp.data.mplot.TfcBuilder.unbuild(ast.inp.data.mplot.TFC)
                KCODE = pymcnp.inp.data.mplot.KcodeBuilder.unbuild(ast.inp.data.mplot.KCODE)
                XS_0 = pymcnp.inp.data.mplot.XsBuilder_0.unbuild(ast.inp.data.mplot.XS_0)
                XS_1 = pymcnp.inp.data.mplot.XsBuilder_1.unbuild(ast.inp.data.mplot.XS_1)
                XS_2 = pymcnp.inp.data.mplot.XsBuilder_2.unbuild(ast.inp.data.mplot.XS_2)
                MT = pymcnp.inp.data.mplot.MtBuilder.unbuild(ast.inp.data.mplot.MT)
                PAR = pymcnp.inp.data.mplot.ParBuilder.unbuild(ast.inp.data.mplot.PAR)
                LINLIN = pymcnp.inp.data.mplot.LinlinBuilder.unbuild(ast.inp.data.mplot.LINLIN)
                LINLOG = pymcnp.inp.data.mplot.LinlogBuilder.unbuild(ast.inp.data.mplot.LINLOG)
                LOGLIN = pymcnp.inp.data.mplot.LoglinBuilder.unbuild(ast.inp.data.mplot.LOGLIN)
                LOGLOG = pymcnp.inp.data.mplot.LoglogBuilder.unbuild(ast.inp.data.mplot.LOGLOG)
                XLIMS = pymcnp.inp.data.mplot.XlimsBuilder.unbuild(ast.inp.data.mplot.XLIMS)
                YLIMS = pymcnp.inp.data.mplot.YlimsBuilder.unbuild(ast.inp.data.mplot.YLIMS)
                SCALES = pymcnp.inp.data.mplot.ScalesBuilder.unbuild(ast.inp.data.mplot.SCALES)
                HIST = pymcnp.inp.data.mplot.HistBuilder.unbuild(ast.inp.data.mplot.HIST)
                PLINEAR = pymcnp.inp.data.mplot.PlinearBuilder.unbuild(ast.inp.data.mplot.PLINEAR)
                SPLINE = pymcnp.inp.data.mplot.SplineBuilder.unbuild(ast.inp.data.mplot.SPLINE)
                BAR = pymcnp.inp.data.mplot.BarBuilder.unbuild(ast.inp.data.mplot.BAR)
                NOERRBAR = pymcnp.inp.data.mplot.NoerrbarBuilder.unbuild(ast.inp.data.mplot.NOERRBAR)
                THICK = pymcnp.inp.data.mplot.ThickBuilder.unbuild(ast.inp.data.mplot.THICK)
                THIN = pymcnp.inp.data.mplot.ThinBuilder.unbuild(ast.inp.data.mplot.THIN)
                LEGEND = pymcnp.inp.data.mplot.LegendBuilder.unbuild(ast.inp.data.mplot.LEGEND)
                CONTOUR = pymcnp.inp.data.mplot.ContourBuilder.unbuild(ast.inp.data.mplot.CONTOUR)
                WASH = pymcnp.inp.data.mplot.WashBuilder.unbuild(ast.inp.data.mplot.WASH)
                FMESH = pymcnp.inp.data.mplot.FmeshBuilder.unbuild(ast.inp.data.mplot.FMESH)
                FMRELERR = pymcnp.inp.data.mplot.FmrelerrBuilder.unbuild(ast.inp.data.mplot.FMRELERR)
                ZLEV = pymcnp.inp.data.mplot.ZlevBuilder.unbuild(ast.inp.data.mplot.ZLEV)
                EBIN = pymcnp.inp.data.mplot.EbinBuilder.unbuild(ast.inp.data.mplot.EBIN)
                TBIN = pymcnp.inp.data.mplot.TbinBuilder.unbuild(ast.inp.data.mplot.TBIN)
                COP = pymcnp.inp.data.mplot.CopBuilder.unbuild(ast.inp.data.mplot.COP)
                TAL = pymcnp.inp.data.mplot.TalBuilder.unbuild(ast.inp.data.mplot.TAL)

                class free:
                    ALL = pymcnp.inp.data.mplot.free.AllBuilder.unbuild(ast.inp.data.mplot.free.ALL)
                    NOALL = pymcnp.inp.data.mplot.free.NoallBuilder.unbuild(ast.inp.data.mplot.free.NOALL)

                class contour:
                    PCT = pymcnp.inp.data.mplot.contour.PctBuilder.unbuild(ast.inp.data.mplot.contour.PCT)
                    LIN = pymcnp.inp.data.mplot.contour.LinBuilder.unbuild(ast.inp.data.mplot.contour.LIN)
                    LOG = pymcnp.inp.data.mplot.contour.LogBuilder.unbuild(ast.inp.data.mplot.contour.LOG)
                    ALL = pymcnp.inp.data.mplot.contour.AllBuilder.unbuild(ast.inp.data.mplot.contour.ALL)
                    NOALL = pymcnp.inp.data.mplot.contour.NoallBuilder.unbuild(ast.inp.data.mplot.contour.NOALL)
                    LINE = pymcnp.inp.data.mplot.contour.LineBuilder.unbuild(ast.inp.data.mplot.contour.LINE)
                    NOLINE = pymcnp.inp.data.mplot.contour.NolineBuilder.unbuild(ast.inp.data.mplot.contour.NOLINE)
                    COLOR = pymcnp.inp.data.mplot.contour.ColorBuilder.unbuild(ast.inp.data.mplot.contour.COLOR)
                    NOCOLOR = pymcnp.inp.data.mplot.contour.NocolorBuilder.unbuild(ast.inp.data.mplot.contour.NOCOLOR)

            class rand:
                GEN = pymcnp.inp.data.rand.GenBuilder.unbuild(ast.inp.data.rand.GEN)
                SEED = pymcnp.inp.data.rand.SeedBuilder.unbuild(ast.inp.data.rand.SEED)
                STRIDE = pymcnp.inp.data.rand.StrideBuilder.unbuild(ast.inp.data.rand.STRIDE)
                HIST = pymcnp.inp.data.rand.HistBuilder.unbuild(ast.inp.data.rand.HIST)

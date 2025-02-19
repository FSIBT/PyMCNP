import re
import typing

from . import data
from . import _card
from ..utils import errors
from ..utils import _parser


class Data(_card.InpCard_):
    """
    Represents INP data cards.

    Attributes:
        option: INP data option.
    """

    _REGEX = re.compile(
        r'\A(((vol)( \S+?)?(( \S+?)+))|((area)(( \S+?)+))|((tr)(\d+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((u)(( \S+?)+))|((lat)(( \S+?)+))|((fill)(( \S+?)+))|((uran)((( \S+?)( \S+?)( \S+?)( \S+?))+))|((dm)(( \S+?)+))|((dawwg)(( (((points)( \S+?))|((xsec)( \S+?))|((block)( \S+?)(( (((ngroup)( \S+?))|((isn)( \S+?))|((niso)( \S+?))|((mt)( \S+?))|((iquad)( \S+?))|((fmmix)( \S+?))|((nosolv)( \S+?))|((noedit)( \S+?))|((nogeod)( \S+?))|((nomix)( \S+?))|((noasg)( \S+?))|((nomacr)( \S+?))|((noslnp)( \S+?))|((noedtt)( \S+?))|((noadjm)( \S+?))|((lib)( \S+?))|((libname)( \S+?))|((fissneut)( \S+?))|((lng)( \S+?))|((balxs)( \S+?))|((ntichi)( \S+?))|((ievt)( \S+?))|((isct)( \S+?))|((ith)( \S+?))|((trcor)( \S+?))|((ibl)( \S+?))|((ibr)( \S+?))|((ibt)( \S+?))|((ibb)( \S+?))|((ibfrnt)( \S+?))|((ibback)( \S+?))|((epsi)( \S+?))|((oitm)( \S+?))|((nosigf)( \S+?))|((srcacc)( \S+?))|((diffsol)( \S+?))|((tsasn)( \S+?))|((tsaepsi)( \S+?))|((tsaits)( \S+?))|((tsabeta)( \S+?))|((ptconv)( \S+?))|((norm)( \S+?))|((xsectp)( \S+?))|((fissrp)( \S+?))|((sourcp)( \S+?))|((angp)( \S+?))|((balp)( \S+?))|((raflux)( \S+?))|((rmflux)( \S+?))|((avatar)( \S+?))|((asleft)( \S+?))|((asrite)( \S+?))|((asbott)( \S+?))|((astop)( \S+?))|((asfrnt)( \S+?))|((asback)( \S+?))|((massed)( \S+?))|((pted)( \S+?))|((zned)( \S+?))|((rzflux)( \S+?))|((rzmflux)( \S+?))|((edoutf)( \S+?))|((byvolp)( \S+?))|((ajed)( \S+?))|((fluxone)( \S+?))))+)?)))+)?)|((embed)(( (((background)( \S+?))|((meshgeo)( \S+?))|((mgeoin)( \S+?))|((meeout)( \S+?))|((meein)( \S+?))|((calcvols)( \S+?))|((debug)( \S+?))|((filetype)( \S+?))|((gmvfile)( \S+?))|((length)( \S+?))|((mcnpumfile)( \S+?))))+)?)|((embee)(\d+?)(( (((embed)( \S+?))|((energy)( \S+?))|((time)( \S+?))|((atom)( \S+?))|((factor)( \S+?))|((list)( \S+?))|((mat)( \S+?))|((mtype)( \S+?))))+)?)|((embeb)(\d+?)(( \S+?)+))|((embem)(\d+?)(( \S+?)+))|((embtb)(\d+?)(( \S+?)+))|((embtm)(\d+?)(( \S+?)+))|((embdb)(\d+?)(( \S+?)+))|((embdf)(\d+?)(( \S+?)+))|((m)(\d+?)((( \S+?)( \S+?))+)(( (((gas)( \S+?))|((estep)( \S+?))|((hstep)( \S+?))|((nlib)( \S+?))|((plib)( \S+?))|((pnlib)( \S+?))|((elib)( \S+?))|((hlib)( \S+?))|((alib)( \S+?))|((slib)( \S+?))|((tlib)( \S+?))|((dlib)( \S+?))|((cond)( \S+?))|((refi)( \S+?))|((refc)(( \S+?)+))|((refs)(( \S+?)+))))+)?)|((mt)(\d+?)( \S+?))|((mx)(\d+?)(:\S+?)(( \S+?)+))|((otfdb)(( \S+?)+))|((totnu)( \S+?)?)|((nonu)(( \S+?)+)?)|((awtab)((( \S+?)( \S+?))+))|((xs)(\d+?)((( \S+?)( \S+?))+))|((void)(( \S+?)+)?)|((mgopt)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((drxs)(( \S+?)+)?)|((mode)(( \S+?)+))|((act)(( (((fission)( \S+?))|((nonfiss)( \S+?))|((dn)( \S+?))|((dg)( \S+?))|((thresh)( \S+?))|((dnbais)( \S+?))|((nap)( \S+?))|((dneb)((( \S+?)( \S+?))+))|((dgeb)((( \S+?)( \S+?))+))|((pecut)( \S+?))|((hlcut)( \S+?))|((sample)( \S+?))))+)?)|((cut)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((elpt)(( \S+?)+))|((thtme)(( \S+?)+))|((mphys)( \S+?)?)|((lca)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((lcb)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((lcc)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((lea)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((leb)( \S+?)( \S+?)( \S+?)( \S+?))|((fmult)( \S+?)(( (((width)( \S+?))|((sfyield)( \S+?))|((watt)( \S+?)( \S+?))|((method)( \S+?))|((data)( \S+?))|((shift)( \S+?))))+)?)|((tropt)(( (((mcscat)( \S+?))|((eloss)( \S+?))|((nreact)( \S+?))|((nescat)( \S+?))|((genxs)( \S+?))))+)?)|((unc)(( \S+?)+))|((cosyp)( \S+?)( \S+?)( \S+?)(( \S+?)+))|((cosy)(( \S+?)+))|((bfld)(\d+?)( \S+?)(( (((field)( \S+?))|((vec)(( \S+?)+))|((maxdeflc)( \S+?))|((maxstep)( \S+?))|((axs)(( \S+?)+))|((ffedges)(( \S+?)+))|((refpnt)(( \S+?)+))))+)?)|((bflcl)(( \S+?)+))|((sdef)(( (((cel)( \S+?))|((sur)( \S+?))|((erg)( \S+?))|((dir)( \S+?))|((vec)(( \S+?)+))|((nrm)( \S+?))|((pos)(( \S+?)+))|((rad)( \S+?))|((ext)( \S+?))|((axs)(( \S+?)+))|((x)( \S+?))|((y)( \S+?))|((z)( \S+?))|((ccc)( \S+?))|((ara)( \S+?))|((wgt)( \S+?))|((eff)( \S+?))|((par)( \S+?))|((dat)( \S+?)( \S+?)( \S+?))|((loc)( \S+?)( \S+?)( \S+?))|((bem)( \S+?)( \S+?)( \S+?))|((bap)( \S+?)( \S+?)( \S+?))))+)?)|((sp)(\d+?)( \S+?)(( \S+?)+))|((sp)( \S+?)( \S+?)( \S+?)?)|((sb)(\d+?)( \S+?)(( \S+?)+))|((sb)( \S+?)( \S+?)( \S+?)?)|((ds)(\d+?)( \S+?)(( \S+?)+))|((ds)(\d+?)( \S+?)((( \S+?)( \S+?))+))|((ds)(\d+?)( \S+?)(((( \S+?)+))+))|((sc)(\d+?)(( \S+?)+))|((ssw)(( \S+?)+)(( \S+?)+)(( (((sym)( \S+?))|((pty)(( \S+?)+))|((cel)(( \S+?)+))))+)?)|((ssr)(( (((old)(( \S+?)+))|((cel)(( \S+?)+))|((new)(( \S+?)+))|((pty)(( \S+?)+))|((col)( \S+?))|((wgt)( \S+?))|((psc)( \S+?))|((axs)(( \S+?)+))|((ext)( \S+?))|((poa)( \S+?))|((bcw)( \S+?)( \S+?)( \S+?))))+)?)|((kcode)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((ksrc)((( \S+?)( \S+?)( \S+?))+))|((kopts)(( (((blocksize)( \S+?))|((kinetics)( \S+?))|((precursor)( \S+?))|((ksental)( \S+?))|((fmat)( \S+?))|((fmatskpt)( \S+?))|((fmatncyc)( \S+?))|((fmatspace)( \S+?))|((fmataccel)( \S+?))|((fmatreduce)( \S+?))|((fmatnx)( \S+?))|((fmatny)( \S+?))|((fmatnz)( \S+?))))+)?)|((hsrc)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((fc)(\d+?)( \S+?))|((fq)(\d+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((de)(\d+?)( \S+?)(( \S+?)+))|((df)(\d+?)( \S+?)(( \S+?)+))|((em)(\d+?)(( \S+?)+))|((tm)(\d+?)(( \S+?)+))|((cm)(\d+?)(( \S+?)+))|((cf)(\d+?)(( \S+?)+))|((sf)(\d+?)(( \S+?)+))|((fs)(\d+?)(( \S+?)+)( \S+?)?( \S+?)?)|((sd)(( \S+?)+))|((fu)(\d+?)(( \S+?)+)( \S+?)?( \S+?)?)|((notrn))|((pert)(\d+?)(:\S+?)(( (((cell)(( \S+?)+))|((mat)( \S+?))|((rho)( \S+?))|((method)( \S+?))|((erg)( \S+?)( \S+?))|((rxn)(( \S+?)+))))+)?)|((kpert)(\d+?)(( (((cell)(( \S+?)+))|((mat)(( \S+?)+))|((rho)(( \S+?)+))|((iso)(( \S+?)+))|((rxn)(( \S+?)+))|((erg)(( \S+?)+))|((linear)( \S+?))))+)?)|((ksen)(\d+?)( \S+?)(( (((iso)(( \S+?)+))|((rxn)(( \S+?)+))|((mt)(( \S+?)+))|((erg)(( \S+?)+))|((ein)(( \S+?)+))|((legendre)( \S+?))|((cos)(( \S+?)+))|((constrain)( \S+?))))+)?)|((fmesh)(\d+?)(:\S+?)(( (((geom)( \S+?))|((origin)( \S+?)( \S+?)( \S+?))|((axs)( \S+?)( \S+?)( \S+?))|((vec)( \S+?)( \S+?)( \S+?))|((imesh)( \S+?))|((iints)( \S+?))|((jmesh)( \S+?))|((jints)( \S+?))|((kmesh)( \S+?))|((kints)( \S+?))|((emesh)( \S+?))|((eints)( \S+?))|((enorm)( \S+?))|((tmesh)( \S+?))|((tints)( \S+?))|((tnorm)( \S+?))|((factor)( \S+?))|((out)( \S+?))|((tr)( \S+?))|((inc)( \S+?)( \S+?)?)|((type)( \S+?))|((kclear)( \S+?))))+)?)|((spdtl)( \S+?))|((imp)(:\S+?)(( \S+?)+))|((var)(( (((rr)( \S+?))))+)?)|((wwe)(:\S+?)(( \S+?)+))|((wwt)(:\S+?)(( \S+?)+))|((wwn)(\d+?)(:\S+?)(( \S+?)+))|((wwp)(:\S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((wwg)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((wwge)(( \S+?)+))|((wwgt)(( \S+?)+))|((mesh)(( (((geom)( \S+?))|((ref)(( \S+?)+))|((origin)(( \S+?)+))|((axs)(( \S+?)+))|((vec)(( \S+?)+))|((imesh)(( \S+?)+))|((iints)( \S+?))|((jmesh)(( \S+?)+))|((jints)( \S+?))|((kmesh)(( \S+?)+))|((kints)( \S+?))))+)?)|((esplt)(:\S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((tsplt)(:\S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((ext)(:\S+?)(( \S+?)+))|((fcl)(:\S+?)(( \S+?)+))|((dxt)(:\S+?)( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( ( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))( \S+?)( \S+?)( \S+?))|((dd)(\d+?)((( \S+?)( \S+?))+))|((pd)(\d+?)(:\S+?)(( \S+?)+))|((dxc)(\d+?)(:\S+?)(( \S+?)+))|((bbrem)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)(( \S+?)+))|((pikmt)((( \S+?)( \S+?)((( \S+?)( \S+?))+))+))|((pwt)(( \S+?)+))|((nps)( \S+?)( \S+?)?)|((ctme)( \S+?))|((stop)(( (((nps)( \S+?)( \S+?)?)|((ctme)( \S+?))|((fk)(\d+?)( \S+?))))+)?)|((print)(( \S+?)+)?)|((talnp)(( \S+?)+)?)|((prdmp)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((ptrac)(( (((buffer)( \S+?))|((file)( \S+?))|((max)( \S+?))|((meph)( \S+?))|((write)( \S+?))|((conic)( \S+?))|((event)( \S+?))|((filter)((( \S+?)( \S+?)?( \S+?))+))|((type)(( \S+?)+))|((nps)(( \S+?)+))|((cell)(( \S+?)+))|((surface)(( \S+?)+))|((tally)(( \S+?)+))|((value)( \S+?))))+)?)|((histp)( \S+?)?(( \S+?)+)?)|((rand)(( (((gen)( \S+?))|((seed)( \S+?))|((stride)( \S+?))|((hist)( \S+?))))+)?)|((dbcn)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))|((lost)( \S+?)( \S+?))|((idum)(( \S+?)+))|((rdum)(( \S+?)+))|((za)( \S+?)?)|((zb)( \S+?)?)|((zc)( \S+?)?)|((zd)( \S+?)?)|((files)((( \S+?)( \S+?)( \S+?)( \S+?)( \S+?))+)))\Z'
    )

    def __init__(
        self,
        option: data.DataOption_,
    ):
        """
        Initializes ``Data``.

        Parameters:
            option: INP data option.

        Returns:
            ``Data``.

        Raises:
            InpError: SEMANTICS_CARD_VALUE.
        """

        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, option)

        self.option: typing.Final[data.DataOption_] = option

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Data`` from INP.

        Parameters:
            source: INP data card.

        Returns:
            ``Data``.

        Raises:
            InpError: SYNTAX_CARD.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Data._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_CARD, source)

        option = next(_parser.process_inp_option(data.DataOption_, tokens[1]))

        d = Data(option)
        d.comments = comments

        return d

    def to_mcnp(self):
        """
        Generates INP from ``Data``.

        Returns:
            INP data card.
        """

        return _parser.postprocess_continuation_line(self.option.to_mcnp())

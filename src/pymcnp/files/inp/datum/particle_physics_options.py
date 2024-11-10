from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors


class ParticlePhysicsOptions(Datum):
    """
    ``ParticlePhysicsOptions`` represents INP particle physics option data
    cards.

    ``ParticlePhysicsOptions`` inherits attributes from ``Datum``. It
    represents the INP problem type data card syntax element.

    Attributes
        designator: Particle designator.
    """

    def __init__(self, designator: types.Designator, parameters: tuple[any]):
        """
        ``__init__`` initializes ``ParticlePhysicsOptions``.

        Parameters:
            designator: Particle designator.
            parameters: Particle physics option data card parameters.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if parameters is None or not parameters:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        match designator:
            case types.Designator.Particle.NEUTRON:
                obj = ParticlePhysicsOptionsNeutron(*parameters)
            case types.Designator.Particle.PHOTON:
                obj = ParticlePhysicsOptionsPhoton(*parameters)
            case types.Designator.Particle.ELECTRON:
                obj = ParticlePhysicsOptionsElectron(*parameters)
            case types.Designator.Particle.PROTON:
                obj = ParticlePhysicsOptionsProton(*parameters)
            case _:
                obj = ParticlePhysicsOptionsOther(designator, *parameters)

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__


class ParticlePhysicsOptionsNeutron(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsNeutron`` represents INP particle physics
    option data cards with the neutron designator.

    ``ParticlePhysicsOptionsNeutron`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with neutron designator
    syntax element.

    Attributes:
        emax: Upper limit for neutron energy and memory control.
        emcnf: Analog energy limit.
        iunr: Unresolved resonance range control.
        colif: Light-ion and heavy-ion recoil and NCIA control.
        cutn: Table-based physics cutoff and memory reduction control.
        ngam: Secondary photon production control.
        i_int_model: Treatment of nuclear reactions control.
        i_els_model: Treatment of nuclear elastic scattering control.
    """

    def __init__(
        self,
        emax: types.McnpReal,
        emcnf: types.McnpReal,
        iunr: types.McnpInteger,
        colif: types.McnpReal,
        cutn: types.McnpReal,
        ngam: types.McnpInteger,
        i_int_model: types.McnpInteger,
        i_els_model: types.McnpInteger,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsNeutron``.

        Parameters:
            emax: Upper limit for neutron energy and memory control.
            emcnf: Analog energy limit.
            iunr: Unresolved resonance range control.
            colif: Light-ion and heavy-ion recoil and NCIA control.
            cutn: Table-based physics cutoff and memory reduction control.
            ngam: Secondary photon production control.
            i_int_model: Treatment of nuclear reactions control.
            i_els_model: Treatment of nuclear elastic scattering control.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if emcnf is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if iunr is None or iunr not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if colif is None or not (
            colif in {0, 3, 5}
            or 0.001 < colif < 1.001
            or 1.001 < colif < 2.001
            or 3.001 < colif < 4.001
        ):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if cutn is None or not (cutn >= 0 or cutn == -1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ngam is None or ngam not in {0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_int_model is None or i_int_model not in {-1, 0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_els_model is None or i_els_model not in {-1, 0}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'phys:n')
        self.mnemonic = DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (
            emax,
            emcnf,
            iunr,
            colif,
            cutn,
            ngam,
            i_int_model,
            i_els_model,
        )
        self.designator = types.Designator.Particle.NEUTRON

        self.emax = emax
        self.emcnf = emcnf
        self.iunr = iunr
        self.colif = colif
        self.cutn = cutn
        self.ngam = ngam
        self.i_int_model = i_int_model
        self.i_els_model = i_els_model


class ParticlePhysicsOptionsPhoton(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsPhoton`` represents INP particle physics option
    data cards with the photon designator.

    ``ParticlePhysicsOptionsPhoton`` inherits attributes from ``Datum``. It
    represents the INP problem type data card with photon designator
    syntax element.

    Attributes:
        emcpf: Energy limit for photon physics treatment.
        ides: Generation of electrions by photons controls.
        nocoh: Coherent Thomson scattering controls.
        ispn: Photonuclear particle production controls.
        nodop: Photon Doppler energy broadening controls.
        fism: Slection of photofission method controls.
    """

    def __init__(
        self,
        emcpf: types.McnpReal,
        ides: types.McnpInteger,
        nocoh: types.McnpInteger,
        ispn: types.McnpInteger,
        nodop: types.McnpInteger,
        fism: types.McnpInteger,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsPhoton``.

        Parameters:
            emcpf: Energy limit for photon physics treatment.
            ides: Generation of electrions by photons controls.
            nocoh: Coherent Thomson scattering controls.
            ispn: Photonuclear particle production controls.
            nodop: Photon Doppler energy broadening controls.
            fism: Slection of photofission method controls.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emcpf is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ides is None or ides not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nocoh is None or nocoh not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ispn is None or ispn not in {-1, 0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nodop is None or nodop not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if fism is None or fism not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'phys:p')
        self.mnemonic = DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (emcpf, ides, nocoh, ispn, nodop, fism)
        self.designator = types.Designator.Particle.PHOTON

        self.emcpf = emcpf
        self.ides = ides
        self.nocoh = nocoh
        self.ispn = ispn
        self.nodop = nodop
        self.fism = fism


class ParticlePhysicsOptionsElectron(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsElectron`` represents INP particle physics
    option data cards with the electron designator.

    ``ParticlePhysicsOptionsElectron`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with electron designator
    syntax element.

    Attributes:
        emax: Limit for electron energy.
        ides: Production of electrons by photons controls.
        iphot: Production of photons by electrons controls.
        ibad: Bremsstrahlung angular distribtuion method controls.
        istrg: Electron continuous-energy slowing down treatment controls.
        bnum: Production of bremsstrahlung photons controls.
        xnum: Smapling of electron-induced x-rays controls.
        rnok: Creation of knock-on electrons controls.
        enum: Generation of photon-induced electrons controls.
        numb: Bremsstrahlung production on each electron sub step.
        i_mcs_model: Choice of Coulomb scattering model controls.
        efac: Stopping power energy spacing controls.
        electron_method_boundary: Start of single-event transport controls.
        ckvnum: Cerenkov photon emission controls.
    """

    def __init__(
        self,
        emax: types.McnpReal,
        ides: types.McnpInteger,
        iphot: types.McnpReal,
        ibad: types.McnpInteger,
        istrg: types.McnpInteger,
        bnum: types.McnpReal,
        xnum: types.McnpReal,
        rnok: types.McnpReal,
        enum: types.McnpReal,
        numb: types.McnpReal,
        i_mcs_model: types.McnpInteger,
        efac: types.McnpReal,
        electron_method_boundary: types.McnpReal,
        ckvnum: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsElectron``.

        Parameters:
            emax: Limit for electron energy.
            ides: Production of electrons by photons controls.
            iphot: Production of photons by electrons controls.
            ibad: Bremsstrahlung angular distribtuion method controls.
            istrg: Electron continuous-energy slowing down treatment controls.
            bnum: Production of bremsstrahlung photons controls.
            xnum: Smapling of electron-induced x-rays controls.
            rnok: Creation of knock-on electrons controls.
            enum: Generation of photon-induced electrons controls.
            numb: Bremsstrahlung production on each electron sub step.
            i_mcs_model: Choice of Coulomb scattering model controls.
            efac: Stopping power energy spacing controls.
            electron_method_boundary: Start of single-event transport controls.
            ckvnum: Cerenkov photon emission controls.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ides is None or ides not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ibad is None or ibad not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if istrg is None or istrg not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if bnum is None or not (bnum >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xnum is None or not (xnum >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if rnok is None or not (rnok >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if enum is None or not (enum >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if numb is None or not (numb >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_mcs_model is None or i_mcs_model not in {0, -1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if electron_method_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'phys:e')
        self.mnemonic = DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (
            emax,
            ides,
            iphot,
            ibad,
            istrg,
            bnum,
            xnum,
            rnok,
            enum,
            numb,
            i_mcs_model,
            efac,
            electron_method_boundary,
            ckvnum,
        )
        self.designator = types.Designator.Particle.ELECTRON

        self.emax = emax
        self.ides = ides
        self.iphot = iphot
        self.ibad = ibad
        self.istrg = istrg
        self.bnum = bnum
        self.xnum = xnum
        self.rnok = rnok
        self.enum = enum
        self.numb = numb
        self.i_mcs_model = i_mcs_model
        self.efac = efac
        self.electron_method_boundary = electron_method_boundary
        self.ckvnum = ckvnum


class ParticlePhysicsOptionsProton(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsProton`` represents INP particle physics option
    data cards with the proton designator.

    ``ParticlePhysicsOptionsProton`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with proton designator syntax
    element.

    Attributes:
        emax: Proton energy limit.
        ean: Analog energy limit.
        tabl: Table-based physics cutoff.
        istrg: Charged-particle straggling controls.
        recl: Light ion recoil control.
        i_mcs_model: Choice of Coulomb scattering model controls.
        i_int_model: Treamtment of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering.
        efac: Stopping power energy spacing controls.
        ckvnum: Cerenkov photon emission controls.
        drp: Lower energy delta-ray cutoff.
    """

    def __init__(
        self,
        emax: types.McnpReal,
        ean: types.McnpReal,
        tabl: types.McnpReal,
        istrg: types.McnpInteger,
        recl: types.McnpReal,
        i_mcs_model: types.McnpInteger,
        i_int_model: types.McnpInteger,
        i_els_model: types.McnpInteger,
        efac: types.McnpReal,
        ckvnum: types.McnpReal,
        drp: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsProton``.

        Parameters:
            emax: Proton energy limit.
            ean: Analog energy limit.
            tabl: Table-based physics cutoff.
            istrg: Charged-particle straggling controls.
            recl: Light ion recoil control.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treamtment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering.
            efac: Stopping power energy spacing controls.
            ckvnum: Cerenkov photon emission controls.
            drp: Lower energy delta-ray cutoff.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ean is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if tabl is None or not (tabl == -1 or tabl >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if istrg is None or istrg not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if recl is None or not (0 <= recl <= 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_mcs_model is None or i_mcs_model not in {-1, 0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_int_model is None or i_int_model not in {-1, 0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_els_model is None or i_els_model not in {-1, 0}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if drp is None or not (drp == -1 or drp >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'phys:h')
        self.mnemonic = DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (
            emax,
            ean,
            tabl,
            istrg,
            recl,
            i_mcs_model,
            i_int_model,
            i_els_model,
            efac,
            ckvnum,
            drp,
        )
        self.designator = types.Designator.Particle.PROTON

        self.emax = emax
        self.ean = ean
        self.tabl = tabl
        self.istrg = istrg
        self.recl = recl
        self.i_mcs_model = i_mcs_model
        self.i_int_model = i_int_model
        self.i_els_model = i_els_model
        self.efac = efac
        self.ckvnum = ckvnum
        self.drp = drp


class ParticlePhysicsOptionsOther(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsProton`` represents INP particle physics option
    data cards with designators other than neutron, photon, electron, and
    proton.

    ``ParticlePhysicsOptionsProton`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with designators other than
    neutron, photon, electron, and proton syntax element.

    Attributes:
        emax: Upper energy limit.
        istrg: Charged-particle straggling controls.
        xmunum: Selection of muonic x-ray data controls.
        xmugam: Probability of emitting k-shell photon.
        i_mcs_model: Choice of Coulomb scattering model controls.
        i_int_model: Treamtment of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering.
        efac: Stopping power energy spacing controls.
        ckvnum: Cerenkov photon emission controls.
        drp: Lower energy delta-ray cutoff.
    """

    def __init__(
        self,
        designator: types.Designator,
        emax: types.McnpReal,
        istrg: types.McnpInteger,
        xmunum: types.McnpInteger,
        xmugam: types.McnpReal,
        i_mcs_model: types.McnpInteger,
        i_int_model: types.McnpInteger,
        i_els_model: types.McnpInteger,
        efac: types.McnpReal,
        ckvnum: types.McnpReal,
        drp: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsOther``.

        Parameters:
            designator: Particle designator.
            emax: Upper energy limit.
            istrg: Charged-particle straggling controls.
            xmunum: Selection of muonic x-ray data controls.
            xmugam: Probability of emitting k-shell photon.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treamtment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering.
            efac: Stopping power energy spacing controls.
            ckvnum: Cerenkov photon emission controls.
            drp: Lower energy delta-ray cutoff.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if istrg is None or istrg not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xmunum is None or xmunum not in {-1, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xmugam is None or not (0 <= xmugam <= 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_mcs_model is None or i_mcs_model not in {-1, 0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_int_model is None or i_int_model not in {-1, 0, 1, 2}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_els_model is None or i_els_model not in {-1, 0}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if drp is None or not (drp == -1 or drp >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id = f'phys:{designator.to_mcnp()}'
        self.mnemonic = DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (
            emax,
            istrg,
            xmunum,
            xmugam,
            i_mcs_model,
            i_int_model,
            i_els_model,
            efac,
            ckvnum,
            drp,
        )
        self.designator = designator

        self.emax = emax
        self.istrg = istrg
        self.xmunum = xmunum
        self.xmugam = xmugam
        self.i_mcs_model = i_mcs_model
        self.i_int_model = i_int_model
        self.i_els_model = i_els_model
        self.efac = efac
        self.ckvnum = ckvnum
        self.drp = drp

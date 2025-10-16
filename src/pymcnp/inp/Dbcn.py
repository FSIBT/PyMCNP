import re

from . import _card
from .. import types
from .. import errors


class Dbcn(_card.Card):
    """
    Represents INP dbcn cards.
    """

    _KEYWORD = 'dbcn'

    _ATTRS = {
        'x1': types.Integer,
        'x2': types.Integer,
        'x3': types.Integer,
        'x4': types.Integer,
        'x5': types.Integer,
        'x6': types.Integer,
        'x7': types.Integer,
        'x8': types.Integer,
        'x9': types.Integer,
        'x10': types.Integer,
        'x11': types.Integer,
        'x12': types.Integer,
        'x13': types.Integer,
        'x14': types.Integer,
        'x15': types.Integer,
        'x16': types.Integer,
        'x17': types.Integer,
        'x18': types.Integer,
        'x19': types.Integer,
        'x20': types.Integer,
        'x21': types.Integer,
        'x22': types.Integer,
        'x23': types.Integer,
        'x24': types.Integer,
        'x25': types.Integer,
        'x26': types.Integer,
        'x27': types.Integer,
        'x28': types.Integer,
        'x29': types.Integer,
        'x30': types.Integer,
        'x31': types.Integer,
        'x32': types.Integer,
        'x33': types.Integer,
        'x34': types.Integer,
        'x35': types.Integer,
        'x36': types.Integer,
        'x37': types.Integer,
        'x38': types.Integer,
        'x39': types.Integer,
        'x40': types.Integer,
        'x41': types.Integer,
        'x42': types.Integer,
        'x43': types.Integer,
        'x44': types.Integer,
        'x45': types.Integer,
        'x46': types.Integer,
        'x47': types.Integer,
        'x48': types.Integer,
        'x49': types.Integer,
        'x50': types.Integer,
        'x51': types.Integer,
        'x52': types.Integer,
        'x53': types.Integer,
        'x54': types.Integer,
        'x55': types.Integer,
        'x56': types.Integer,
        'x57': types.Integer,
        'x58': types.Integer,
        'x59': types.Integer,
        'x60': types.Integer,
        'x61': types.Integer,
        'x62': types.Integer,
        'x63': types.Integer,
        'x64': types.Integer,
        'x65': types.Integer,
        'x66': types.Integer,
        'x67': types.Integer,
        'x68': types.Integer,
        'x69': types.Integer,
        'x70': types.Integer,
        'x71': types.Integer,
        'x72': types.Integer,
        'x73': types.Integer,
        'x74': types.Integer,
        'x75': types.Integer,
        'x76': types.Integer,
        'x77': types.Integer,
        'x78': types.Integer,
        'x79': types.Integer,
        'x80': types.Integer,
        'x81': types.Integer,
        'x82': types.Integer,
        'x83': types.Integer,
        'x84': types.Integer,
        'x85': types.Integer,
        'x86': types.Integer,
        'x87': types.Integer,
        'x88': types.Integer,
        'x89': types.Integer,
        'x90': types.Integer,
        'x91': types.Integer,
        'x92': types.Integer,
        'x93': types.Integer,
        'x94': types.Integer,
        'x95': types.Integer,
        'x96': types.Integer,
        'x97': types.Integer,
        'x98': types.Integer,
        'x99': types.Integer,
        'x100': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Adbcn( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        x1: str | int | types.Integer = None,
        x2: str | int | types.Integer = None,
        x3: str | int | types.Integer = None,
        x4: str | int | types.Integer = None,
        x5: str | int | types.Integer = None,
        x6: str | int | types.Integer = None,
        x7: str | int | types.Integer = None,
        x8: str | int | types.Integer = None,
        x9: str | int | types.Integer = None,
        x10: str | int | types.Integer = None,
        x11: str | int | types.Integer = None,
        x12: str | int | types.Integer = None,
        x13: str | int | types.Integer = None,
        x14: str | int | types.Integer = None,
        x15: str | int | types.Integer = None,
        x16: str | int | types.Integer = None,
        x17: str | int | types.Integer = None,
        x18: str | int | types.Integer = None,
        x19: str | int | types.Integer = None,
        x20: str | int | types.Integer = None,
        x21: str | int | types.Integer = None,
        x22: str | int | types.Integer = None,
        x23: str | int | types.Integer = None,
        x24: str | int | types.Integer = None,
        x25: str | int | types.Integer = None,
        x26: str | int | types.Integer = None,
        x27: str | int | types.Integer = None,
        x28: str | int | types.Integer = None,
        x29: str | int | types.Integer = None,
        x30: str | int | types.Integer = None,
        x31: str | int | types.Integer = None,
        x32: str | int | types.Integer = None,
        x33: str | int | types.Integer = None,
        x34: str | int | types.Integer = None,
        x35: str | int | types.Integer = None,
        x36: str | int | types.Integer = None,
        x37: str | int | types.Integer = None,
        x38: str | int | types.Integer = None,
        x39: str | int | types.Integer = None,
        x40: str | int | types.Integer = None,
        x41: str | int | types.Integer = None,
        x42: str | int | types.Integer = None,
        x43: str | int | types.Integer = None,
        x44: str | int | types.Integer = None,
        x45: str | int | types.Integer = None,
        x46: str | int | types.Integer = None,
        x47: str | int | types.Integer = None,
        x48: str | int | types.Integer = None,
        x49: str | int | types.Integer = None,
        x50: str | int | types.Integer = None,
        x51: str | int | types.Integer = None,
        x52: str | int | types.Integer = None,
        x53: str | int | types.Integer = None,
        x54: str | int | types.Integer = None,
        x55: str | int | types.Integer = None,
        x56: str | int | types.Integer = None,
        x57: str | int | types.Integer = None,
        x58: str | int | types.Integer = None,
        x59: str | int | types.Integer = None,
        x60: str | int | types.Integer = None,
        x61: str | int | types.Integer = None,
        x62: str | int | types.Integer = None,
        x63: str | int | types.Integer = None,
        x64: str | int | types.Integer = None,
        x65: str | int | types.Integer = None,
        x66: str | int | types.Integer = None,
        x67: str | int | types.Integer = None,
        x68: str | int | types.Integer = None,
        x69: str | int | types.Integer = None,
        x70: str | int | types.Integer = None,
        x71: str | int | types.Integer = None,
        x72: str | int | types.Integer = None,
        x73: str | int | types.Integer = None,
        x74: str | int | types.Integer = None,
        x75: str | int | types.Integer = None,
        x76: str | int | types.Integer = None,
        x77: str | int | types.Integer = None,
        x78: str | int | types.Integer = None,
        x79: str | int | types.Integer = None,
        x80: str | int | types.Integer = None,
        x81: str | int | types.Integer = None,
        x82: str | int | types.Integer = None,
        x83: str | int | types.Integer = None,
        x84: str | int | types.Integer = None,
        x85: str | int | types.Integer = None,
        x86: str | int | types.Integer = None,
        x87: str | int | types.Integer = None,
        x88: str | int | types.Integer = None,
        x89: str | int | types.Integer = None,
        x90: str | int | types.Integer = None,
        x91: str | int | types.Integer = None,
        x92: str | int | types.Integer = None,
        x93: str | int | types.Integer = None,
        x94: str | int | types.Integer = None,
        x95: str | int | types.Integer = None,
        x96: str | int | types.Integer = None,
        x97: str | int | types.Integer = None,
        x98: str | int | types.Integer = None,
        x99: str | int | types.Integer = None,
        x100: str | int | types.Integer = None,
    ):
        """
        Initializes `Dbcn`.

        Parameters:
            x1: Obsolete; pseudorandom number for the first particle history.
            x2: Debug print interval.
            x3: Lower history number inclusive limit for logging.
            x4: Upper history number inclusive limit for logging.
            x5: Maximnum number of events per history for logging.
            x6: Detector/DXTRAN underflow limit.
            x7: Volume and sufrace area printing on/off.
            x8: Obsolete; starting history offset.
            x9: Distance allowed between cpincident repeated-structures.
            x10: Half-life threshold for stable nuclides.
            x11: Collision event lost particle logging on/off.
            x12: Expected number of random numbers.
            x13: Obsolete; random number stride.
            x14: Obsolete; random number multiplier.
            x15: Usual selection of statistics quantities printing on/off.
            x16: History score grid accumulation scaling.
            x17: Angular treatment for secondary particles setting.
            x18: Energy-indexing alogrithm for election transport settings.
            x19: Developer; Quadratic polynomical interpolation parameter.
            x20: Unused.
            x21: Unused.
            x22: Unsued.
            x23: Pulse-height tally variance reducation tress setting.
            x24: Grazing contribution cutoff for surface fluxx tallies settings.
            x25: Unused.
            x26: Unused.
            x27: Antiparticle promotion settings.
            x28: Bank size.
            x29: Unused.
            x30: Unused.
            x31: Unused.
            x32: GENXS behavior setting.
            x33: Additional interpolation/smoothing method for heavy ions on/off.
            x34: Developer; Muon-induced gammas bug parameter.
            x35: Slight spreading of nuclear exitation on/off.
            x36: User-provided data for muon-induced gamma rays on/off.
            x37: Mimumum of internal bremsstrahlung spectrum.
            x38: Barashenkov/Polanski data file on/off.
            x39: Default S(α,β) smoothing behavior on/off.
            x40: Developer; MCPLIB and XSDIR lines writing setting.
            x41: Developer; Phonton/election data printing setting.
            x42: Model cross section setting.
            x43: Developer; Photo form-factor interpolation setting.
            x44: Developer; Coherent scattering in isolation setting.
            x45: MCNP6/MCNPX elastic scattering method selector.
            x46: CEM-to_LAQGSM photonuclear energy boundary setting.
            x47: Cosmic-rasy spectra setting.
            x48: MCNP6 threading on/off.
            x49: Normal input checking on/off.
            x50: TFC priting setting.
            x51: Developer; Photon-induced fluoresence on/off.
            x52: Developer; Compton-induced relaxation on/off.
            x53: Photoelectric relazation data setting.
            x54: Sampling method for ENDF Law 9 setting.
            x55: Spontaneous decay integration time.
            x56: Unused.
            x57: Unused.
            x58: Unused.
            x59: Unused.
            x60: Print number of calls to each high-energy model.
            x61: Developer; models of knock-on electron angles.
            x62: Developer; single-event electrons excitation energy loss debugger.
            x63: Unused.
            x64: Developer; single-event electrons angular deflaction debugger.
            x65: Developer; single-event ionization and treat deflection dubgger.
            x66: Developer; single-event bremsstrahlung photon angles setting.
            x67: Particle histories setting for detectors and DXTRAN.
            x68: Unused.
            x69: LJA array size setting.
            x70: Developer; interaction models setting.
            x71: Model photonuclear capability on/off.
            x72: Log-log/linear interpolation in ELXS_MOD setting.
            x73: Unused.
            x74: Unused.
            x75: Print extra info for F-matrix calculation on/off.
            x76: Print array storage info after setup on/off.
            x77: Has-based cross-section serach bin number.
            x78: Developer; S(A,B) method old/new setting.
            x79: MT for absorption and fission setting.
            x80: Unused.
            x81: Developer; interpolation for electron elastic scatter setting.
            x82: Developer; interpolation for electron elastic scatter setting.
            x83: Developer; interpolation for electron partial x-s setting.
            x84: Developer; interpolation for electron bremsstrahlung energy setting.
            x85: Developer; interpolation for electron bremsstrahlung energy setting.
            x86: Developer; interpolation for electron excitation setting.
            x87: Developer; interpolation for electron knock-on energy setting.
            x88: Developer; interpolation for electron knock-on energy setting.
            x89: Developer; interpolation for electron ionization x-s setting.
            x90: Mximum number of terms for Goudsmit-Saunderson distribution.
            x91: Minimum ROC curve count value.
            x92: Maximum ROC curve count value.
            x93: Unused.
            x94: Unused.
            x95: Unused.
            x96: Unused.
            x97: Unused.
            x98: Unused.
            x99: Unused.
            x100: Coincident-surface method old/new setting.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.x1: types.Integer = x1
        self.x2: types.Integer = x2
        self.x3: types.Integer = x3
        self.x4: types.Integer = x4
        self.x5: types.Integer = x5
        self.x6: types.Integer = x6
        self.x7: types.Integer = x7
        self.x8: types.Integer = x8
        self.x9: types.Integer = x9
        self.x10: types.Integer = x10
        self.x11: types.Integer = x11
        self.x12: types.Integer = x12
        self.x13: types.Integer = x13
        self.x14: types.Integer = x14
        self.x15: types.Integer = x15
        self.x16: types.Integer = x16
        self.x17: types.Integer = x17
        self.x18: types.Integer = x18
        self.x19: types.Integer = x19
        self.x20: types.Integer = x20
        self.x21: types.Integer = x21
        self.x22: types.Integer = x22
        self.x23: types.Integer = x23
        self.x24: types.Integer = x24
        self.x25: types.Integer = x25
        self.x26: types.Integer = x26
        self.x27: types.Integer = x27
        self.x28: types.Integer = x28
        self.x29: types.Integer = x29
        self.x30: types.Integer = x30
        self.x31: types.Integer = x31
        self.x32: types.Integer = x32
        self.x33: types.Integer = x33
        self.x34: types.Integer = x34
        self.x35: types.Integer = x35
        self.x36: types.Integer = x36
        self.x37: types.Integer = x37
        self.x38: types.Integer = x38
        self.x39: types.Integer = x39
        self.x40: types.Integer = x40
        self.x41: types.Integer = x41
        self.x42: types.Integer = x42
        self.x43: types.Integer = x43
        self.x44: types.Integer = x44
        self.x45: types.Integer = x45
        self.x46: types.Integer = x46
        self.x47: types.Integer = x47
        self.x48: types.Integer = x48
        self.x49: types.Integer = x49
        self.x50: types.Integer = x50
        self.x51: types.Integer = x51
        self.x52: types.Integer = x52
        self.x53: types.Integer = x53
        self.x54: types.Integer = x54
        self.x55: types.Integer = x55
        self.x56: types.Integer = x56
        self.x57: types.Integer = x57
        self.x58: types.Integer = x58
        self.x59: types.Integer = x59
        self.x60: types.Integer = x60
        self.x61: types.Integer = x61
        self.x62: types.Integer = x62
        self.x63: types.Integer = x63
        self.x64: types.Integer = x64
        self.x65: types.Integer = x65
        self.x66: types.Integer = x66
        self.x67: types.Integer = x67
        self.x68: types.Integer = x68
        self.x69: types.Integer = x69
        self.x70: types.Integer = x70
        self.x71: types.Integer = x71
        self.x72: types.Integer = x72
        self.x73: types.Integer = x73
        self.x74: types.Integer = x74
        self.x75: types.Integer = x75
        self.x76: types.Integer = x76
        self.x77: types.Integer = x77
        self.x78: types.Integer = x78
        self.x79: types.Integer = x79
        self.x80: types.Integer = x80
        self.x81: types.Integer = x81
        self.x82: types.Integer = x82
        self.x83: types.Integer = x83
        self.x84: types.Integer = x84
        self.x85: types.Integer = x85
        self.x86: types.Integer = x86
        self.x87: types.Integer = x87
        self.x88: types.Integer = x88
        self.x89: types.Integer = x89
        self.x90: types.Integer = x90
        self.x91: types.Integer = x91
        self.x92: types.Integer = x92
        self.x93: types.Integer = x93
        self.x94: types.Integer = x94
        self.x95: types.Integer = x95
        self.x96: types.Integer = x96
        self.x97: types.Integer = x97
        self.x98: types.Integer = x98
        self.x99: types.Integer = x99
        self.x100: types.Integer = x100

    @property
    def x1(self) -> types.Integer:
        """
        Obsolete; pseudorandom number for the first particle history

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x1

    @x1.setter
    def x1(self, x1: str | int | types.Integer) -> None:
        """
        Sets `x1`.

        Parameters:
            x1: Obsolete; pseudorandom number for the first particle history.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x1 is not None:
            if isinstance(x1, types.Integer):
                x1 = x1
            elif isinstance(x1, int):
                x1 = types.Integer(x1)
            elif isinstance(x1, str):
                x1 = types.Integer.from_mcnp(x1)

        if x1 is not None and not (x1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x1)

        self._x1: types.Integer = x1

    @property
    def x2(self) -> types.Integer:
        """
        Debug print interval

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x2

    @x2.setter
    def x2(self, x2: str | int | types.Integer) -> None:
        """
        Sets `x2`.

        Parameters:
            x2: Debug print interval.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x2 is not None:
            if isinstance(x2, types.Integer):
                x2 = x2
            elif isinstance(x2, int):
                x2 = types.Integer(x2)
            elif isinstance(x2, str):
                x2 = types.Integer.from_mcnp(x2)

        self._x2: types.Integer = x2

    @property
    def x3(self) -> types.Integer:
        """
        Lower history number inclusive limit for logging

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x3

    @x3.setter
    def x3(self, x3: str | int | types.Integer) -> None:
        """
        Sets `x3`.

        Parameters:
            x3: Lower history number inclusive limit for logging.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x3 is not None:
            if isinstance(x3, types.Integer):
                x3 = x3
            elif isinstance(x3, int):
                x3 = types.Integer(x3)
            elif isinstance(x3, str):
                x3 = types.Integer.from_mcnp(x3)

        self._x3: types.Integer = x3

    @property
    def x4(self) -> types.Integer:
        """
        Upper history number inclusive limit for logging

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x4

    @x4.setter
    def x4(self, x4: str | int | types.Integer) -> None:
        """
        Sets `x4`.

        Parameters:
            x4: Upper history number inclusive limit for logging.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x4 is not None:
            if isinstance(x4, types.Integer):
                x4 = x4
            elif isinstance(x4, int):
                x4 = types.Integer(x4)
            elif isinstance(x4, str):
                x4 = types.Integer.from_mcnp(x4)

        self._x4: types.Integer = x4

    @property
    def x5(self) -> types.Integer:
        """
        Maximnum number of events per history for logging

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x5

    @x5.setter
    def x5(self, x5: str | int | types.Integer) -> None:
        """
        Sets `x5`.

        Parameters:
            x5: Maximnum number of events per history for logging.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x5 is not None:
            if isinstance(x5, types.Integer):
                x5 = x5
            elif isinstance(x5, int):
                x5 = types.Integer(x5)
            elif isinstance(x5, str):
                x5 = types.Integer.from_mcnp(x5)

        self._x5: types.Integer = x5

    @property
    def x6(self) -> types.Integer:
        """
        Detector/DXTRAN underflow limit

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x6

    @x6.setter
    def x6(self, x6: str | int | types.Integer) -> None:
        """
        Sets `x6`.

        Parameters:
            x6: Detector/DXTRAN underflow limit.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x6 is not None:
            if isinstance(x6, types.Integer):
                x6 = x6
            elif isinstance(x6, int):
                x6 = types.Integer(x6)
            elif isinstance(x6, str):
                x6 = types.Integer.from_mcnp(x6)

        if x6 is not None and not (x6 >= 50 and x6 <= 200):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x6)

        self._x6: types.Integer = x6

    @property
    def x7(self) -> types.Integer:
        """
        Volume and sufrace area printing on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x7

    @x7.setter
    def x7(self, x7: str | int | types.Integer) -> None:
        """
        Sets `x7`.

        Parameters:
            x7: Volume and sufrace area printing on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x7 is not None:
            if isinstance(x7, types.Integer):
                x7 = x7
            elif isinstance(x7, int):
                x7 = types.Integer(x7)
            elif isinstance(x7, str):
                x7 = types.Integer.from_mcnp(x7)

        self._x7: types.Integer = x7

    @property
    def x8(self) -> types.Integer:
        """
        Obsolete; starting history offset

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x8

    @x8.setter
    def x8(self, x8: str | int | types.Integer) -> None:
        """
        Sets `x8`.

        Parameters:
            x8: Obsolete; starting history offset.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x8 is not None:
            if isinstance(x8, types.Integer):
                x8 = x8
            elif isinstance(x8, int):
                x8 = types.Integer(x8)
            elif isinstance(x8, str):
                x8 = types.Integer.from_mcnp(x8)

        self._x8: types.Integer = x8

    @property
    def x9(self) -> types.Integer:
        """
        Distance allowed between cpincident repeated-structures

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x9

    @x9.setter
    def x9(self, x9: str | int | types.Integer) -> None:
        """
        Sets `x9`.

        Parameters:
            x9: Distance allowed between cpincident repeated-structures.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x9 is not None:
            if isinstance(x9, types.Integer):
                x9 = x9
            elif isinstance(x9, int):
                x9 = types.Integer(x9)
            elif isinstance(x9, str):
                x9 = types.Integer.from_mcnp(x9)

        self._x9: types.Integer = x9

    @property
    def x10(self) -> types.Integer:
        """
        Half-life threshold for stable nuclides

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x10

    @x10.setter
    def x10(self, x10: str | int | types.Integer) -> None:
        """
        Sets `x10`.

        Parameters:
            x10: Half-life threshold for stable nuclides.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x10 is not None:
            if isinstance(x10, types.Integer):
                x10 = x10
            elif isinstance(x10, int):
                x10 = types.Integer(x10)
            elif isinstance(x10, str):
                x10 = types.Integer.from_mcnp(x10)

        self._x10: types.Integer = x10

    @property
    def x11(self) -> types.Integer:
        """
        Collision event lost particle logging on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x11

    @x11.setter
    def x11(self, x11: str | int | types.Integer) -> None:
        """
        Sets `x11`.

        Parameters:
            x11: Collision event lost particle logging on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x11 is not None:
            if isinstance(x11, types.Integer):
                x11 = x11
            elif isinstance(x11, int):
                x11 = types.Integer(x11)
            elif isinstance(x11, str):
                x11 = types.Integer.from_mcnp(x11)

        self._x11: types.Integer = x11

    @property
    def x12(self) -> types.Integer:
        """
        Expected number of random numbers

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x12

    @x12.setter
    def x12(self, x12: str | int | types.Integer) -> None:
        """
        Sets `x12`.

        Parameters:
            x12: Expected number of random numbers.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x12 is not None:
            if isinstance(x12, types.Integer):
                x12 = x12
            elif isinstance(x12, int):
                x12 = types.Integer(x12)
            elif isinstance(x12, str):
                x12 = types.Integer.from_mcnp(x12)

        self._x12: types.Integer = x12

    @property
    def x13(self) -> types.Integer:
        """
        Obsolete; random number stride

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x13

    @x13.setter
    def x13(self, x13: str | int | types.Integer) -> None:
        """
        Sets `x13`.

        Parameters:
            x13: Obsolete; random number stride.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x13 is not None:
            if isinstance(x13, types.Integer):
                x13 = x13
            elif isinstance(x13, int):
                x13 = types.Integer(x13)
            elif isinstance(x13, str):
                x13 = types.Integer.from_mcnp(x13)

        self._x13: types.Integer = x13

    @property
    def x14(self) -> types.Integer:
        """
        Obsolete; random number multiplier

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x14

    @x14.setter
    def x14(self, x14: str | int | types.Integer) -> None:
        """
        Sets `x14`.

        Parameters:
            x14: Obsolete; random number multiplier.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x14 is not None:
            if isinstance(x14, types.Integer):
                x14 = x14
            elif isinstance(x14, int):
                x14 = types.Integer(x14)
            elif isinstance(x14, str):
                x14 = types.Integer.from_mcnp(x14)

        self._x14: types.Integer = x14

    @property
    def x15(self) -> types.Integer:
        """
        Usual selection of statistics quantities printing on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x15

    @x15.setter
    def x15(self, x15: str | int | types.Integer) -> None:
        """
        Sets `x15`.

        Parameters:
            x15: Usual selection of statistics quantities printing on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x15 is not None:
            if isinstance(x15, types.Integer):
                x15 = x15
            elif isinstance(x15, int):
                x15 = types.Integer(x15)
            elif isinstance(x15, str):
                x15 = types.Integer.from_mcnp(x15)

        self._x15: types.Integer = x15

    @property
    def x16(self) -> types.Integer:
        """
        History score grid accumulation scaling

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x16

    @x16.setter
    def x16(self, x16: str | int | types.Integer) -> None:
        """
        Sets `x16`.

        Parameters:
            x16: History score grid accumulation scaling.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x16 is not None:
            if isinstance(x16, types.Integer):
                x16 = x16
            elif isinstance(x16, int):
                x16 = types.Integer(x16)
            elif isinstance(x16, str):
                x16 = types.Integer.from_mcnp(x16)

        self._x16: types.Integer = x16

    @property
    def x17(self) -> types.Integer:
        """
        Angular treatment for secondary particles setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x17

    @x17.setter
    def x17(self, x17: str | int | types.Integer) -> None:
        """
        Sets `x17`.

        Parameters:
            x17: Angular treatment for secondary particles setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x17 is not None:
            if isinstance(x17, types.Integer):
                x17 = x17
            elif isinstance(x17, int):
                x17 = types.Integer(x17)
            elif isinstance(x17, str):
                x17 = types.Integer.from_mcnp(x17)

        self._x17: types.Integer = x17

    @property
    def x18(self) -> types.Integer:
        """
        Energy-indexing alogrithm for election transport settings

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x18

    @x18.setter
    def x18(self, x18: str | int | types.Integer) -> None:
        """
        Sets `x18`.

        Parameters:
            x18: Energy-indexing alogrithm for election transport settings.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x18 is not None:
            if isinstance(x18, types.Integer):
                x18 = x18
            elif isinstance(x18, int):
                x18 = types.Integer(x18)
            elif isinstance(x18, str):
                x18 = types.Integer.from_mcnp(x18)

        self._x18: types.Integer = x18

    @property
    def x19(self) -> types.Integer:
        """
        Developer; Quadratic polynomical interpolation parameter

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x19

    @x19.setter
    def x19(self, x19: str | int | types.Integer) -> None:
        """
        Sets `x19`.

        Parameters:
            x19: Developer; Quadratic polynomical interpolation parameter.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x19 is not None:
            if isinstance(x19, types.Integer):
                x19 = x19
            elif isinstance(x19, int):
                x19 = types.Integer(x19)
            elif isinstance(x19, str):
                x19 = types.Integer.from_mcnp(x19)

        self._x19: types.Integer = x19

    @property
    def x20(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x20

    @x20.setter
    def x20(self, x20: str | int | types.Integer) -> None:
        """
        Sets `x20`.

        Parameters:
            x20: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x20 is not None:
            if isinstance(x20, types.Integer):
                x20 = x20
            elif isinstance(x20, int):
                x20 = types.Integer(x20)
            elif isinstance(x20, str):
                x20 = types.Integer.from_mcnp(x20)

        self._x20: types.Integer = x20

    @property
    def x21(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x21

    @x21.setter
    def x21(self, x21: str | int | types.Integer) -> None:
        """
        Sets `x21`.

        Parameters:
            x21: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x21 is not None:
            if isinstance(x21, types.Integer):
                x21 = x21
            elif isinstance(x21, int):
                x21 = types.Integer(x21)
            elif isinstance(x21, str):
                x21 = types.Integer.from_mcnp(x21)

        self._x21: types.Integer = x21

    @property
    def x22(self) -> types.Integer:
        """
        Unsued

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x22

    @x22.setter
    def x22(self, x22: str | int | types.Integer) -> None:
        """
        Sets `x22`.

        Parameters:
            x22: Unsued.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x22 is not None:
            if isinstance(x22, types.Integer):
                x22 = x22
            elif isinstance(x22, int):
                x22 = types.Integer(x22)
            elif isinstance(x22, str):
                x22 = types.Integer.from_mcnp(x22)

        self._x22: types.Integer = x22

    @property
    def x23(self) -> types.Integer:
        """
        Pulse-height tally variance reducation tress setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x23

    @x23.setter
    def x23(self, x23: str | int | types.Integer) -> None:
        """
        Sets `x23`.

        Parameters:
            x23: Pulse-height tally variance reducation tress setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x23 is not None:
            if isinstance(x23, types.Integer):
                x23 = x23
            elif isinstance(x23, int):
                x23 = types.Integer(x23)
            elif isinstance(x23, str):
                x23 = types.Integer.from_mcnp(x23)

        self._x23: types.Integer = x23

    @property
    def x24(self) -> types.Integer:
        """
        Grazing contribution cutoff for surface fluxx tallies settings

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x24

    @x24.setter
    def x24(self, x24: str | int | types.Integer) -> None:
        """
        Sets `x24`.

        Parameters:
            x24: Grazing contribution cutoff for surface fluxx tallies settings.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x24 is not None:
            if isinstance(x24, types.Integer):
                x24 = x24
            elif isinstance(x24, int):
                x24 = types.Integer(x24)
            elif isinstance(x24, str):
                x24 = types.Integer.from_mcnp(x24)

        self._x24: types.Integer = x24

    @property
    def x25(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x25

    @x25.setter
    def x25(self, x25: str | int | types.Integer) -> None:
        """
        Sets `x25`.

        Parameters:
            x25: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x25 is not None:
            if isinstance(x25, types.Integer):
                x25 = x25
            elif isinstance(x25, int):
                x25 = types.Integer(x25)
            elif isinstance(x25, str):
                x25 = types.Integer.from_mcnp(x25)

        self._x25: types.Integer = x25

    @property
    def x26(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x26

    @x26.setter
    def x26(self, x26: str | int | types.Integer) -> None:
        """
        Sets `x26`.

        Parameters:
            x26: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x26 is not None:
            if isinstance(x26, types.Integer):
                x26 = x26
            elif isinstance(x26, int):
                x26 = types.Integer(x26)
            elif isinstance(x26, str):
                x26 = types.Integer.from_mcnp(x26)

        self._x26: types.Integer = x26

    @property
    def x27(self) -> types.Integer:
        """
        Antiparticle promotion settings

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x27

    @x27.setter
    def x27(self, x27: str | int | types.Integer) -> None:
        """
        Sets `x27`.

        Parameters:
            x27: Antiparticle promotion settings.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x27 is not None:
            if isinstance(x27, types.Integer):
                x27 = x27
            elif isinstance(x27, int):
                x27 = types.Integer(x27)
            elif isinstance(x27, str):
                x27 = types.Integer.from_mcnp(x27)

        self._x27: types.Integer = x27

    @property
    def x28(self) -> types.Integer:
        """
        Bank size

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x28

    @x28.setter
    def x28(self, x28: str | int | types.Integer) -> None:
        """
        Sets `x28`.

        Parameters:
            x28: Bank size.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x28 is not None:
            if isinstance(x28, types.Integer):
                x28 = x28
            elif isinstance(x28, int):
                x28 = types.Integer(x28)
            elif isinstance(x28, str):
                x28 = types.Integer.from_mcnp(x28)

        self._x28: types.Integer = x28

    @property
    def x29(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x29

    @x29.setter
    def x29(self, x29: str | int | types.Integer) -> None:
        """
        Sets `x29`.

        Parameters:
            x29: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x29 is not None:
            if isinstance(x29, types.Integer):
                x29 = x29
            elif isinstance(x29, int):
                x29 = types.Integer(x29)
            elif isinstance(x29, str):
                x29 = types.Integer.from_mcnp(x29)

        self._x29: types.Integer = x29

    @property
    def x30(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x30

    @x30.setter
    def x30(self, x30: str | int | types.Integer) -> None:
        """
        Sets `x30`.

        Parameters:
            x30: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x30 is not None:
            if isinstance(x30, types.Integer):
                x30 = x30
            elif isinstance(x30, int):
                x30 = types.Integer(x30)
            elif isinstance(x30, str):
                x30 = types.Integer.from_mcnp(x30)

        self._x30: types.Integer = x30

    @property
    def x31(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x31

    @x31.setter
    def x31(self, x31: str | int | types.Integer) -> None:
        """
        Sets `x31`.

        Parameters:
            x31: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x31 is not None:
            if isinstance(x31, types.Integer):
                x31 = x31
            elif isinstance(x31, int):
                x31 = types.Integer(x31)
            elif isinstance(x31, str):
                x31 = types.Integer.from_mcnp(x31)

        self._x31: types.Integer = x31

    @property
    def x32(self) -> types.Integer:
        """
        GENXS behavior setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x32

    @x32.setter
    def x32(self, x32: str | int | types.Integer) -> None:
        """
        Sets `x32`.

        Parameters:
            x32: GENXS behavior setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x32 is not None:
            if isinstance(x32, types.Integer):
                x32 = x32
            elif isinstance(x32, int):
                x32 = types.Integer(x32)
            elif isinstance(x32, str):
                x32 = types.Integer.from_mcnp(x32)

        self._x32: types.Integer = x32

    @property
    def x33(self) -> types.Integer:
        """
        Additional interpolation/smoothing method for heavy ions on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x33

    @x33.setter
    def x33(self, x33: str | int | types.Integer) -> None:
        """
        Sets `x33`.

        Parameters:
            x33: Additional interpolation/smoothing method for heavy ions on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x33 is not None:
            if isinstance(x33, types.Integer):
                x33 = x33
            elif isinstance(x33, int):
                x33 = types.Integer(x33)
            elif isinstance(x33, str):
                x33 = types.Integer.from_mcnp(x33)

        self._x33: types.Integer = x33

    @property
    def x34(self) -> types.Integer:
        """
        Developer; Muon-induced gammas bug parameter

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x34

    @x34.setter
    def x34(self, x34: str | int | types.Integer) -> None:
        """
        Sets `x34`.

        Parameters:
            x34: Developer; Muon-induced gammas bug parameter.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x34 is not None:
            if isinstance(x34, types.Integer):
                x34 = x34
            elif isinstance(x34, int):
                x34 = types.Integer(x34)
            elif isinstance(x34, str):
                x34 = types.Integer.from_mcnp(x34)

        self._x34: types.Integer = x34

    @property
    def x35(self) -> types.Integer:
        """
        Slight spreading of nuclear exitation on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x35

    @x35.setter
    def x35(self, x35: str | int | types.Integer) -> None:
        """
        Sets `x35`.

        Parameters:
            x35: Slight spreading of nuclear exitation on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x35 is not None:
            if isinstance(x35, types.Integer):
                x35 = x35
            elif isinstance(x35, int):
                x35 = types.Integer(x35)
            elif isinstance(x35, str):
                x35 = types.Integer.from_mcnp(x35)

        self._x35: types.Integer = x35

    @property
    def x36(self) -> types.Integer:
        """
        User-provided data for muon-induced gamma rays on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x36

    @x36.setter
    def x36(self, x36: str | int | types.Integer) -> None:
        """
        Sets `x36`.

        Parameters:
            x36: User-provided data for muon-induced gamma rays on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x36 is not None:
            if isinstance(x36, types.Integer):
                x36 = x36
            elif isinstance(x36, int):
                x36 = types.Integer(x36)
            elif isinstance(x36, str):
                x36 = types.Integer.from_mcnp(x36)

        self._x36: types.Integer = x36

    @property
    def x37(self) -> types.Integer:
        """
        Mimumum of internal bremsstrahlung spectrum

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x37

    @x37.setter
    def x37(self, x37: str | int | types.Integer) -> None:
        """
        Sets `x37`.

        Parameters:
            x37: Mimumum of internal bremsstrahlung spectrum.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x37 is not None:
            if isinstance(x37, types.Integer):
                x37 = x37
            elif isinstance(x37, int):
                x37 = types.Integer(x37)
            elif isinstance(x37, str):
                x37 = types.Integer.from_mcnp(x37)

        self._x37: types.Integer = x37

    @property
    def x38(self) -> types.Integer:
        """
        Barashenkov/Polanski data file on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x38

    @x38.setter
    def x38(self, x38: str | int | types.Integer) -> None:
        """
        Sets `x38`.

        Parameters:
            x38: Barashenkov/Polanski data file on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x38 is not None:
            if isinstance(x38, types.Integer):
                x38 = x38
            elif isinstance(x38, int):
                x38 = types.Integer(x38)
            elif isinstance(x38, str):
                x38 = types.Integer.from_mcnp(x38)

        self._x38: types.Integer = x38

    @property
    def x39(self) -> types.Integer:
        """
        Default S(α,β) smoothing behavior on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x39

    @x39.setter
    def x39(self, x39: str | int | types.Integer) -> None:
        """
        Sets `x39`.

        Parameters:
            x39: Default S(α,β) smoothing behavior on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x39 is not None:
            if isinstance(x39, types.Integer):
                x39 = x39
            elif isinstance(x39, int):
                x39 = types.Integer(x39)
            elif isinstance(x39, str):
                x39 = types.Integer.from_mcnp(x39)

        self._x39: types.Integer = x39

    @property
    def x40(self) -> types.Integer:
        """
        Developer; MCPLIB and XSDIR lines writing setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x40

    @x40.setter
    def x40(self, x40: str | int | types.Integer) -> None:
        """
        Sets `x40`.

        Parameters:
            x40: Developer; MCPLIB and XSDIR lines writing setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x40 is not None:
            if isinstance(x40, types.Integer):
                x40 = x40
            elif isinstance(x40, int):
                x40 = types.Integer(x40)
            elif isinstance(x40, str):
                x40 = types.Integer.from_mcnp(x40)

        self._x40: types.Integer = x40

    @property
    def x41(self) -> types.Integer:
        """
        Developer; Phonton/election data printing setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x41

    @x41.setter
    def x41(self, x41: str | int | types.Integer) -> None:
        """
        Sets `x41`.

        Parameters:
            x41: Developer; Phonton/election data printing setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x41 is not None:
            if isinstance(x41, types.Integer):
                x41 = x41
            elif isinstance(x41, int):
                x41 = types.Integer(x41)
            elif isinstance(x41, str):
                x41 = types.Integer.from_mcnp(x41)

        self._x41: types.Integer = x41

    @property
    def x42(self) -> types.Integer:
        """
        Model cross section setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x42

    @x42.setter
    def x42(self, x42: str | int | types.Integer) -> None:
        """
        Sets `x42`.

        Parameters:
            x42: Model cross section setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x42 is not None:
            if isinstance(x42, types.Integer):
                x42 = x42
            elif isinstance(x42, int):
                x42 = types.Integer(x42)
            elif isinstance(x42, str):
                x42 = types.Integer.from_mcnp(x42)

        self._x42: types.Integer = x42

    @property
    def x43(self) -> types.Integer:
        """
        Developer; Photo form-factor interpolation setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x43

    @x43.setter
    def x43(self, x43: str | int | types.Integer) -> None:
        """
        Sets `x43`.

        Parameters:
            x43: Developer; Photo form-factor interpolation setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x43 is not None:
            if isinstance(x43, types.Integer):
                x43 = x43
            elif isinstance(x43, int):
                x43 = types.Integer(x43)
            elif isinstance(x43, str):
                x43 = types.Integer.from_mcnp(x43)

        self._x43: types.Integer = x43

    @property
    def x44(self) -> types.Integer:
        """
        Developer; Coherent scattering in isolation setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x44

    @x44.setter
    def x44(self, x44: str | int | types.Integer) -> None:
        """
        Sets `x44`.

        Parameters:
            x44: Developer; Coherent scattering in isolation setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x44 is not None:
            if isinstance(x44, types.Integer):
                x44 = x44
            elif isinstance(x44, int):
                x44 = types.Integer(x44)
            elif isinstance(x44, str):
                x44 = types.Integer.from_mcnp(x44)

        self._x44: types.Integer = x44

    @property
    def x45(self) -> types.Integer:
        """
        MCNP6/MCNPX elastic scattering method selector

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x45

    @x45.setter
    def x45(self, x45: str | int | types.Integer) -> None:
        """
        Sets `x45`.

        Parameters:
            x45: MCNP6/MCNPX elastic scattering method selector.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x45 is not None:
            if isinstance(x45, types.Integer):
                x45 = x45
            elif isinstance(x45, int):
                x45 = types.Integer(x45)
            elif isinstance(x45, str):
                x45 = types.Integer.from_mcnp(x45)

        self._x45: types.Integer = x45

    @property
    def x46(self) -> types.Integer:
        """
        CEM-to_LAQGSM photonuclear energy boundary setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x46

    @x46.setter
    def x46(self, x46: str | int | types.Integer) -> None:
        """
        Sets `x46`.

        Parameters:
            x46: CEM-to_LAQGSM photonuclear energy boundary setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x46 is not None:
            if isinstance(x46, types.Integer):
                x46 = x46
            elif isinstance(x46, int):
                x46 = types.Integer(x46)
            elif isinstance(x46, str):
                x46 = types.Integer.from_mcnp(x46)

        self._x46: types.Integer = x46

    @property
    def x47(self) -> types.Integer:
        """
        Cosmic-rasy spectra setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x47

    @x47.setter
    def x47(self, x47: str | int | types.Integer) -> None:
        """
        Sets `x47`.

        Parameters:
            x47: Cosmic-rasy spectra setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x47 is not None:
            if isinstance(x47, types.Integer):
                x47 = x47
            elif isinstance(x47, int):
                x47 = types.Integer(x47)
            elif isinstance(x47, str):
                x47 = types.Integer.from_mcnp(x47)

        self._x47: types.Integer = x47

    @property
    def x48(self) -> types.Integer:
        """
        MCNP6 threading on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x48

    @x48.setter
    def x48(self, x48: str | int | types.Integer) -> None:
        """
        Sets `x48`.

        Parameters:
            x48: MCNP6 threading on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x48 is not None:
            if isinstance(x48, types.Integer):
                x48 = x48
            elif isinstance(x48, int):
                x48 = types.Integer(x48)
            elif isinstance(x48, str):
                x48 = types.Integer.from_mcnp(x48)

        self._x48: types.Integer = x48

    @property
    def x49(self) -> types.Integer:
        """
        Normal input checking on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x49

    @x49.setter
    def x49(self, x49: str | int | types.Integer) -> None:
        """
        Sets `x49`.

        Parameters:
            x49: Normal input checking on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x49 is not None:
            if isinstance(x49, types.Integer):
                x49 = x49
            elif isinstance(x49, int):
                x49 = types.Integer(x49)
            elif isinstance(x49, str):
                x49 = types.Integer.from_mcnp(x49)

        self._x49: types.Integer = x49

    @property
    def x50(self) -> types.Integer:
        """
        TFC priting setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x50

    @x50.setter
    def x50(self, x50: str | int | types.Integer) -> None:
        """
        Sets `x50`.

        Parameters:
            x50: TFC priting setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x50 is not None:
            if isinstance(x50, types.Integer):
                x50 = x50
            elif isinstance(x50, int):
                x50 = types.Integer(x50)
            elif isinstance(x50, str):
                x50 = types.Integer.from_mcnp(x50)

        self._x50: types.Integer = x50

    @property
    def x51(self) -> types.Integer:
        """
        Developer; Photon-induced fluoresence on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x51

    @x51.setter
    def x51(self, x51: str | int | types.Integer) -> None:
        """
        Sets `x51`.

        Parameters:
            x51: Developer; Photon-induced fluoresence on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x51 is not None:
            if isinstance(x51, types.Integer):
                x51 = x51
            elif isinstance(x51, int):
                x51 = types.Integer(x51)
            elif isinstance(x51, str):
                x51 = types.Integer.from_mcnp(x51)

        self._x51: types.Integer = x51

    @property
    def x52(self) -> types.Integer:
        """
        Developer; Compton-induced relaxation on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x52

    @x52.setter
    def x52(self, x52: str | int | types.Integer) -> None:
        """
        Sets `x52`.

        Parameters:
            x52: Developer; Compton-induced relaxation on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x52 is not None:
            if isinstance(x52, types.Integer):
                x52 = x52
            elif isinstance(x52, int):
                x52 = types.Integer(x52)
            elif isinstance(x52, str):
                x52 = types.Integer.from_mcnp(x52)

        self._x52: types.Integer = x52

    @property
    def x53(self) -> types.Integer:
        """
        Photoelectric relazation data setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x53

    @x53.setter
    def x53(self, x53: str | int | types.Integer) -> None:
        """
        Sets `x53`.

        Parameters:
            x53: Photoelectric relazation data setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x53 is not None:
            if isinstance(x53, types.Integer):
                x53 = x53
            elif isinstance(x53, int):
                x53 = types.Integer(x53)
            elif isinstance(x53, str):
                x53 = types.Integer.from_mcnp(x53)

        self._x53: types.Integer = x53

    @property
    def x54(self) -> types.Integer:
        """
        Sampling method for ENDF Law 9 setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x54

    @x54.setter
    def x54(self, x54: str | int | types.Integer) -> None:
        """
        Sets `x54`.

        Parameters:
            x54: Sampling method for ENDF Law 9 setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x54 is not None:
            if isinstance(x54, types.Integer):
                x54 = x54
            elif isinstance(x54, int):
                x54 = types.Integer(x54)
            elif isinstance(x54, str):
                x54 = types.Integer.from_mcnp(x54)

        self._x54: types.Integer = x54

    @property
    def x55(self) -> types.Integer:
        """
        Spontaneous decay integration time

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x55

    @x55.setter
    def x55(self, x55: str | int | types.Integer) -> None:
        """
        Sets `x55`.

        Parameters:
            x55: Spontaneous decay integration time.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x55 is not None:
            if isinstance(x55, types.Integer):
                x55 = x55
            elif isinstance(x55, int):
                x55 = types.Integer(x55)
            elif isinstance(x55, str):
                x55 = types.Integer.from_mcnp(x55)

        self._x55: types.Integer = x55

    @property
    def x56(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x56

    @x56.setter
    def x56(self, x56: str | int | types.Integer) -> None:
        """
        Sets `x56`.

        Parameters:
            x56: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x56 is not None:
            if isinstance(x56, types.Integer):
                x56 = x56
            elif isinstance(x56, int):
                x56 = types.Integer(x56)
            elif isinstance(x56, str):
                x56 = types.Integer.from_mcnp(x56)

        self._x56: types.Integer = x56

    @property
    def x57(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x57

    @x57.setter
    def x57(self, x57: str | int | types.Integer) -> None:
        """
        Sets `x57`.

        Parameters:
            x57: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x57 is not None:
            if isinstance(x57, types.Integer):
                x57 = x57
            elif isinstance(x57, int):
                x57 = types.Integer(x57)
            elif isinstance(x57, str):
                x57 = types.Integer.from_mcnp(x57)

        self._x57: types.Integer = x57

    @property
    def x58(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x58

    @x58.setter
    def x58(self, x58: str | int | types.Integer) -> None:
        """
        Sets `x58`.

        Parameters:
            x58: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x58 is not None:
            if isinstance(x58, types.Integer):
                x58 = x58
            elif isinstance(x58, int):
                x58 = types.Integer(x58)
            elif isinstance(x58, str):
                x58 = types.Integer.from_mcnp(x58)

        self._x58: types.Integer = x58

    @property
    def x59(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x59

    @x59.setter
    def x59(self, x59: str | int | types.Integer) -> None:
        """
        Sets `x59`.

        Parameters:
            x59: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x59 is not None:
            if isinstance(x59, types.Integer):
                x59 = x59
            elif isinstance(x59, int):
                x59 = types.Integer(x59)
            elif isinstance(x59, str):
                x59 = types.Integer.from_mcnp(x59)

        self._x59: types.Integer = x59

    @property
    def x60(self) -> types.Integer:
        """
        Print number of calls to each high-energy model

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x60

    @x60.setter
    def x60(self, x60: str | int | types.Integer) -> None:
        """
        Sets `x60`.

        Parameters:
            x60: Print number of calls to each high-energy model.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x60 is not None:
            if isinstance(x60, types.Integer):
                x60 = x60
            elif isinstance(x60, int):
                x60 = types.Integer(x60)
            elif isinstance(x60, str):
                x60 = types.Integer.from_mcnp(x60)

        self._x60: types.Integer = x60

    @property
    def x61(self) -> types.Integer:
        """
        Developer; models of knock-on electron angles

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x61

    @x61.setter
    def x61(self, x61: str | int | types.Integer) -> None:
        """
        Sets `x61`.

        Parameters:
            x61: Developer; models of knock-on electron angles.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x61 is not None:
            if isinstance(x61, types.Integer):
                x61 = x61
            elif isinstance(x61, int):
                x61 = types.Integer(x61)
            elif isinstance(x61, str):
                x61 = types.Integer.from_mcnp(x61)

        self._x61: types.Integer = x61

    @property
    def x62(self) -> types.Integer:
        """
        Developer; single-event electrons excitation energy loss debugger

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x62

    @x62.setter
    def x62(self, x62: str | int | types.Integer) -> None:
        """
        Sets `x62`.

        Parameters:
            x62: Developer; single-event electrons excitation energy loss debugger.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x62 is not None:
            if isinstance(x62, types.Integer):
                x62 = x62
            elif isinstance(x62, int):
                x62 = types.Integer(x62)
            elif isinstance(x62, str):
                x62 = types.Integer.from_mcnp(x62)

        self._x62: types.Integer = x62

    @property
    def x63(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x63

    @x63.setter
    def x63(self, x63: str | int | types.Integer) -> None:
        """
        Sets `x63`.

        Parameters:
            x63: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x63 is not None:
            if isinstance(x63, types.Integer):
                x63 = x63
            elif isinstance(x63, int):
                x63 = types.Integer(x63)
            elif isinstance(x63, str):
                x63 = types.Integer.from_mcnp(x63)

        self._x63: types.Integer = x63

    @property
    def x64(self) -> types.Integer:
        """
        Developer; single-event electrons angular deflaction debugger

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x64

    @x64.setter
    def x64(self, x64: str | int | types.Integer) -> None:
        """
        Sets `x64`.

        Parameters:
            x64: Developer; single-event electrons angular deflaction debugger.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x64 is not None:
            if isinstance(x64, types.Integer):
                x64 = x64
            elif isinstance(x64, int):
                x64 = types.Integer(x64)
            elif isinstance(x64, str):
                x64 = types.Integer.from_mcnp(x64)

        self._x64: types.Integer = x64

    @property
    def x65(self) -> types.Integer:
        """
        Developer; single-event ionization and treat deflection dubgger

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x65

    @x65.setter
    def x65(self, x65: str | int | types.Integer) -> None:
        """
        Sets `x65`.

        Parameters:
            x65: Developer; single-event ionization and treat deflection dubgger.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x65 is not None:
            if isinstance(x65, types.Integer):
                x65 = x65
            elif isinstance(x65, int):
                x65 = types.Integer(x65)
            elif isinstance(x65, str):
                x65 = types.Integer.from_mcnp(x65)

        self._x65: types.Integer = x65

    @property
    def x66(self) -> types.Integer:
        """
        Developer; single-event bremsstrahlung photon angles setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x66

    @x66.setter
    def x66(self, x66: str | int | types.Integer) -> None:
        """
        Sets `x66`.

        Parameters:
            x66: Developer; single-event bremsstrahlung photon angles setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x66 is not None:
            if isinstance(x66, types.Integer):
                x66 = x66
            elif isinstance(x66, int):
                x66 = types.Integer(x66)
            elif isinstance(x66, str):
                x66 = types.Integer.from_mcnp(x66)

        self._x66: types.Integer = x66

    @property
    def x67(self) -> types.Integer:
        """
        Particle histories setting for detectors and DXTRAN

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x67

    @x67.setter
    def x67(self, x67: str | int | types.Integer) -> None:
        """
        Sets `x67`.

        Parameters:
            x67: Particle histories setting for detectors and DXTRAN.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x67 is not None:
            if isinstance(x67, types.Integer):
                x67 = x67
            elif isinstance(x67, int):
                x67 = types.Integer(x67)
            elif isinstance(x67, str):
                x67 = types.Integer.from_mcnp(x67)

        self._x67: types.Integer = x67

    @property
    def x68(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x68

    @x68.setter
    def x68(self, x68: str | int | types.Integer) -> None:
        """
        Sets `x68`.

        Parameters:
            x68: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x68 is not None:
            if isinstance(x68, types.Integer):
                x68 = x68
            elif isinstance(x68, int):
                x68 = types.Integer(x68)
            elif isinstance(x68, str):
                x68 = types.Integer.from_mcnp(x68)

        self._x68: types.Integer = x68

    @property
    def x69(self) -> types.Integer:
        """
        LJA array size setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x69

    @x69.setter
    def x69(self, x69: str | int | types.Integer) -> None:
        """
        Sets `x69`.

        Parameters:
            x69: LJA array size setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x69 is not None:
            if isinstance(x69, types.Integer):
                x69 = x69
            elif isinstance(x69, int):
                x69 = types.Integer(x69)
            elif isinstance(x69, str):
                x69 = types.Integer.from_mcnp(x69)

        self._x69: types.Integer = x69

    @property
    def x70(self) -> types.Integer:
        """
        Developer; interaction models setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x70

    @x70.setter
    def x70(self, x70: str | int | types.Integer) -> None:
        """
        Sets `x70`.

        Parameters:
            x70: Developer; interaction models setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x70 is not None:
            if isinstance(x70, types.Integer):
                x70 = x70
            elif isinstance(x70, int):
                x70 = types.Integer(x70)
            elif isinstance(x70, str):
                x70 = types.Integer.from_mcnp(x70)

        self._x70: types.Integer = x70

    @property
    def x71(self) -> types.Integer:
        """
        Model photonuclear capability on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x71

    @x71.setter
    def x71(self, x71: str | int | types.Integer) -> None:
        """
        Sets `x71`.

        Parameters:
            x71: Model photonuclear capability on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x71 is not None:
            if isinstance(x71, types.Integer):
                x71 = x71
            elif isinstance(x71, int):
                x71 = types.Integer(x71)
            elif isinstance(x71, str):
                x71 = types.Integer.from_mcnp(x71)

        self._x71: types.Integer = x71

    @property
    def x72(self) -> types.Integer:
        """
        Log-log/linear interpolation in ELXS_MOD setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x72

    @x72.setter
    def x72(self, x72: str | int | types.Integer) -> None:
        """
        Sets `x72`.

        Parameters:
            x72: Log-log/linear interpolation in ELXS_MOD setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x72 is not None:
            if isinstance(x72, types.Integer):
                x72 = x72
            elif isinstance(x72, int):
                x72 = types.Integer(x72)
            elif isinstance(x72, str):
                x72 = types.Integer.from_mcnp(x72)

        self._x72: types.Integer = x72

    @property
    def x73(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x73

    @x73.setter
    def x73(self, x73: str | int | types.Integer) -> None:
        """
        Sets `x73`.

        Parameters:
            x73: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x73 is not None:
            if isinstance(x73, types.Integer):
                x73 = x73
            elif isinstance(x73, int):
                x73 = types.Integer(x73)
            elif isinstance(x73, str):
                x73 = types.Integer.from_mcnp(x73)

        self._x73: types.Integer = x73

    @property
    def x74(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x74

    @x74.setter
    def x74(self, x74: str | int | types.Integer) -> None:
        """
        Sets `x74`.

        Parameters:
            x74: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x74 is not None:
            if isinstance(x74, types.Integer):
                x74 = x74
            elif isinstance(x74, int):
                x74 = types.Integer(x74)
            elif isinstance(x74, str):
                x74 = types.Integer.from_mcnp(x74)

        self._x74: types.Integer = x74

    @property
    def x75(self) -> types.Integer:
        """
        Print extra info for F-matrix calculation on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x75

    @x75.setter
    def x75(self, x75: str | int | types.Integer) -> None:
        """
        Sets `x75`.

        Parameters:
            x75: Print extra info for F-matrix calculation on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x75 is not None:
            if isinstance(x75, types.Integer):
                x75 = x75
            elif isinstance(x75, int):
                x75 = types.Integer(x75)
            elif isinstance(x75, str):
                x75 = types.Integer.from_mcnp(x75)

        self._x75: types.Integer = x75

    @property
    def x76(self) -> types.Integer:
        """
        Print array storage info after setup on/off

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x76

    @x76.setter
    def x76(self, x76: str | int | types.Integer) -> None:
        """
        Sets `x76`.

        Parameters:
            x76: Print array storage info after setup on/off.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x76 is not None:
            if isinstance(x76, types.Integer):
                x76 = x76
            elif isinstance(x76, int):
                x76 = types.Integer(x76)
            elif isinstance(x76, str):
                x76 = types.Integer.from_mcnp(x76)

        self._x76: types.Integer = x76

    @property
    def x77(self) -> types.Integer:
        """
        Has-based cross-section serach bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x77

    @x77.setter
    def x77(self, x77: str | int | types.Integer) -> None:
        """
        Sets `x77`.

        Parameters:
            x77: Has-based cross-section serach bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x77 is not None:
            if isinstance(x77, types.Integer):
                x77 = x77
            elif isinstance(x77, int):
                x77 = types.Integer(x77)
            elif isinstance(x77, str):
                x77 = types.Integer.from_mcnp(x77)

        self._x77: types.Integer = x77

    @property
    def x78(self) -> types.Integer:
        """
        Developer; S(A,B) method old/new setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x78

    @x78.setter
    def x78(self, x78: str | int | types.Integer) -> None:
        """
        Sets `x78`.

        Parameters:
            x78: Developer; S(A,B) method old/new setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x78 is not None:
            if isinstance(x78, types.Integer):
                x78 = x78
            elif isinstance(x78, int):
                x78 = types.Integer(x78)
            elif isinstance(x78, str):
                x78 = types.Integer.from_mcnp(x78)

        self._x78: types.Integer = x78

    @property
    def x79(self) -> types.Integer:
        """
        MT for absorption and fission setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x79

    @x79.setter
    def x79(self, x79: str | int | types.Integer) -> None:
        """
        Sets `x79`.

        Parameters:
            x79: MT for absorption and fission setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x79 is not None:
            if isinstance(x79, types.Integer):
                x79 = x79
            elif isinstance(x79, int):
                x79 = types.Integer(x79)
            elif isinstance(x79, str):
                x79 = types.Integer.from_mcnp(x79)

        self._x79: types.Integer = x79

    @property
    def x80(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x80

    @x80.setter
    def x80(self, x80: str | int | types.Integer) -> None:
        """
        Sets `x80`.

        Parameters:
            x80: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x80 is not None:
            if isinstance(x80, types.Integer):
                x80 = x80
            elif isinstance(x80, int):
                x80 = types.Integer(x80)
            elif isinstance(x80, str):
                x80 = types.Integer.from_mcnp(x80)

        self._x80: types.Integer = x80

    @property
    def x81(self) -> types.Integer:
        """
        Developer; interpolation for electron elastic scatter setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x81

    @x81.setter
    def x81(self, x81: str | int | types.Integer) -> None:
        """
        Sets `x81`.

        Parameters:
            x81: Developer; interpolation for electron elastic scatter setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x81 is not None:
            if isinstance(x81, types.Integer):
                x81 = x81
            elif isinstance(x81, int):
                x81 = types.Integer(x81)
            elif isinstance(x81, str):
                x81 = types.Integer.from_mcnp(x81)

        self._x81: types.Integer = x81

    @property
    def x82(self) -> types.Integer:
        """
        Developer; interpolation for electron elastic scatter setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x82

    @x82.setter
    def x82(self, x82: str | int | types.Integer) -> None:
        """
        Sets `x82`.

        Parameters:
            x82: Developer; interpolation for electron elastic scatter setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x82 is not None:
            if isinstance(x82, types.Integer):
                x82 = x82
            elif isinstance(x82, int):
                x82 = types.Integer(x82)
            elif isinstance(x82, str):
                x82 = types.Integer.from_mcnp(x82)

        self._x82: types.Integer = x82

    @property
    def x83(self) -> types.Integer:
        """
        Developer; interpolation for electron partial x-s setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x83

    @x83.setter
    def x83(self, x83: str | int | types.Integer) -> None:
        """
        Sets `x83`.

        Parameters:
            x83: Developer; interpolation for electron partial x-s setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x83 is not None:
            if isinstance(x83, types.Integer):
                x83 = x83
            elif isinstance(x83, int):
                x83 = types.Integer(x83)
            elif isinstance(x83, str):
                x83 = types.Integer.from_mcnp(x83)

        self._x83: types.Integer = x83

    @property
    def x84(self) -> types.Integer:
        """
        Developer; interpolation for electron bremsstrahlung energy setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x84

    @x84.setter
    def x84(self, x84: str | int | types.Integer) -> None:
        """
        Sets `x84`.

        Parameters:
            x84: Developer; interpolation for electron bremsstrahlung energy setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x84 is not None:
            if isinstance(x84, types.Integer):
                x84 = x84
            elif isinstance(x84, int):
                x84 = types.Integer(x84)
            elif isinstance(x84, str):
                x84 = types.Integer.from_mcnp(x84)

        self._x84: types.Integer = x84

    @property
    def x85(self) -> types.Integer:
        """
        Developer; interpolation for electron bremsstrahlung energy setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x85

    @x85.setter
    def x85(self, x85: str | int | types.Integer) -> None:
        """
        Sets `x85`.

        Parameters:
            x85: Developer; interpolation for electron bremsstrahlung energy setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x85 is not None:
            if isinstance(x85, types.Integer):
                x85 = x85
            elif isinstance(x85, int):
                x85 = types.Integer(x85)
            elif isinstance(x85, str):
                x85 = types.Integer.from_mcnp(x85)

        self._x85: types.Integer = x85

    @property
    def x86(self) -> types.Integer:
        """
        Developer; interpolation for electron excitation setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x86

    @x86.setter
    def x86(self, x86: str | int | types.Integer) -> None:
        """
        Sets `x86`.

        Parameters:
            x86: Developer; interpolation for electron excitation setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x86 is not None:
            if isinstance(x86, types.Integer):
                x86 = x86
            elif isinstance(x86, int):
                x86 = types.Integer(x86)
            elif isinstance(x86, str):
                x86 = types.Integer.from_mcnp(x86)

        self._x86: types.Integer = x86

    @property
    def x87(self) -> types.Integer:
        """
        Developer; interpolation for electron knock-on energy setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x87

    @x87.setter
    def x87(self, x87: str | int | types.Integer) -> None:
        """
        Sets `x87`.

        Parameters:
            x87: Developer; interpolation for electron knock-on energy setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x87 is not None:
            if isinstance(x87, types.Integer):
                x87 = x87
            elif isinstance(x87, int):
                x87 = types.Integer(x87)
            elif isinstance(x87, str):
                x87 = types.Integer.from_mcnp(x87)

        self._x87: types.Integer = x87

    @property
    def x88(self) -> types.Integer:
        """
        Developer; interpolation for electron knock-on energy setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x88

    @x88.setter
    def x88(self, x88: str | int | types.Integer) -> None:
        """
        Sets `x88`.

        Parameters:
            x88: Developer; interpolation for electron knock-on energy setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x88 is not None:
            if isinstance(x88, types.Integer):
                x88 = x88
            elif isinstance(x88, int):
                x88 = types.Integer(x88)
            elif isinstance(x88, str):
                x88 = types.Integer.from_mcnp(x88)

        self._x88: types.Integer = x88

    @property
    def x89(self) -> types.Integer:
        """
        Developer; interpolation for electron ionization x-s setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x89

    @x89.setter
    def x89(self, x89: str | int | types.Integer) -> None:
        """
        Sets `x89`.

        Parameters:
            x89: Developer; interpolation for electron ionization x-s setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x89 is not None:
            if isinstance(x89, types.Integer):
                x89 = x89
            elif isinstance(x89, int):
                x89 = types.Integer(x89)
            elif isinstance(x89, str):
                x89 = types.Integer.from_mcnp(x89)

        self._x89: types.Integer = x89

    @property
    def x90(self) -> types.Integer:
        """
        Mximum number of terms for Goudsmit-Saunderson distribution

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x90

    @x90.setter
    def x90(self, x90: str | int | types.Integer) -> None:
        """
        Sets `x90`.

        Parameters:
            x90: Mximum number of terms for Goudsmit-Saunderson distribution.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x90 is not None:
            if isinstance(x90, types.Integer):
                x90 = x90
            elif isinstance(x90, int):
                x90 = types.Integer(x90)
            elif isinstance(x90, str):
                x90 = types.Integer.from_mcnp(x90)

        self._x90: types.Integer = x90

    @property
    def x91(self) -> types.Integer:
        """
        Minimum ROC curve count value

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x91

    @x91.setter
    def x91(self, x91: str | int | types.Integer) -> None:
        """
        Sets `x91`.

        Parameters:
            x91: Minimum ROC curve count value.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x91 is not None:
            if isinstance(x91, types.Integer):
                x91 = x91
            elif isinstance(x91, int):
                x91 = types.Integer(x91)
            elif isinstance(x91, str):
                x91 = types.Integer.from_mcnp(x91)

        self._x91: types.Integer = x91

    @property
    def x92(self) -> types.Integer:
        """
        Maximum ROC curve count value

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x92

    @x92.setter
    def x92(self, x92: str | int | types.Integer) -> None:
        """
        Sets `x92`.

        Parameters:
            x92: Maximum ROC curve count value.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x92 is not None:
            if isinstance(x92, types.Integer):
                x92 = x92
            elif isinstance(x92, int):
                x92 = types.Integer(x92)
            elif isinstance(x92, str):
                x92 = types.Integer.from_mcnp(x92)

        self._x92: types.Integer = x92

    @property
    def x93(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x93

    @x93.setter
    def x93(self, x93: str | int | types.Integer) -> None:
        """
        Sets `x93`.

        Parameters:
            x93: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x93 is not None:
            if isinstance(x93, types.Integer):
                x93 = x93
            elif isinstance(x93, int):
                x93 = types.Integer(x93)
            elif isinstance(x93, str):
                x93 = types.Integer.from_mcnp(x93)

        self._x93: types.Integer = x93

    @property
    def x94(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x94

    @x94.setter
    def x94(self, x94: str | int | types.Integer) -> None:
        """
        Sets `x94`.

        Parameters:
            x94: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x94 is not None:
            if isinstance(x94, types.Integer):
                x94 = x94
            elif isinstance(x94, int):
                x94 = types.Integer(x94)
            elif isinstance(x94, str):
                x94 = types.Integer.from_mcnp(x94)

        self._x94: types.Integer = x94

    @property
    def x95(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x95

    @x95.setter
    def x95(self, x95: str | int | types.Integer) -> None:
        """
        Sets `x95`.

        Parameters:
            x95: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x95 is not None:
            if isinstance(x95, types.Integer):
                x95 = x95
            elif isinstance(x95, int):
                x95 = types.Integer(x95)
            elif isinstance(x95, str):
                x95 = types.Integer.from_mcnp(x95)

        self._x95: types.Integer = x95

    @property
    def x96(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x96

    @x96.setter
    def x96(self, x96: str | int | types.Integer) -> None:
        """
        Sets `x96`.

        Parameters:
            x96: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x96 is not None:
            if isinstance(x96, types.Integer):
                x96 = x96
            elif isinstance(x96, int):
                x96 = types.Integer(x96)
            elif isinstance(x96, str):
                x96 = types.Integer.from_mcnp(x96)

        self._x96: types.Integer = x96

    @property
    def x97(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x97

    @x97.setter
    def x97(self, x97: str | int | types.Integer) -> None:
        """
        Sets `x97`.

        Parameters:
            x97: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x97 is not None:
            if isinstance(x97, types.Integer):
                x97 = x97
            elif isinstance(x97, int):
                x97 = types.Integer(x97)
            elif isinstance(x97, str):
                x97 = types.Integer.from_mcnp(x97)

        self._x97: types.Integer = x97

    @property
    def x98(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x98

    @x98.setter
    def x98(self, x98: str | int | types.Integer) -> None:
        """
        Sets `x98`.

        Parameters:
            x98: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x98 is not None:
            if isinstance(x98, types.Integer):
                x98 = x98
            elif isinstance(x98, int):
                x98 = types.Integer(x98)
            elif isinstance(x98, str):
                x98 = types.Integer.from_mcnp(x98)

        self._x98: types.Integer = x98

    @property
    def x99(self) -> types.Integer:
        """
        Unused

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x99

    @x99.setter
    def x99(self, x99: str | int | types.Integer) -> None:
        """
        Sets `x99`.

        Parameters:
            x99: Unused.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x99 is not None:
            if isinstance(x99, types.Integer):
                x99 = x99
            elif isinstance(x99, int):
                x99 = types.Integer(x99)
            elif isinstance(x99, str):
                x99 = types.Integer.from_mcnp(x99)

        self._x99: types.Integer = x99

    @property
    def x100(self) -> types.Integer:
        """
        Coincident-surface method old/new setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x100

    @x100.setter
    def x100(self, x100: str | int | types.Integer) -> None:
        """
        Sets `x100`.

        Parameters:
            x100: Coincident-surface method old/new setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x100 is not None:
            if isinstance(x100, types.Integer):
                x100 = x100
            elif isinstance(x100, int):
                x100 = types.Integer(x100)
            elif isinstance(x100, str):
                x100 = types.Integer.from_mcnp(x100)

        self._x100: types.Integer = x100

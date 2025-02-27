import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Dbcn(DataOption_, keyword='dbcn'):
    """
    Represents INP dbcn elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

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
        r'dbcn( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)'
    )

    def __init__(
        self,
        x1: types.Integer,
        x2: types.Integer,
        x3: types.Integer,
        x4: types.Integer,
        x5: types.Integer,
        x6: types.Integer,
        x7: types.Integer,
        x8: types.Integer,
        x9: types.Integer,
        x10: types.Integer,
        x11: types.Integer,
        x12: types.Integer,
        x13: types.Integer,
        x14: types.Integer,
        x15: types.Integer,
        x16: types.Integer,
        x17: types.Integer,
        x18: types.Integer,
        x19: types.Integer,
        x20: types.Integer,
        x21: types.Integer,
        x22: types.Integer,
        x23: types.Integer,
        x24: types.Integer,
        x25: types.Integer,
        x26: types.Integer,
        x27: types.Integer,
        x28: types.Integer,
        x29: types.Integer,
        x30: types.Integer,
        x31: types.Integer,
        x32: types.Integer,
        x33: types.Integer,
        x34: types.Integer,
        x35: types.Integer,
        x36: types.Integer,
        x37: types.Integer,
        x38: types.Integer,
        x39: types.Integer,
        x40: types.Integer,
        x41: types.Integer,
        x42: types.Integer,
        x43: types.Integer,
        x44: types.Integer,
        x45: types.Integer,
        x46: types.Integer,
        x47: types.Integer,
        x48: types.Integer,
        x49: types.Integer,
        x50: types.Integer,
        x51: types.Integer,
        x52: types.Integer,
        x53: types.Integer,
        x54: types.Integer,
        x55: types.Integer,
        x56: types.Integer,
        x57: types.Integer,
        x58: types.Integer,
        x59: types.Integer,
        x60: types.Integer,
        x61: types.Integer,
        x62: types.Integer,
        x63: types.Integer,
        x64: types.Integer,
        x65: types.Integer,
        x66: types.Integer,
        x67: types.Integer,
        x68: types.Integer,
        x69: types.Integer,
        x70: types.Integer,
        x71: types.Integer,
        x72: types.Integer,
        x73: types.Integer,
        x74: types.Integer,
        x75: types.Integer,
        x76: types.Integer,
        x77: types.Integer,
        x78: types.Integer,
        x79: types.Integer,
        x80: types.Integer,
        x81: types.Integer,
        x82: types.Integer,
        x83: types.Integer,
        x84: types.Integer,
        x85: types.Integer,
        x86: types.Integer,
        x87: types.Integer,
        x88: types.Integer,
        x89: types.Integer,
        x90: types.Integer,
        x91: types.Integer,
        x92: types.Integer,
        x93: types.Integer,
        x94: types.Integer,
        x95: types.Integer,
        x96: types.Integer,
        x97: types.Integer,
        x98: types.Integer,
        x99: types.Integer,
        x100: types.Integer,
    ):
        """
        Initializes ``Dbcn``.

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x1 is None or not (x1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x1)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x2)
        if x3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x3)
        if x4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x4)
        if x5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x5)
        if x6 is None or not (50 <= x6 <= 200):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x6)
        if x7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x7)
        if x8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x8)
        if x9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x9)
        if x10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x10)
        if x11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x11)
        if x12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x12)
        if x13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x13)
        if x14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x14)
        if x15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x15)
        if x16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x16)
        if x17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x17)
        if x18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x18)
        if x19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x19)
        if x20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x20)
        if x21 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x21)
        if x22 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x22)
        if x23 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x23)
        if x24 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x24)
        if x25 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x25)
        if x26 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x26)
        if x27 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x27)
        if x28 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x28)
        if x29 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x29)
        if x30 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x30)
        if x31 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x31)
        if x32 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x32)
        if x33 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x33)
        if x34 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x34)
        if x35 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x35)
        if x36 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x36)
        if x37 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x37)
        if x38 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x38)
        if x39 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x39)
        if x40 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x40)
        if x41 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x41)
        if x42 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x42)
        if x43 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x43)
        if x44 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x44)
        if x45 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x45)
        if x46 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x46)
        if x47 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x47)
        if x48 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x48)
        if x49 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x49)
        if x50 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x50)
        if x51 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x51)
        if x52 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x52)
        if x53 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x53)
        if x54 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x54)
        if x55 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x55)
        if x56 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x56)
        if x57 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x57)
        if x58 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x58)
        if x59 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x59)
        if x60 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x60)
        if x61 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x61)
        if x62 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x62)
        if x63 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x63)
        if x64 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x64)
        if x65 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x65)
        if x66 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x66)
        if x67 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x67)
        if x68 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x68)
        if x69 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x69)
        if x70 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x70)
        if x71 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x71)
        if x72 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x72)
        if x73 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x73)
        if x74 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x74)
        if x75 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x75)
        if x76 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x76)
        if x77 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x77)
        if x78 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x78)
        if x79 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x79)
        if x80 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x80)
        if x81 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x81)
        if x82 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x82)
        if x83 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x83)
        if x84 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x84)
        if x85 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x85)
        if x86 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x86)
        if x87 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x87)
        if x88 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x88)
        if x89 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x89)
        if x90 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x90)
        if x91 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x91)
        if x92 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x92)
        if x93 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x93)
        if x94 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x94)
        if x95 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x95)
        if x96 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x96)
        if x97 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x97)
        if x98 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x98)
        if x99 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x99)
        if x100 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x100)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x1,
                x2,
                x3,
                x4,
                x5,
                x6,
                x7,
                x8,
                x9,
                x10,
                x11,
                x12,
                x13,
                x14,
                x15,
                x16,
                x17,
                x18,
                x19,
                x20,
                x21,
                x22,
                x23,
                x24,
                x25,
                x26,
                x27,
                x28,
                x29,
                x30,
                x31,
                x32,
                x33,
                x34,
                x35,
                x36,
                x37,
                x38,
                x39,
                x40,
                x41,
                x42,
                x43,
                x44,
                x45,
                x46,
                x47,
                x48,
                x49,
                x50,
                x51,
                x52,
                x53,
                x54,
                x55,
                x56,
                x57,
                x58,
                x59,
                x60,
                x61,
                x62,
                x63,
                x64,
                x65,
                x66,
                x67,
                x68,
                x69,
                x70,
                x71,
                x72,
                x73,
                x74,
                x75,
                x76,
                x77,
                x78,
                x79,
                x80,
                x81,
                x82,
                x83,
                x84,
                x85,
                x86,
                x87,
                x88,
                x89,
                x90,
                x91,
                x92,
                x93,
                x94,
                x95,
                x96,
                x97,
                x98,
                x99,
                x100,
            ]
        )

        self.x1: typing.Final[types.Integer] = x1
        self.x2: typing.Final[types.Integer] = x2
        self.x3: typing.Final[types.Integer] = x3
        self.x4: typing.Final[types.Integer] = x4
        self.x5: typing.Final[types.Integer] = x5
        self.x6: typing.Final[types.Integer] = x6
        self.x7: typing.Final[types.Integer] = x7
        self.x8: typing.Final[types.Integer] = x8
        self.x9: typing.Final[types.Integer] = x9
        self.x10: typing.Final[types.Integer] = x10
        self.x11: typing.Final[types.Integer] = x11
        self.x12: typing.Final[types.Integer] = x12
        self.x13: typing.Final[types.Integer] = x13
        self.x14: typing.Final[types.Integer] = x14
        self.x15: typing.Final[types.Integer] = x15
        self.x16: typing.Final[types.Integer] = x16
        self.x17: typing.Final[types.Integer] = x17
        self.x18: typing.Final[types.Integer] = x18
        self.x19: typing.Final[types.Integer] = x19
        self.x20: typing.Final[types.Integer] = x20
        self.x21: typing.Final[types.Integer] = x21
        self.x22: typing.Final[types.Integer] = x22
        self.x23: typing.Final[types.Integer] = x23
        self.x24: typing.Final[types.Integer] = x24
        self.x25: typing.Final[types.Integer] = x25
        self.x26: typing.Final[types.Integer] = x26
        self.x27: typing.Final[types.Integer] = x27
        self.x28: typing.Final[types.Integer] = x28
        self.x29: typing.Final[types.Integer] = x29
        self.x30: typing.Final[types.Integer] = x30
        self.x31: typing.Final[types.Integer] = x31
        self.x32: typing.Final[types.Integer] = x32
        self.x33: typing.Final[types.Integer] = x33
        self.x34: typing.Final[types.Integer] = x34
        self.x35: typing.Final[types.Integer] = x35
        self.x36: typing.Final[types.Integer] = x36
        self.x37: typing.Final[types.Integer] = x37
        self.x38: typing.Final[types.Integer] = x38
        self.x39: typing.Final[types.Integer] = x39
        self.x40: typing.Final[types.Integer] = x40
        self.x41: typing.Final[types.Integer] = x41
        self.x42: typing.Final[types.Integer] = x42
        self.x43: typing.Final[types.Integer] = x43
        self.x44: typing.Final[types.Integer] = x44
        self.x45: typing.Final[types.Integer] = x45
        self.x46: typing.Final[types.Integer] = x46
        self.x47: typing.Final[types.Integer] = x47
        self.x48: typing.Final[types.Integer] = x48
        self.x49: typing.Final[types.Integer] = x49
        self.x50: typing.Final[types.Integer] = x50
        self.x51: typing.Final[types.Integer] = x51
        self.x52: typing.Final[types.Integer] = x52
        self.x53: typing.Final[types.Integer] = x53
        self.x54: typing.Final[types.Integer] = x54
        self.x55: typing.Final[types.Integer] = x55
        self.x56: typing.Final[types.Integer] = x56
        self.x57: typing.Final[types.Integer] = x57
        self.x58: typing.Final[types.Integer] = x58
        self.x59: typing.Final[types.Integer] = x59
        self.x60: typing.Final[types.Integer] = x60
        self.x61: typing.Final[types.Integer] = x61
        self.x62: typing.Final[types.Integer] = x62
        self.x63: typing.Final[types.Integer] = x63
        self.x64: typing.Final[types.Integer] = x64
        self.x65: typing.Final[types.Integer] = x65
        self.x66: typing.Final[types.Integer] = x66
        self.x67: typing.Final[types.Integer] = x67
        self.x68: typing.Final[types.Integer] = x68
        self.x69: typing.Final[types.Integer] = x69
        self.x70: typing.Final[types.Integer] = x70
        self.x71: typing.Final[types.Integer] = x71
        self.x72: typing.Final[types.Integer] = x72
        self.x73: typing.Final[types.Integer] = x73
        self.x74: typing.Final[types.Integer] = x74
        self.x75: typing.Final[types.Integer] = x75
        self.x76: typing.Final[types.Integer] = x76
        self.x77: typing.Final[types.Integer] = x77
        self.x78: typing.Final[types.Integer] = x78
        self.x79: typing.Final[types.Integer] = x79
        self.x80: typing.Final[types.Integer] = x80
        self.x81: typing.Final[types.Integer] = x81
        self.x82: typing.Final[types.Integer] = x82
        self.x83: typing.Final[types.Integer] = x83
        self.x84: typing.Final[types.Integer] = x84
        self.x85: typing.Final[types.Integer] = x85
        self.x86: typing.Final[types.Integer] = x86
        self.x87: typing.Final[types.Integer] = x87
        self.x88: typing.Final[types.Integer] = x88
        self.x89: typing.Final[types.Integer] = x89
        self.x90: typing.Final[types.Integer] = x90
        self.x91: typing.Final[types.Integer] = x91
        self.x92: typing.Final[types.Integer] = x92
        self.x93: typing.Final[types.Integer] = x93
        self.x94: typing.Final[types.Integer] = x94
        self.x95: typing.Final[types.Integer] = x95
        self.x96: typing.Final[types.Integer] = x96
        self.x97: typing.Final[types.Integer] = x97
        self.x98: typing.Final[types.Integer] = x98
        self.x99: typing.Final[types.Integer] = x99
        self.x100: typing.Final[types.Integer] = x100

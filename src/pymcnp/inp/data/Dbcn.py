import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Dbcn(DataOption):
    """
    Represents INP dbcn elements.

    Attributes:
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
    """

    _ATTRS = {
        'x1': types.IntegerOrJump,
        'x2': types.IntegerOrJump,
        'x3': types.IntegerOrJump,
        'x4': types.IntegerOrJump,
        'x5': types.IntegerOrJump,
        'x6': types.IntegerOrJump,
        'x7': types.IntegerOrJump,
        'x8': types.IntegerOrJump,
        'x9': types.IntegerOrJump,
        'x10': types.IntegerOrJump,
        'x11': types.IntegerOrJump,
        'x12': types.IntegerOrJump,
        'x13': types.IntegerOrJump,
        'x14': types.IntegerOrJump,
        'x15': types.IntegerOrJump,
        'x16': types.IntegerOrJump,
        'x17': types.IntegerOrJump,
        'x18': types.IntegerOrJump,
        'x19': types.IntegerOrJump,
        'x20': types.IntegerOrJump,
        'x21': types.IntegerOrJump,
        'x22': types.IntegerOrJump,
        'x23': types.IntegerOrJump,
        'x24': types.IntegerOrJump,
        'x25': types.IntegerOrJump,
        'x26': types.IntegerOrJump,
        'x27': types.IntegerOrJump,
        'x28': types.IntegerOrJump,
        'x29': types.IntegerOrJump,
        'x30': types.IntegerOrJump,
        'x31': types.IntegerOrJump,
        'x32': types.IntegerOrJump,
        'x33': types.IntegerOrJump,
        'x34': types.IntegerOrJump,
        'x35': types.IntegerOrJump,
        'x36': types.IntegerOrJump,
        'x37': types.IntegerOrJump,
        'x38': types.IntegerOrJump,
        'x39': types.IntegerOrJump,
        'x40': types.IntegerOrJump,
        'x41': types.IntegerOrJump,
        'x42': types.IntegerOrJump,
        'x43': types.IntegerOrJump,
        'x44': types.IntegerOrJump,
        'x45': types.IntegerOrJump,
        'x46': types.IntegerOrJump,
        'x47': types.IntegerOrJump,
        'x48': types.IntegerOrJump,
        'x49': types.IntegerOrJump,
        'x50': types.IntegerOrJump,
        'x51': types.IntegerOrJump,
        'x52': types.IntegerOrJump,
        'x53': types.IntegerOrJump,
        'x54': types.IntegerOrJump,
        'x55': types.IntegerOrJump,
        'x56': types.IntegerOrJump,
        'x57': types.IntegerOrJump,
        'x58': types.IntegerOrJump,
        'x59': types.IntegerOrJump,
        'x60': types.IntegerOrJump,
        'x61': types.IntegerOrJump,
        'x62': types.IntegerOrJump,
        'x63': types.IntegerOrJump,
        'x64': types.IntegerOrJump,
        'x65': types.IntegerOrJump,
        'x66': types.IntegerOrJump,
        'x67': types.IntegerOrJump,
        'x68': types.IntegerOrJump,
        'x69': types.IntegerOrJump,
        'x70': types.IntegerOrJump,
        'x71': types.IntegerOrJump,
        'x72': types.IntegerOrJump,
        'x73': types.IntegerOrJump,
        'x74': types.IntegerOrJump,
        'x75': types.IntegerOrJump,
        'x76': types.IntegerOrJump,
        'x77': types.IntegerOrJump,
        'x78': types.IntegerOrJump,
        'x79': types.IntegerOrJump,
        'x80': types.IntegerOrJump,
        'x81': types.IntegerOrJump,
        'x82': types.IntegerOrJump,
        'x83': types.IntegerOrJump,
        'x84': types.IntegerOrJump,
        'x85': types.IntegerOrJump,
        'x86': types.IntegerOrJump,
        'x87': types.IntegerOrJump,
        'x88': types.IntegerOrJump,
        'x89': types.IntegerOrJump,
        'x90': types.IntegerOrJump,
        'x91': types.IntegerOrJump,
        'x92': types.IntegerOrJump,
        'x93': types.IntegerOrJump,
        'x94': types.IntegerOrJump,
        'x95': types.IntegerOrJump,
        'x96': types.IntegerOrJump,
        'x97': types.IntegerOrJump,
        'x98': types.IntegerOrJump,
        'x99': types.IntegerOrJump,
        'x100': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Adbcn( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        x1: types.IntegerOrJump,
        x2: types.IntegerOrJump,
        x3: types.IntegerOrJump,
        x4: types.IntegerOrJump,
        x5: types.IntegerOrJump,
        x6: types.IntegerOrJump,
        x7: types.IntegerOrJump,
        x8: types.IntegerOrJump,
        x9: types.IntegerOrJump,
        x10: types.IntegerOrJump,
        x11: types.IntegerOrJump,
        x12: types.IntegerOrJump,
        x13: types.IntegerOrJump,
        x14: types.IntegerOrJump,
        x15: types.IntegerOrJump,
        x16: types.IntegerOrJump,
        x17: types.IntegerOrJump,
        x18: types.IntegerOrJump,
        x19: types.IntegerOrJump,
        x20: types.IntegerOrJump,
        x21: types.IntegerOrJump,
        x22: types.IntegerOrJump,
        x23: types.IntegerOrJump,
        x24: types.IntegerOrJump,
        x25: types.IntegerOrJump,
        x26: types.IntegerOrJump,
        x27: types.IntegerOrJump,
        x28: types.IntegerOrJump,
        x29: types.IntegerOrJump,
        x30: types.IntegerOrJump,
        x31: types.IntegerOrJump,
        x32: types.IntegerOrJump,
        x33: types.IntegerOrJump,
        x34: types.IntegerOrJump,
        x35: types.IntegerOrJump,
        x36: types.IntegerOrJump,
        x37: types.IntegerOrJump,
        x38: types.IntegerOrJump,
        x39: types.IntegerOrJump,
        x40: types.IntegerOrJump,
        x41: types.IntegerOrJump,
        x42: types.IntegerOrJump,
        x43: types.IntegerOrJump,
        x44: types.IntegerOrJump,
        x45: types.IntegerOrJump,
        x46: types.IntegerOrJump,
        x47: types.IntegerOrJump,
        x48: types.IntegerOrJump,
        x49: types.IntegerOrJump,
        x50: types.IntegerOrJump,
        x51: types.IntegerOrJump,
        x52: types.IntegerOrJump,
        x53: types.IntegerOrJump,
        x54: types.IntegerOrJump,
        x55: types.IntegerOrJump,
        x56: types.IntegerOrJump,
        x57: types.IntegerOrJump,
        x58: types.IntegerOrJump,
        x59: types.IntegerOrJump,
        x60: types.IntegerOrJump,
        x61: types.IntegerOrJump,
        x62: types.IntegerOrJump,
        x63: types.IntegerOrJump,
        x64: types.IntegerOrJump,
        x65: types.IntegerOrJump,
        x66: types.IntegerOrJump,
        x67: types.IntegerOrJump,
        x68: types.IntegerOrJump,
        x69: types.IntegerOrJump,
        x70: types.IntegerOrJump,
        x71: types.IntegerOrJump,
        x72: types.IntegerOrJump,
        x73: types.IntegerOrJump,
        x74: types.IntegerOrJump,
        x75: types.IntegerOrJump,
        x76: types.IntegerOrJump,
        x77: types.IntegerOrJump,
        x78: types.IntegerOrJump,
        x79: types.IntegerOrJump,
        x80: types.IntegerOrJump,
        x81: types.IntegerOrJump,
        x82: types.IntegerOrJump,
        x83: types.IntegerOrJump,
        x84: types.IntegerOrJump,
        x85: types.IntegerOrJump,
        x86: types.IntegerOrJump,
        x87: types.IntegerOrJump,
        x88: types.IntegerOrJump,
        x89: types.IntegerOrJump,
        x90: types.IntegerOrJump,
        x91: types.IntegerOrJump,
        x92: types.IntegerOrJump,
        x93: types.IntegerOrJump,
        x94: types.IntegerOrJump,
        x95: types.IntegerOrJump,
        x96: types.IntegerOrJump,
        x97: types.IntegerOrJump,
        x98: types.IntegerOrJump,
        x99: types.IntegerOrJump,
        x100: types.IntegerOrJump,
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
            InpError: SEMANTICS_OPTION.
        """

        if x1 is None or not (x1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x1)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x2)
        if x3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x3)
        if x4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x4)
        if x5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x5)
        if x6 is None or not (50 <= x6 <= 200):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x6)
        if x7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x7)
        if x8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x8)
        if x9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x9)
        if x10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x10)
        if x11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x11)
        if x12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x12)
        if x13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x13)
        if x14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x14)
        if x15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x15)
        if x16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x16)
        if x17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x17)
        if x18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x18)
        if x19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x19)
        if x20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x20)
        if x21 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x21)
        if x22 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x22)
        if x23 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x23)
        if x24 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x24)
        if x25 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x25)
        if x26 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x26)
        if x27 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x27)
        if x28 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x28)
        if x29 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x29)
        if x30 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x30)
        if x31 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x31)
        if x32 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x32)
        if x33 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x33)
        if x34 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x34)
        if x35 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x35)
        if x36 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x36)
        if x37 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x37)
        if x38 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x38)
        if x39 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x39)
        if x40 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x40)
        if x41 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x41)
        if x42 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x42)
        if x43 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x43)
        if x44 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x44)
        if x45 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x45)
        if x46 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x46)
        if x47 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x47)
        if x48 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x48)
        if x49 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x49)
        if x50 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x50)
        if x51 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x51)
        if x52 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x52)
        if x53 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x53)
        if x54 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x54)
        if x55 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x55)
        if x56 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x56)
        if x57 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x57)
        if x58 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x58)
        if x59 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x59)
        if x60 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x60)
        if x61 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x61)
        if x62 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x62)
        if x63 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x63)
        if x64 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x64)
        if x65 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x65)
        if x66 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x66)
        if x67 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x67)
        if x68 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x68)
        if x69 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x69)
        if x70 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x70)
        if x71 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x71)
        if x72 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x72)
        if x73 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x73)
        if x74 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x74)
        if x75 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x75)
        if x76 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x76)
        if x77 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x77)
        if x78 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x78)
        if x79 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x79)
        if x80 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x80)
        if x81 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x81)
        if x82 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x82)
        if x83 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x83)
        if x84 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x84)
        if x85 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x85)
        if x86 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x86)
        if x87 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x87)
        if x88 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x88)
        if x89 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x89)
        if x90 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x90)
        if x91 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x91)
        if x92 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x92)
        if x93 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x93)
        if x94 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x94)
        if x95 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x95)
        if x96 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x96)
        if x97 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x97)
        if x98 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x98)
        if x99 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x99)
        if x100 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x100)

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

        self.x1: typing.Final[types.IntegerOrJump] = x1
        self.x2: typing.Final[types.IntegerOrJump] = x2
        self.x3: typing.Final[types.IntegerOrJump] = x3
        self.x4: typing.Final[types.IntegerOrJump] = x4
        self.x5: typing.Final[types.IntegerOrJump] = x5
        self.x6: typing.Final[types.IntegerOrJump] = x6
        self.x7: typing.Final[types.IntegerOrJump] = x7
        self.x8: typing.Final[types.IntegerOrJump] = x8
        self.x9: typing.Final[types.IntegerOrJump] = x9
        self.x10: typing.Final[types.IntegerOrJump] = x10
        self.x11: typing.Final[types.IntegerOrJump] = x11
        self.x12: typing.Final[types.IntegerOrJump] = x12
        self.x13: typing.Final[types.IntegerOrJump] = x13
        self.x14: typing.Final[types.IntegerOrJump] = x14
        self.x15: typing.Final[types.IntegerOrJump] = x15
        self.x16: typing.Final[types.IntegerOrJump] = x16
        self.x17: typing.Final[types.IntegerOrJump] = x17
        self.x18: typing.Final[types.IntegerOrJump] = x18
        self.x19: typing.Final[types.IntegerOrJump] = x19
        self.x20: typing.Final[types.IntegerOrJump] = x20
        self.x21: typing.Final[types.IntegerOrJump] = x21
        self.x22: typing.Final[types.IntegerOrJump] = x22
        self.x23: typing.Final[types.IntegerOrJump] = x23
        self.x24: typing.Final[types.IntegerOrJump] = x24
        self.x25: typing.Final[types.IntegerOrJump] = x25
        self.x26: typing.Final[types.IntegerOrJump] = x26
        self.x27: typing.Final[types.IntegerOrJump] = x27
        self.x28: typing.Final[types.IntegerOrJump] = x28
        self.x29: typing.Final[types.IntegerOrJump] = x29
        self.x30: typing.Final[types.IntegerOrJump] = x30
        self.x31: typing.Final[types.IntegerOrJump] = x31
        self.x32: typing.Final[types.IntegerOrJump] = x32
        self.x33: typing.Final[types.IntegerOrJump] = x33
        self.x34: typing.Final[types.IntegerOrJump] = x34
        self.x35: typing.Final[types.IntegerOrJump] = x35
        self.x36: typing.Final[types.IntegerOrJump] = x36
        self.x37: typing.Final[types.IntegerOrJump] = x37
        self.x38: typing.Final[types.IntegerOrJump] = x38
        self.x39: typing.Final[types.IntegerOrJump] = x39
        self.x40: typing.Final[types.IntegerOrJump] = x40
        self.x41: typing.Final[types.IntegerOrJump] = x41
        self.x42: typing.Final[types.IntegerOrJump] = x42
        self.x43: typing.Final[types.IntegerOrJump] = x43
        self.x44: typing.Final[types.IntegerOrJump] = x44
        self.x45: typing.Final[types.IntegerOrJump] = x45
        self.x46: typing.Final[types.IntegerOrJump] = x46
        self.x47: typing.Final[types.IntegerOrJump] = x47
        self.x48: typing.Final[types.IntegerOrJump] = x48
        self.x49: typing.Final[types.IntegerOrJump] = x49
        self.x50: typing.Final[types.IntegerOrJump] = x50
        self.x51: typing.Final[types.IntegerOrJump] = x51
        self.x52: typing.Final[types.IntegerOrJump] = x52
        self.x53: typing.Final[types.IntegerOrJump] = x53
        self.x54: typing.Final[types.IntegerOrJump] = x54
        self.x55: typing.Final[types.IntegerOrJump] = x55
        self.x56: typing.Final[types.IntegerOrJump] = x56
        self.x57: typing.Final[types.IntegerOrJump] = x57
        self.x58: typing.Final[types.IntegerOrJump] = x58
        self.x59: typing.Final[types.IntegerOrJump] = x59
        self.x60: typing.Final[types.IntegerOrJump] = x60
        self.x61: typing.Final[types.IntegerOrJump] = x61
        self.x62: typing.Final[types.IntegerOrJump] = x62
        self.x63: typing.Final[types.IntegerOrJump] = x63
        self.x64: typing.Final[types.IntegerOrJump] = x64
        self.x65: typing.Final[types.IntegerOrJump] = x65
        self.x66: typing.Final[types.IntegerOrJump] = x66
        self.x67: typing.Final[types.IntegerOrJump] = x67
        self.x68: typing.Final[types.IntegerOrJump] = x68
        self.x69: typing.Final[types.IntegerOrJump] = x69
        self.x70: typing.Final[types.IntegerOrJump] = x70
        self.x71: typing.Final[types.IntegerOrJump] = x71
        self.x72: typing.Final[types.IntegerOrJump] = x72
        self.x73: typing.Final[types.IntegerOrJump] = x73
        self.x74: typing.Final[types.IntegerOrJump] = x74
        self.x75: typing.Final[types.IntegerOrJump] = x75
        self.x76: typing.Final[types.IntegerOrJump] = x76
        self.x77: typing.Final[types.IntegerOrJump] = x77
        self.x78: typing.Final[types.IntegerOrJump] = x78
        self.x79: typing.Final[types.IntegerOrJump] = x79
        self.x80: typing.Final[types.IntegerOrJump] = x80
        self.x81: typing.Final[types.IntegerOrJump] = x81
        self.x82: typing.Final[types.IntegerOrJump] = x82
        self.x83: typing.Final[types.IntegerOrJump] = x83
        self.x84: typing.Final[types.IntegerOrJump] = x84
        self.x85: typing.Final[types.IntegerOrJump] = x85
        self.x86: typing.Final[types.IntegerOrJump] = x86
        self.x87: typing.Final[types.IntegerOrJump] = x87
        self.x88: typing.Final[types.IntegerOrJump] = x88
        self.x89: typing.Final[types.IntegerOrJump] = x89
        self.x90: typing.Final[types.IntegerOrJump] = x90
        self.x91: typing.Final[types.IntegerOrJump] = x91
        self.x92: typing.Final[types.IntegerOrJump] = x92
        self.x93: typing.Final[types.IntegerOrJump] = x93
        self.x94: typing.Final[types.IntegerOrJump] = x94
        self.x95: typing.Final[types.IntegerOrJump] = x95
        self.x96: typing.Final[types.IntegerOrJump] = x96
        self.x97: typing.Final[types.IntegerOrJump] = x97
        self.x98: typing.Final[types.IntegerOrJump] = x98
        self.x99: typing.Final[types.IntegerOrJump] = x99
        self.x100: typing.Final[types.IntegerOrJump] = x100


@dataclasses.dataclass
class DbcnBuilder:
    """
    Builds ``Dbcn``.

    Attributes:
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
    """

    x1: str | int | types.IntegerOrJump
    x2: str | int | types.IntegerOrJump
    x3: str | int | types.IntegerOrJump
    x4: str | int | types.IntegerOrJump
    x5: str | int | types.IntegerOrJump
    x6: str | int | types.IntegerOrJump
    x7: str | int | types.IntegerOrJump
    x8: str | int | types.IntegerOrJump
    x9: str | int | types.IntegerOrJump
    x10: str | int | types.IntegerOrJump
    x11: str | int | types.IntegerOrJump
    x12: str | int | types.IntegerOrJump
    x13: str | int | types.IntegerOrJump
    x14: str | int | types.IntegerOrJump
    x15: str | int | types.IntegerOrJump
    x16: str | int | types.IntegerOrJump
    x17: str | int | types.IntegerOrJump
    x18: str | int | types.IntegerOrJump
    x19: str | int | types.IntegerOrJump
    x20: str | int | types.IntegerOrJump
    x21: str | int | types.IntegerOrJump
    x22: str | int | types.IntegerOrJump
    x23: str | int | types.IntegerOrJump
    x24: str | int | types.IntegerOrJump
    x25: str | int | types.IntegerOrJump
    x26: str | int | types.IntegerOrJump
    x27: str | int | types.IntegerOrJump
    x28: str | int | types.IntegerOrJump
    x29: str | int | types.IntegerOrJump
    x30: str | int | types.IntegerOrJump
    x31: str | int | types.IntegerOrJump
    x32: str | int | types.IntegerOrJump
    x33: str | int | types.IntegerOrJump
    x34: str | int | types.IntegerOrJump
    x35: str | int | types.IntegerOrJump
    x36: str | int | types.IntegerOrJump
    x37: str | int | types.IntegerOrJump
    x38: str | int | types.IntegerOrJump
    x39: str | int | types.IntegerOrJump
    x40: str | int | types.IntegerOrJump
    x41: str | int | types.IntegerOrJump
    x42: str | int | types.IntegerOrJump
    x43: str | int | types.IntegerOrJump
    x44: str | int | types.IntegerOrJump
    x45: str | int | types.IntegerOrJump
    x46: str | int | types.IntegerOrJump
    x47: str | int | types.IntegerOrJump
    x48: str | int | types.IntegerOrJump
    x49: str | int | types.IntegerOrJump
    x50: str | int | types.IntegerOrJump
    x51: str | int | types.IntegerOrJump
    x52: str | int | types.IntegerOrJump
    x53: str | int | types.IntegerOrJump
    x54: str | int | types.IntegerOrJump
    x55: str | int | types.IntegerOrJump
    x56: str | int | types.IntegerOrJump
    x57: str | int | types.IntegerOrJump
    x58: str | int | types.IntegerOrJump
    x59: str | int | types.IntegerOrJump
    x60: str | int | types.IntegerOrJump
    x61: str | int | types.IntegerOrJump
    x62: str | int | types.IntegerOrJump
    x63: str | int | types.IntegerOrJump
    x64: str | int | types.IntegerOrJump
    x65: str | int | types.IntegerOrJump
    x66: str | int | types.IntegerOrJump
    x67: str | int | types.IntegerOrJump
    x68: str | int | types.IntegerOrJump
    x69: str | int | types.IntegerOrJump
    x70: str | int | types.IntegerOrJump
    x71: str | int | types.IntegerOrJump
    x72: str | int | types.IntegerOrJump
    x73: str | int | types.IntegerOrJump
    x74: str | int | types.IntegerOrJump
    x75: str | int | types.IntegerOrJump
    x76: str | int | types.IntegerOrJump
    x77: str | int | types.IntegerOrJump
    x78: str | int | types.IntegerOrJump
    x79: str | int | types.IntegerOrJump
    x80: str | int | types.IntegerOrJump
    x81: str | int | types.IntegerOrJump
    x82: str | int | types.IntegerOrJump
    x83: str | int | types.IntegerOrJump
    x84: str | int | types.IntegerOrJump
    x85: str | int | types.IntegerOrJump
    x86: str | int | types.IntegerOrJump
    x87: str | int | types.IntegerOrJump
    x88: str | int | types.IntegerOrJump
    x89: str | int | types.IntegerOrJump
    x90: str | int | types.IntegerOrJump
    x91: str | int | types.IntegerOrJump
    x92: str | int | types.IntegerOrJump
    x93: str | int | types.IntegerOrJump
    x94: str | int | types.IntegerOrJump
    x95: str | int | types.IntegerOrJump
    x96: str | int | types.IntegerOrJump
    x97: str | int | types.IntegerOrJump
    x98: str | int | types.IntegerOrJump
    x99: str | int | types.IntegerOrJump
    x100: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``DbcnBuilder`` into ``Dbcn``.

        Returns:
            ``Dbcn`` for ``DbcnBuilder``.
        """

        if isinstance(self.x1, types.Integer):
            x1 = self.x1
        elif isinstance(self.x1, int):
            x1 = types.IntegerOrJump(self.x1)
        elif isinstance(self.x1, str):
            x1 = types.IntegerOrJump.from_mcnp(self.x1)

        if isinstance(self.x2, types.Integer):
            x2 = self.x2
        elif isinstance(self.x2, int):
            x2 = types.IntegerOrJump(self.x2)
        elif isinstance(self.x2, str):
            x2 = types.IntegerOrJump.from_mcnp(self.x2)

        if isinstance(self.x3, types.Integer):
            x3 = self.x3
        elif isinstance(self.x3, int):
            x3 = types.IntegerOrJump(self.x3)
        elif isinstance(self.x3, str):
            x3 = types.IntegerOrJump.from_mcnp(self.x3)

        if isinstance(self.x4, types.Integer):
            x4 = self.x4
        elif isinstance(self.x4, int):
            x4 = types.IntegerOrJump(self.x4)
        elif isinstance(self.x4, str):
            x4 = types.IntegerOrJump.from_mcnp(self.x4)

        if isinstance(self.x5, types.Integer):
            x5 = self.x5
        elif isinstance(self.x5, int):
            x5 = types.IntegerOrJump(self.x5)
        elif isinstance(self.x5, str):
            x5 = types.IntegerOrJump.from_mcnp(self.x5)

        if isinstance(self.x6, types.Integer):
            x6 = self.x6
        elif isinstance(self.x6, int):
            x6 = types.IntegerOrJump(self.x6)
        elif isinstance(self.x6, str):
            x6 = types.IntegerOrJump.from_mcnp(self.x6)

        if isinstance(self.x7, types.Integer):
            x7 = self.x7
        elif isinstance(self.x7, int):
            x7 = types.IntegerOrJump(self.x7)
        elif isinstance(self.x7, str):
            x7 = types.IntegerOrJump.from_mcnp(self.x7)

        if isinstance(self.x8, types.Integer):
            x8 = self.x8
        elif isinstance(self.x8, int):
            x8 = types.IntegerOrJump(self.x8)
        elif isinstance(self.x8, str):
            x8 = types.IntegerOrJump.from_mcnp(self.x8)

        if isinstance(self.x9, types.Integer):
            x9 = self.x9
        elif isinstance(self.x9, int):
            x9 = types.IntegerOrJump(self.x9)
        elif isinstance(self.x9, str):
            x9 = types.IntegerOrJump.from_mcnp(self.x9)

        if isinstance(self.x10, types.Integer):
            x10 = self.x10
        elif isinstance(self.x10, int):
            x10 = types.IntegerOrJump(self.x10)
        elif isinstance(self.x10, str):
            x10 = types.IntegerOrJump.from_mcnp(self.x10)

        if isinstance(self.x11, types.Integer):
            x11 = self.x11
        elif isinstance(self.x11, int):
            x11 = types.IntegerOrJump(self.x11)
        elif isinstance(self.x11, str):
            x11 = types.IntegerOrJump.from_mcnp(self.x11)

        if isinstance(self.x12, types.Integer):
            x12 = self.x12
        elif isinstance(self.x12, int):
            x12 = types.IntegerOrJump(self.x12)
        elif isinstance(self.x12, str):
            x12 = types.IntegerOrJump.from_mcnp(self.x12)

        if isinstance(self.x13, types.Integer):
            x13 = self.x13
        elif isinstance(self.x13, int):
            x13 = types.IntegerOrJump(self.x13)
        elif isinstance(self.x13, str):
            x13 = types.IntegerOrJump.from_mcnp(self.x13)

        if isinstance(self.x14, types.Integer):
            x14 = self.x14
        elif isinstance(self.x14, int):
            x14 = types.IntegerOrJump(self.x14)
        elif isinstance(self.x14, str):
            x14 = types.IntegerOrJump.from_mcnp(self.x14)

        if isinstance(self.x15, types.Integer):
            x15 = self.x15
        elif isinstance(self.x15, int):
            x15 = types.IntegerOrJump(self.x15)
        elif isinstance(self.x15, str):
            x15 = types.IntegerOrJump.from_mcnp(self.x15)

        if isinstance(self.x16, types.Integer):
            x16 = self.x16
        elif isinstance(self.x16, int):
            x16 = types.IntegerOrJump(self.x16)
        elif isinstance(self.x16, str):
            x16 = types.IntegerOrJump.from_mcnp(self.x16)

        if isinstance(self.x17, types.Integer):
            x17 = self.x17
        elif isinstance(self.x17, int):
            x17 = types.IntegerOrJump(self.x17)
        elif isinstance(self.x17, str):
            x17 = types.IntegerOrJump.from_mcnp(self.x17)

        if isinstance(self.x18, types.Integer):
            x18 = self.x18
        elif isinstance(self.x18, int):
            x18 = types.IntegerOrJump(self.x18)
        elif isinstance(self.x18, str):
            x18 = types.IntegerOrJump.from_mcnp(self.x18)

        if isinstance(self.x19, types.Integer):
            x19 = self.x19
        elif isinstance(self.x19, int):
            x19 = types.IntegerOrJump(self.x19)
        elif isinstance(self.x19, str):
            x19 = types.IntegerOrJump.from_mcnp(self.x19)

        if isinstance(self.x20, types.Integer):
            x20 = self.x20
        elif isinstance(self.x20, int):
            x20 = types.IntegerOrJump(self.x20)
        elif isinstance(self.x20, str):
            x20 = types.IntegerOrJump.from_mcnp(self.x20)

        if isinstance(self.x21, types.Integer):
            x21 = self.x21
        elif isinstance(self.x21, int):
            x21 = types.IntegerOrJump(self.x21)
        elif isinstance(self.x21, str):
            x21 = types.IntegerOrJump.from_mcnp(self.x21)

        if isinstance(self.x22, types.Integer):
            x22 = self.x22
        elif isinstance(self.x22, int):
            x22 = types.IntegerOrJump(self.x22)
        elif isinstance(self.x22, str):
            x22 = types.IntegerOrJump.from_mcnp(self.x22)

        if isinstance(self.x23, types.Integer):
            x23 = self.x23
        elif isinstance(self.x23, int):
            x23 = types.IntegerOrJump(self.x23)
        elif isinstance(self.x23, str):
            x23 = types.IntegerOrJump.from_mcnp(self.x23)

        if isinstance(self.x24, types.Integer):
            x24 = self.x24
        elif isinstance(self.x24, int):
            x24 = types.IntegerOrJump(self.x24)
        elif isinstance(self.x24, str):
            x24 = types.IntegerOrJump.from_mcnp(self.x24)

        if isinstance(self.x25, types.Integer):
            x25 = self.x25
        elif isinstance(self.x25, int):
            x25 = types.IntegerOrJump(self.x25)
        elif isinstance(self.x25, str):
            x25 = types.IntegerOrJump.from_mcnp(self.x25)

        if isinstance(self.x26, types.Integer):
            x26 = self.x26
        elif isinstance(self.x26, int):
            x26 = types.IntegerOrJump(self.x26)
        elif isinstance(self.x26, str):
            x26 = types.IntegerOrJump.from_mcnp(self.x26)

        if isinstance(self.x27, types.Integer):
            x27 = self.x27
        elif isinstance(self.x27, int):
            x27 = types.IntegerOrJump(self.x27)
        elif isinstance(self.x27, str):
            x27 = types.IntegerOrJump.from_mcnp(self.x27)

        if isinstance(self.x28, types.Integer):
            x28 = self.x28
        elif isinstance(self.x28, int):
            x28 = types.IntegerOrJump(self.x28)
        elif isinstance(self.x28, str):
            x28 = types.IntegerOrJump.from_mcnp(self.x28)

        if isinstance(self.x29, types.Integer):
            x29 = self.x29
        elif isinstance(self.x29, int):
            x29 = types.IntegerOrJump(self.x29)
        elif isinstance(self.x29, str):
            x29 = types.IntegerOrJump.from_mcnp(self.x29)

        if isinstance(self.x30, types.Integer):
            x30 = self.x30
        elif isinstance(self.x30, int):
            x30 = types.IntegerOrJump(self.x30)
        elif isinstance(self.x30, str):
            x30 = types.IntegerOrJump.from_mcnp(self.x30)

        if isinstance(self.x31, types.Integer):
            x31 = self.x31
        elif isinstance(self.x31, int):
            x31 = types.IntegerOrJump(self.x31)
        elif isinstance(self.x31, str):
            x31 = types.IntegerOrJump.from_mcnp(self.x31)

        if isinstance(self.x32, types.Integer):
            x32 = self.x32
        elif isinstance(self.x32, int):
            x32 = types.IntegerOrJump(self.x32)
        elif isinstance(self.x32, str):
            x32 = types.IntegerOrJump.from_mcnp(self.x32)

        if isinstance(self.x33, types.Integer):
            x33 = self.x33
        elif isinstance(self.x33, int):
            x33 = types.IntegerOrJump(self.x33)
        elif isinstance(self.x33, str):
            x33 = types.IntegerOrJump.from_mcnp(self.x33)

        if isinstance(self.x34, types.Integer):
            x34 = self.x34
        elif isinstance(self.x34, int):
            x34 = types.IntegerOrJump(self.x34)
        elif isinstance(self.x34, str):
            x34 = types.IntegerOrJump.from_mcnp(self.x34)

        if isinstance(self.x35, types.Integer):
            x35 = self.x35
        elif isinstance(self.x35, int):
            x35 = types.IntegerOrJump(self.x35)
        elif isinstance(self.x35, str):
            x35 = types.IntegerOrJump.from_mcnp(self.x35)

        if isinstance(self.x36, types.Integer):
            x36 = self.x36
        elif isinstance(self.x36, int):
            x36 = types.IntegerOrJump(self.x36)
        elif isinstance(self.x36, str):
            x36 = types.IntegerOrJump.from_mcnp(self.x36)

        if isinstance(self.x37, types.Integer):
            x37 = self.x37
        elif isinstance(self.x37, int):
            x37 = types.IntegerOrJump(self.x37)
        elif isinstance(self.x37, str):
            x37 = types.IntegerOrJump.from_mcnp(self.x37)

        if isinstance(self.x38, types.Integer):
            x38 = self.x38
        elif isinstance(self.x38, int):
            x38 = types.IntegerOrJump(self.x38)
        elif isinstance(self.x38, str):
            x38 = types.IntegerOrJump.from_mcnp(self.x38)

        if isinstance(self.x39, types.Integer):
            x39 = self.x39
        elif isinstance(self.x39, int):
            x39 = types.IntegerOrJump(self.x39)
        elif isinstance(self.x39, str):
            x39 = types.IntegerOrJump.from_mcnp(self.x39)

        if isinstance(self.x40, types.Integer):
            x40 = self.x40
        elif isinstance(self.x40, int):
            x40 = types.IntegerOrJump(self.x40)
        elif isinstance(self.x40, str):
            x40 = types.IntegerOrJump.from_mcnp(self.x40)

        if isinstance(self.x41, types.Integer):
            x41 = self.x41
        elif isinstance(self.x41, int):
            x41 = types.IntegerOrJump(self.x41)
        elif isinstance(self.x41, str):
            x41 = types.IntegerOrJump.from_mcnp(self.x41)

        if isinstance(self.x42, types.Integer):
            x42 = self.x42
        elif isinstance(self.x42, int):
            x42 = types.IntegerOrJump(self.x42)
        elif isinstance(self.x42, str):
            x42 = types.IntegerOrJump.from_mcnp(self.x42)

        if isinstance(self.x43, types.Integer):
            x43 = self.x43
        elif isinstance(self.x43, int):
            x43 = types.IntegerOrJump(self.x43)
        elif isinstance(self.x43, str):
            x43 = types.IntegerOrJump.from_mcnp(self.x43)

        if isinstance(self.x44, types.Integer):
            x44 = self.x44
        elif isinstance(self.x44, int):
            x44 = types.IntegerOrJump(self.x44)
        elif isinstance(self.x44, str):
            x44 = types.IntegerOrJump.from_mcnp(self.x44)

        if isinstance(self.x45, types.Integer):
            x45 = self.x45
        elif isinstance(self.x45, int):
            x45 = types.IntegerOrJump(self.x45)
        elif isinstance(self.x45, str):
            x45 = types.IntegerOrJump.from_mcnp(self.x45)

        if isinstance(self.x46, types.Integer):
            x46 = self.x46
        elif isinstance(self.x46, int):
            x46 = types.IntegerOrJump(self.x46)
        elif isinstance(self.x46, str):
            x46 = types.IntegerOrJump.from_mcnp(self.x46)

        if isinstance(self.x47, types.Integer):
            x47 = self.x47
        elif isinstance(self.x47, int):
            x47 = types.IntegerOrJump(self.x47)
        elif isinstance(self.x47, str):
            x47 = types.IntegerOrJump.from_mcnp(self.x47)

        if isinstance(self.x48, types.Integer):
            x48 = self.x48
        elif isinstance(self.x48, int):
            x48 = types.IntegerOrJump(self.x48)
        elif isinstance(self.x48, str):
            x48 = types.IntegerOrJump.from_mcnp(self.x48)

        if isinstance(self.x49, types.Integer):
            x49 = self.x49
        elif isinstance(self.x49, int):
            x49 = types.IntegerOrJump(self.x49)
        elif isinstance(self.x49, str):
            x49 = types.IntegerOrJump.from_mcnp(self.x49)

        if isinstance(self.x50, types.Integer):
            x50 = self.x50
        elif isinstance(self.x50, int):
            x50 = types.IntegerOrJump(self.x50)
        elif isinstance(self.x50, str):
            x50 = types.IntegerOrJump.from_mcnp(self.x50)

        if isinstance(self.x51, types.Integer):
            x51 = self.x51
        elif isinstance(self.x51, int):
            x51 = types.IntegerOrJump(self.x51)
        elif isinstance(self.x51, str):
            x51 = types.IntegerOrJump.from_mcnp(self.x51)

        if isinstance(self.x52, types.Integer):
            x52 = self.x52
        elif isinstance(self.x52, int):
            x52 = types.IntegerOrJump(self.x52)
        elif isinstance(self.x52, str):
            x52 = types.IntegerOrJump.from_mcnp(self.x52)

        if isinstance(self.x53, types.Integer):
            x53 = self.x53
        elif isinstance(self.x53, int):
            x53 = types.IntegerOrJump(self.x53)
        elif isinstance(self.x53, str):
            x53 = types.IntegerOrJump.from_mcnp(self.x53)

        if isinstance(self.x54, types.Integer):
            x54 = self.x54
        elif isinstance(self.x54, int):
            x54 = types.IntegerOrJump(self.x54)
        elif isinstance(self.x54, str):
            x54 = types.IntegerOrJump.from_mcnp(self.x54)

        if isinstance(self.x55, types.Integer):
            x55 = self.x55
        elif isinstance(self.x55, int):
            x55 = types.IntegerOrJump(self.x55)
        elif isinstance(self.x55, str):
            x55 = types.IntegerOrJump.from_mcnp(self.x55)

        if isinstance(self.x56, types.Integer):
            x56 = self.x56
        elif isinstance(self.x56, int):
            x56 = types.IntegerOrJump(self.x56)
        elif isinstance(self.x56, str):
            x56 = types.IntegerOrJump.from_mcnp(self.x56)

        if isinstance(self.x57, types.Integer):
            x57 = self.x57
        elif isinstance(self.x57, int):
            x57 = types.IntegerOrJump(self.x57)
        elif isinstance(self.x57, str):
            x57 = types.IntegerOrJump.from_mcnp(self.x57)

        if isinstance(self.x58, types.Integer):
            x58 = self.x58
        elif isinstance(self.x58, int):
            x58 = types.IntegerOrJump(self.x58)
        elif isinstance(self.x58, str):
            x58 = types.IntegerOrJump.from_mcnp(self.x58)

        if isinstance(self.x59, types.Integer):
            x59 = self.x59
        elif isinstance(self.x59, int):
            x59 = types.IntegerOrJump(self.x59)
        elif isinstance(self.x59, str):
            x59 = types.IntegerOrJump.from_mcnp(self.x59)

        if isinstance(self.x60, types.Integer):
            x60 = self.x60
        elif isinstance(self.x60, int):
            x60 = types.IntegerOrJump(self.x60)
        elif isinstance(self.x60, str):
            x60 = types.IntegerOrJump.from_mcnp(self.x60)

        if isinstance(self.x61, types.Integer):
            x61 = self.x61
        elif isinstance(self.x61, int):
            x61 = types.IntegerOrJump(self.x61)
        elif isinstance(self.x61, str):
            x61 = types.IntegerOrJump.from_mcnp(self.x61)

        if isinstance(self.x62, types.Integer):
            x62 = self.x62
        elif isinstance(self.x62, int):
            x62 = types.IntegerOrJump(self.x62)
        elif isinstance(self.x62, str):
            x62 = types.IntegerOrJump.from_mcnp(self.x62)

        if isinstance(self.x63, types.Integer):
            x63 = self.x63
        elif isinstance(self.x63, int):
            x63 = types.IntegerOrJump(self.x63)
        elif isinstance(self.x63, str):
            x63 = types.IntegerOrJump.from_mcnp(self.x63)

        if isinstance(self.x64, types.Integer):
            x64 = self.x64
        elif isinstance(self.x64, int):
            x64 = types.IntegerOrJump(self.x64)
        elif isinstance(self.x64, str):
            x64 = types.IntegerOrJump.from_mcnp(self.x64)

        if isinstance(self.x65, types.Integer):
            x65 = self.x65
        elif isinstance(self.x65, int):
            x65 = types.IntegerOrJump(self.x65)
        elif isinstance(self.x65, str):
            x65 = types.IntegerOrJump.from_mcnp(self.x65)

        if isinstance(self.x66, types.Integer):
            x66 = self.x66
        elif isinstance(self.x66, int):
            x66 = types.IntegerOrJump(self.x66)
        elif isinstance(self.x66, str):
            x66 = types.IntegerOrJump.from_mcnp(self.x66)

        if isinstance(self.x67, types.Integer):
            x67 = self.x67
        elif isinstance(self.x67, int):
            x67 = types.IntegerOrJump(self.x67)
        elif isinstance(self.x67, str):
            x67 = types.IntegerOrJump.from_mcnp(self.x67)

        if isinstance(self.x68, types.Integer):
            x68 = self.x68
        elif isinstance(self.x68, int):
            x68 = types.IntegerOrJump(self.x68)
        elif isinstance(self.x68, str):
            x68 = types.IntegerOrJump.from_mcnp(self.x68)

        if isinstance(self.x69, types.Integer):
            x69 = self.x69
        elif isinstance(self.x69, int):
            x69 = types.IntegerOrJump(self.x69)
        elif isinstance(self.x69, str):
            x69 = types.IntegerOrJump.from_mcnp(self.x69)

        if isinstance(self.x70, types.Integer):
            x70 = self.x70
        elif isinstance(self.x70, int):
            x70 = types.IntegerOrJump(self.x70)
        elif isinstance(self.x70, str):
            x70 = types.IntegerOrJump.from_mcnp(self.x70)

        if isinstance(self.x71, types.Integer):
            x71 = self.x71
        elif isinstance(self.x71, int):
            x71 = types.IntegerOrJump(self.x71)
        elif isinstance(self.x71, str):
            x71 = types.IntegerOrJump.from_mcnp(self.x71)

        if isinstance(self.x72, types.Integer):
            x72 = self.x72
        elif isinstance(self.x72, int):
            x72 = types.IntegerOrJump(self.x72)
        elif isinstance(self.x72, str):
            x72 = types.IntegerOrJump.from_mcnp(self.x72)

        if isinstance(self.x73, types.Integer):
            x73 = self.x73
        elif isinstance(self.x73, int):
            x73 = types.IntegerOrJump(self.x73)
        elif isinstance(self.x73, str):
            x73 = types.IntegerOrJump.from_mcnp(self.x73)

        if isinstance(self.x74, types.Integer):
            x74 = self.x74
        elif isinstance(self.x74, int):
            x74 = types.IntegerOrJump(self.x74)
        elif isinstance(self.x74, str):
            x74 = types.IntegerOrJump.from_mcnp(self.x74)

        if isinstance(self.x75, types.Integer):
            x75 = self.x75
        elif isinstance(self.x75, int):
            x75 = types.IntegerOrJump(self.x75)
        elif isinstance(self.x75, str):
            x75 = types.IntegerOrJump.from_mcnp(self.x75)

        if isinstance(self.x76, types.Integer):
            x76 = self.x76
        elif isinstance(self.x76, int):
            x76 = types.IntegerOrJump(self.x76)
        elif isinstance(self.x76, str):
            x76 = types.IntegerOrJump.from_mcnp(self.x76)

        if isinstance(self.x77, types.Integer):
            x77 = self.x77
        elif isinstance(self.x77, int):
            x77 = types.IntegerOrJump(self.x77)
        elif isinstance(self.x77, str):
            x77 = types.IntegerOrJump.from_mcnp(self.x77)

        if isinstance(self.x78, types.Integer):
            x78 = self.x78
        elif isinstance(self.x78, int):
            x78 = types.IntegerOrJump(self.x78)
        elif isinstance(self.x78, str):
            x78 = types.IntegerOrJump.from_mcnp(self.x78)

        if isinstance(self.x79, types.Integer):
            x79 = self.x79
        elif isinstance(self.x79, int):
            x79 = types.IntegerOrJump(self.x79)
        elif isinstance(self.x79, str):
            x79 = types.IntegerOrJump.from_mcnp(self.x79)

        if isinstance(self.x80, types.Integer):
            x80 = self.x80
        elif isinstance(self.x80, int):
            x80 = types.IntegerOrJump(self.x80)
        elif isinstance(self.x80, str):
            x80 = types.IntegerOrJump.from_mcnp(self.x80)

        if isinstance(self.x81, types.Integer):
            x81 = self.x81
        elif isinstance(self.x81, int):
            x81 = types.IntegerOrJump(self.x81)
        elif isinstance(self.x81, str):
            x81 = types.IntegerOrJump.from_mcnp(self.x81)

        if isinstance(self.x82, types.Integer):
            x82 = self.x82
        elif isinstance(self.x82, int):
            x82 = types.IntegerOrJump(self.x82)
        elif isinstance(self.x82, str):
            x82 = types.IntegerOrJump.from_mcnp(self.x82)

        if isinstance(self.x83, types.Integer):
            x83 = self.x83
        elif isinstance(self.x83, int):
            x83 = types.IntegerOrJump(self.x83)
        elif isinstance(self.x83, str):
            x83 = types.IntegerOrJump.from_mcnp(self.x83)

        if isinstance(self.x84, types.Integer):
            x84 = self.x84
        elif isinstance(self.x84, int):
            x84 = types.IntegerOrJump(self.x84)
        elif isinstance(self.x84, str):
            x84 = types.IntegerOrJump.from_mcnp(self.x84)

        if isinstance(self.x85, types.Integer):
            x85 = self.x85
        elif isinstance(self.x85, int):
            x85 = types.IntegerOrJump(self.x85)
        elif isinstance(self.x85, str):
            x85 = types.IntegerOrJump.from_mcnp(self.x85)

        if isinstance(self.x86, types.Integer):
            x86 = self.x86
        elif isinstance(self.x86, int):
            x86 = types.IntegerOrJump(self.x86)
        elif isinstance(self.x86, str):
            x86 = types.IntegerOrJump.from_mcnp(self.x86)

        if isinstance(self.x87, types.Integer):
            x87 = self.x87
        elif isinstance(self.x87, int):
            x87 = types.IntegerOrJump(self.x87)
        elif isinstance(self.x87, str):
            x87 = types.IntegerOrJump.from_mcnp(self.x87)

        if isinstance(self.x88, types.Integer):
            x88 = self.x88
        elif isinstance(self.x88, int):
            x88 = types.IntegerOrJump(self.x88)
        elif isinstance(self.x88, str):
            x88 = types.IntegerOrJump.from_mcnp(self.x88)

        if isinstance(self.x89, types.Integer):
            x89 = self.x89
        elif isinstance(self.x89, int):
            x89 = types.IntegerOrJump(self.x89)
        elif isinstance(self.x89, str):
            x89 = types.IntegerOrJump.from_mcnp(self.x89)

        if isinstance(self.x90, types.Integer):
            x90 = self.x90
        elif isinstance(self.x90, int):
            x90 = types.IntegerOrJump(self.x90)
        elif isinstance(self.x90, str):
            x90 = types.IntegerOrJump.from_mcnp(self.x90)

        if isinstance(self.x91, types.Integer):
            x91 = self.x91
        elif isinstance(self.x91, int):
            x91 = types.IntegerOrJump(self.x91)
        elif isinstance(self.x91, str):
            x91 = types.IntegerOrJump.from_mcnp(self.x91)

        if isinstance(self.x92, types.Integer):
            x92 = self.x92
        elif isinstance(self.x92, int):
            x92 = types.IntegerOrJump(self.x92)
        elif isinstance(self.x92, str):
            x92 = types.IntegerOrJump.from_mcnp(self.x92)

        if isinstance(self.x93, types.Integer):
            x93 = self.x93
        elif isinstance(self.x93, int):
            x93 = types.IntegerOrJump(self.x93)
        elif isinstance(self.x93, str):
            x93 = types.IntegerOrJump.from_mcnp(self.x93)

        if isinstance(self.x94, types.Integer):
            x94 = self.x94
        elif isinstance(self.x94, int):
            x94 = types.IntegerOrJump(self.x94)
        elif isinstance(self.x94, str):
            x94 = types.IntegerOrJump.from_mcnp(self.x94)

        if isinstance(self.x95, types.Integer):
            x95 = self.x95
        elif isinstance(self.x95, int):
            x95 = types.IntegerOrJump(self.x95)
        elif isinstance(self.x95, str):
            x95 = types.IntegerOrJump.from_mcnp(self.x95)

        if isinstance(self.x96, types.Integer):
            x96 = self.x96
        elif isinstance(self.x96, int):
            x96 = types.IntegerOrJump(self.x96)
        elif isinstance(self.x96, str):
            x96 = types.IntegerOrJump.from_mcnp(self.x96)

        if isinstance(self.x97, types.Integer):
            x97 = self.x97
        elif isinstance(self.x97, int):
            x97 = types.IntegerOrJump(self.x97)
        elif isinstance(self.x97, str):
            x97 = types.IntegerOrJump.from_mcnp(self.x97)

        if isinstance(self.x98, types.Integer):
            x98 = self.x98
        elif isinstance(self.x98, int):
            x98 = types.IntegerOrJump(self.x98)
        elif isinstance(self.x98, str):
            x98 = types.IntegerOrJump.from_mcnp(self.x98)

        if isinstance(self.x99, types.Integer):
            x99 = self.x99
        elif isinstance(self.x99, int):
            x99 = types.IntegerOrJump(self.x99)
        elif isinstance(self.x99, str):
            x99 = types.IntegerOrJump.from_mcnp(self.x99)

        if isinstance(self.x100, types.Integer):
            x100 = self.x100
        elif isinstance(self.x100, int):
            x100 = types.IntegerOrJump(self.x100)
        elif isinstance(self.x100, str):
            x100 = types.IntegerOrJump.from_mcnp(self.x100)

        return Dbcn(
            x1=x1,
            x2=x2,
            x3=x3,
            x4=x4,
            x5=x5,
            x6=x6,
            x7=x7,
            x8=x8,
            x9=x9,
            x10=x10,
            x11=x11,
            x12=x12,
            x13=x13,
            x14=x14,
            x15=x15,
            x16=x16,
            x17=x17,
            x18=x18,
            x19=x19,
            x20=x20,
            x21=x21,
            x22=x22,
            x23=x23,
            x24=x24,
            x25=x25,
            x26=x26,
            x27=x27,
            x28=x28,
            x29=x29,
            x30=x30,
            x31=x31,
            x32=x32,
            x33=x33,
            x34=x34,
            x35=x35,
            x36=x36,
            x37=x37,
            x38=x38,
            x39=x39,
            x40=x40,
            x41=x41,
            x42=x42,
            x43=x43,
            x44=x44,
            x45=x45,
            x46=x46,
            x47=x47,
            x48=x48,
            x49=x49,
            x50=x50,
            x51=x51,
            x52=x52,
            x53=x53,
            x54=x54,
            x55=x55,
            x56=x56,
            x57=x57,
            x58=x58,
            x59=x59,
            x60=x60,
            x61=x61,
            x62=x62,
            x63=x63,
            x64=x64,
            x65=x65,
            x66=x66,
            x67=x67,
            x68=x68,
            x69=x69,
            x70=x70,
            x71=x71,
            x72=x72,
            x73=x73,
            x74=x74,
            x75=x75,
            x76=x76,
            x77=x77,
            x78=x78,
            x79=x79,
            x80=x80,
            x81=x81,
            x82=x82,
            x83=x83,
            x84=x84,
            x85=x85,
            x86=x86,
            x87=x87,
            x88=x88,
            x89=x89,
            x90=x90,
            x91=x91,
            x92=x92,
            x93=x93,
            x94=x94,
            x95=x95,
            x96=x96,
            x97=x97,
            x98=x98,
            x99=x99,
            x100=x100,
        )

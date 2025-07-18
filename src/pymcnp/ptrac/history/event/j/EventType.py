from . import _keyword
from ..... import errors


class EventType(_keyword.JKeyword):
    """
    Represents PTRAC event event-types.
    """

    SOURCE = '1000'
    BANK_DXTRAN_TRACK = '2001'
    REJECTED_DXTRAN_TRACK = '-2001'
    BANK_ENERGY_SPLIT = '2002'
    REJECTED_ENERGY_SPLIT = '-2002'
    BANK_WEIGHT_WINDOW_SURFACE_SPLIT = '2003'
    REJECTED_WEIGHT_WINDOW_SURFACE_SPLIT = '-2003'
    BANK_WEIGHT_WINDOW_COLLISION_SPLIT = '2004'
    REJECTED_WEIGHT_WINDOW_COLLISION_SPLIT = '-2004'
    BANK_FORCED_COLLISION_UNCOLLIDED_PART = '2005'
    REJECTED_FORCED_COLLISION_UNCOLLIDED_PART = '-2005'
    BANK_IMPORTANCE_SPLIT = '2006'
    REJECTED_IMPORTANCE_SPLIT = '-2006'
    BANK_NEUTRON_FROM_LIBRARY_PROTONS = '2007'
    REJECTED_NEUTRON_FROM_LIBRARY_PROTONS = '-2007'
    BANK_PHOTON_FROM_NEUTRON = '2008'
    REJECTED_PHOTON_FROM_NEUTRON = '-2008'
    BANK_PHOTON_FROM_DOUBLE_FLUORENSCENE = '2009'
    REJECTED_PHOTON_FROM_DOUBLE_FLUORENSCENE = '-2009'
    BANK_PHOTON_FROM_ANNIHILATION = '2010'
    REJECTED_PHOTON_FROM_ANNIHILATION = '-2010'
    BANK_ELECTRON_FROM_PHOTOELECTRIC = '2011'
    REJECTED_ELECTRON_FROM_PHOTOELECTRIC = '-2011'
    BANK_ELECTRON_FROM_COMPTON = '2012'
    REJECTED_ELECTRON_FROM_COMPTON = '-2012'
    BANK_ELECTRON_FROM_PAIR_PRODUCTION = '2013'
    REJECTED_ELECTRON_FROM_PAIR_PRODUCTION = '-2013'
    BANK_AUGER_ELECTRON_FROM_PHOTON = '2014'
    REJECTED_AUGER_ELECTRON_FROM_PHOTON = '-2014'
    BANK_POSITRON_FROM_PAIR_PRODUCTION = '2015'
    REJECTED_POSITRON_FROM_PAIR_PRODUCTION = '-2015'
    BANK_BREMSSTRAHLUNG_FROM_ELECTRON = '2016'
    REJECTED_BREMSSTRAHLUNG_FROM_ELECTRON = '-2016'
    BANK_KNOCK_ON_ELECTRON = '2017'
    REJECTED_KNOCK_ON_ELECTRON = '-2017'
    BANK_PHOTON_FROM_ELECTRON = '2018'
    REJECTED_PHOTON_FROM_ELECTRON = '-2018'
    BANK_PHOTON_FROM_NEUTRON_MULTIGROUP = '2019'
    REJECTED_PHOTON_FROM_NEUTRON_MULTIGROUP = '-2019'
    BANK_NEUTRON_MULTIGROUP = '2020'
    REJECTED_NEUTRON_MULTIGROUP = '-2020'
    BANK_NEUTRON_K_MULTIGROUP = '2021'
    REJECTED_NEUTRON_K_MULTIGROUP = '-2021'
    BANK_PHOTO_FROM_PHOTON_MULTIGROUP = '2022'
    REJECTED_PHOTO_FROM_PHOTON_MULTIGROUP = '-2022'
    BANK_ADJOINT_WEIGHT_SPLIT_MULTIGROUP = '2023'
    REJECTED_ADJOINT_WEIGHT_SPLIT_MULTIGROUP = '-2023'
    BANK_WEIGHT_WINDOW_PSEUDO_COLLISION_SPLIT = '2024'
    REJECTED_WEIGHT_WINDOW_PSEUDO_COLLISION_SPLIT = '-2024'
    BANK_SECONDARIES_FROM_PHOTONUCLEAR = '2025'
    REJECTED_SECONDARIES_FROM_PHOTONUCLEAR = '-2025'
    BANK_DXTRAN_ANNIHILATION_PHOTON = '2026'
    REJECTED_DXTRAN_ANNIHILATION_PHOTON = '-2026'
    BANK_LIGHT_IONS_FROM_NEUTRONS = '2030'
    REJECTED_LIGHT_IONS_FROM_NEUTRONS = '-2030'
    BANK_LIGHT_IONS_FROM_PROTONS = '2031'
    REJECTED_LIGHT_IONS_FROM_PROTONS = '-2031'
    BANK_LIBRARY_NEUTRONS_FROM_MODEL_NETURONS = '2032'
    REJECTED_LIBRARY_NEUTRONS_FROM_MODEL_NETURONS = '-2032'
    BANK_SECONDARIES_FROM_INELASTIC_INTERACTIONS = '2033'
    REJECTED_SECONDARIES_FROM_INELASTIC_INTERACTIONS = '-2033'
    BANK_SECONARIES_FORM_ELASTIC_INTERACTIONS = '2034'
    REJECTED_SECONARIES_FORM_ELASTIC_INTERACTIONS = '-2034'
    SURFACE = '3000'
    COLLISION = '4000'
    TERMINAL = '5000'
    FLAG = '9000'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EventType`` from PTRAC.

        Parameters:
            source: PTRAC for ``EventType``.

        Returns:
            ``EventType``.

        Raises:
            PtracError: SYNTAX_KEYWORD.
        """

        try:
            return EventType(source)
        except ValueError:
            raise errors.PtracError(errors.PtracCode.SYNTAX_KEYWORD, source)

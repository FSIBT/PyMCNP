"""
'types'
"""


from __future__ import annotations
import re
from enum import StrEnum
from typing import Callable

ELEMENTS = {
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    "Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20,
    "Sc": 21,
    "Ti": 22,
    "V": 23,
    "Cr": 24,
    "Mn": 25,
    "Fe": 26,
    "Co": 27,
    "Ni": 28,
    "Cu": 29,
    "Zn": 30,
    "Ga": 31,
    "Ge": 32,
    "As": 33,
    "Se": 34,
    "Br": 35,
    "Kr": 36,
    "Rb": 37,
    "Sr": 38,
    "Y": 39,
    "Zr": 40,
    "Nb": 41,
    "Mo": 42,
    "Tc": 43,
    "Ru": 44,
    "Rh": 45,
    "Rd": 46,
    "Ag": 47,
    "Cd": 48,
    "In": 49,
    "Sn": 50,
    "Sb": 51,
    "Te": 52,
    "I": 53,
    "Xe": 54,
    "Cs": 55,
    "Ba": 56,
    "La": 57,
    "Ce": 58,
    "Pr": 59,
    "Nd": 60,
    "Pm": 61,
    "Sm": 62,
    "Eu": 63,
    "Gd": 64,
    "Tb": 65,
    "Dy": 66,
    "Ho": 67,
    "Er": 68,
    "Tm": 69,
    "Yb": 70,
    "Lu": 71,
    "Hf": 72,
    "Ta": 73,
    "W": 74,
    "Re": 75,
    "Os": 76,
    "Ir": 77,
    "Pt": 78,
    "Au": 79,
    "Hg": 80,
    "Tl": 81,
    "Pb": 82,
    "Bi": 83,
    "Po": 84,
    "At": 85,
    "Rn": 86,
    "Fr": 87,
    "Ra": 88,
    "Ac": 89,
    "Th": 90,
    "Pa": 91,
    "U": 92,
    "Np": 93,
    "Pu": 94,
    "Am": 95,
    "Cm": 96,
    "Bk": 97,
    "Cf": 98,
    "Es": 99,
    "Fm": 100,
    "Md": 101,
    "No": 102,
    "Lr": 103,
    "Rf": 104,
    "Db": 105,
    "Sg": 106,
    "Bh": 107,
    "Hs": 108,
    "Mt": 109,
    "Ds": 110,
    "Rg": 111,
    "Cn": 112,
    "Nh": 113,
    "Fl": 114,
    "Mc": 115,
    "Lv": 116,
    "Ts": 117,
    "Og": 118,
}

ELEMENTS_PATTERN = re.compile(
    r"\d+|H|He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca|Sc|Ti|V|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Y|Zr|Nb|Mo|Tc|Ru|Rh|Rd|Ag|Cd|In|Sn|Sb|Te|I|Xe|Cs|Ba|La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy|Ho|Er|Tm|Yb|Lu|Hf|Ta|W|Re|Os|Ir|Pt|Au|Hg|Tl|Pb|Bi|Po|At|Rn|Fr|Ra|Ac|Th|Pa|U|Np|Pu|Am|Cm|Bk|Cf|Es|Fm|Md|No|Lr|Rf|Db|Sg|Bh|Hs|Mt|Ds|Rg|Cn|Nh|Fl|Mc|Lv|Ts|Og"
)
Z_PATTERN = re.compile(r"\A[+-]?[0-9]+\Z")
R_PATTERN = re.compile(r"\A[+-]?(([0-9]+)|([0-9]+[.][0-9]*)|([.][0-9]+))([Ee]([+-][0-9]+))?\Z")


def cast_fortran_integer(string: str, hook: Callable[int, bool] = lambda _: True) -> int:
    """
    'cast_fortran_integer'
    """

    if Z_PATTERN.match(string) is not None:
        value = int(string)
        if hook(value):
            return value

    return None


def cast_fortran_real(string: str, hook: Callable[float, bool] = lambda _: True) -> float:
    """
    'cast_fortran_real'
    """

    if R_PATTERN.match(string) is not None:
        value = float(string)
        if hook(value):
            return value

    return None


class Zaid:
    """
    'Zaid'
    """

    def __init__(self):
        """
        '__init__' initializes 'Zaid'.
        """

        self.z: int = None
        self.a: int = None
        self.abx: str = None

    @classmethod
    def cast_mcnp_zaid(cls, string: str, hook: Callable[Zaid, bool] = lambda _: True):
        """
        'cast_mcnp_zaid'
        """

        string = string.lower()

        try:
            if "." in string:
                zaid.abx = string[-3:]
                string = string[:-4]

            zaid.a = int(string[-3:-1])
            zaid.z = int(string[:-3])

            if hook(zaid):
                return zaid

        except IndexError:
            pass

        return None


class Designator(StrEnum):
    """
    'Designator'
    """

    NEUTRON = "n"
    ANTI_NEUTRON = "q"
    PHOTON = "p"
    ELECTRON = "e"
    POSITRON = "f"
    NEGATIVE_MUON = "|"
    POSITIVE_MUON = "!"
    ELECTRON_NEUTRINO = "u"
    ANTI_ELECTRON_NEUTRINO = "<"
    MUON_NEUTRINO = "v"
    ANTI_MUON_MEUTRINO = ">"
    PROTON = "h"
    ANTI_PROTON = "g"
    LAMBDA_BARYON = "l"
    ANTI_LAMBDA_BARYON = "b"
    POSITIVE_SIGMA_BARYON = "+"
    ANTI_POSITIVE_SIGMA_BARYON = "_"
    NEGATIVE_SIGMA_BARYON = "-"
    ANTI_NEGATIVE_SIGMA_BARYON = "~"
    CASCADE = "x"
    ANTI_CASCADE = "c"
    NEGATIVE_CASCADE = "y"
    POSITIVE_CASCADE = "w"
    OMEGA_BARYON = "o"
    ANTI_OMEGA_BARYON = "@"
    POSITIVE_PION = "/"
    NEGATIVE_PION = "*"
    NEUTRAL_PION = "z"
    POSITIVE_KAON = "k"
    NEGATIVE_KAON = "?"
    SHORT_KAON = "%"
    LONG_KAON = "^"
    DEUTERON = "d"
    TRITON = "t"
    HELION = "s"
    ALPHA = "a"
    HEAVY_IONS = "#"

    @classmethod
    def cast_mcnp_designator(cls, string: str, hook: Callable[Designator, bool] = lambda _: True) -> tuple[Designator]:
        """
        'cast_mcnp_designator'
        """

        string = string.lower()

        designators = []

        for substring in string.split(","):
            try:
                value = designators.append(cls(substring))
                if hook(value):
                    return tuple(designators) if designators else None
            except ValueError:
                pass

        return None

"""
Define elements and materials made out of elements.

"""

from typing import Optional, List

from ..input_line import InputLine


class Element:
    def __init__(
        self,
        Z: int,
        A: int,
        fraction: float,
        library: Optional[str] = None,
    ):
        self.Z = Z
        self.A = A
        self.fraction = fraction

        self.library = library

    def to_mcnp(self):
        if self.library is None:
            return f"{self.Z}{self.A:03d} {self.fraction} "

        return f"{self.Z}{self.A:03d}.{self.library} {self.fraction} "

    @classmethod
    def from_mcnp(cls, ZZZAAA: str, fraction: str):
        tmp = ZZZAAA.split(".")
        if len(tmp) == 2:
            ZA = tmp[0]
            library = tmp[1]
        else:
            ZA = tmp[0]
            library = None
        Z = int(ZA[:-3])
        A = int(ZA[-3:])
        fraction = float(fraction)
        return cls(Z, A, fraction, library)

    @classmethod
    def is_element(cls, ZZZAAA: str) -> bool:
        tmp = ZZZAAA.split(".")
        ZA = tmp[0]
        Z = ZA[:-3]
        A = ZA[-3:]

        if Z.isnumeric() and Z.isnumeric():
            return True
        return False

    def __str__(self):
        l = self.library
        f = self.fraction
        if f > 0:
            unit = "atomic fraction"
        else:
            unit = "weight fraction"

        out = f"Element: Z={self.Z:3d} A={self.A:3d} fraction={abs(f)} {unit}"
        if l:
            out += "library={l}\n"
        else:
            out += "\n"
        return out


class Material:
    all_materials = []

    def __init__(
        self,
        elements: List[Element],
        id=None,
        comment: Optional[str] = None,
    ):
        self.id = id
        self.elements = elements
        self.comment = comment

    def get_new_id(self):
        """Return the smallest unused id"""
        existing_ids = self.get_all_material_ids()
        for i in range(1, 99_999_999):
            if i not in existing_ids:
                return i

    def to_mcnp(self):
        out = f"m{self.id}"
        for e in self.elements:
            out += " " + e.to_mcnp()
        out = out.strip()
        if self.comment:
            out += f" $ {self.comment}"
        return out + "\n"

    @classmethod
    def from_mcnp(cls, line: InputLine):
        # skip m
        line.text = line.text[1:]
        comment = line.comment

        values = line.text.split()
        id = values[0]
        elements = []
        for za, f in zip(values[1::2], values[2::2]):
            if not Element.is_element(za):
                break
            e = Element.from_mcnp(za, f)
            elements.append(e)

        return cls(id=id, elements=elements, comment=comment)

    @classmethod
    def get_all_materials(cls):
        return cls.all_materials

    @classmethod
    def get_all_material_ids(cls):
        return [x.id for x in cls.all_materialss()]

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        out = f"Material {self.id}{comment}:\n"
        for element in self.elements:
            out += f"   {element}"

        return out

"""
Define elements and materials made out of elements.

"""

from typing import Optional, List


class Element:
    def __init__(self, Z: int, A: int, fraction: float, library: Optional[str] = None):
        self.Z = Z
        self.A = A
        self.fraction = fraction

        self.library = library

    def to_mcnp(self):
        return f"{self.Z}{self.A:03d} {self.fraction}"

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

    def __init__(self, elements: List[Element], id=None):
        self.id = id
        self.elements = elements

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
        return out

    @classmethod
    def from_mcnp(cls, line: str):
        # skip m
        line = line[1:]
        values = line.split()
        id = values[0]
        elements = []
        for za, f in zip(values[1::2], values[2::2]):
            if not za.isnumeric():
                break
            e = Element.from_mcnp(za, f)
            elements.append(e)

        return cls(id=id, elements=elements)

    @classmethod
    def get_all_materials(cls):
        return cls.all_materials

    @classmethod
    def get_all_material_ids(cls):
        return [x.id for x in cls.all_materialss()]

    def __str__(self):
        out = f"Material {self.id}:\n"
        for element in self.elements:
            out += f"   {element}"

        return out

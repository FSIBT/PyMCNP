"""A python class to reprsent a single MCNP cell.

Cells are defined by a unique id, material, density, geometry
definitions and extra parameters.

TODO:
* a lot more error checking during parameter parsing
* ability to error check/parse geometry
* add a name as a comment in the output or read it in from an inline comment
* to_mcnp need to check line length of the output (are continuation lines
  allowed in cells?)
"""

from typing import Optional

from rich import print

from ..input_line import InputLine


class Cell:
    """Represent a MCNP cell"""

    all_cells = []

    PARAMETERS = [
        "IMP",
        "VOL",
        "PWT",
        "EXT",
        "FCL",
        "WWN",
        "DXC",
        "NONU",
        "PD",
        "TMP",
        "U",
        "TRCL",
        "LAT",
        "FILL",
        "ELPT",
        "COSY",
        "BFLCL",
        "UNC",
    ]

    def __init__(
        self,
        material: int,
        density: float,
        geometry: str,
        id: Optional[int] = None,
        parameters: Optional[dict] = None,
        comment: Optional[str] = None,
    ):
        if id is None:
            self.id = self.get_new_id()
        else:
            self.id = id
        self.material = material
        self.density = density
        self.geometry = geometry
        if parameters is not None:
            for p in parameters:
                if p not in self.PARAMETERS:
                    print(f"[red]ERROR[/] Cell parameter {p} not allowed.")

        self.parameters = parameters
        self.comment = comment

        self.all_cells.append(self)

    def get_new_id(self):
        """Return the smallest unused id"""
        existing_ids = self.get_all_cell_ids()
        for i in range(1, 99_999_999):
            if i not in existing_ids:
                return i

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        material = self.material if self.material is not None else "0"
        density = self.density if self.density is not None else ""
        out = f"{self.id} {material} {density} {self.geometry} "
        for k, v in self.parameters.items():
            out += f"{k}={v} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        """Currently only support lines where all parameters are given.

        At the moment the line cannot include any comments

        TODO: also parse missing material and density correclty

        """
        components = line.text.split()
        comment = line.comment

        id = int(components[0])
        material = int(components[1])
        density = float(components[2])
        for i, c in enumerate(components):
            for p in cls.PARAMETERS:
                if c.startswith(p):
                    break
        geometry = " ".join(components[3:i])

        parameters = {}
        for c in components[i:]:
            k, v = c.split(":")
            parameters[k] = v
        return cls(
            material=material,
            density=density,
            id=id,
            geometry=geometry,
            parameters=parameters,
            comment=comment,
        )

    @classmethod
    def get_all_cells(cls):
        return cls.all_cells

    @classmethod
    def get_all_cell_ids(cls):
        return [x.id for x in cls.all_cells()]

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Cell {self.id}{comment}:\n"
        out += f"   material = {self.material}\n"

        if self.density > 0:
            unit = "1e24 atoms/cm3"
        else:
            unit = "g/cm3"

        out += f"   density = {self.density} {unit}\n"
        out += f"   geometry = {self.geometry}\n"
        if self.parameters:
            out += "   parameters:\n"
            for k, v in self.parameters.items():
                out += f"      {k} : {v}\n"
        return out

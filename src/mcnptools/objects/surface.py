"""A python class to reprsent a single MCNP surface.

Surfaces are defined by a unique id, a type and parameters.

TODO:
* support more types

"""

from typing import Optional, List

import numpy as np
from rich import print

from ..input_line import InputLine


class Surface:
    """Represent a MCNP surface."""

    all_surfaces = []

    TYPES = ["RPP", "RCC", "SPH", "SO"]

    def __init__(
        self,
        type: str,
        parameters: List[float],
        id: Optional[int] = None,
        comment: Optional[str] = None,
    ):
        if id is None:
            self.id = self.get_new_id()
        else:
            self.id = id

        self.type = type
        self.parameters = parameters
        self.comment = comment

        self.all_surfaces.append(self)

    def get_new_id(self):
        """Return the smallest unused id"""
        existing_ids = self.get_all_cell_ids()
        for i in range(1, 99_999_999):
            if i not in existing_ids:
                return i

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type} "
        out += " ".join(str(x) for x in self.parameters)
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    @classmethod
    def from_mcnp(cls, line):
        """Currently only support lines where all parameters are given.

        At the moment the line cannot include any comments

        """
        components = line.text.split()
        comment = line.comment

        id = int(components[0])
        type = components[1].upper()
        if type not in cls.TYPES:
            print(f"[orange3]Warning[/] {type} not supported at the moment")
        parameters = [float(x) for x in components[2:]]

        if type == "RPP":
            return RPP(id=id, *parameters)
        elif type == "RCC":
            return RCC(id=id, *parameters)
        elif type == "SPH":
            return SPH(id=id, *parameters)
        elif type == "SO":
            return SO(id=id, *parameters)

        return cls(id=id, type=type, parameters=parameters, comment=comment)

    @classmethod
    def get_all_surfacess(cls):
        return cls.all_surfaces

    @classmethod
    def get_all_surface_ids(cls):
        return [x.id for x in cls.all_surfaces()]

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface id={self.id}{comment}:\n"
        out += f"   type = {self.type}\n"

        out += "   parameters:\n"
        out += "      " + " ".join(str(x) for x in self.parameters)
        return out


class RPP(Surface):
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, id: Optional[int] = None):
        super().__init__(
            id=id,
            type="RPP",
            parameters=[xmin, xmax, ymin, ymax, zmin, zmax],
        )

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface RPP id={self.id}{comment}:\n"
        xmin, xmax, ymin, ymax, zmin, zmax = self.parameters
        out += f"    {xmin=} {xmax=}\n"
        out += f"    {ymin=} {ymax=}\n"
        out += f"    {zmin=} {zmax=}\n"

        return out


class RCC(Surface):
    def __init__(self, vx, vy, vz, hx, hy, hz, r, id: Optional[int] = None):
        super().__init__(id=id, type="RCC", parameters=[vx, vy, vz, hx, hy, hz, r])

        self.center = np.array([vx, vy, vz])
        self.direction = np.array([hx, hy, hz])
        self.height = np.linalg.norm(self.direction)
        self.direction = self.direction / self.height
        self.radius = r

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface RCC id={self.id}{comment}:\n"
        vx, vy, vz, hx, hy, hz, r = self.parameters
        out += f"    {vx=} {vy=} {vz=}\n"
        out += f"    {hx=} {hy=} {hz=}\n"
        out += f"    {r=}\n"

        return out


class SPH(Surface):
    def __init__(self, vx, vy, vz, r, id: Optional[int] = None):
        super().__init__(id=id, type="SPH", parameters=[vx, vy, vz, r])

        self.center = np.array([vx, vy, vz])
        self.radius = r

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface SPH id={self.id}{comment}:\n"
        vx, vy, vz, r = self.parameters
        out += f"    {vx=} {vy=} {vz=}\n"
        out += f"    {r=}\n"

        return out


class SO(Surface):
    def __init__(self, r, id: Optional[int] = None):
        super().__init__(id=id, type="SO", parameters=[r])

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface SO id={self.id}{comment}:\n"
        r = self.parameters[0]
        out += f"    {r=}\n"

        return out

"""A python class to reprsent a single MCNP surface.

Surfaces are defined by a unique id, a type and parameters.

For several types, we support specialized classes, for example SO
(sphere at origin), which gets initialized with a radius instead of a
generic parameter array.

All surfaces also have a `'is_detector` flag that gets set by having
the word `detector` in the comment. This can be useful when wanting to
do parameter scans or access locations of all detectors (which can be
accessed by the all_detector class variable.


TODO:
* support more types

"""

from typing import Optional, List

import numpy as np
from rich import print

from ..input_line import InputLine


def detector_hook(self):
    """A custom feature used to identify detector surfaces.

    This hook will add a new property "is_detector" to surfaces that
    will be true if a surface comment includes the word "detector". It
    also will keep a list of all detector surfaces in the class.

    """
    self.is_detector: bool = False
    if self.comment:
        self.is_detector = "detector" in self.comment

    if self.is_detector:
        if "all_detectors" not in self.hook_data:
            self.data["all_detectors"] = []
        self.data["all_detectors"].append(self)


class Surface:
    """Represent a MCNP surface.

    This is also a base class for more specialized classes.

    """

    all_surfaces = []
    # storage space for hooks
    data = {}

    # option to register functions to be called after the init of each instance
    # this can be used to for example scan for custom keywords in the comments
    # one possible us is to mark surfaces as comments
    # hook functions should take the instance as an argument
    _post_init_hooks = []

    TYPES = ["RPP", "RCC", "SPH", "SO", "CX", "CY", "CZ", "PX", "PY", "PZ"]

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
        self.center = None

        self.all_surfaces.append(self)

        for func in self._post_init_hooks:
            func(self)

    @classmethod
    def register_post_init_hook(cls, func):
        cls._post_init_hooks.append(func)

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
    def from_mcnp(cls, line: InputLine):
        """Currently only support lines where all parameters are given.

        At the moment the line cannot include any comments

        """
        components = line.text.split()
        comment = line.comment

        id = int(components[0])
        type = components[1].upper()
        if type not in cls.TYPES:
            print(
                f"[orange3]Warning[/] Surface {type} not supported at the moment. '{line.text}'"
            )
        parameters = [float(x) for x in components[2:]]

        if type == "RPP":
            return RPP(id=id, *parameters, comment=comment)
        elif type == "RCC":
            return RCC(id=id, *parameters, comment=comment)
        elif type == "SPH":
            return SPH(id=id, *parameters, comment=comment)
        elif type == "SO":
            return SO(id=id, *parameters, comment=comment)
        elif type == "CX":
            return CX(id=id, radius=parameters[0], comment=comment)
        elif type == "CY":
            return CY(id=id, radius=parameters[0], comment=comment)
        elif type == "CZ":
            return CZ(id=id, radius=parameters[0], comment=comment)
        elif type == "PX":
            return PX(id=id, distance=parameters[0], comment=comment)
        elif type == "PY":
            return PY(id=id, distance=parameters[0], comment=comment)
        elif type == "PZ":
            return PZ(id=id, distance=parameters[0], comment=comment)

        return cls(id=id, type=type, parameters=parameters, comment=comment)

    @classmethod
    def get_all_surfacess(cls):
        return cls.all_surfaces

    @classmethod
    def get_all_surface_ids(cls):
        return [x.id for x in cls.all_surfaces()]

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface id={self.id}:\n"
        out += f"   type = {self.type}\n"

        out += "    parameters:\n"
        out += "       " + " ".join(str(x) for x in self.parameters)
        return out


class RPP(Surface):
    def __init__(
        self,
        xmin,
        xmax,
        ymin,
        ymax,
        zmin,
        zmax,
        id: Optional[int] = None,
        comment: Optional[str] = None,
    ):
        super().__init__(
            id=id,
            type="RPP",
            parameters=[xmin, xmax, ymin, ymax, zmin, zmax],
            comment=comment,
        )
        self.center = [(xmax - xmin) / 2, (ymax - ymin) / 2, (zmax - zmin) / 2]

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type} "
        out += f"{self.xmin} {self.xmax} "
        out += f"{self.ymin} {self.ymax} "
        out += f"{self.zmin} {self.zmax} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface RPP id={self.id}{comment}:\n"
        xmin, xmax, ymin, ymax, zmin, zmax = self.parameters
        out += f"    {xmin=} {xmax=}\n"
        out += f"    {ymin=} {ymax=}\n"
        out += f"    {zmin=} {zmax=}\n"

        return out


class CX(Surface):
    """Cylinder along x axis."""

    def __init__(self, radius, id: Optional[int] = None, comment: Optional[str] = None):
        super().__init__(id=id, type="CX", parameters=[radius], comment=comment)
        self.radius = radius
        self.center = np.array([0, 0, 0])

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type} {self.radius} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        out = f"{self.name} {comment} radius={self.parameters[0]}"

        return out


class CY(CX):
    """Cylinder along y axis."""

    def __init__(self, radius, id: Optional[int] = None, comment: Optional[str] = None):
        super().__init__(id=id, radius=radius, comment=comment)
        self.type = "CY"


class CZ(CX):
    """Cylinder along z axis."""

    def __init__(self, radius, id: Optional[int] = None, comment: Optional[str] = None):
        super().__init__(id=id, radius=radius, comment=comment)
        self.type = "CZ"


class PX(Surface):
    """Plane normal to x axis."""

    def __init__(
        self, distance, id: Optional[int] = None, comment: Optional[str] = None
    ):
        super().__init__(id=id, type="PX", parameters=[distance], comment=comment)
        self.distance = distance
        self.center = np.array([distance, 0, 0])

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type} {self.distance} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    def __str__(self):
        comment = f" ({self.comment})" if self.comment else ""
        out = f"{self.name} {comment} distance={self.parameters[0]}"

        return out


class PY(PX):
    """Plane normal to y axis."""

    def __init__(
        self, distance, id: Optional[int] = None, comment: Optional[str] = None
    ):
        super().__init__(id=id, distance=distance, comment=comment)
        self.type = "PY"
        self.center = np.array([0, distance, 0])


class PZ(PX):
    """Plane normal to z axis."""

    def __init__(
        self, distance, id: Optional[int] = None, comment: Optional[str] = None
    ):
        super().__init__(id=id, distance=distance, comment=comment)
        self.name = "PZ"
        self.center = np.array([0, 0, distance])


class RCC(Surface):
    """Right circular cylinder"""

    def __init__(
        self,
        vx,
        vy,
        vz,
        hx,
        hy,
        hz,
        r,
        id: Optional[int] = None,
        comment: Optional[str] = None,
    ):
        super().__init__(
            id=id,
            type="RCC",
            parameters=[vx, vy, vz, hx, hy, hz, r],
            comment=comment,
        )

        self.bottom_center = np.array([vx, vy, vz])
        self.direction = np.array([hx, hy, hz])
        self.height = np.linalg.norm(self.direction)
        self.direction = self.direction / self.height
        self.radius = r
        self.center = self.bottom_center + 0.5 * self.height * self.direction

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type}"
        for x in self.bottom_center:
            out += f" {x}"
        for x in self.height * self.direction:
            out += f" {x}"
        out += f" {self.radius} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface RCC id={self.id}{comment}:\n"
        vx, vy, vz, hx, hy, hz, r = self.parameters
        out += f"    {vx=} {vy=} {vz=}\n"
        out += f"    {hx=} {hy=} {hz=}\n"
        out += f"    {r=}\n"

        return out


class SPH(Surface):
    """Sphere."""

    def __init__(
        self, vx, vy, vz, r, id: Optional[int] = None, comment: Optional[str] = None
    ):
        super().__init__(
            id=id,
            type="SPH",
            parameters=[vx, vy, vz, r],
            comment=comment,
        )

        self.center = np.array([vx, vy, vz])
        self.radius = r

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type} "
        for x in self.center:
            out += f" {x}"
        out += f" {self.radius} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface SPH id={self.id}{comment}:\n"
        vx, vy, vz, r = self.parameters
        out += f"    {vx=} {vy=} {vz=}\n"
        out += f"    {r=}\n"

        return out


class SO(Surface):
    """Sphere at origin."""

    def __init__(self, r, id: Optional[int] = None, comment: Optional[str] = None):
        super().__init__(
            id=id,
            type="SO",
            parameters=[r],
            comment=comment,
        )
        self.center = np.array([0, 0, 0])
        self.radius = r

    def to_mcnp(self):
        """Create a line for and MCNP file."""
        out = f"{self.id} {self.type} {self.radius} "
        if self.comment:
            out += f"$ {self.comment}"
        return out.strip() + "\n"

    def __str__(self):
        comment = f" {self.comment}" if self.comment else ""

        out = f"Surface SO id={self.id}{comment}:\n"
        r = self.parameters[0]
        out += f"    {r=}\n"

        return out

import dataclasses

from . import line
from .Types import EventType, Particle, Surface

# J-line slot names per form: `(source event, any other event)`; the same slot means different things per event type.
_SLOTS = {
    line.J_0: ({'cell': 'ncl', 'material': 'mat'}, {}),
    line.J_1: (
        {'cell': 'ncl__ipt__ntyn_mtp_angle_branch', 'material': 'mat__ncl'},
        {'nsx': 'nsr__nsx_nsf_nter', 'cell': 'mat__ncl', 'material': 'ncp__mat'},
    ),
    line.J_2: (
        {'particle': 'ipt__ntyn_mtp_angle_branch', 'cell': 'ncl__ipt', 'material': 'mat__ncl'},
        {'nsx': 'nsr__nsx_nsf_nter', 'particle': 'ncl__ipt', 'cell': 'mat__ncl', 'material': 'ncp__mat'},
    ),
    line.J_3: (
        {'particle': 'ipt', 'cell': 'ncl', 'material': 'mat'},
        {'nsx': 'nsx_nsf_nter', 'particle': 'ipt', 'cell': 'ncl', 'material': 'mat'},
    ),
}


@dataclasses.dataclass(slots=True)
class Event:
    """
    Represents a PTRAC event with its own type, history, and meaningful values.

    Values that PTRAC does not write for this event (e.g., the particle with some `J` forms, or direction and energy without `WRITE=ALL`) are `None`.

    Attributes:
        nps: History number.
        type: Event type.
        creation_code: Bank event code (`2xxx`) naming how the banked particle was made, `None` for other events.
        j: Raw `J` line, whose `type` is the type of the next event.
        p: Raw `P` line.
    """

    nps: int
    type: EventType
    creation_code: int | None
    j: line.J
    p: line.P_0 | line.P_1

    def _slot(self, role: str) -> str | None:
        slots = _SLOTS[type(self.j)][self.type is not EventType.SOURCE]
        name = slots.get(role)
        return None if name is None else str(getattr(self.j, name)).strip()

    @property
    def particle(self) -> Particle | int | None:
        """
        Particle type, or the raw `ipt` number if it is not a common one.
        """

        value = self._slot('particle')
        if not value:
            return None
        number = int(value)
        try:
            return Particle(number)
        except ValueError:
            return number

    @property
    def cell(self) -> int | None:
        """
        Cell of the event; for a surface crossing the cell entered.
        """

        value = self._slot('cell')
        return int(value) if value else None

    @property
    def cell_entered(self) -> int | None:
        """
        Cell entered, for surface crossings only.
        """

        return self.cell if self.type is EventType.SURFACE else None

    @property
    def material(self) -> int | None:
        """
        Material of the cell.
        """

        value = self._slot('material')
        return int(value) if value else None

    @property
    def surface(self) -> Surface | None:
        """
        Surface crossed, for surface crossings only.
        """

        if self.type is not EventType.SURFACE:
            return None
        value = self._slot('nsx')
        return Surface.parse(value) if value else None

    @property
    def zaid(self) -> int | None:
        """
        Nuclide ZAID of the collision, or of the collision that produced a banked particle.
        `None` if not written or 0, which is the case for photons made by photon interactions.
        """

        if self.type not in (EventType.COLLISION, EventType.BANK):
            return None
        value = self._slot('nsx')
        return (int(float(value)) or None) if value else None

    @property
    def position(self) -> tuple[float, float, float]:
        return float(self.p.x), float(self.p.y), float(self.p.z)

    @property
    def direction(self) -> tuple[float, float, float] | None:
        p = self.p
        return (float(p.u), float(p.v), float(p.w)) if isinstance(p, line.P_1) else None

    @property
    def energy(self) -> float | None:
        return float(self.p.erg) if isinstance(self.p, line.P_1) else None

    @property
    def weight(self) -> float | None:
        return float(self.p.wgt) if isinstance(self.p, line.P_1) else None

    @property
    def time(self) -> float | None:
        return float(self.p.tme) if isinstance(self.p, line.P_1) else None

    @property
    def raw(self) -> str:
        """
        The event as written in the file, `J` line then `P` line.
        """

        return f'{self.j.to_mcnp()}\n{self.p.to_mcnp()}'

    def to_dict(self) -> dict:
        """
        Converts the event to a flat dictionary, e.g., for `pandas.DataFrame`.
        """

        x, y, z = self.position
        u, v, w = self.direction or (None, None, None)
        particle = self.particle
        surface = self.surface
        return {
            'nps': self.nps,
            'type': self.type.name,
            'creation_code': self.creation_code,
            'particle': getattr(particle, 'name', particle),
            'cell': self.cell,
            'material': self.material,
            'surface': None if surface is None else surface.number,
            'facet': None if surface is None else surface.facet,
            'zaid': self.zaid,
            'x': x,
            'y': y,
            'z': z,
            'u': u,
            'v': v,
            'w': w,
            'energy': self.energy,
            'weight': self.weight,
            'time': self.time,
        }

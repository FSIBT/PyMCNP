import dataclasses

from . import block
from .Types import EventType, Particle, Surface

# J-line value positions per number of values after `type`: `(source event, any other event)`.
# The same position means different things per event type, and PTRAC writes 4 to 7 values depending on its options.
_SLOTS = {
    4: ({'cell': 2, 'material': 3}, {}),
    5: ({'cell': 2, 'material': 3}, {'nsx': 1, 'cell': 3, 'material': 4}),
    6: ({'particle': 2, 'cell': 3, 'material': 4}, {'nsx': 1, 'particle': 3, 'cell': 4, 'material': 5}),
    7: ({'particle': 3, 'cell': 4, 'material': 5}, {'nsx': 1, 'particle': 3, 'cell': 4, 'material': 5}),
}


def _values(event: block.Event) -> tuple[list[str], list[str]]:
    """
    Splits event blocks into their J-line values after `type` and their P-line values.
    """

    names = list(type(event)._fields)
    j = names[names.index('type') + 1 : names.index('newline')]
    p = names[names.index('blank_1') + 1 :]
    return [str(getattr(event, name)).strip() for name in j], [str(getattr(event, name)).strip() for name in p]


@dataclasses.dataclass(slots=True)
class Event:
    """
    Represents a PTRAC event with its own type, history, and meaningful values.

    A PTRAC event block's `type` is the type of the next event, so the event blocks of `pymcnp.ptrac.block` cannot know their own type.
    This class pairs each event block with its type and reads the values by their meaning.
    Values that PTRAC does not write for this event (e.g., the particle with some forms, or direction and energy without `WRITE=ALL`) are `None`.

    Attributes:
        nps: History number.
        type: Event type.
        creation_code: Bank event code (`2xxx`) naming how the banked particle was made, `None` for other events.
        block: Event block as parsed.
    """

    nps: int
    type: EventType
    creation_code: int | None
    block: block.Event
    _j: list[str] = dataclasses.field(init=False, repr=False, compare=False)
    _p: list[str] = dataclasses.field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        self._j, self._p = _values(self.block)

    def _slot(self, role: str) -> str | None:
        slots = _SLOTS.get(len(self._j), ({}, {}))[self.type is not EventType.SOURCE]
        index = slots.get(role)
        return None if index is None else self._j[index]

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
        x, y, z = self._p[:3]
        return float(x), float(y), float(z)

    @property
    def direction(self) -> tuple[float, float, float] | None:
        if len(self._p) < 9:
            return None
        u, v, w = self._p[3:6]
        return float(u), float(v), float(w)

    @property
    def energy(self) -> float | None:
        return float(self._p[6]) if len(self._p) >= 9 else None

    @property
    def weight(self) -> float | None:
        return float(self._p[7]) if len(self._p) >= 9 else None

    @property
    def time(self) -> float | None:
        return float(self._p[8]) if len(self._p) >= 9 else None

    @property
    def raw(self) -> str:
        """
        The event as written in the file, `J` line then `P` line.
        """

        return self.block.to_mcnp()

    def to_dict(self) -> dict:
        """
        Converts the event to a flat dictionary with plain Python values (`int`, `float`, `str`, `None`), e.g., for `pandas.DataFrame`.
        Use `pymcnp.ptrac.to_dataframe` for columns with proper dtypes (nullable `Int64` for the integers).
        """

        x, y, z = self.position
        u, v, w = self.direction or (None, None, None)
        particle = self.particle
        surface = self.surface
        return {
            'nps': self.nps,
            'type': self.type.name,
            'creation_code': self.creation_code,
            'particle': None if particle is None else getattr(particle, 'name', str(particle)),
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

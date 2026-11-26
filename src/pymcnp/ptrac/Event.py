import dataclasses

from . import block
from .Types import EventType, Particle, Surface

# Roles of the J-line values `Event` reads, by PTRAC header variable ID (MCNP manual, PTRAC file format):
# 10 ZAID (NXS(2,IEX)), 12 surface (NSF(PBL%I%JSU)), 16 particle (PBL%I%IPT), 17 cell (NCL(PBL%I%ICL)), 18 material (MAT(PBL%I%ICL)).
_ROLES_BY_ID = {10: 'nsx', 12: 'nsx', 16: 'particle', 17: 'cell', 18: 'material'}

# The same roles by event block field name, for events read without the header.
_ROLES_BY_FIELD = {'nxs_2_iex': 'nsx', 'nsf_pbl_i_jsu': 'nsx', 'pbl_i_ipt': 'particle', 'ncl_pbl_i_icl': 'cell', 'mat_pbl_i_icl': 'material'}

# Event types in the order of the header's J/P line pairs, after the NPS line.
_ORDER = (EventType.SOURCE, EventType.BANK, EventType.SURFACE, EventType.COLLISION, EventType.TERMINAL)

# Layout of the J-line values per event type: number of values after `type`, and position by role.
Layout = dict[EventType, tuple[int, dict[str, int]]]

_EVENT_TYPE_ID = 7


def _layout(header: block.Header) -> Layout | None:
    """
    Reads the positions of the J-line values from the variable IDs of PTRAC headers.

    The header's `n1` to `n11` count the variable IDs of the NPS line, then of the J and P lines of source, bank,
    surface, collision and termination events; `l` lists the IDs in that order. Each J line starts with the event
    type (ID 7).

    Returns:
        Layout per event type, `None` if the counts and IDs are not numbers or do not fit together.
    """

    try:
        counts = [int(getattr(header, f'n{i}')) for i in range(1, 12)]
        ids = [int(i) for i in header.l]
    except ValueError:
        return None
    if sum(counts) != len(ids):
        return None

    layout: Layout = {}
    start = counts[0]
    for kind, j, p in zip(_ORDER, counts[1::2], counts[2::2]):
        line = ids[start : start + j]
        if line[:1] != [_EVENT_TYPE_ID]:
            return None
        layout[kind] = (j - 1, {_ROLES_BY_ID[i]: index for index, i in enumerate(line[1:]) if i in _ROLES_BY_ID})
        start += j + p

    return layout


def _values(event: block.Event) -> tuple[list[str], list[str], dict[str, int]]:
    """
    Splits event blocks into their J-line values after `type` and their P-line values, and finds the positions of
    the J-line values by the block's field names.
    """

    names = list(type(event)._fields)
    j = names[names.index('type') + 1 : names.index('newline')]
    p = names[names.index('blank_1') + 1 :]
    roles = {_ROLES_BY_FIELD[name]: index for index, name in enumerate(j) if name in _ROLES_BY_FIELD}
    return [str(getattr(event, name)).strip() for name in j], [str(getattr(event, name)).strip() for name in p], roles


@dataclasses.dataclass(slots=True)
class Event:
    """
    Represents a PTRAC event with its own type, history, and meaningful values.

    A PTRAC event block's `type` is the type of the next event, so the event blocks of `pymcnp.ptrac.block` cannot know their own type.
    This class pairs each event block with its type and reads the values by their meaning.
    The J-line values are found by the variable IDs of the file's header, which `Ptrac.stream` and the other PTRAC readers pass as the
    init-only argument `_layout` (an implementation detail, not stored); without it, by the event block's field names.
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
    _layout: dataclasses.InitVar[Layout | None] = None
    _j: list[str] = dataclasses.field(init=False, repr=False, compare=False)
    _p: list[str] = dataclasses.field(init=False, repr=False, compare=False)
    _roles: dict[str, int] = dataclasses.field(init=False, repr=False, compare=False)

    def __post_init__(self, _layout: Layout | None) -> None:
        # `_layout`: positions of the J-line values per event type, from the header's variable IDs; `None` (or a layout
        # whose number of values differs from the event's) to use the event block's field names.
        self._j, self._p, self._roles = _values(self.block)
        count, roles = (_layout or {}).get(self.type, (None, {}))
        if count == len(self._j):
            self._roles = roles

    def _slot(self, role: str) -> str | None:
        index = self._roles.get(role)
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

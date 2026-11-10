import dataclasses
import collections.abc

from .Event import Event
from .Types import EventType, Particle


@dataclasses.dataclass(eq=False)
class Track:
    """
    Represents one particle track: a source or bank event, followed by its surface crossings and collisions up to its terminal event.

    Attributes:
        nps: History number.
        index: Track number within the history, in file order.
        creation: Source or bank event that started the track.
        events: All events of the track, starting with `creation`.
        parent: Track this particle was banked from, `None` for source particles or if it cannot be found.
        parent_zaid: Nuclide ZAID of the collision that started the chain this track descends from.
            For a photon made by a photon interaction (bank ZAID 0) this is inherited from its parent track, `None` if unknown.
    """

    nps: int
    index: int
    creation: Event
    events: list[Event]
    parent: 'Track | None' = None
    parent_zaid: int | None = None

    def entries(self, cell: int | None = None, surface: int | None = None) -> collections.abc.Iterator[Event]:
        """
        Yields the surface crossings of the track, optionally only those entering `cell` and/or crossing `surface` (any facet).
        """

        for event in self.events:
            if event.type is not EventType.SURFACE:
                continue
            if cell is not None and event.cell_entered != cell:
                continue
            if surface is not None and (event.surface is None or event.surface.number != surface):
                continue
            yield event

    @property
    def particle(self) -> Particle | int | None:
        return self.creation.particle

    @property
    def creation_code(self) -> int | None:
        """
        Bank event code (`2xxx`), `None` for source particles.
        """

        return self.creation.creation_code


def _key(event: Event) -> tuple[float, float, float, float | None]:
    return (*event.position, event.time)


def tracks(
    events: collections.abc.Iterable[Event],
    particle: Particle | None = None,
    entered: int | None = None,
) -> collections.abc.Iterator[Track]:
    """
    Groups events into tracks and resolves where banked particles came from.

    A banked particle is written at the point where it was created, so its parent is the earlier track that has an event at the same position (and time, if written) in the same history.

    Parents are resolved for every track, so filtering never changes `parent` or `parent_zaid`.

    Parameters:
        events: Events in file order.
        particle: Only yield tracks of this particle.
        entered: Only yield tracks with a surface crossing that enters this cell.

    Yields:
        Tracks in file order; parents come before their children.
    """

    def wanted(track: Track) -> bool:
        if particle is not None and track.particle != particle:
            return False
        return entered is None or next(track.entries(cell=entered), None) is not None

    for track in _tracks(events):
        if wanted(track):
            yield track


def _tracks(events: collections.abc.Iterable[Event]) -> collections.abc.Iterator[Track]:
    nps: int | None = None
    current: Track | None = None
    seen: dict[tuple, Track] = {}
    count = 0

    for event in events:
        if event.nps != nps:
            if current is not None:
                yield current
            nps, current, seen, count = event.nps, None, {}, 0

        if event.type in (EventType.SOURCE, EventType.BANK):
            if current is not None:
                yield current
            current = Track(event.nps, count, event, [event])
            count += 1
            if event.type is EventType.BANK:
                current.parent = seen.get(_key(event))
                current.parent_zaid = event.zaid or (current.parent.parent_zaid if current.parent else None)
        elif current is not None:
            current.events.append(event)
        else:
            continue

        if event.type is EventType.BANK:
            seen.setdefault(_key(event), current)
        else:
            seen[_key(event)] = current

    if current is not None:
        yield current

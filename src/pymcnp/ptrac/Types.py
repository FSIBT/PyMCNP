import enum
import dataclasses


class EventType(enum.IntEnum):
    """
    Represents PTRAC event types.

    Bank events carry a sub-code (`2xxx`) that `Event.creation_code` keeps.
    """

    SOURCE = 1000
    BANK = 2000
    SURFACE = 3000
    COLLISION = 4000
    TERMINAL = 5000
    END = 9000

    @classmethod
    def from_code(cls, code: int) -> 'EventType':
        """
        Converts a PTRAC event code (`1000`, `-2013`, ...) to an event type.

        Raises:
            ValueError: Unknown code.
        """

        code = abs(int(code))
        return cls(2000 if 2000 <= code < 3000 else code)


class Particle(enum.IntEnum):
    """
    Represents PTRAC particle types (`ipt`), the common ones.
    """

    NEUTRON = 1
    PHOTON = 2
    ELECTRON = 3
    POSITRON = 8
    PROTON = 9
    ALPHA = 34


@dataclasses.dataclass(frozen=True)
class Surface:
    """
    Represents a surface crossed, e.g., `3.1` is facet 1 of surface 3.

    Attributes:
        number: Surface number.
        facet: Macrobody facet, 0 if the surface is not a macrobody.
    """

    number: int
    facet: int = 0

    @classmethod
    def parse(cls, text: str) -> 'Surface':
        """
        Parses a PTRAC surface value, e.g., `'3.1'`, `'12'` or `'-5.2'`.
        """

        whole, _, fraction = text.strip().partition('.')
        return cls(abs(int(whole)), int(fraction) if fraction else 0)

    def __str__(self) -> str:
        return f'{self.number}.{self.facet}' if self.facet else str(self.number)

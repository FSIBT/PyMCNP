import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Vol(DataOption):
    """
    Represents INP vol elements.

    Attributes:
        no: Volume calculation on/off.
        volumes: Tuple of cell volumes.
    """

    _ATTRS = {
        'no': types.String,
        'volumes': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Avol(?: (no))?((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, volumes: types.Tuple[types.RealOrJump], no: types.String = None):
        """
        Initializes ``Vol``.

        Parameters:
            no: Volume calculation on/off.
            volumes: Tuple of cell volumes.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if no is not None and no not in {'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, no)
        if volumes is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, volumes)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                no,
                volumes,
            ]
        )

        self.no: typing.Final[types.String] = no
        self.volumes: typing.Final[types.Tuple[types.RealOrJump]] = volumes


@dataclasses.dataclass
class VolBuilder:
    """
    Builds ``Vol``.

    Attributes:
        no: Volume calculation on/off.
        volumes: Tuple of cell volumes.
    """

    volumes: list[str] | list[float] | list[types.RealOrJump]
    no: str | types.String = None

    def build(self):
        """
        Builds ``VolBuilder`` into ``Vol``.

        Returns:
            ``Vol`` for ``VolBuilder``.
        """

        no = None
        if isinstance(self.no, types.String):
            no = self.no
        elif isinstance(self.no, str):
            no = types.String.from_mcnp(self.no)

        volumes = []
        for item in self.volumes:
            if isinstance(item, types.RealOrJump):
                volumes.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                volumes.append(types.RealOrJump(item))
            elif isinstance(item, str):
                volumes.append(types.RealOrJump.from_mcnp(item))
        volumes = types.Tuple(volumes)

        return Vol(
            no=no,
            volumes=volumes,
        )

import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Vol(_option.DataOption):
    """
    Represents INP vol elements.

    Attributes:
        no: Volume calculation on/off.
        volumes: Tuple of cell volumes.
    """

    _KEYWORD = 'vol'

    _ATTRS = {
        'no': types.String,
        'volumes': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Avol(?: (no))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, volumes: types.Tuple[types.Real], no: types.String = None):
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
        self.volumes: typing.Final[types.Tuple[types.Real]] = volumes


@dataclasses.dataclass
class VolBuilder(_option.DataOptionBuilder):
    """
    Builds ``Vol``.

    Attributes:
        no: Volume calculation on/off.
        volumes: Tuple of cell volumes.
    """

    volumes: list[str] | list[float] | list[types.Real]
    no: str | types.String = None

    def build(self):
        """
        Builds ``VolBuilder`` into ``Vol``.

        Returns:
            ``Vol`` for ``VolBuilder``.
        """

        no = self.no
        if isinstance(self.no, types.String):
            no = self.no
        elif isinstance(self.no, str):
            no = types.String.from_mcnp(self.no)

        if self.volumes:
            volumes = []
            for item in self.volumes:
                if isinstance(item, types.Real):
                    volumes.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    volumes.append(types.Real(item))
                elif isinstance(item, str):
                    volumes.append(types.Real.from_mcnp(item))
            volumes = types.Tuple(volumes)
        else:
            volumes = None

        return Vol(
            no=no,
            volumes=volumes,
        )

    @staticmethod
    def unbuild(ast: Vol):
        """
        Unbuilds ``Vol`` into ``VolBuilder``

        Returns:
            ``VolBuilder`` for ``Vol``.
        """

        return VolBuilder(
            no=copy.deepcopy(ast.no),
            volumes=copy.deepcopy(ast.volumes),
        )

import re
import typing
import dataclasses


from .option_ import SswOption_
from ....utils import types
from ....utils import errors


class Cel(SswOption_, keyword='cel'):
    """
    Represents INP cel elements.

    Attributes:
        cfs: Cells from which KCODE neutrons are written.
    """

    _ATTRS = {
        'cfs': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Acel((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, cfs: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Cel``.

        Parameters:
            cfs: Cells from which KCODE neutrons are written.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cfs is None or not (filter(lambda entry: not (1 <= entry <= 99_999_999), cfs)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cfs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cfs,
            ]
        )

        self.cfs: typing.Final[types.Tuple[types.IntegerOrJump]] = cfs


@dataclasses.dataclass
class CelBuilder:
    """
    Builds ``Cel``.

    Attributes:
        cfs: Cells from which KCODE neutrons are written.
    """

    cfs: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``CelBuilder`` into ``Cel``.

        Returns:
            ``Cel`` for ``CelBuilder``.
        """

        cfs = []
        for item in self.cfs:
            if isinstance(item, types.IntegerOrJump):
                cfs.append(item)
            elif isinstance(item, int):
                cfs.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                cfs.append(types.IntegerOrJump.from_mcnp(item))
        cfs = types.Tuple(cfs)

        return Cel(
            cfs=cfs,
        )

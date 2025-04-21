import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Idum(DataOption, keyword='idum'):
    """
    Represents INP idum elements.

    Attributes:
        intergers: Integer array.
    """

    _ATTRS = {
        'intergers': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Aidum((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, intergers: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Idum``.

        Parameters:
            intergers: Integer array.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if intergers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, intergers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                intergers,
            ]
        )

        self.intergers: typing.Final[types.Tuple[types.IntegerOrJump]] = intergers


@dataclasses.dataclass
class IdumBuilder:
    """
    Builds ``Idum``.

    Attributes:
        intergers: Integer array.
    """

    intergers: list[str] | list[int] | list[types.IntegerOrJump]

    def build(self):
        """
        Builds ``IdumBuilder`` into ``Idum``.

        Returns:
            ``Idum`` for ``IdumBuilder``.
        """

        intergers = []
        for item in self.intergers:
            if isinstance(item, types.IntegerOrJump):
                intergers.append(item)
            elif isinstance(item, int):
                intergers.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                intergers.append(types.IntegerOrJump.from_mcnp(item))
        intergers = types.Tuple(intergers)

        return Idum(
            intergers=intergers,
        )

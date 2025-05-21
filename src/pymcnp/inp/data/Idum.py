import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Idum(DataOption):
    """
    Represents INP idum elements.

    Attributes:
        intergers: Integer array.
    """

    _KEYWORD = 'idum'

    _ATTRS = {
        'intergers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aidum((?: {types.Integer._REGEX.pattern})+?)\Z')

    def __init__(self, intergers: types.Tuple[types.Integer]):
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

        self.intergers: typing.Final[types.Tuple[types.Integer]] = intergers


@dataclasses.dataclass
class IdumBuilder:
    """
    Builds ``Idum``.

    Attributes:
        intergers: Integer array.
    """

    intergers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``IdumBuilder`` into ``Idum``.

        Returns:
            ``Idum`` for ``IdumBuilder``.
        """

        if self.intergers:
            intergers = []
            for item in self.intergers:
                if isinstance(item, types.Integer):
                    intergers.append(item)
                elif isinstance(item, int):
                    intergers.append(types.Integer(item))
                elif isinstance(item, str):
                    intergers.append(types.Integer.from_mcnp(item))
            intergers = types.Tuple(intergers)
        else:
            intergers = None

        return Idum(
            intergers=intergers,
        )

    @staticmethod
    def unbuild(ast: Idum):
        """
        Unbuilds ``Idum`` into ``IdumBuilder``

        Returns:
            ``IdumBuilder`` for ``Idum``.
        """

        return Idum(
            intergers=copy.deepcopy(ast.intergers),
        )

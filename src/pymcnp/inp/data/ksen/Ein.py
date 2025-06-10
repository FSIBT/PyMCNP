import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Ein(_option.KsenOption):
    """
    Represents INP ein elements.

    Attributes:
        energies: List of ranges for incident energies.
    """

    _KEYWORD = 'ein'

    _ATTRS = {
        'energies': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aein((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, energies: types.Tuple[types.Real]):
        """
        Initializes ``Ein``.

        Parameters:
            energies: List of ranges for incident energies.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if energies is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, energies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                energies,
            ]
        )

        self.energies: typing.Final[types.Tuple[types.Real]] = energies


@dataclasses.dataclass
class EinBuilder(_option.KsenOptionBuilder):
    """
    Builds ``Ein``.

    Attributes:
        energies: List of ranges for incident energies.
    """

    energies: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``EinBuilder`` into ``Ein``.

        Returns:
            ``Ein`` for ``EinBuilder``.
        """

        if self.energies:
            energies = []
            for item in self.energies:
                if isinstance(item, types.Real):
                    energies.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    energies.append(types.Real(item))
                elif isinstance(item, str):
                    energies.append(types.Real.from_mcnp(item))
            energies = types.Tuple(energies)
        else:
            energies = None

        return Ein(
            energies=energies,
        )

    @staticmethod
    def unbuild(ast: Ein):
        """
        Unbuilds ``Ein`` into ``EinBuilder``

        Returns:
            ``EinBuilder`` for ``Ein``.
        """

        return EinBuilder(
            energies=copy.deepcopy(ast.energies),
        )

import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Erg(_option.KsenOption):
    """
    Represents INP erg elements.

    Attributes:
        energies: List of energies.
    """

    _KEYWORD = 'erg'

    _ATTRS = {
        'energies': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aerg((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, energies: types.Tuple[types.Real]):
        """
        Initializes ``Erg``.

        Parameters:
            energies: List of energies.

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
class ErgBuilder(_option.KsenOptionBuilder):
    """
    Builds ``Erg``.

    Attributes:
        energies: List of energies.
    """

    energies: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``ErgBuilder`` into ``Erg``.

        Returns:
            ``Erg`` for ``ErgBuilder``.
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

        return Erg(
            energies=energies,
        )

    @staticmethod
    def unbuild(ast: Erg):
        """
        Unbuilds ``Erg`` into ``ErgBuilder``

        Returns:
            ``ErgBuilder`` for ``Erg``.
        """

        return ErgBuilder(
            energies=copy.deepcopy(ast.energies),
        )

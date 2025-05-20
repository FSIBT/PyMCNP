import re
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Axs(SsrOption):
    """
    Represents INP axs elements.

    Attributes:
        cosines: Direction cosines defining.
    """

    _ATTRS = {
        'cosines': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, cosines: types.Tuple[types.Real]):
        """
        Initializes ``Axs``.

        Parameters:
            cosines: Direction cosines defining.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cosines)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cosines,
            ]
        )

        self.cosines: typing.Final[types.Tuple[types.Real]] = cosines


@dataclasses.dataclass
class AxsBuilder:
    """
    Builds ``Axs``.

    Attributes:
        cosines: Direction cosines defining.
    """

    cosines: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``AxsBuilder`` into ``Axs``.

        Returns:
            ``Axs`` for ``AxsBuilder``.
        """

        if self.cosines:
            cosines = []
            for item in self.cosines:
                if isinstance(item, types.Real):
                    cosines.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    cosines.append(types.Real(item))
                elif isinstance(item, str):
                    cosines.append(types.Real.from_mcnp(item))
            cosines = types.Tuple(cosines)
        else:
            cosines = None

        return Axs(
            cosines=cosines,
        )

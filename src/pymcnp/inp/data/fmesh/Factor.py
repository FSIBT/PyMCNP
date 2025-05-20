import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Factor(FmeshOption):
    """
    Represents INP factor elements.

    Attributes:
        multiple: Multiplicative factor for each mesh.
    """

    _ATTRS = {
        'multiple': types.Real,
    }

    _REGEX = re.compile(rf'\Afactor( {types.Real._REGEX.pattern})\Z')

    def __init__(self, multiple: types.Real):
        """
        Initializes ``Factor``.

        Parameters:
            multiple: Multiplicative factor for each mesh.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if multiple is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, multiple)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                multiple,
            ]
        )

        self.multiple: typing.Final[types.Real] = multiple


@dataclasses.dataclass
class FactorBuilder:
    """
    Builds ``Factor``.

    Attributes:
        multiple: Multiplicative factor for each mesh.
    """

    multiple: str | float | types.Real

    def build(self):
        """
        Builds ``FactorBuilder`` into ``Factor``.

        Returns:
            ``Factor`` for ``FactorBuilder``.
        """

        multiple = self.multiple
        if isinstance(self.multiple, types.Real):
            multiple = self.multiple
        elif isinstance(self.multiple, float) or isinstance(self.multiple, int):
            multiple = types.Real(self.multiple)
        elif isinstance(self.multiple, str):
            multiple = types.Real.from_mcnp(self.multiple)

        return Factor(
            multiple=multiple,
        )

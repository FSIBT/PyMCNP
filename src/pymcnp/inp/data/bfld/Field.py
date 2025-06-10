import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Field(_option.BfldOption):
    """
    Represents INP field elements.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    _KEYWORD = 'field'

    _ATTRS = {
        'strength_gradient': types.Real,
    }

    _REGEX = re.compile(rf'\Afield( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, strength_gradient: types.Real):
        """
        Initializes ``Field``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if strength_gradient is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, strength_gradient)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                strength_gradient,
            ]
        )

        self.strength_gradient: typing.Final[types.Real] = strength_gradient


@dataclasses.dataclass
class FieldBuilder(_option.BfldOptionBuilder):
    """
    Builds ``Field``.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    strength_gradient: str | float | types.Real

    def build(self):
        """
        Builds ``FieldBuilder`` into ``Field``.

        Returns:
            ``Field`` for ``FieldBuilder``.
        """

        strength_gradient = self.strength_gradient
        if isinstance(self.strength_gradient, types.Real):
            strength_gradient = self.strength_gradient
        elif isinstance(self.strength_gradient, float) or isinstance(self.strength_gradient, int):
            strength_gradient = types.Real(self.strength_gradient)
        elif isinstance(self.strength_gradient, str):
            strength_gradient = types.Real.from_mcnp(self.strength_gradient)

        return Field(
            strength_gradient=strength_gradient,
        )

    @staticmethod
    def unbuild(ast: Field):
        """
        Unbuilds ``Field`` into ``FieldBuilder``

        Returns:
            ``FieldBuilder`` for ``Field``.
        """

        return FieldBuilder(
            strength_gradient=copy.deepcopy(ast.strength_gradient),
        )

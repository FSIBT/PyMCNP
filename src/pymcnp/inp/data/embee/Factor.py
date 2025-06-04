import re
import copy
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Factor(EmbeeOption):
    """
    Represents INP factor elements.

    Attributes:
        constant: Multiplicative constant.
    """

    _KEYWORD = 'factor'

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(rf'\Afactor( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, constant: types.Real):
        """
        Initializes ``Factor``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.Real] = constant


@dataclasses.dataclass
class FactorBuilder:
    """
    Builds ``Factor``.

    Attributes:
        constant: Multiplicative constant.
    """

    constant: str | float | types.Real

    def build(self):
        """
        Builds ``FactorBuilder`` into ``Factor``.

        Returns:
            ``Factor`` for ``FactorBuilder``.
        """

        constant = self.constant
        if isinstance(self.constant, types.Real):
            constant = self.constant
        elif isinstance(self.constant, float) or isinstance(self.constant, int):
            constant = types.Real(self.constant)
        elif isinstance(self.constant, str):
            constant = types.Real.from_mcnp(self.constant)

        return Factor(
            constant=constant,
        )

    @staticmethod
    def unbuild(ast: Factor):
        """
        Unbuilds ``Factor`` into ``FactorBuilder``

        Returns:
            ``FactorBuilder`` for ``Factor``.
        """

        return Factor(
            constant=copy.deepcopy(ast.constant),
        )

import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Wgt(_option.SsrOption):
    """
    Represents INP wgt elements.

    Attributes:
        constant: Particle weight multiplier.
    """

    _KEYWORD = 'wgt'

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, constant: types.Real):
        """
        Initializes ``Wgt``.

        Parameters:
            constant: Particle weight multiplier.

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
class WgtBuilder(_option.SsrOptionBuilder):
    """
    Builds ``Wgt``.

    Attributes:
        constant: Particle weight multiplier.
    """

    constant: str | float | types.Real

    def build(self):
        """
        Builds ``WgtBuilder`` into ``Wgt``.

        Returns:
            ``Wgt`` for ``WgtBuilder``.
        """

        constant = self.constant
        if isinstance(self.constant, types.Real):
            constant = self.constant
        elif isinstance(self.constant, float) or isinstance(self.constant, int):
            constant = types.Real(self.constant)
        elif isinstance(self.constant, str):
            constant = types.Real.from_mcnp(self.constant)

        return Wgt(
            constant=constant,
        )

    @staticmethod
    def unbuild(ast: Wgt):
        """
        Unbuilds ``Wgt`` into ``WgtBuilder``

        Returns:
            ``WgtBuilder`` for ``Wgt``.
        """

        return WgtBuilder(
            constant=copy.deepcopy(ast.constant),
        )

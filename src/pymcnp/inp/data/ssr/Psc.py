import re
import copy
import typing
import dataclasses


from ._option import SsrOption
from ....utils import types
from ....utils import errors


class Psc(SsrOption):
    """
    Represents INP psc elements.

    Attributes:
        constant: Constant for approximation in PSC evaluation.
    """

    _KEYWORD = 'psc'

    _ATTRS = {
        'constant': types.Real,
    }

    _REGEX = re.compile(rf'\Apsc( {types.Real._REGEX.pattern})\Z')

    def __init__(self, constant: types.Real):
        """
        Initializes ``Psc``.

        Parameters:
            constant: Constant for approximation in PSC evaluation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if constant is None or not (constant.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, constant)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                constant,
            ]
        )

        self.constant: typing.Final[types.Real] = constant


@dataclasses.dataclass
class PscBuilder:
    """
    Builds ``Psc``.

    Attributes:
        constant: Constant for approximation in PSC evaluation.
    """

    constant: str | float | types.Real

    def build(self):
        """
        Builds ``PscBuilder`` into ``Psc``.

        Returns:
            ``Psc`` for ``PscBuilder``.
        """

        constant = self.constant
        if isinstance(self.constant, types.Real):
            constant = self.constant
        elif isinstance(self.constant, float) or isinstance(self.constant, int):
            constant = types.Real(self.constant)
        elif isinstance(self.constant, str):
            constant = types.Real.from_mcnp(self.constant)

        return Psc(
            constant=constant,
        )

    @staticmethod
    def unbuild(ast: Psc):
        """
        Unbuilds ``Psc`` into ``PscBuilder``

        Returns:
            ``PscBuilder`` for ``Psc``.
        """

        return Psc(
            constant=copy.deepcopy(ast.constant),
        )

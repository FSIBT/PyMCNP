import re
import copy
import typing
import dataclasses


from . import var
from ._option import DataOption
from ...utils import types


class Var(DataOption):
    """
    Represents INP var elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'var'

    _ATTRS = {
        'options': types.Tuple[var.VarOption],
    }

    _REGEX = re.compile(rf'\Avar((?: (?:{var.VarOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: types.Tuple[var.VarOption] = None):
        """
        Initializes ``Var``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[var.VarOption]] = options


@dataclasses.dataclass
class VarBuilder:
    """
    Builds ``Var``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[var.VarOption] = None

    def build(self):
        """
        Builds ``VarBuilder`` into ``Var``.

        Returns:
            ``Var`` for ``VarBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, var.VarOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(var.VarOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Var(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Var):
        """
        Unbuilds ``Var`` into ``VarBuilder``

        Returns:
            ``VarBuilder`` for ``Var``.
        """

        return Var(
            options=copy.deepcopy(ast.options),
        )

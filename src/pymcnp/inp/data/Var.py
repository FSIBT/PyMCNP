import re
import typing
import dataclasses


from . import var
from .option_ import DataOption_
from ...utils import types


class Var(DataOption_, keyword='var'):
    """
    Represents INP var elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[var.VarOption_],
    }

    _REGEX = re.compile(rf'\Avar((?: (?:{var.VarOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[var.VarOption_] = None):
        """
        Initializes ``Var``.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.options: typing.Final[types.Tuple[var.VarOption_]] = options


@dataclasses.dataclass
class VarBuilder:
    """
    Builds ``Var``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[var.VarOption_] = None

    def build(self):
        """
        Builds ``VarBuilder`` into ``Var``.

        Returns:
            ``Var`` for ``VarBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, var.VarOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(var.VarOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Var(
            options=options,
        )

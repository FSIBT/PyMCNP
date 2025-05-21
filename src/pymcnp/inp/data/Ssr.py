import re
import copy
import typing
import dataclasses


from . import ssr
from ._option import DataOption
from ...utils import types


class Ssr(DataOption):
    """
    Represents INP ssr elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'ssr'

    _ATTRS = {
        'options': types.Tuple[ssr.SsrOption],
    }

    _REGEX = re.compile(rf'\Assr((?: (?:{ssr.SsrOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[ssr.SsrOption] = None):
        """
        Initializes ``Ssr``.

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

        self.options: typing.Final[types.Tuple[ssr.SsrOption]] = options


@dataclasses.dataclass
class SsrBuilder:
    """
    Builds ``Ssr``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[ssr.SsrOption] = None

    def build(self):
        """
        Builds ``SsrBuilder`` into ``Ssr``.

        Returns:
            ``Ssr`` for ``SsrBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, ssr.SsrOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(ssr.SsrOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Ssr(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Ssr):
        """
        Unbuilds ``Ssr`` into ``SsrBuilder``

        Returns:
            ``SsrBuilder`` for ``Ssr``.
        """

        return Ssr(
            options=copy.deepcopy(ast.options),
        )

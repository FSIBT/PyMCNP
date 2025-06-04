import re
import copy
import typing
import dataclasses


from . import ptrac
from ._option import DataOption
from ...utils import types


class Ptrac(DataOption):
    """
    Represents INP ptrac elements.

    Attributes:
        options: Dictionary of options.
    """

    _KEYWORD = 'ptrac'

    _ATTRS = {
        'options': types.Tuple[ptrac.PtracOption],
    }

    _REGEX = re.compile(rf'\Aptrac((?: (?:{ptrac.PtracOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, options: types.Tuple[ptrac.PtracOption] = None):
        """
        Initializes ``Ptrac``.

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

        self.options: typing.Final[types.Tuple[ptrac.PtracOption]] = options


@dataclasses.dataclass
class PtracBuilder:
    """
    Builds ``Ptrac``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[ptrac.PtracOption] = None

    def build(self):
        """
        Builds ``PtracBuilder`` into ``Ptrac``.

        Returns:
            ``Ptrac`` for ``PtracBuilder``.
        """

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, ptrac.PtracOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(ptrac.PtracOption.from_mcnp(item))
                else:
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Ptrac(
            options=options,
        )

    @staticmethod
    def unbuild(ast: Ptrac):
        """
        Unbuilds ``Ptrac`` into ``PtracBuilder``

        Returns:
            ``PtracBuilder`` for ``Ptrac``.
        """

        return Ptrac(
            options=copy.deepcopy(ast.options),
        )

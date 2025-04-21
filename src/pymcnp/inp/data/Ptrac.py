import re
import typing
import dataclasses


from . import ptrac
from ._option import DataOption
from ...utils import types


class Ptrac(DataOption, keyword='ptrac'):
    """
    Represents INP ptrac elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[ptrac.PtracOption],
    }

    _REGEX = re.compile(rf'\Aptrac((?: (?:{ptrac.PtracOption._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[ptrac.PtracOption] = None):
        """
        Initializes ``Ptrac``.

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

        options = []
        for item in self.options:
            if isinstance(item, ptrac.PtracOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(ptrac.PtracOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Ptrac(
            options=options,
        )

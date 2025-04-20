import re
import typing
import dataclasses


from . import ssr
from .option_ import DataOption_
from ...utils import types


class Ssr(DataOption_, keyword='ssr'):
    """
    Represents INP ssr elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[ssr.SsrOption_],
    }

    _REGEX = re.compile(rf'\Assr((?: (?:{ssr.SsrOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[ssr.SsrOption_] = None):
        """
        Initializes ``Ssr``.

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

        self.options: typing.Final[types.Tuple[ssr.SsrOption_]] = options


@dataclasses.dataclass
class SsrBuilder:
    """
    Builds ``Ssr``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[ssr.SsrOption_] = None

    def build(self):
        """
        Builds ``SsrBuilder`` into ``Ssr``.

        Returns:
            ``Ssr`` for ``SsrBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, ssr.SsrOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(ssr.SsrOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Ssr(
            options=options,
        )

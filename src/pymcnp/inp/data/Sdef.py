import re
import typing
import dataclasses


from . import sdef
from .option_ import DataOption_
from ...utils import types


class Sdef(DataOption_, keyword='sdef'):
    """
    Represents INP sdef elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[sdef.SdefOption_],
    }

    _REGEX = re.compile(rf'\Asdef((?: (?:{sdef.SdefOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[sdef.SdefOption_] = None):
        """
        Initializes ``Sdef``.

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

        self.options: typing.Final[types.Tuple[sdef.SdefOption_]] = options


@dataclasses.dataclass
class SdefBuilder:
    """
    Builds ``Sdef``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[sdef.SdefOption_] = None

    def build(self):
        """
        Builds ``SdefBuilder`` into ``Sdef``.

        Returns:
            ``Sdef`` for ``SdefBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, sdef.SdefOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(sdef.SdefOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Sdef(
            options=options,
        )

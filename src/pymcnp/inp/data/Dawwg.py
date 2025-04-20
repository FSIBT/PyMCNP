import re
import typing
import dataclasses


from . import dawwg
from .option_ import DataOption_
from ...utils import types


class Dawwg(DataOption_, keyword='dawwg'):
    """
    Represents INP dawwg elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[dawwg.DawwgOption_],
    }

    _REGEX = re.compile(rf'\Adawwg((?: (?:{dawwg.DawwgOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[dawwg.DawwgOption_] = None):
        """
        Initializes ``Dawwg``.

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

        self.options: typing.Final[types.Tuple[dawwg.DawwgOption_]] = options


@dataclasses.dataclass
class DawwgBuilder:
    """
    Builds ``Dawwg``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[dawwg.DawwgOption_] = None

    def build(self):
        """
        Builds ``DawwgBuilder`` into ``Dawwg``.

        Returns:
            ``Dawwg`` for ``DawwgBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, dawwg.DawwgOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(dawwg.DawwgOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Dawwg(
            options=options,
        )

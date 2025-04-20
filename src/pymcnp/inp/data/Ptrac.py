import re
import typing
import dataclasses


from . import ptrac
from .option_ import DataOption_
from ...utils import types


class Ptrac(DataOption_, keyword='ptrac'):
    """
    Represents INP ptrac elements.

    Attributes:
        options: Dictionary of options.
    """

    _ATTRS = {
        'options': types.Tuple[ptrac.PtracOption_],
    }

    _REGEX = re.compile(rf'\Aptrac((?: (?:{ptrac.PtracOption_._REGEX.pattern}))+?)?\Z')

    def __init__(self, options: types.Tuple[ptrac.PtracOption_] = None):
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

        self.options: typing.Final[types.Tuple[ptrac.PtracOption_]] = options


@dataclasses.dataclass
class PtracBuilder:
    """
    Builds ``Ptrac``.

    Attributes:
        options: Dictionary of options.
    """

    options: list[str] | list[ptrac.PtracOption_] = None

    def build(self):
        """
        Builds ``PtracBuilder`` into ``Ptrac``.

        Returns:
            ``Ptrac`` for ``PtracBuilder``.
        """

        options = []
        for item in self.options:
            if isinstance(item, ptrac.PtracOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(ptrac.PtracOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Ptrac(
            options=options,
        )

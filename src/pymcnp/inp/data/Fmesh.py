import re
import typing
import dataclasses


from . import fmesh
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fmesh(DataOption_, keyword='fmesh'):
    """
    Represents INP fmesh elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'options': types.Tuple[fmesh.FmeshOption_],
    }

    _REGEX = re.compile(rf'\Afmesh(\d+):(\S+)((?: (?:{fmesh.FmeshOption_._REGEX.pattern}))+?)?\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        options: types.Tuple[fmesh.FmeshOption_] = None,
    ):
        """
        Initializes ``Fmesh``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (0 < suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.options: typing.Final[types.Tuple[fmesh.FmeshOption_]] = options


@dataclasses.dataclass
class FmeshBuilder:
    """
    Builds ``Fmesh``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    options: list[str] | list[fmesh.FmeshOption_] = None

    def build(self):
        """
        Builds ``FmeshBuilder`` into ``Fmesh``.

        Returns:
            ``Fmesh`` for ``FmeshBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        options = []
        for item in self.options:
            if isinstance(item, fmesh.FmeshOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(fmesh.FmeshOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Fmesh(
            suffix=suffix,
            designator=designator,
            options=options,
        )

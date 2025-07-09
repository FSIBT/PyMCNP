import re
import copy
import typing
import dataclasses


from . import fmesh
from . import _option
from ...utils import types
from ...utils import errors


class Fmesh(_option.DataOption):
    """
    Represents INP fmesh elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    _KEYWORD = 'fmesh'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'options': types.Tuple[fmesh.FmeshOption],
    }

    _REGEX = re.compile(rf'\Afmesh(\d+):(\S+)((?: (?:{fmesh.FmeshOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: types.Integer, designator: types.Designator, options: types.Tuple[fmesh.FmeshOption] = None):
        """
        Initializes ``Fmesh``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix > 0 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                options,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.options: typing.Final[types.Tuple[fmesh.FmeshOption]] = options


@dataclasses.dataclass
class FmeshBuilder(_option.DataOptionBuilder):
    """
    Builds ``Fmesh``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    options: list[str] | list[fmesh.FmeshOption] = None

    def build(self):
        """
        Builds ``FmeshBuilder`` into ``Fmesh``.

        Returns:
            ``Fmesh`` for ``FmeshBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if self.options:
            options = []
            for item in self.options:
                if isinstance(item, fmesh.FmeshOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(fmesh.FmeshOption.from_mcnp(item))
                elif isinstance(item, fmesh.FmeshOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Fmesh(
            suffix=suffix,
            designator=designator,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Fmesh):
        """
        Unbuilds ``Fmesh`` into ``FmeshBuilder``

        Returns:
            ``FmeshBuilder`` for ``Fmesh``.
        """

        return FmeshBuilder(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            options=copy.deepcopy(ast.options),
        )

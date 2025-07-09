import re
import copy
import typing
import dataclasses


from . import pert
from . import _option
from ...utils import types
from ...utils import errors


class Pert(_option.DataOption):
    """
    Represents INP pert elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    _KEYWORD = 'pert'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'options': types.Tuple[pert.PertOption],
    }

    _REGEX = re.compile(rf'\Apert(\d+):(\S+)((?: (?:{pert.PertOption._REGEX.pattern[2:-2]}))+?)?\Z')

    def __init__(self, suffix: types.Integer, designator: types.Designator, options: types.Tuple[pert.PertOption] = None):
        """
        Initializes ``Pert``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
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
        self.options: typing.Final[types.Tuple[pert.PertOption]] = options


@dataclasses.dataclass
class PertBuilder(_option.DataOptionBuilder):
    """
    Builds ``Pert``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    options: list[str] | list[pert.PertOption] = None

    def build(self):
        """
        Builds ``PertBuilder`` into ``Pert``.

        Returns:
            ``Pert`` for ``PertBuilder``.
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
                if isinstance(item, pert.PertOption):
                    options.append(item)
                elif isinstance(item, str):
                    options.append(pert.PertOption.from_mcnp(item))
                elif isinstance(item, pert.PertOptionBuilder):
                    options.append(item.build())
            options = types.Tuple(options)
        else:
            options = None

        return Pert(
            suffix=suffix,
            designator=designator,
            options=options,
        )

    @staticmethod
    def unbuild(ast: Pert):
        """
        Unbuilds ``Pert`` into ``PertBuilder``

        Returns:
            ``PertBuilder`` for ``Pert``.
        """

        return PertBuilder(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            options=copy.deepcopy(ast.options),
        )

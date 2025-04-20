import re
import typing
import dataclasses


from . import pert
from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Pert(DataOption_, keyword='pert'):
    """
    Represents INP pert elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'options': types.Tuple[pert.PertOption_],
    }

    _REGEX = re.compile(rf'\Apert(\d+):(\S+)((?: (?:{pert.PertOption_._REGEX.pattern}))+?)?\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        options: types.Tuple[pert.PertOption_] = None,
    ):
        """
        Initializes ``Pert``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
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
        self.options: typing.Final[types.Tuple[pert.PertOption_]] = options


@dataclasses.dataclass
class PertBuilder:
    """
    Builds ``Pert``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        options: Dictionary of options.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    options: list[str] | list[pert.PertOption_] = None

    def build(self):
        """
        Builds ``PertBuilder`` into ``Pert``.

        Returns:
            ``Pert`` for ``PertBuilder``.
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
            if isinstance(item, pert.PertOption_):
                options.append(item)
            elif isinstance(item, str):
                options.append(pert.PertOption_.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Pert(
            suffix=suffix,
            designator=designator,
            options=options,
        )

import re
import typing
import dataclasses


from . import fmult
from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fmult(DataOption, keyword='fmult'):
    """
    Represents INP fmult elements.

    Attributes:
        zaid: Nuclide for which data are entered.
        options: Dictionary of options.
    """

    _ATTRS = {
        'zaid': types.Zaid,
        'options': types.Tuple[fmult.FmultOption],
    }

    _REGEX = re.compile(
        rf'\Afmult( {types.Zaid._REGEX.pattern})((?: (?:{fmult.FmultOption._REGEX.pattern}))+?)?\Z'
    )

    def __init__(self, zaid: types.Zaid, options: types.Tuple[fmult.FmultOption] = None):
        """
        Initializes ``Fmult``.

        Parameters:
            zaid: Nuclide for which data are entered.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if zaid is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaid)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaid,
                options,
            ]
        )

        self.zaid: typing.Final[types.Zaid] = zaid
        self.options: typing.Final[types.Tuple[fmult.FmultOption]] = options


@dataclasses.dataclass
class FmultBuilder:
    """
    Builds ``Fmult``.

    Attributes:
        zaid: Nuclide for which data are entered.
        options: Dictionary of options.
    """

    zaid: str | types.Zaid
    options: list[str] | list[fmult.FmultOption] = None

    def build(self):
        """
        Builds ``FmultBuilder`` into ``Fmult``.

        Returns:
            ``Fmult`` for ``FmultBuilder``.
        """

        if isinstance(self.zaid, types.Zaid):
            zaid = self.zaid
        elif isinstance(self.zaid, str):
            zaid = types.Zaid.from_mcnp(self.zaid)

        options = []
        for item in self.options:
            if isinstance(item, fmult.FmultOption):
                options.append(item)
            elif isinstance(item, str):
                options.append(fmult.FmultOption.from_mcnp(item))
            else:
                options.append(item.build())
        options = types.Tuple(options)

        return Fmult(
            zaid=zaid,
            options=options,
        )

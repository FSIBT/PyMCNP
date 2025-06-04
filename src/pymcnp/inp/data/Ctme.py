import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ctme(DataOption):
    """
    Represents INP ctme elements.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    _KEYWORD = 'ctme'

    _ATTRS = {
        'tme': types.Integer,
    }

    _REGEX = re.compile(rf'\Actme( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, tme: types.Integer):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if tme is None or not (tme.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tme)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tme,
            ]
        )

        self.tme: typing.Final[types.Integer] = tme


@dataclasses.dataclass
class CtmeBuilder:
    """
    Builds ``Ctme``.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    tme: str | int | types.Integer

    def build(self):
        """
        Builds ``CtmeBuilder`` into ``Ctme``.

        Returns:
            ``Ctme`` for ``CtmeBuilder``.
        """

        tme = self.tme
        if isinstance(self.tme, types.Integer):
            tme = self.tme
        elif isinstance(self.tme, int):
            tme = types.Integer(self.tme)
        elif isinstance(self.tme, str):
            tme = types.Integer.from_mcnp(self.tme)

        return Ctme(
            tme=tme,
        )

    @staticmethod
    def unbuild(ast: Ctme):
        """
        Unbuilds ``Ctme`` into ``CtmeBuilder``

        Returns:
            ``CtmeBuilder`` for ``Ctme``.
        """

        return Ctme(
            tme=copy.deepcopy(ast.tme),
        )

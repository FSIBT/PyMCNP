import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fu(DataOption):
    """
    Represents INP fu elements.

    Attributes:
        suffix: Data card option suffix.
        bounds: Input parameters for user bins.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    _KEYWORD = 'fu'

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        'nt': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\Afu(\d+)((?: {types.Real._REGEX.pattern})+?)(?: (nt))?(?: (c))?\Z')

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.Real],
        nt: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``Fu``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Input parameters for user bins.
            nt: Notation to inhibit automatic totaling.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if bounds is None or not (filter(lambda entry: not (entry > -1), bounds)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)
        if nt is not None and nt not in {'nt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nt)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, c)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
                nt,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
        self.nt: typing.Final[types.String] = nt
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class FuBuilder:
    """
    Builds ``Fu``.

    Attributes:
        suffix: Data card option suffix.
        bounds: Input parameters for user bins.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    bounds: list[str] | list[float] | list[types.Real]
    nt: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``FuBuilder`` into ``Fu``.

        Returns:
            ``Fu`` for ``FuBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.bounds:
            bounds = []
            for item in self.bounds:
                if isinstance(item, types.Real):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.Real(item))
                elif isinstance(item, str):
                    bounds.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        nt = self.nt
        if isinstance(self.nt, types.String):
            nt = self.nt
        elif isinstance(self.nt, str):
            nt = types.String.from_mcnp(self.nt)

        c = self.c
        if isinstance(self.c, types.String):
            c = self.c
        elif isinstance(self.c, str):
            c = types.String.from_mcnp(self.c)

        return Fu(
            suffix=suffix,
            bounds=bounds,
            nt=nt,
            c=c,
        )

    @staticmethod
    def unbuild(ast: Fu):
        """
        Unbuilds ``Fu`` into ``FuBuilder``

        Returns:
            ``FuBuilder`` for ``Fu``.
        """

        return Fu(
            suffix=copy.deepcopy(ast.suffix),
            bounds=copy.deepcopy(ast.bounds),
            nt=copy.deepcopy(ast.nt),
            c=copy.deepcopy(ast.c),
        )

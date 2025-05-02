import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Filter(PtracOption):
    """
    Represents INP filter elements.

    Attributes:
        variables: MCNP6 variables for filtering.
    """

    _ATTRS = {
        'variables': types.Tuple[types.PtracFilter],
    }

    _REGEX = re.compile(rf'\Afilter((?: {types.PtracFilter._REGEX.pattern})+?)\Z')

    def __init__(self, variables: types.Tuple[types.PtracFilter]):
        """
        Initializes ``Filter``.

        Parameters:
            variables: MCNP6 variables for filtering.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if variables is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, variables)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                variables,
            ]
        )

        self.variables: typing.Final[types.Tuple[types.PtracFilter]] = variables


@dataclasses.dataclass
class FilterBuilder:
    """
    Builds ``Filter``.

    Attributes:
        variables: MCNP6 variables for filtering.
    """

    variables: list[str] | list[types.PtracFilter]

    def build(self):
        """
        Builds ``FilterBuilder`` into ``Filter``.

        Returns:
            ``Filter`` for ``FilterBuilder``.
        """

        variables = []
        for item in self.variables:
            if isinstance(item, types.PtracFilter):
                variables.append(item)
            elif isinstance(item, str):
                variables.append(types.PtracFilter.from_mcnp(item))
            else:
                variables.append(item.build())
        variables = types.Tuple(variables)

        return Filter(
            variables=variables,
        )

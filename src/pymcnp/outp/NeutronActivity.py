import re
import typing

from . import _block
from .. import types
from .. import errors


class NeutronActivity(_block.Block):
    """
    Represents OUTP `1neutron activity in each cell` blocks.

    Attributes:
        cells: Activity table.
        total_tracks: Total trackes entering.
        total_population: Total population.
        total_collisions: Total collisions.
        total_weighted_collisions: Total weighted collisions per history.
    """

    _REGEX = re.compile(
        r'\A1neutron  activity in each cell                                                                         print table 126\n\n'
        r'                       tracks     population   collisions   collisions     number        flux        average      average\n'
        r'              cell    entering                               [*] weight     weighted     weighted   track weight   track mfp\n'
        r'                                                          [(]per history[)]    energy       energy     [(]relative[)]      [(]cm[)]\n\n'
        r'((?:.+\n)+)\n'
        r'           total    (.{10})    (.{9})   (.{10})    (.{10})\Z'
    )

    def __init__(
        self,
        cells: types.String,
        total_tracks: types.String,
        total_population: types.String,
        total_collisions: types.String,
        total_weighted_collisions: types.String,
    ):
        """
        Initializes `NeutronActivity`.

        Parameters:
            cells: Activity table.
            total_tracks: Total trackes entering.
            total_population: Total population.
            total_collisions: Total collisions.
            total_weighted_collisions: Total weighted collisions per history.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if cells is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, cells)
        if total_tracks is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total_tracks)
        if total_population is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total_population)
        if total_collisions is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total_collisions)
        if total_weighted_collisions is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total_weighted_collisions)

        self.cells: typing.Final[types.String] = cells
        self.total_tracks: typing.Final[types.String] = total_tracks
        self.total_population: typing.Final[types.String] = total_population
        self.total_collisions: typing.Final[types.String] = total_collisions
        self.total_weighted_collisions: typing.Final[types.String] = total_weighted_collisions

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `NeutronActivity` from OUTP.

        Parameters:
            source: OUTP for `NeutronActivity`.

        Returns:
            `NeutronActivity`.
        """

        tokens = NeutronActivity._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        cells = types.String.from_mcnp(tokens[1])
        total_tracks = types.String.from_mcnp(tokens[2])
        total_population = types.String.from_mcnp(tokens[3])
        total_collisions = types.String.from_mcnp(tokens[4])
        total_weighted_collisions = types.String.from_mcnp(tokens[5])

        return NeutronActivity(
            cells,
            total_tracks,
            total_population,
            total_collisions,
            total_weighted_collisions,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `NeutronActivity`.

        Returns:
            OUTP for `NeutronActivity`.
        """

        return f"""
1neutron  activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

{self.cells}
           total    {self.total_tracks:10}    {self.total_population:10}  {self.total_collisions:10}    {self.total_weighted_collisions:10}
"""[1:-1]

import re

from . import _block
from .. import types
from .. import errors
from .. import _fields


class NeutronActivity(_fields.Fields, _block.Block):
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

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SEMANTICS_TABLE

    cells = _fields.Field(types.String, 'Activity table')
    total_tracks = _fields.Field(types.String, 'Total trackes entering')
    total_population = _fields.Field(types.String, 'Total population')
    total_collisions = _fields.Field(types.String, 'Total collisions')
    total_weighted_collisions = _fields.Field(types.String, 'Total weighted collisions per history')

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

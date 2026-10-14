from __future__ import annotations
import re

from . import _block
from .. import types
from .. import errors
from .. import _fields


class Header(_fields.Fields, _block.Block):
    """
    Represents MESHTAL header blocks.

    Attributes:
        code: Simulation name.
        version: Simulation version.
        ld: Simulation load date.
        probid: Simulation problem identification description.
        title: Simulation title.
        histories: Number of histories used.
        number: Mesh tally number.
        particle: Mesh tally particle type.
        bins_x: Mesh tally x-direction bins.
        bins_y: Mesh tally y-direction bins.
        bins_z: Mesh tally z-direction bins.
        bins_energy: Mesh tally energy bins.
        bins_time: Mesh tally time bins.
        columns: Tallies heading.
    """

    _REGEX = re.compile(
        r'\A(.{7})version (.{6})ld=(.{10})probid =(.{20})\n\s([^\n]+)\n\sNumber of histories used for normalizing tallies =(.{17})\n\n\sMesh Tally Number(.{10})\n\s(.{8}) mesh tally[.]\n\n Tally bin boundaries:\n((?:    .+\n)+)\n(.+)\n\Z',
        re.IGNORECASE,
    )

    _ERROR = errors.MeshtalError
    _CODE = errors.MeshtalCode.SEMANTICS_BLOCK
    _ORDER = ('code', 'version', 'ld', 'probid', 'title', 'histories', 'number', 'particle', 'columns', 'bins_x', 'bins_y', 'bins_z', 'bins_energy', 'bins_time')

    code = _fields.Field(types.String, 'Simulation name')
    version = _fields.Field(types.String, 'Simulation version')
    ld = _fields.Field(types.String, 'Simulation load date')
    probid = _fields.Field(types.String, 'Simulation problem identification description')
    title = _fields.Field(types.String, 'Simulation title')
    histories = _fields.Field(types.Integer, 'Number of histories used')
    number = _fields.Field(types.Integer, 'Mesh tally number')
    particle = _fields.Field(types.String, 'Mesh tally particle type')
    bins_x = _fields.Field(types.String, 'Mesh tally x-direction bins', optional=True)
    bins_y = _fields.Field(types.String, 'Mesh tally y-direction bins', optional=True)
    bins_z = _fields.Field(types.String, 'Mesh tally z-direction bins', optional=True)
    bins_energy = _fields.Field(types.String, 'Mesh tally energy bins', optional=True)
    bins_time = _fields.Field(types.String, 'Mesh tally time bins', optional=True)
    columns = _fields.Field(types.String, 'Tallies heading')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Header` from MESHTAL.

        Parameters:
            source: MESHTAL for `Header`.

        Returns:
            `Header`.

        Raises:
            PtracError: SYNTAX_BLOCK.
        """

        tokens = Header._REGEX.match(source)

        if not tokens:
            raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_BLOCK, source)

        code = types.String.from_mcnp(tokens[1])
        version = types.String.from_mcnp(tokens[2])
        ld = types.String.from_mcnp(tokens[3])
        probid = types.String.from_mcnp(tokens[4])
        title = types.String.from_mcnp(tokens[5])
        histories = types.Integer.from_mcnp(tokens[6])
        number = types.Integer.from_mcnp(tokens[7])
        particle = types.String.from_mcnp(tokens[8])

        bins_x = None
        bins_y = None
        bins_z = None
        bins_energy = None
        bins_time = None
        for match in re.findall(r'\s+([^\n:]+):([^\n]+)(?:\n|\Z)', tokens[9]):
            if match[0] == 'X direction':
                bins_x = match[1]
            elif match[0] == 'Y direction':
                bins_y = match[1]
            elif match[0] == 'Z direction':
                bins_z = match[1]
            elif match[0] == 'Energy bin boundaries':
                bins_energy = match[1]
            elif match[0] == 'Time bin boundaries':
                bins_time = match[1]
            else:
                raise errors.MeshtalError(errors.MeshtalCode.SYNTAX_BLOCK, source)

        columns = types.String.from_mcnp(tokens[10])

        return Header(
            code,
            version,
            ld,
            probid,
            title,
            histories,
            number,
            particle,
            columns,
            bins_x=bins_x,
            bins_y=bins_y,
            bins_z=bins_z,
            bins_energy=bins_energy,
            bins_time=bins_time,
        )

    def to_mcnp(self):
        """
        Generates MESTHAL from `Header`.

        Returns:
            INP for `Header`.
        """

        bins = ''
        bins += f'    X direction:{"".join(map(str, self.bins_x))}\n' if self.bins_x else ''
        bins += f'    Y direction:{"".join(map(str, self.bins_y))}\n' if self.bins_y else ''
        bins += f'    Z direction:{"".join(map(str, self.bins_z))}\n' if self.bins_z else ''
        bins += f'    Time bin boundaries:{"".join(map(str, self.bins_time))}\n' if self.bins_time else ''
        bins += f'    Energy bin boundaries:{"".join(map(str, self.bins_energy))}\n' if self.bins_energy else ''

        return f'{self.code:>7}version {self.version:>6}ld={self.ld:>10}probid ={self.probid:>20}\n {self.title}\n Number of histories used for normalizing tallies ={self.histories:>17.2F}\n\n Mesh Tally Number{self.number:>10}\n {self.particle:>8} mesh tally.\n\n Tally bin boundaries:\n{bins}\n{self.columns}\n'

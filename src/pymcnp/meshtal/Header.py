from __future__ import annotations
import re
import typing

from . import _block
from .. import types
from .. import errors


class Header(_block.Block):
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

    def __init__(
        self,
        code: types.String,
        version: types.String,
        ld: types.String,
        probid: types.String,
        title: types.String,
        histories: types.Integer,
        number: types.Integer,
        particle: types.String,
        columns: types.String,
        bins_x: types.String = None,
        bins_y: types.String = None,
        bins_z: types.String = None,
        bins_energy: types.String = None,
        bins_time: types.String = None,
    ):
        """
        Initializes `Header`.

        Parameters:
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

        Raises:
            PtracError: SEMANTICS_BLOCK.
        """

        if code is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, code)

        if version is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, version)

        if ld is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, ld)

        if probid is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, probid)

        if title is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, title)

        if histories is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, histories)

        if number is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, number)

        if particle is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, particle)

        if columns is None:
            raise errors.MeshtalError(errors.MeshtalCode.SEMANTICS_BLOCK, columns)

        self.code: typing.Final[types.String] = code
        self.version: typing.Final[types.String] = version
        self.ld: typing.Final[types.String] = ld
        self.probid: typing.Final[types.String] = probid
        self.title: typing.Final[types.String] = title
        self.histories: typing.Final[types.Integer] = histories
        self.number: typing.Final[types.Integer] = number
        self.particle: typing.Final[types.String] = particle
        self.bins_x: typing.Final[types.String] = bins_x
        self.bins_y: typing.Final[types.String] = bins_y
        self.bins_z: typing.Final[types.String] = bins_z
        self.bins_energy: typing.Final[types.String] = bins_energy
        self.bins_time: typing.Final[types.String] = bins_time
        self.columns: typing.Final[types.String] = columns

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

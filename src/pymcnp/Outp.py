import re
import typing

import pandas

from . import outp
from .utils import types
from .utils import errors
from .utils import _object


class Outp(_object.McnpFile):
    """
    Represents OUTP files.

    Attributes:
        header: OUPT header.
        blocks: OUTP tables.
        footer: OUTP footer.
    """

    _REGEX = re.compile(rf'\A({outp.Header._REGEX.pattern[2:-2]})([\s\S]*)\Z')

    def __init__(
        self,
        header: outp.Header,
        blocks: types.Tuple[outp.Block],
    ):
        """
        Initializes ``Outp``.

        Parameters:
            header: OUPT header.
            blocks: OUTP tables.
            footer: OUTP footer.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if header is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, header)

        if blocks is None or None in blocks:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, blocks)

        self.header: typing.Final[outp.Header] = header
        self.blocks: typing.Final[types.Tuple[outp.Block]] = blocks

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Outp`` from OUTP.

        Parameters:
            source: OUTP for ``Outp``.

        Returns:
            ``Outp``.
        """

        tokens = re.split(r'(\n\d)', source)

        if len(tokens) > 2:
            header = outp.Header.from_mcnp(tokens[0] + '\n')
            tokens[1] = '1' + ''.join(filter(bool, tokens[1:]))
        else:
            header = outp.Header.from_mcnp(tokens[0])
            tokens.append('')

        blocks = []
        for subsource in outp.Block._REGEX.finditer(tokens[1]):
            for subclass in outp.Block.__subclasses__():
                try:
                    if block := subclass.from_mcnp(subsource[0]):
                        break
                except Exception:
                    continue

            blocks.append(block)

        blocks = types.Tuple(blocks)

        return Outp(
            header,
            blocks,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``Outp``.

        Returns:
            OUTP for ``Outp``.
        """

        return self.header.to_mcnp() + '\n'.join(map(str, self.blocks))

    def to_dataframe(self):
        """
        Generates ``pandas.DataFrame`` from ``Outp``.

        Returns:
            Tuple of ``pandas.DataFrame``.
        """

        tallynps1 = {}
        tallynps2 = {}
        tallynps4 = {}

        for block in self.blocks:
            if isinstance(block, outp.TallyNps1):
                tallynps1[block.tally] = {subtally.surface: map(float, subtally.tallies.split('\n')) for subtally in block.subtallies}
            elif isinstance(block, outp.TallyNps2):
                tallynps2[block.tally] = {subtally.surface: map(float, subtally.tallies.split('\n')) for subtally in block.subtallies}
            elif isinstance(block, outp.TallyNps4):
                tallynps4[block.tally] = {subtally.cell: map(float, subtally.energies.split('\n')) for subtally in block.subtallies}
            else:
                continue

        return (
            pandas.DataFrame(tallynps1) if tallynps1 else None,
            pandas.DataFrame(tallynps2) if tallynps2 else None,
            pandas.DataFrame(tallynps4) if tallynps4 else None,
        )

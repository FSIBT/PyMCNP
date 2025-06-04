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

    _REGEX = re.compile(
        rf'\A({outp.Header._REGEX.pattern[2:-2]})'
        r'([\s\S]*)'
        rf'({outp.Footer._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(
        self,
        header: outp.Header,
        blocks: types.Tuple[outp.Block],
        footer: outp.Footer,
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

        if footer is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, footer)

        self.header: typing.Final[outp.Header] = header
        self.blocks: typing.Final[types.Tuple[outp.Block]] = blocks
        self.footer: typing.Final[outp.Footer] = footer

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Outp`` from OUTP.

        Parameters:
            source: OUTP for ``Outp``.

        Returns:
            ``Outp``.
        """

        tokens = Outp._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        offset = 0
        header = outp.Header.from_mcnp(tokens[1 + offset])
        offset += outp.Header._REGEX.groups

        blocks = []
        for subsource in outp.Block._REGEX.finditer(tokens[2 + offset]):
            for subclass in outp.Block.__subclasses__():
                try:
                    if block := subclass.from_mcnp(subsource[0]):
                        break
                    else:
                        continue
                except Exception:
                    continue
            else:
                raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

            blocks.append(block)

        blocks = types.Tuple(blocks)
        footer = outp.Footer.from_mcnp(tokens[3 + offset])

        return Outp(
            header,
            blocks,
            footer,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``Outp``.

        Returns:
            OUTP for ``Outp``.
        """

        return f'{self.header}\n{"\n".join(map(str, self.blocks))}{self.footer}'

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
                tallynps1[block.tally] = block
            elif isinstance(block, outp.TallyNps2):
                tallynps2[block.tally] = block
            elif isinstance(block, outp.TallyNps4):
                tallynps4[block.tally] = block
            else:
                continue

        return (
            pandas.DataFrame(tallynps1),
            pandas.DataFrame(tallynps2),
            pandas.DataFrame(tallynps4),
        )

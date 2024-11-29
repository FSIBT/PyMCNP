"""
Contains classes representing INP files.
"""

import re
from typing import Final

import pathlib

from .comment import Comment
from .cell import Cell
from .surface import Surface
from .surface_mnemonic import SurfaceMnemonic
from .surface_cards import P
from .surface_cards import Px
from .surface_cards import Py
from .surface_cards import Pz
from .surface_cards import So
from .surface_cards import S
from .surface_cards import Sx
from .surface_cards import Sy
from .surface_cards import Sz
from .surface_cards import C_x
from .surface_cards import C_y
from .surface_cards import C_z
from .surface_cards import Cx
from .surface_cards import Cy
from .surface_cards import Cz
from .surface_cards import K_x
from .surface_cards import K_y
from .surface_cards import K_z
from .surface_cards import Kx
from .surface_cards import Ky
from .surface_cards import Sq
from .surface_cards import Gq
from .surface_cards import Tx
from .surface_cards import Ty
from .surface_cards import Tz
from .surface_cards import X
from .surface_cards import Y
from .surface_cards import Z
from .surface_cards import Box
from .surface_cards import Rpp
from .surface_cards import Sph
from .surface_cards import Rcc
from .surface_cards import Rhp
from .surface_cards import Rec
from .surface_cards import Trc
from .surface_cards import Ell
from .surface_cards import Wed
from .surface_cards import Arb
from .data import Data
from .data import _Placeholder
from .data_mnemonic import DataMnemonic
from .data_cards import Area
from .data_cards import U
from .data_cards import Lat
from .data_cards import Fill
from .data_cards import Uran
from .data_cards import Dm
from .data_cards import Embed
from .data_cards import Embee
from .data_cards import Embeb
from .data_cards import Embem
from .data_cards import Embtb
from .data_cards import Embtm
from .data_cards import Embdb
from .data_cards import Embdf
from .data_cards import M
from .data_cards import Mt
from .data_cards import Otfdb
from .data_cards import Nonu
from .data_cards import Awtab
from .data_cards import Xs
from .data_cards import Void
from .data_cards import Mgopt
from .data_cards import Drxs
from .data_cards import Mode
from .data_cards import Act
from .data_cards import Cut
from .data_cards import Elpt
from .data_cards import Thtme
from .data_cards import Lca
from .data_cards import Lcb
from .data_cards import Lcc
from .data_cards import Lae
from .data_cards import Leb
from .data_cards import Fmult
from .data_cards import Tropt
from .data_cards import Unc
from .data_cards import Cosyp
from .data_cards import Cosy
from .data_cards import Bfld
from .data_cards import Bflcl
from .data_cards import Sdef
from .data_cards import Sc
from .data_cards import Ssr
from .data_cards import Kcode
from .data_cards import Ksrc
from .data_cards import Kopts
from .data_cards import Hsrc
from .data_cards import Nps
from .data_cards import Rand
from ..utils import errors
from ..utils import _parser
from ..utils import _object


class Inp(_object.PyMcnpFileObject):
    """
    Represents INP files.

    ``Inp`` implements ``_object.PyMcnpFileObject``.

    Attributes:
        message: INP message.
        title: INP title.
        cells: INP cell card block.
        cells_comments: INP cell card block comments.
        surfaces: INP surface card block.
        surfaces_comments: INP surface card block comments.
        data_geometry: INP data card block geometry section.
        data_material: INP data card block material section.
        data_physics: INP data card block physics section.
        data_source: INP data card block source section.
        data_tally: INP data card block tally section.
        data_variance: INP data card block variance section.
        data_micellaneous: INP data card block micellaneous section.
        data_comments: INP data card block comments.
        other: INP other block.
    """

    def __init__(
        self,
        title: str,
        cells: dict[int, Cell],
        cells_comments: dict[Comment],
        surfaces: dict[int, Surface],
        surfaces_comments: dict[Comment],
        data_geometry: dict[int, Data],
        data_material: dict[int, Data],
        data_physics: dict[int, Data],
        data_source: dict[int, Data],
        data_tally: dict[int, Data],
        data_variance: dict[int, Data],
        data_micellaneous: dict[int, Data],
        data_comments: tuple[Comment],
        message: str = '',
        other: str = '',
    ):
        """
        Initializes ``Inp``.

        Parameters:
            message: INP message.
            title: INP title.
            cells: INP cell card block.
            cells_comments: INP cell card block comments.
            surfaces: INP surface card block.
            surfaces_comments: INP surface card block comments.
            data_geometry: INP data card block geometry section.
            data_material: INP data card block material section.
            data_physics: INP data card block physics section.
            data_source: INP data card block source section.
            data_tally: INP data card block tally section.
            data_variance: INP data card block variance section.
            data_micellaneous: INP data card block micellaneous section.
            data_comments: INP data card block comments.
            other: INP other block.

        Raises:
            McnpError: INVALID_INP_MESSAGE.
            McnpError: INVALID_INP_TITLE.
            McnpError: INVALID_INP_COMMENTS.
            McnpError: INVALID_INP_CELLS.
            McnpError: INVALID_INP_SURFACES.
            McnpError: INVALID_INP_DATA.
            McnpError: INVALID_INP_OTHER.
        """

        if message is None:
            raise errors.McnpError(errors.McnoCodes.INVALID_INP_MESSAGE, info=message)

        if title is None or not len(title) < 80:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_TITLE, info=title)

        if cells is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_CELLS, info=cells)

        for key, card in cells.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_CELLS, info=cells)

        if cells_comments is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_COMMENTS, info=cells_comments)

        for card in cells_comments:
            if card is None:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_COMMENTS, info=cells_comments)

        if surfaces is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_SURFACES, info=surfaces)

        for key, card in surfaces.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_SURFACES, info=surfaces)

        if surfaces_comments is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_COMMENTS, info=surfaces_comments)

        for card in surfaces_comments:
            if card is None:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_COMMENTS, info=surfaces_comments)

        if data_geometry is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_geometry)

        for key, card in data_geometry.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_geometry)

        if data_material is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_material)

        for key, card in data_material.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_material)

        if data_physics is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_physics)

        for key, card in data_physics.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_physics)

        if data_source is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_source)

        for key, card in data_source.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_source)

        if data_tally is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_tally)

        for key, card in data_tally.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_tally)

        if data_variance is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_variance)

        for key, card in data_variance.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_variance)

        if data_micellaneous is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_micellaneous)

        for key, card in data_micellaneous.items():
            if card is None or card.ident != key:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_DATA, info=data_micellaneous)

        if data_comments is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_COMMENTS, info=data_comments)

        for card in data_comments:
            if card is None:
                raise errors.McnpError(errors.McnpCode.INVALID_INP_COMMENTS, info=data_comments)

        if other is None:
            raise errors.McnpError(errors.McnpCode.INVALID_INP_OTHER, info=other)

        self.title: Final[str] = title
        self.cells: Final[dict[int, Cell]] = cells
        self.cells_comments: Final[tuple[Comment]] = cells_comments
        self.surfaces: Final[dict[int, Surface]] = surfaces
        self.surfaces_comments: Final[tuple[Comment]] = surfaces_comments
        self.data_geometry: Final[dict[int, Data]] = data_geometry
        self.data_material: Final[dict[int, Data]] = data_material
        self.data_physics: Final[dict[int, Data]] = data_physics
        self.data_source: Final[dict[int, Data]] = data_source
        self.data_tally: Final[dict[int, Data]] = data_tally
        self.data_variance: Final[dict[int, Data]] = data_variance
        self.data_micellaneous: Final[dict[int, Data]] = data_micellaneous
        self.data_comments: Final[tuple[Comment]] = data_comments
        self.message: Final[str] = message
        self.other: Final[str] = other

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Inp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Inp``.

        Returns:
            ``Inp`` object.

        Raises:
            McnpError: EXPECTED_TOKEN.
            McnpError: UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        lines = _parser.Parser(
            source.split('\n'),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        # Processing Message & Title
        message = lines.popl()[:9] if lines.peekl()[:9] == 'message:' else ''
        title = lines.popl()

        # Processing Cell Cards
        cells = {}
        cells_comments = []
        while lines and lines.peekl() != '':
            line = lines.popl()

            if re.match(r'c[^a-zA-Z]*', line):
                cells_comments.append(Comment.from_mcnp(line))
            else:
                card = Cell.from_mcnp(line)
                cells[card.ident] = card

        lines.popl()

        # Processing Surface Cards
        surfaces = {}
        surfaces_comments = []
        while lines and lines.peekl() != '':
            line = lines.popl()

            if re.match(r'c[^a-zA-Z]*', line):
                surfaces_comments.append(Comment.from_mcnp(line))
            else:
                mnemonic = re.search(r'[a-zA-z*]+', line)
                mnemonic = mnemonic.group() if mnemonic else ''
                mnemonic = SurfaceMnemonic.from_mcnp(mnemonic)

                match mnemonic:
                    case SurfaceMnemonic.P:
                        card = P.from_mcnp(line)
                    case SurfaceMnemonic.PX:
                        card = Px.from_mcnp(line)
                    case SurfaceMnemonic.PY:
                        card = Py.from_mcnp(line)
                    case SurfaceMnemonic.PZ:
                        card = Pz.from_mcnp(line)
                    case SurfaceMnemonic.SO:
                        card = So.from_mcnp(line)
                    case SurfaceMnemonic.S:
                        card = S.from_mcnp(line)
                    case SurfaceMnemonic.SX:
                        card = Sx.from_mcnp(line)
                    case SurfaceMnemonic.SY:
                        card = Sy.from_mcnp(line)
                    case SurfaceMnemonic.SZ:
                        card = Sz.from_mcnp(line)
                    case SurfaceMnemonic.C_X:
                        card = C_x.from_mcnp(line)
                    case SurfaceMnemonic.C_Y:
                        card = C_y.from_mcnp(line)
                    case SurfaceMnemonic.C_Z:
                        card = C_z.from_mcnp(line)
                    case SurfaceMnemonic.CX:
                        card = Cx.from_mcnp(line)
                    case SurfaceMnemonic.CY:
                        card = Cy.from_mcnp(line)
                    case SurfaceMnemonic.CZ:
                        card = Cz.from_mcnp(line)
                    case SurfaceMnemonic.K_X:
                        card = K_x.from_mcnp(line)
                    case SurfaceMnemonic.K_Y:
                        card = K_y.from_mcnp(line)
                    case SurfaceMnemonic.K_Z:
                        card = K_z.from_mcnp(line)
                    case SurfaceMnemonic.KX:
                        card = Kx.from_mcnp(line)
                    case SurfaceMnemonic.KY:
                        card = Ky.from_mcnp(line)
                    case SurfaceMnemonic.KZ:
                        card = Kx.from_mcnp(line)
                    case SurfaceMnemonic.SQ:
                        card = Sq.from_mcnp(line)
                    case SurfaceMnemonic.GQ:
                        card = Gq.from_mcnp(line)
                    case SurfaceMnemonic.TX:
                        card = Tx.from_mcnp(line)
                    case SurfaceMnemonic.TY:
                        card = Ty.from_mcnp(line)
                    case SurfaceMnemonic.TZ:
                        card = Tz.from_mcnp(line)
                    case SurfaceMnemonic.X:
                        card = X.from_mcnp(line)
                    case SurfaceMnemonic.Y:
                        card = Y.from_mcnp(line)
                    case SurfaceMnemonic.Z:
                        card = Z.from_mcnp(line)
                    case SurfaceMnemonic.BOX:
                        card = Box.from_mcnp(line)
                    case SurfaceMnemonic.RPP:
                        card = Rpp.from_mcnp(line)
                    case SurfaceMnemonic.SPH:
                        card = Sph.from_mcnp(line)
                    case SurfaceMnemonic.RCC:
                        card = Rcc.from_mcnp(line)
                    case SurfaceMnemonic.RHP:
                        card = Rhp.from_mcnp(line)
                    case SurfaceMnemonic.REC:
                        card = Rec.from_mcnp(line)
                    case SurfaceMnemonic.TRC:
                        card = Trc.from_mcnp(line)
                    case SurfaceMnemonic.ELL:
                        card = Ell.from_mcnp(line)
                    case SurfaceMnemonic.WED:
                        card = Wed.from_mcnp(line)
                    case SurfaceMnemonic.ARB:
                        card = Arb.from_mcnp(line)

                surfaces[card.ident] = card

        lines.popl()

        # Processing Data Cards
        data_geometry = {}
        data_material = {}
        data_physics = {}
        data_source = {}
        data_tally = {}
        data_variance = {}
        data_micellaneous = {}
        data_comments = []

        while lines and lines.peekl() != '':
            line = lines.popl()

            if re.match(r'c[^a-zA-Z]*', line):
                data_comments.append(Comment.from_mcnp(line))
            else:
                mnemonic = re.search(r'[a-zA-z*]+', line)
                mnemonic = mnemonic.group() if mnemonic else ''
                mnemonic = DataMnemonic.from_mcnp(mnemonic)

                match mnemonic:
                    case DataMnemonic.AREA:
                        card = Area.from_mcnp(line)
                    case DataMnemonic.U:
                        card = U.from_mcnp(line)
                    case DataMnemonic.LAT:
                        card = Lat.from_mcnp(line)
                    case DataMnemonic.FILL:
                        card = Fill.from_mcnp(line)
                    case DataMnemonic.URAN:
                        card = Uran.from_mcnp(line)
                    case DataMnemonic.DM:
                        card = Dm.from_mcnp(line)
                    case DataMnemonic.EMBED:
                        card = Embed.from_mcnp(line)
                    case DataMnemonic.EMBEE:
                        card = Embee.from_mcnp(line)
                    case DataMnemonic.EMBEE:
                        card = Embee.from_mcnp(line)
                    case DataMnemonic.EMBEB:
                        card = Embeb.from_mcnp(line)
                    case DataMnemonic.EMBEM:
                        card = Embem.from_mcnp(line)
                    case DataMnemonic.EMBTB:
                        card = Embtb.from_mcnp(line)
                    case DataMnemonic.EMBTM:
                        card = Embtm.from_mcnp(line)
                    case DataMnemonic.EMBDB:
                        card = Embdb.from_mcnp(line)
                    case DataMnemonic.EMBDF:
                        card = Embdf.from_mcnp(line)
                    case DataMnemonic.M:
                        card = M.from_mcnp(line)
                    case DataMnemonic.MT:
                        card = Mt.from_mcnp(line)
                    case DataMnemonic.OTFDB:
                        card = Otfdb.from_mcnp(line)
                    case DataMnemonic.NONU:
                        card = Nonu.from_mcnp(line)
                    case DataMnemonic.AWTAB:
                        card = Awtab.from_mcnp(line)
                    case DataMnemonic.XS:
                        card = Xs.from_mcnp(line)
                    case DataMnemonic.VOID:
                        card = Void.from_mcnp(line)
                    case DataMnemonic.MGOPT:
                        card = Mgopt.from_mcnp(line)
                    case DataMnemonic.DRXS:
                        card = Drxs.from_mcnp(line)
                    case DataMnemonic.MODE:
                        card = Mode.from_mcnp(line)
                    case DataMnemonic.ACT:
                        card = Act.from_mcnp(line)
                    case DataMnemonic.CUT:
                        card = Cut.from_mcnp(line)
                    case DataMnemonic.ELPT:
                        card = Elpt.from_mcnp(line)
                    case DataMnemonic.THTME:
                        card = Thtme.from_mcnp(line)
                    case DataMnemonic.LCA:
                        card = Lca.from_mcnp(line)
                    case DataMnemonic.LCB:
                        card = Lcb.from_mcnp(line)
                    case DataMnemonic.LCC:
                        card = Lcc.from_mcnp(line)
                    case DataMnemonic.LEA:
                        card = Lae.from_mcnp(line)
                    case DataMnemonic.LEB:
                        card = Leb.from_mcnp(line)
                    case DataMnemonic.FMULT:
                        card = Fmult.from_mcnp(line)
                    case DataMnemonic.TROPT:
                        card = Tropt.from_mcnp(line)
                    case DataMnemonic.UNC:
                        card = Unc.from_mcnp(line)
                    case DataMnemonic.COSYP:
                        card = Cosyp.from_mcnp(line)
                    case DataMnemonic.COSY:
                        card = Cosy.from_mcnp(line)
                    case DataMnemonic.BFLD:
                        card = Bfld.from_mcnp(line)
                    case DataMnemonic.BFLCL:
                        card = Bflcl.from_mcnp(line)
                    case DataMnemonic.SDEF:
                        card = Sdef.from_mcnp(line)
                    case DataMnemonic.SC:
                        card = Sc.from_mcnp(line)
                    case DataMnemonic.SSR:
                        card = Ssr.from_mcnp(line)
                    case DataMnemonic.KCODE:
                        card = Kcode.from_mcnp(line)
                    case DataMnemonic.KSRC:
                        card = Ksrc.from_mcnp(line)
                    case DataMnemonic.KOPTS:
                        card = Kopts.from_mcnp(line)
                    case DataMnemonic.HSRC:
                        card = Hsrc.from_mcnp(line)
                    case DataMnemonic.NPS:
                        card = Nps.from_mcnp(line)
                    case DataMnemonic.RAND:
                        card = Rand.from_mcnp(line)
                    case _:
                        card = _Placeholder.from_mcnp(line)

                if card.mnemonic in Data.GEOMETRY_MNEMONICS:
                    data_geometry[card.ident] = card
                elif card.mnemonic in Data.MATERIAL_MNEMONICS:
                    data_material[card.ident] = card
                elif card.mnemonic in Data.PHYSICS_MNEMONICS:
                    data_physics[card.ident] = card
                elif card.mnemonic in Data.SOURCE_MNEMONICS:
                    data_source[card.ident] = card
                elif card.mnemonic in Data.TALLY_MNEMONICS:
                    data_tally[card.ident] = card
                elif card.mnemonic in Data.VARIENCE_MNEMONICS:
                    data_variance[card.ident] = card
                elif card.mnemonic in Data.MICELLANEOUS_MNEMONICS:
                    data_micellaneous[card.ident] = card
                else:
                    data_micellaneous[card.ident] = card

        other = ''
        while lines:
            other += lines.popl()

        return Inp(
            title,
            cells,
            tuple(cells_comments),
            surfaces,
            tuple(surfaces_comments),
            data_geometry,
            data_material,
            data_physics,
            data_source,
            data_tally,
            data_variance,
            data_micellaneous,
            tuple(data_comments),
            message=message,
            other=other,
        )

    def to_mcnp(self, makeFancy: bool = True) -> str:
        """
        Generates INP from ``Inp`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Parameters:
            makeFancy: Prettifier on/off.

        Returns:
            INP for ``Inp``.
        """

        # Appending Message
        source = self.message + '\n' if self.message else ''

        # Appending Title
        source += self.title + '\n'

        # Appending Blocks
        DELIMITER = 'c ' + '=' * 76 + '\n'

        if makeFancy:
            source += DELIMITER
            source += f'c {'cells':^76.76}\n'
            source += DELIMITER

        source += '\n'.join(card.to_mcnp() for card in self.cells.values())
        source += '\n\n'

        if makeFancy and self.surfaces:
            source += DELIMITER
            source += f'c {'surfaces':^76.76}\n'
            source += DELIMITER

        source += '\n'.join(card.to_mcnp() for card in self.surfaces.values())
        source += '\n\n'

        if self.data_geometry:
            if makeFancy:
                source += DELIMITER
                source += f'c {'geometry data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in self.data_geometry.values())
            source += '\nc\n'

        if self.data_material:
            if makeFancy:
                source += DELIMITER
                source += f'c {'material data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in self.data_material.values())
            source += '\nc\n'

        if self.data_physics:
            if makeFancy:
                source += DELIMITER
                source += f'c {'physics data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in (self.data_physics).values())
            source += '\nc\n'

        if self.data_source:
            if makeFancy:
                source += DELIMITER
                source += f'c {'source data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in (self.data_source).values())
            source += '\nc\n'

        if self.data_tally:
            if makeFancy:
                source += DELIMITER
                source += f'c {'tally data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in (self.data_tally).values())
            source += '\nc\n'

        if self.data_variance:
            if makeFancy:
                source += DELIMITER
                source += f'c {'variance data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in (self.data_variance).values())
            source += '\nc\n'

        if self.data_micellaneous:
            if makeFancy:
                source += DELIMITER
                source += f'c {'micellaneous data':^76.76}\n'
                source += DELIMITER

            source += '\n'.join(card.to_mcnp() for card in (self.data_micellaneous).values())
            source += '\n'

        # Appending Extra
        source += self.other

        return source

    @staticmethod
    def from_mcnp_file(filename: str | pathlib.Path):
        """
        Generates ``Inp`` objects from MCNP files.

        ``from_mcnp_file`` translates from MCNP files to PyMCNP.

        Parameters:
            filename: MCNP file path.

        Returns:
            ``Inp`` object.
        """

        filename = pathlib.Path(filename)
        source = filename.read_text()

        return Inp.from_mcnp(source)

    def to_mcnp_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP files from ``Inp`` objects.

        ``to_mcnp_file`` translates from PyMCNP to MCNP files.

        Parameters:
            filename: new MCNP file path.
        """

        filename = pathlib.Path(filename)
        filename.write_text(self.to_mcnp())

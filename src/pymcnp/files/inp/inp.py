"""
Contains classes representing INP files.
"""

import re
from typing import Final

import pathlib

from . import cell
from . import data
from . import surface
from .subclasses_surfaces import P
from .subclasses_surfaces import Px
from .subclasses_surfaces import Py
from .subclasses_surfaces import Pz
from .subclasses_surfaces import So
from .subclasses_surfaces import S
from .subclasses_surfaces import Sx
from .subclasses_surfaces import Sy
from .subclasses_surfaces import Sz
from .subclasses_surfaces import C_x
from .subclasses_surfaces import C_y
from .subclasses_surfaces import C_z
from .subclasses_surfaces import Cx
from .subclasses_surfaces import Cy
from .subclasses_surfaces import Cz
from .subclasses_surfaces import K_x
from .subclasses_surfaces import K_y
from .subclasses_surfaces import K_z
from .subclasses_surfaces import Kx
from .subclasses_surfaces import Ky
from .subclasses_surfaces import Sq
from .subclasses_surfaces import Gq
from .subclasses_surfaces import Tx
from .subclasses_surfaces import Ty
from .subclasses_surfaces import Tz
from .subclasses_surfaces import X
from .subclasses_surfaces import Y
from .subclasses_surfaces import Z
from .subclasses_surfaces import Box
from .subclasses_surfaces import Rpp
from .subclasses_surfaces import Sph
from .subclasses_surfaces import Rcc
from .subclasses_surfaces import Rhp
from .subclasses_surfaces import Rec
from .subclasses_surfaces import Trc
from .subclasses_surfaces import Ell
from .subclasses_surfaces import Wed
from .subclasses_surfaces import Arb
from .subclasses_data import Area
from .subclasses_data import U
from .subclasses_data import Lat
from .subclasses_data import Fill
from .subclasses_data import Uran
from .subclasses_data import Dm
from .subclasses_data import Embed
from .subclasses_data import Embee
from .subclasses_data import Embeb
from .subclasses_data import Embem
from .subclasses_data import Embtb
from .subclasses_data import Embtm
from .subclasses_data import Embdb
from .subclasses_data import Embdf
from .subclasses_data import M
from .subclasses_data import Mt
from .subclasses_data import Otfdb
from .subclasses_data import Nonu
from .subclasses_data import Awtab
from .subclasses_data import Xs
from .subclasses_data import Void
from .subclasses_data import Mgopt
from .subclasses_data import Drxs
from .subclasses_data import Mode
from .subclasses_data import Act
from .subclasses_data import Cut
from .subclasses_data import Elpt
from .subclasses_data import Thtme
from .subclasses_data import Lca
from .subclasses_data import Lcb
from .subclasses_data import Lcc
from .subclasses_data import Lae
from .subclasses_data import Leb
from .subclasses_data import Fmult
from .subclasses_data import Tropt
from .subclasses_data import Unc
from .subclasses_data import Cosyp
from .subclasses_data import Cosy
from .subclasses_data import Bfld
from .subclasses_data import Bflcl
from .subclasses_data import Sdef
from .subclasses_data import Sc
from .subclasses_data import Ssr
from .subclasses_data import Kcode
from .subclasses_data import Ksrc
from .subclasses_data import Kopts
from .subclasses_data import Hsrc
from .subclasses_data import Nps
from .subclasses_data import Rand
from . import comment
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
        cells: dict[int, cell.Cell],
        cells_comments: dict[comment.Comment],
        surfaces: dict[int, surface.Surface],
        surfaces_comments: dict[comment.Comment],
        data_geometry: dict[int, data.Data],
        data_material: dict[int, data.Data],
        data_physics: dict[int, data.Data],
        data_source: dict[int, data.Data],
        data_tally: dict[int, data.Data],
        data_variance: dict[int, data.Data],
        data_micellaneous: dict[int, data.Data],
        data_comments: tuple[comment.Comment],
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
        self.cells: Final[dict[int, cell.Cell]] = cells
        self.cells_comments: Final[tuple[comment.Comment]] = cells_comments
        self.surfaces: Final[dict[int, surface.Surface]] = surfaces
        self.surfaces_comments: Final[tuple[comment.Comment]] = surfaces_comments
        self.data_geometry: Final[dict[int, data.Data]] = data_geometry
        self.data_material: Final[dict[int, data.Data]] = data_material
        self.data_physics: Final[dict[int, data.Data]] = data_physics
        self.data_source: Final[dict[int, data.Data]] = data_source
        self.data_tally: Final[dict[int, data.Data]] = data_tally
        self.data_variance: Final[dict[int, data.Data]] = data_variance
        self.data_micellaneous: Final[dict[int, data.Data]] = data_micellaneous
        self.data_comments: Final[tuple[comment.Comment]] = data_comments
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
                cells_comments.append(comment.Comment.from_mcnp(line))
            else:
                card = cell.Cell.from_mcnp(line)
                cells[card.ident] = card

        lines.popl()

        # Processing Surface Cards
        surfaces = {}
        surfaces_comments = []
        while lines and lines.peekl() != '':
            line = lines.popl()

            if re.match(r'c[^a-zA-Z]*', line):
                surfaces_comments.append(comment.Comment.from_mcnp(line))
            else:
                mnemonic = re.search(r'[a-zA-z*]+', line)
                mnemonic = mnemonic.group() if mnemonic else ''
                mnemonic = surface.SurfaceMnemonic.from_mcnp(mnemonic)

                match mnemonic:
                    case surface.SurfaceMnemonic.P:
                        card = P.from_mcnp(line)
                    case surface.SurfaceMnemonic.PX:
                        card = Px.from_mcnp(line)
                    case surface.SurfaceMnemonic.PY:
                        card = Py.from_mcnp(line)
                    case surface.SurfaceMnemonic.PZ:
                        card = Pz.from_mcnp(line)
                    case surface.SurfaceMnemonic.SO:
                        card = So.from_mcnp(line)
                    case surface.SurfaceMnemonic.S:
                        card = S.from_mcnp(line)
                    case surface.SurfaceMnemonic.SX:
                        card = Sx.from_mcnp(line)
                    case surface.SurfaceMnemonic.SY:
                        card = Sy.from_mcnp(line)
                    case surface.SurfaceMnemonic.SZ:
                        card = Sz.from_mcnp(line)
                    case surface.SurfaceMnemonic.C_X:
                        card = C_x.from_mcnp(line)
                    case surface.SurfaceMnemonic.C_Y:
                        card = C_y.from_mcnp(line)
                    case surface.SurfaceMnemonic.C_Z:
                        card = C_z.from_mcnp(line)
                    case surface.SurfaceMnemonic.CX:
                        card = Cx.from_mcnp(line)
                    case surface.SurfaceMnemonic.CY:
                        card = Cy.from_mcnp(line)
                    case surface.SurfaceMnemonic.CZ:
                        card = Cz.from_mcnp(line)
                    case surface.SurfaceMnemonic.K_X:
                        card = K_x.from_mcnp(line)
                    case surface.SurfaceMnemonic.K_Y:
                        card = K_y.from_mcnp(line)
                    case surface.SurfaceMnemonic.K_Z:
                        card = K_z.from_mcnp(line)
                    case surface.SurfaceMnemonic.KX:
                        card = Kx.from_mcnp(line)
                    case surface.SurfaceMnemonic.KY:
                        card = Ky.from_mcnp(line)
                    case surface.SurfaceMnemonic.KZ:
                        card = Kx.from_mcnp(line)
                    case surface.SurfaceMnemonic.SQ:
                        card = Sq.from_mcnp(line)
                    case surface.SurfaceMnemonic.GQ:
                        card = Gq.from_mcnp(line)
                    case surface.SurfaceMnemonic.TX:
                        card = Tx.from_mcnp(line)
                    case surface.SurfaceMnemonic.TY:
                        card = Ty.from_mcnp(line)
                    case surface.SurfaceMnemonic.TZ:
                        card = Tz.from_mcnp(line)
                    case surface.SurfaceMnemonic.X:
                        card = X.from_mcnp(line)
                    case surface.SurfaceMnemonic.Y:
                        card = Y.from_mcnp(line)
                    case surface.SurfaceMnemonic.Z:
                        card = Z.from_mcnp(line)
                    case surface.SurfaceMnemonic.BOX:
                        card = Box.from_mcnp(line)
                    case surface.SurfaceMnemonic.RPP:
                        card = Rpp.from_mcnp(line)
                    case surface.SurfaceMnemonic.SPH:
                        card = Sph.from_mcnp(line)
                    case surface.SurfaceMnemonic.RCC:
                        card = Rcc.from_mcnp(line)
                    case surface.SurfaceMnemonic.RHP:
                        card = Rhp.from_mcnp(line)
                    case surface.SurfaceMnemonic.REC:
                        card = Rec.from_mcnp(line)
                    case surface.SurfaceMnemonic.TRC:
                        card = Trc.from_mcnp(line)
                    case surface.SurfaceMnemonic.ELL:
                        card = Ell.from_mcnp(line)
                    case surface.SurfaceMnemonic.WED:
                        card = Wed.from_mcnp(line)
                    case surface.SurfaceMnemonic.ARB:
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
                data_comments.append(comment.Comment.from_mcnp(line))
            else:
                mnemonic = re.search(r'[a-zA-z*]+', line)
                mnemonic = mnemonic.group() if mnemonic else ''
                mnemonic = data.DataMnemonic.from_mcnp(mnemonic)

                match mnemonic:
                    case data.DataMnemonic.AREA:
                        card = Area.from_mcnp(line)
                    case data.DataMnemonic.U:
                        card = U.from_mcnp(line)
                    case data.DataMnemonic.LAT:
                        card = Lat.from_mcnp(line)
                    case data.DataMnemonic.FILL:
                        card = Fill.from_mcnp(line)
                    case data.DataMnemonic.URAN:
                        card = Uran.from_mcnp(line)
                    case data.DataMnemonic.DM:
                        card = Dm.from_mcnp(line)
                    case data.DataMnemonic.EMBED:
                        card = Embed.from_mcnp(line)
                    case data.DataMnemonic.EMBEE:
                        card = Embee.from_mcnp(line)
                    case data.DataMnemonic.EMBEE:
                        card = Embee.from_mcnp(line)
                    case data.DataMnemonic.EMBEB:
                        card = Embeb.from_mcnp(line)
                    case data.DataMnemonic.EMBEM:
                        card = Embem.from_mcnp(line)
                    case data.DataMnemonic.EMBTB:
                        card = Embtb.from_mcnp(line)
                    case data.DataMnemonic.EMBTM:
                        card = Embtm.from_mcnp(line)
                    case data.DataMnemonic.EMBDB:
                        card = Embdb.from_mcnp(line)
                    case data.DataMnemonic.EMBDF:
                        card = Embdf.from_mcnp(line)
                    case data.DataMnemonic.M:
                        card = M.from_mcnp(line)
                    case data.DataMnemonic.MT:
                        card = Mt.from_mcnp(line)
                    case data.DataMnemonic.OTFDB:
                        card = Otfdb.from_mcnp(line)
                    case data.DataMnemonic.NONU:
                        card = Nonu.from_mcnp(line)
                    case data.DataMnemonic.AWTAB:
                        card = Awtab.from_mcnp(line)
                    case data.DataMnemonic.XS:
                        card = Xs.from_mcnp(line)
                    case data.DataMnemonic.VOID:
                        card = Void.from_mcnp(line)
                    case data.DataMnemonic.MGOPT:
                        card = Mgopt.from_mcnp(line)
                    case data.DataMnemonic.DRXS:
                        card = Drxs.from_mcnp(line)
                    case data.DataMnemonic.MODE:
                        card = Mode.from_mcnp(line)
                    case data.DataMnemonic.ACT:
                        card = Act.from_mcnp(line)
                    case data.DataMnemonic.CUT:
                        card = Cut.from_mcnp(line)
                    case data.DataMnemonic.ELPT:
                        card = Elpt.from_mcnp(line)
                    case data.DataMnemonic.THTME:
                        card = Thtme.from_mcnp(line)
                    case data.DataMnemonic.LCA:
                        card = Lca.from_mcnp(line)
                    case data.DataMnemonic.LCB:
                        card = Lcb.from_mcnp(line)
                    case data.DataMnemonic.LCC:
                        card = Lcc.from_mcnp(line)
                    case data.DataMnemonic.LEA:
                        card = Lae.from_mcnp(line)
                    case data.DataMnemonic.LEB:
                        card = Leb.from_mcnp(line)
                    case data.DataMnemonic.FMULT:
                        card = Fmult.from_mcnp(line)
                    case data.DataMnemonic.TROPT:
                        card = Tropt.from_mcnp(line)
                    case data.DataMnemonic.UNC:
                        card = Unc.from_mcnp(line)
                    case data.DataMnemonic.COSYP:
                        card = Cosyp.from_mcnp(line)
                    case data.DataMnemonic.COSY:
                        card = Cosy.from_mcnp(line)
                    case data.DataMnemonic.BFLD:
                        card = Bfld.from_mcnp(line)
                    case data.DataMnemonic.BFLCL:
                        card = Bflcl.from_mcnp(line)
                    case data.DataMnemonic.SDEF:
                        card = Sdef.from_mcnp(line)
                    case data.DataMnemonic.SC:
                        card = Sc.from_mcnp(line)
                    case data.DataMnemonic.SSR:
                        card = Ssr.from_mcnp(line)
                    case data.DataMnemonic.KCODE:
                        card = Kcode.from_mcnp(line)
                    case data.DataMnemonic.KSRC:
                        card = Ksrc.from_mcnp(line)
                    case data.DataMnemonic.KOPTS:
                        card = Kopts.from_mcnp(line)
                    case data.DataMnemonic.HSRC:
                        card = Hsrc.from_mcnp(line)
                    case data.DataMnemonic.NPS:
                        card = Nps.from_mcnp(line)
                    case data.DataMnemonic.RAND:
                        card = Rand.from_mcnp(line)
                    case _:
                        card = data._Placeholder.from_mcnp(line)

                if card.mnemonic in data.Data.GEOMETRY_MNEMONICS:
                    data_geometry[card.ident] = card
                elif card.mnemonic in data.Data.MATERIAL_MNEMONICS:
                    data_material[card.ident] = card
                elif card.mnemonic in data.Data.PHYSICS_MNEMONICS:
                    data_physics[card.ident] = card
                elif card.mnemonic in data.Data.SOURCE_MNEMONICS:
                    data_source[card.ident] = card
                elif card.mnemonic in data.Data.TALLY_MNEMONICS:
                    data_tally[card.ident] = card
                elif card.mnemonic in data.Data.VARIENCE_MNEMONICS:
                    data_variance[card.ident] = card
                elif card.mnemonic in data.Data.MICELLANEOUS_MNEMONICS:
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

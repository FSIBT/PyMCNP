"""
Contains the class representing INP files.

``inp`` packages the ``Inp`` class, providing an object-oriented, importable
interface for INP files.
"""

import re
import pathlib
from typing import Final

from . import cell
from . import data
from . import surface
from . import comment
from ..utils import errors
from ..utils import _parser


class Inp:
    """
    ``Inp`` represents INP files.

    ``Inp`` implements INP files as a Python class. Its attributes store
    INP blocks, and its methods provide entry points and endpoints for working
    with INP. It represents the INP file syntax element.

    Attributes:
        message: INP message.
        title: INP title.
        cells: INP cell card block.
        surfaces: INP surface card block.
        data: INP data card block.
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
        ``__init__`` initializes ``Inp``.
        """

        if message is None:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.INVALID_INP_MESSAGE)

        if title is None or not len(title) < 80:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_TITLE)

        if cells is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_CELLS)

        for key, card in cells.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_CELLS)

        if cells_comments is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_COMMENTS)

        for card in cells_comments:
            if card is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_COMMENTS)

        if surfaces is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_SURFACES)

        for key, card in surfaces.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_SURFACES)

        if surfaces_comments is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_COMMENTS)

        for card in surfaces_comments:
            if card is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_COMMENTS)

        if data_geometry is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_geometry.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if data_material is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_material.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if data_physics is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_physics.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if data_source is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_source.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if data_tally is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_tally.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if data_variance is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_variance.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if data_micellaneous is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        for key, card in data_micellaneous.items():
            if card is None or card.ident != key:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_DATA)

        if cells_comments is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_COMMENTS)

        for card in data_comments:
            if card is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_COMMENTS)

        if other is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_INP_OTHER)

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
        ``from_mcnp`` generates ``Inp`` objects from INP.

        ``from_mcnp`` constructs instances of ``Inp`` from INP source strings,
        so it operates as a class constructor method and INP parser.

        Parameters:
            source: Complete INP source string.

        Returns:
            ``Inp`` object.
        """

        source = _parser.Preprocessor.process_inp(source)
        lines = _parser.Parser(
            source.split('\n'),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_INP),
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
                        card = surface.P.from_mcnp(line)
                    case surface.SurfaceMnemonic.PX:
                        card = surface.Px.from_mcnp(line)
                    case surface.SurfaceMnemonic.PY:
                        card = surface.Py.from_mcnp(line)
                    case surface.SurfaceMnemonic.PZ:
                        card = surface.Pz.from_mcnp(line)
                    case surface.SurfaceMnemonic.SO:
                        card = surface.So.from_mcnp(line)
                    case surface.SurfaceMnemonic.S:
                        card = surface.S.from_mcnp(line)
                    case surface.SurfaceMnemonic.SX:
                        card = surface.Sx.from_mcnp(line)
                    case surface.SurfaceMnemonic.SY:
                        card = surface.Sy.from_mcnp(line)
                    case surface.SurfaceMnemonic.SZ:
                        card = surface.Sz.from_mcnp(line)
                    case surface.SurfaceMnemonic.C_X:
                        card = surface.C_x.from_mcnp(line)
                    case surface.SurfaceMnemonic.C_Y:
                        card = surface.C_y.from_mcnp(line)
                    case surface.SurfaceMnemonic.C_Z:
                        card = surface.C_z.from_mcnp(line)
                    case surface.SurfaceMnemonic.CX:
                        card = surface.Cx.from_mcnp(line)
                    case surface.SurfaceMnemonic.CY:
                        card = surface.Cy.from_mcnp(line)
                    case surface.SurfaceMnemonic.CZ:
                        card = surface.Cz.from_mcnp(line)
                    case surface.SurfaceMnemonic.K_X:
                        card = surface.K_x.from_mcnp(line)
                    case surface.SurfaceMnemonic.K_Y:
                        card = surface.K_y.from_mcnp(line)
                    case surface.SurfaceMnemonic.K_Z:
                        card = surface.K_z.from_mcnp(line)
                    case surface.SurfaceMnemonic.KX:
                        card = surface.Kx.from_mcnp(line)
                    case surface.SurfaceMnemonic.KY:
                        card = surface.Ky.from_mcnp(line)
                    case surface.SurfaceMnemonic.KZ:
                        card = surface.Kx.from_mcnp(line)
                    case surface.SurfaceMnemonic.SQ:
                        card = surface.Sq.from_mcnp(line)
                    case surface.SurfaceMnemonic.GQ:
                        card = surface.Gq.from_mcnp(line)
                    case surface.SurfaceMnemonic.TX:
                        card = surface.Tx.from_mcnp(line)
                    case surface.SurfaceMnemonic.TY:
                        card = surface.Ty.from_mcnp(line)
                    case surface.SurfaceMnemonic.TZ:
                        card = surface.Tz.from_mcnp(line)
                    case surface.SurfaceMnemonic.X:
                        card = surface.X.from_mcnp(line)
                    case surface.SurfaceMnemonic.Y:
                        card = surface.Y.from_mcnp(line)
                    case surface.SurfaceMnemonic.Z:
                        card = surface.Z.from_mcnp(line)
                    case surface.SurfaceMnemonic.BOX:
                        card = surface.Box.from_mcnp(line)
                    case surface.SurfaceMnemonic.RPP:
                        card = surface.Rpp.from_mcnp(line)
                    case surface.SurfaceMnemonic.SPH:
                        card = surface.Sph.from_mcnp(line)
                    case surface.SurfaceMnemonic.RCC:
                        card = surface.Rcc.from_mcnp(line)
                    case surface.SurfaceMnemonic.RHP:
                        card = surface.Rhp.from_mcnp(line)
                    case surface.SurfaceMnemonic.REC:
                        card = surface.Rec.from_mcnp(line)
                    case surface.SurfaceMnemonic.TRC:
                        card = surface.Trc.from_mcnp(line)
                    case surface.SurfaceMnemonic.ELL:
                        card = surface.Ell.from_mcnp(line)
                    case surface.SurfaceMnemonic.WED:
                        card = surface.Wed.from_mcnp(line)
                    case surface.SurfaceMnemonic.ARB:
                        card = surface.Arb.from_mcnp(line)

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
                        card = data.Area.from_mcnp(line)
                    case data.DataMnemonic.U:
                        card = data.U.from_mcnp(line)
                    case data.DataMnemonic.LAT:
                        card = data.Lat.from_mcnp(line)
                    case data.DataMnemonic.FILL:
                        card = data.Fill.from_mcnp(line)
                    case data.DataMnemonic.URAN:
                        card = data.Uran.from_mcnp(line)
                    case data.DataMnemonic.DM:
                        card = data.Dm.from_mcnp(line)
                    case data.DataMnemonic.EMBED:
                        card = data.Embed.from_mcnp(line)
                    case data.DataMnemonic.EMBEE:
                        card = data.Embee.from_mcnp(line)
                    case data.DataMnemonic.EMBEE:
                        card = data.Embee.from_mcnp(line)
                    case data.DataMnemonic.EMBEB:
                        card = data.Embeb.from_mcnp(line)
                    case data.DataMnemonic.EMBEM:
                        card = data.Embem.from_mcnp(line)
                    case data.DataMnemonic.EMBTB:
                        card = data.Embtb.from_mcnp(line)
                    case data.DataMnemonic.EMBTM:
                        card = data.Embtm.from_mcnp(line)
                    case data.DataMnemonic.EMBDB:
                        card = data.Embdb.from_mcnp(line)
                    case data.DataMnemonic.EMBDF:
                        card = data.Embdf.from_mcnp(line)
                    case data.DataMnemonic.M:
                        card = data.M.from_mcnp(line)
                    case data.DataMnemonic.MT:
                        card = data.Mt.from_mcnp(line)
                    case data.DataMnemonic.OTFDB:
                        card = data.Otfdb.from_mcnp(line)
                    case data.DataMnemonic.NONU:
                        card = data.Nonu.from_mcnp(line)
                    case data.DataMnemonic.AWTAB:
                        card = data.Awtab.from_mcnp(line)
                    case data.DataMnemonic.XS:
                        card = data.Xs.from_mcnp(line)
                    case data.DataMnemonic.VOID:
                        card = data.Void.from_mcnp(line)
                    case data.DataMnemonic.MGOPT:
                        card = data.Mgopt.from_mcnp(line)
                    case data.DataMnemonic.DRXS:
                        card = data.Drxs.from_mcnp(line)
                    case data.DataMnemonic.MODE:
                        card = data.Mode.from_mcnp(line)
                    case data.DataMnemonic.ACT:
                        card = data.Act.from_mcnp(line)
                    case data.DataMnemonic.CUT:
                        card = data.Cut.from_mcnp(line)
                    case data.DataMnemonic.ELPT:
                        card = data.Elpt.from_mcnp(line)
                    case data.DataMnemonic.THTME:
                        card = data.Thtme.from_mcnp(line)
                    case data.DataMnemonic.LCA:
                        card = data.Lca.from_mcnp(line)
                    case data.DataMnemonic.LCB:
                        card = data.Lbc.from_mcnp(line)
                    case data.DataMnemonic.LCC:
                        card = data.Lcc.from_mcnp(line)
                    case data.DataMnemonic.LEA:
                        card = data.Lae.from_mcnp(line)
                    case data.DataMnemonic.LEB:
                        card = data.Leb.from_mcnp(line)
                    case data.DataMnemonic.FMULT:
                        card = data.Fmult.from_mcnp(line)
                    case data.DataMnemonic.TROPT:
                        card = data.Tropt.from_mcnp(line)
                    case data.DataMnemonic.UNC:
                        card = data.Unc.from_mcnp(line)
                    case data.DataMnemonic.COSYP:
                        card = data.Cosyp.from_mcnp(line)
                    case data.DataMnemonic.COSY:
                        card = data.Cosy.from_mcnp(line)
                    case data.DataMnemonic.BFLD:
                        card = data.Bfld.from_mcnp(line)
                    case data.DataMnemonic.BFLCL:
                        card = data.Bflcl.from_mcnp(line)
                    case data.DataMnemonic.SDEF:
                        card = data.Sdef.from_mcnp(line)
                    case data.DataMnemonic.SC:
                        card = data.Sc.from_mcnp(line)
                    case data.DataMnemonic.SSR:
                        card = data.Ssr.from_mcnp(line)
                    case data.DataMnemonic.KCODE:
                        card = data.Kcode.from_mcnp(line)
                    case data.DataMnemonic.KSRC:
                        card = data.Ksrc.from_mcnp(line)
                    case data.DataMnemonic.KOPTS:
                        card = data.Kopts.from_mcnp(line)
                    case data.DataMnemonic.HSRC:
                        card = data.Hsrc.from_mcnp(line)
                    case data.DataMnemonic.NPS:
                        card = data.Nps.from_mcnp(line)
                    case data.DataMnemonic.RAND:
                        card = data.Rand.from_mcnp(line)
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

    @staticmethod
    def from_mcnp_file(filename: str | pathlib.Path):
        """
        ``from_mcnp_file`` generates ``Inp`` objects from INP files.

        ``from_mcnp_file`` constructs instances of ``Inp`` from INP files,
        so it operates as a class constructor method and INP parser.

        Parameters:
            filename: Name of file to parse.

        Returns:
            ``Inp`` object.
        """

        filename = pathlib.Path(filename)
        source = filename.read_text()

        return Inp.from_mcnp(source)

    def to_mcnp(self, comments: bool = True) -> str:
        """
        ``to_mcnp`` generates INP from ``Inp`` objects.

        ``to_mcnp`` creates INP source string from ``INP`` objects, so it
        provides an MCNP endpoint.

        Returns:
            INP string for ``Inp`` object.
        """

        # Appending Message
        source = self.message + '\n' if self.message else ''

        # Appending Title
        source += self.title + '\n'

        # Appending Blocks
        if comments and self.cells:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'cells':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in self.cells.values():
                source += f'{card.to_mcnp()}\n'

            source += '\n'

        if comments and self.surfaces:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'surfaces':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in self.surfaces.values():
                source += f'{card.to_mcnp()}\n'

            source += '\n'

        if comments and self.data_geometry:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'geometry data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_geometry).values():
                source += f'{card.to_mcnp()}\n'

            source += 'c\n'

        if comments and self.data_material:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'material data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_material).values():
                source += f'{card.to_mcnp()}\n'

            source += 'c\n'

        if comments and self.data_physics:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'physics data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_physics).values():
                source += f'{card.to_mcnp()}\n'

            source += 'c\n'

        if comments and self.data_source:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'source data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_source).values():
                source += f'{card.to_mcnp()}\n'

            source += 'c\n'

        if comments and self.data_tally:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'tally data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_tally).values():
                source += f'{card.to_mcnp()}\n'

            source += 'c\n'

        if comments and self.data_variance:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'variance data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_variance).values():
                source += f'{card.to_mcnp()}\n'

            source += 'c\n'

        if comments and self.data_micellaneous:
            source += (
                'c ============================================================================\n'
            )
            source += f'c {'micellaneous data':^76.76}\n'
            source += (
                'c ============================================================================\n'
            )

            for card in (self.data_micellaneous).values():
                source += f'{card.to_mcnp()}\n'

        return source

    def to_mcnp_file(self, filename: str | pathlib.Path) -> int:
        """
        ``to_mcnp`` generates INP from ``Inp`` objects.

        ``to_mcnp`` creates INP source string from ``INp`` objects, so it
        provides an MCNP endpoint.

        Parameters:
            filename: Name of file to write INP string for ``Inp`` object.

        Returns:
            Number of bytes written.
        """

        filename = pathlib.Path(filename)
        filename.write_text(self.to_mcnp())

        return 0

    def to_arguments(self) -> dict:
        """
        ``to_arguments`` makes dictionaries from ``Inp`` objects.

        ``to_arguments`` creates Python dictionaries from ``Inp`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Inp`` object.
        """

        return {
            'message': self.message,
            'title': self.title,
            'cells': {ident: card.to_arguments() for ident, card in self.cells.items()},
            'surfaces': {ident: card.to_arguments() for ident, card in self.surfaces.items()},
            'data': {
                ident: card.to_arguments()
                for ident, card in (
                    self.data_geometry
                    | self.data_material
                    | self.data_physics
                    | self.data_source
                    | self.data_tally
                    | self.data_variance
                    | self.data_micellaneous
                ).items()
            },
            'other': self.other,
        }

    def __str__(self):
        return self.to_mcnp()

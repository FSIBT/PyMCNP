import re
import collections

from . import inp
from .inp import _field
from . import _file
from . import types
from . import errors


Cell = types.Union(inp.Cell, inp.Like, inp.Comment)
Surface = types.Union(
    inp.Arb,
    inp.Box,
    inp.C_x,
    inp.C_y,
    inp.C_z,
    inp.Cx,
    inp.Cy,
    inp.Cz,
    inp.Ell,
    inp.Gq,
    inp.K_x,
    inp.K_y,
    inp.K_z,
    inp.Kx,
    inp.Ky,
    inp.Kz,
    inp.P_0,
    inp.P_1,
    inp.Px,
    inp.Py,
    inp.Pz,
    inp.Rcc,
    inp.Rec,
    inp.Rhp,
    inp.Rpp,
    inp.S,
    inp.So,
    inp.Sph,
    inp.Sq,
    inp.Sx,
    inp.Sy,
    inp.Sz,
    inp.Trc,
    inp.Tx,
    inp.Ty,
    inp.Tz,
    inp.Wed,
    inp.X,
    inp.Y,
    inp.Z,
    inp.Comment,
)
Data = types.Union(
    inp.Act,
    inp.Area,
    inp.Awtab,
    inp.Bbrem,
    inp.Bflcl,
    inp.Bfld,
    inp.C,
    inp.Cf,
    inp.Cm,
    inp.Cosy,
    inp.Cosyp,
    inp.Ctme,
    inp.Cut,
    inp.Dawwg,
    inp.Dbcn,
    inp.Dd,
    inp.De,
    inp.Df_0,
    inp.Df_1,
    inp.Dm,
    inp.Drxs,
    inp.Ds_0,
    inp.Ds_1,
    inp.Ds_2,
    inp.Ds_3,
    inp.Dxc,
    inp.Dxt,
    inp.E,
    inp.Elpt,
    inp.Em,
    inp.Embdb,
    inp.Embdf,
    inp.Embeb,
    inp.Embed,
    inp.Embee,
    inp.Embem,
    inp.Embtb,
    inp.Embtm,
    inp.Esplt,
    inp.Ext,
    inp.F_0,
    inp.F_1,
    inp.F_2,
    inp.F_3,
    inp.F_4,
    inp.Fc,
    inp.Fcl,
    inp.Fic,
    inp.Files,
    inp.Fill,
    inp.Fip,
    inp.Fir,
    inp.Fm,
    inp.Fmesh,
    inp.Fmult,
    inp.Fq,
    inp.Fs,
    inp.Ft,
    inp.Fu,
    inp.Histp,
    inp.Hsrc,
    inp.Idum,
    inp.Imp,
    inp.Kcode,
    inp.Kopts,
    inp.Kpert,
    inp.Ksen,
    inp.Ksrc,
    inp.Lat,
    inp.Lca,
    inp.Lcb,
    inp.Lcc,
    inp.Lea,
    inp.Leb,
    inp.Lost,
    inp.M_0,
    inp.M_1,
    inp.Mesh,
    inp.Mgopt,
    inp.Mode,
    inp.Mphys,
    inp.Mplot,
    inp.Mt,
    inp.Mx,
    inp.Nonu,
    inp.Notrn,
    inp.Nps,
    inp.Otfdb,
    inp.Pd,
    inp.Pert,
    inp.Phys_0,
    inp.Phys_1,
    inp.Phys_2,
    inp.Phys_3,
    inp.Phys_4,
    inp.Pikmt,
    inp.Prdmp,
    inp.Print,
    inp.Ptrac,
    inp.Pwt,
    inp.Rand,
    inp.Rdum,
    inp.Sb_0,
    inp.Sb_1,
    inp.Sc,
    inp.Sd,
    inp.Sdef,
    inp.Sf,
    inp.Si_0,
    inp.Si_1,
    inp.Si_2,
    inp.Sp_0,
    inp.Sp_1,
    inp.Spdtl,
    inp.Ssr,
    inp.Ssw,
    inp.Stop,
    inp.T_0,
    inp.T_1,
    inp.Talnp,
    inp.Tf_0,
    inp.Tf_1,
    inp.Thtme,
    inp.Tm,
    inp.Tmp,
    inp.Totnu,
    inp.Tr_0,
    inp.Tr_1,
    inp.Tr_2,
    inp.Tr_3,
    inp.Tr_4,
    inp.Tropt,
    inp.Tsplt,
    inp.U,
    inp.Unc,
    inp.Uran,
    inp.Var,
    inp.Void,
    inp.Vol,
    inp.Wwe,
    inp.Wwg,
    inp.Wwge,
    inp.Wwgt,
    inp.Wwn,
    inp.Wwp,
    inp.Wwt,
    inp.Xs,
    inp.Za,
    inp.Zb,
    inp.Zc,
    inp.Zd,
    inp.Comment,
)


def _block(union, values, parse=None):
    items = []
    for value in values:
        if isinstance(value, union.__bases__):
            items.append(value)
        elif isinstance(value, str):
            try:
                items.append(inp.Comment.from_mcnp(value))
            except errors.InpError:
                items.append((parse or union.from_mcnp)(value))

    return items


class Inp(_field.Fields, _file.File):
    """
    Represents INP files.
    """

    _CODE = errors.InpCode.SEMANTICS_FILE

    _REGEX = re.compile(r'\A((?:message:).+\n)?(.+)(?:\n)([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n|\Z))([\S\s]+)?\Z', re.IGNORECASE)

    title = _field.Field(types.String, 'File title', required=True, numeric=(), invalid=lambda self, value: not len(value) < 80)
    cells = _field.Field.tuple(
        inp.Card,
        'File cell card block',
        required=True,
        numeric=(),
        before=lambda values: _block(Cell, values, lambda item: (inp.Like if 'like' in item else inp.Cell).from_mcnp(item)),
        invalid=lambda self, value: (
            all(isinstance(cell, inp.Cell) and (not cell.options or not any(isinstance(option, inp.cell.Imp) for option in cell.options)) for cell in value)
            and (not hasattr(self, '_data') or all(isinstance(data, inp.data.Imp) for data in self.data))
        ),
    )
    surfaces = _field.Field.tuple(inp.Card, 'File surface card block', required=True, numeric=(), before=lambda values: _block(Surface, values))
    data = _field.Field.tuple(inp.Card, 'File data card block', required=True, numeric=(), before=lambda values: _block(Data, values))
    message = _field.Field(types.String, 'File message', numeric=())
    other = _field.Field(types.String, 'File other block', numeric=())

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Inp` from INP.

        Parameters:
            source: INP for `Inp`.

        Returns:
            `Inp`.

        Raises:
            InpError: SYNTAX_FILE.
        """

        source = Inp._preprocess(source)
        tokens = Inp._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_FILE, source)

        message = types.String.from_mcnp(tokens[1]) if tokens[1] else None
        title = types.String.from_mcnp(tokens[2])
        cells = types.Tuple(Cell)(tuple(Cell.from_mcnp(token) for token in tokens[3].strip().split('\n')))
        surfaces = types.Tuple(Surface)(tuple(Surface.from_mcnp(token) for token in tokens[4].strip().split('\n')))
        data = types.Tuple(Data)(tuple(Data.from_mcnp(token) for token in tokens[5].strip().split('\n')))
        other = types.String.from_mcnp(tokens[6]) if tokens[6] else None

        return Inp(
            title,
            cells,
            surfaces,
            data,
            message=message,
            other=other,
        )

    def to_mcnp(self):
        """
        Generates INP from `Inp`.

        Returns:
            INP for `Inp`.
        """

        # DELIMITER = 'c ' + '=' * 76 + '\n'
        # source += DELIMITER
        # source += f'c {"cells":^76.76}\n'
        # source += DELIMITER

        return (
            (self.message.value + '\n' if self.message else '')
            + self.title.value
            + '\n'
            + '\n'.join(map(str, self.cells))
            + '\n\n'
            + '\n'.join(map(str, self.surfaces))
            + '\n\n'
            + '\n'.join(map(str, self.data))
            + '\n\n'
            + (self.other.value if self.other is not None else '')
        )

    @staticmethod
    def _preprocess(source: str):
        """
        Preprocess INP for `from_mcnp`.

        Parameters:
            source: INP to preprocess.
        """

        source = re.sub(r'\n +\n', '\n\n', source)

        # Preprocessing vertical data format.
        tokens = re.split(r'\n(#(?: \S+)+\n(?: *\d\S*(?: +\S+)+\n)+)', source)
        source = ''
        for token in tokens:
            if match := re.match(r'#((?: \S+)+)\n((?: *\d\S*(?: +\S+)+\n)+)', token):
                cards = re.split(r'\s+', match[1])[1:]
                rows = [[card] for card in cards]

                lines = match[2].split('\n')[:-1]
                for line in lines:
                    parameters = re.split(r'\s+', line)
                    if len(parameters) != len(rows):
                        raise errors.InpError(errors.InpCode.SYNTAX_FILE, line)

                    for parameter, row in zip(parameters, rows):
                        row.append(parameter)

                source += '\n' + '\n'.join([' '.join(row) for row in rows]) + '\n'
            else:
                source += token

        source = re.sub(r'& *\n *', '\n    ', source)

        # Preproessing inline comments.
        tokens = collections.deque(source.split('\n'))
        source = ''
        while tokens:
            token = tokens.popleft()

            comments = ['']

            split = token.split('$', maxsplit=1)
            source += split[0]
            if len(split) == 2:
                comments.append(split[1])

            while tokens and re.match(r'\s+.+', tokens[0]):
                token = tokens.popleft()

                split = token.split('$', maxsplit=1)
                source += split[0]
                if len(split) == 2:
                    comments.append(split[1])

            source += ' $'.join(comments) + '\n'

        source = re.sub(r' +', ' ', source)
        source = re.sub(r'[(] ', '(', source)
        source = re.sub(r' [)]', ')', source)
        source = re.sub(r'\n \n', '\n\n', source)
        source = re.sub(r' = | =|= |=', ' ', source)
        source = re.sub(r'\t', '    ', source)
        source = source.strip()

        return source

    @property
    def nps(self) -> types.Integer:
        """
        File nps.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        try:
            card_nps = next(filter(lambda card: isinstance(card, inp.Nps), self.data))
            return card_nps.npp
        except StopIteration:
            return None

    @nps.setter
    def nps(self, nps: str | int | types.Integer) -> None:
        """
        Sets `nps`.

        Parameters:
            nps: File nps.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if nps is not None:
            if isinstance(nps, int):
                nps = types.Integer(nps)
            elif isinstance(nps, str):
                nps = types.Integer.from_mcnp(nps)

        try:
            card_nps = next(filter(lambda card: isinstance(card, inp.Nps), self.data))
            card_nps.npp = nps
        except StopIteration:
            self.data = [*self.data, inp.Nps(nps)]

    @property
    def seed(self) -> types.Integer:
        """
        File seed.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        try:
            card_rand = next(filter(lambda card: isinstance(card, inp.Rand), self.data))
            option_seed = next(filter(lambda option: isinstance(option, inp.rand.Seed), card_rand.options or []))
            return option_seed.seed
        except StopIteration:
            return None

    @seed.setter
    def seed(self, seed: str | int | types.Integer) -> None:
        """
        Sets `seed`.

        Parameters:
            seed: File seed.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if seed is not None:
            if isinstance(seed, int):
                seed = types.Integer(seed)
            elif isinstance(seed, str):
                seed = types.Integer.from_mcnp(seed)

        try:
            card_rand = next(filter(lambda card: isinstance(card, inp.Rand), self.data))

            try:
                option_seed = next(filter(lambda option: isinstance(option, inp.rand.Seed), card_rand.options or []))
                option_seed.seed = seed
            except StopIteration:
                option_seed = inp.rand.Seed(seed)
                card_rand.options = [*(card_rand.options or []), option_seed]

        except StopIteration:
            option_seed = inp.rand.Seed(seed)
            card_rand = inp.Rand([option_seed])
            self.data = [*self.data, card_rand]

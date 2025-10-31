import re
import collections

from . import inp
from . import _file
from . import types
from . import errors


Cell = types.Union(inp.Cell, inp.Like, inp.Comment)
Surface = types.Union(inp.Surface, inp.Comment)
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


class Inp(_file.File):
    """
    Represents INP files.
    """

    _REGEX = re.compile(r'\A((?:message:).+\n)?(.+)(?:\n)([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n))([\s\S]+?(?:\n\n|\Z))([\S\s]+)?\Z', re.IGNORECASE)

    def __init__(
        self,
        title: types.String,
        cells: types.Tuple(Cell),
        surfaces: types.Tuple(Surface),
        data: types.Tuple(Data),
        message: types.String = None,
        other: types.String = None,
    ):
        """
        Initializes `Inp`.

        Parameters:
            title: File title.
            cells: File cell card block.
            surfaces: File surface card block.
            data: File data card block.
            message: File message.
            other: File other block.

        Returns:
            `Inp`.

        Raises:
            InpError: SEMATNICS_INP.
        """

        self.title: types.String = title
        self.cells: types.Tuple(Cell) = cells
        self.surfaces: types.Tuple(Surface) = surfaces
        self.data: types.Tuple(Data) = data
        self.message: types.String = message
        self.other: types.String = other

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
    def title(self) -> types.String:
        """
        File title.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._title

    @title.setter
    def title(self, title: str | types.String) -> None:
        """
        Sets `title`.

        Parameters:
            title: File title.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if title is not None:
            if isinstance(title, types.String):
                title = title
            elif isinstance(title, str):
                title = types.String.from_mcnp(title)

        if title is None or not len(title) < 80:
            raise errors.InpError(errors.InpCode.SEMANTICS_FILE, title)

        self._title: types.Integer = title

    @property
    def cells(self) -> types.Tuple(Cell):
        """
        File cells card block.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cells

    @cells.setter
    def cells(self, cells: list[str] | list[inp.Cell | inp.Like | inp.Comment]) -> None:
        """
        Sets `cells`.

        Parameters:
            cells: File cells.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cells is not None:
            array = []
            for item in cells:
                if isinstance(item, inp.Cell):
                    array.append(item)
                elif isinstance(item, inp.Like):
                    array.append(item)
                elif isinstance(item, inp.Comment):
                    array.append(item)
                elif isinstance(item, str):
                    try:
                        array.append(inp.Comment.from_mcnp(item))
                        continue
                    except errors.InpError:
                        pass

                    if 'like' in item:
                        array.append(inp.Like.from_mcnp(item))
                    else:
                        array.append(inp.Cell.from_mcnp(item))

            cells = types.Tuple(inp.Card)(array)

        if cells is None or None in cells:
            raise errors.InpError(errors.InpCode.SEMANTICS_FILE, cells)

        if all(isinstance(cell, inp.Cell) and (not cell.options or not any(isinstance(option, inp.cell.Imp) for option in cell.options)) for cell in cells) and (
            not hasattr(self, '_data') or all(isinstance(data, inp.data.Imp) for data in self.data)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_FILE, cells)

        self._cells: types.Tuple(Cell) = cells

    @property
    def surfaces(self) -> types.Tuple(Surface):
        """
        File surfaces card block.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._surfaces

    @surfaces.setter
    def surfaces(self, surfaces: list[str] | list[inp.Surface | inp.Comment]) -> None:
        """
        Sets `surfaces`.

        Parameters:
            surfaces: File surfaces.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if surfaces is not None:
            array = []
            for item in surfaces:
                if isinstance(item, inp.Surface):
                    array.append(item)
                elif isinstance(item, inp.Comment):
                    array.append(item)
                elif isinstance(item, str):
                    try:
                        array.append(inp.Comment.from_mcnp(item))
                        continue
                    except errors.InpError:
                        pass
                    array.append(inp.Surface.from_mcnp(item))

            surfaces = types.Tuple(inp.Card)(array)

        if surfaces is None or None in surfaces:
            raise errors.InpError(errors.InpCode.SEMANTICS_FILE, surfaces)

        self._surfaces: types.Tuple(Surface) = surfaces

    @property
    def data(self) -> types.Tuple(Data):
        """
        File data card block.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._data

    @data.setter
    def data(
        self,
        data: list[str]
        | list[
            inp.Act
            | inp.Area
            | inp.Awtab
            | inp.Bbrem
            | inp.Bflcl
            | inp.Bfld
            | inp.C
            | inp.Cf
            | inp.Cm
            | inp.Cosy
            | inp.Cosyp
            | inp.Ctme
            | inp.Cut
            | inp.Dawwg
            | inp.Dbcn
            | inp.Dd
            | inp.De
            | inp.Df_0
            | inp.Df_1
            | inp.Dm
            | inp.Drxs
            | inp.Ds_0
            | inp.Ds_1
            | inp.Ds_2
            | inp.Ds_3
            | inp.Dxc
            | inp.Dxt
            | inp.E
            | inp.Elpt
            | inp.Em
            | inp.Embdb
            | inp.Embdf
            | inp.Embeb
            | inp.Embed
            | inp.Embee
            | inp.Embem
            | inp.Embtb
            | inp.Embtm
            | inp.Esplt
            | inp.Ext
            | inp.F_0
            | inp.F_1
            | inp.F_2
            | inp.F_3
            | inp.F_4
            | inp.Fc
            | inp.Fcl
            | inp.Fic
            | inp.Files
            | inp.Fill
            | inp.Fip
            | inp.Fir
            | inp.Fm
            | inp.Fmesh
            | inp.Fmult
            | inp.Fq
            | inp.Fs
            | inp.Ft
            | inp.Fu
            | inp.Histp
            | inp.Hsrc
            | inp.Idum
            | inp.Imp
            | inp.Kcode
            | inp.Kopts
            | inp.Kpert
            | inp.Ksen
            | inp.Ksrc
            | inp.Lat
            | inp.Lca
            | inp.Lcb
            | inp.Lcc
            | inp.Lea
            | inp.Leb
            | inp.Lost
            | inp.M_0
            | inp.M_1
            | inp.Mesh
            | inp.Mgopt
            | inp.Mode
            | inp.Mphys
            | inp.Mplot
            | inp.Mt
            | inp.Mx
            | inp.Nonu
            | inp.Notrn
            | inp.Nps
            | inp.Otfdb
            | inp.Pd
            | inp.Pert
            | inp.Phys_0
            | inp.Phys_1
            | inp.Phys_2
            | inp.Phys_3
            | inp.Phys_4
            | inp.Pikmt
            | inp.Prdmp
            | inp.Print
            | inp.Ptrac
            | inp.Pwt
            | inp.Rand
            | inp.Rdum
            | inp.Sb_0
            | inp.Sb_1
            | inp.Sc
            | inp.Sd
            | inp.Sdef
            | inp.Sf
            | inp.Si_0
            | inp.Si_1
            | inp.Si_2
            | inp.Sp_0
            | inp.Sp_1
            | inp.Spdtl
            | inp.Ssr
            | inp.Ssw
            | inp.Stop
            | inp.T_0
            | inp.T_1
            | inp.Talnp
            | inp.Tf_0
            | inp.Tf_1
            | inp.Thtme
            | inp.Tm
            | inp.Tmp
            | inp.Totnu
            | inp.Tr_0
            | inp.Tr_1
            | inp.Tr_2
            | inp.Tr_3
            | inp.Tr_4
            | inp.Tropt
            | inp.Tsplt
            | inp.U
            | inp.Unc
            | inp.Uran
            | inp.Var
            | inp.Void
            | inp.Vol
            | inp.Wwe
            | inp.Wwg
            | inp.Wwge
            | inp.Wwgt
            | inp.Wwn
            | inp.Wwp
            | inp.Wwt
            | inp.Xs
            | inp.Za
            | inp.Zb
            | inp.Zc
            | inp.Zd
            | inp.Comment
        ],
    ) -> None:
        """
        Sets `data`.

        Parameters:
            data: File data.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if data is not None:
            array = []
            for item in data:
                if isinstance(item, inp.Card) and not (isinstance(item, inp.Surface) or isinstance(item, inp.Like) or isinstance(item, inp.Cell)):
                    array.append(item)
                elif isinstance(item, str):
                    try:
                        array.append(inp.Comment.from_mcnp(item))
                        continue
                    except errors.InpError:
                        pass

                    array.append(Data.from_mcnp(item))

            data = types.Tuple(Data)(array)

        if data is None or None in data:
            raise errors.InpError(errors.InpCode.SEMANTICS_FILE, data)

        self._data: types.Tuple(Data) = data

    @property
    def message(self) -> types.String:
        """
        File message.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._message

    @message.setter
    def message(self, message: str | types.String) -> None:
        """
        Sets `message`.

        Parameters:
            message: File message.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if message is not None:
            if isinstance(message, types.String):
                message = message
            elif isinstance(message, str):
                message = types.String.from_mcnp(message)

        self._message: types.Integer = message

    @property
    def other(self) -> types.Integer:
        """
        File other.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._other

    @other.setter
    def other(self, other: str | types.String) -> None:
        """
        Sets `other`.

        Parameters:
            other: File other.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if other is not None:
            if isinstance(other, types.String):
                other = other
            elif isinstance(other, str):
                other = types.String.from_mcnp(other)

        self._other: types.Integer = other

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
            if isinstance(nps, types.Integer):
                nps = nps
            elif isinstance(nps, int):
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
            if isinstance(seed, types.Integer):
                seed = seed
            elif isinstance(seed, int):
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

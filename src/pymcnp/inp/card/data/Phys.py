import typing
import decimal
import dataclasses


from .... import abc
from ..Data import Data
from ... import literal


class Phys(Data):
    """
    Represents phys data cards.
    """

    pass


class Phys_0(Phys):
    """
    Represents phys data cards, form #0.

    Attributes:
        keyword: phys data card `PHYS:N` symbol.
        emax: phys data card `emax` parameter.
        emcnf: phys data card `emcnf` parameter.
        iunr: phys data card `iunr` parameter.
        j_0: phys data card `J` parameter, #0.
        j_1: phys data card `J` parameter, #1.
        j_2: phys data card `J` parameter, #2.
        coilf: phys data card `coilf` parameter.
        cutn: phys data card `cutn` parameter.
        ngam: phys data card `ngam` parameter.
        j_3: phys data card `J` parameter, #3.
        j_4: phys data card `J` parameter, #4.
        i_int_model: phys data card `i_int_model` parameter.
        i_els_model: phys data card `i_els_model` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PHYS:N'] | str = abc.Terminal[r'PHYS:N']('PHYS:N')
    emax: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    emcnf: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    iunr: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j_0: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_1: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_2: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    coilf: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    cutn: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    ngam: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j_3: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_4: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    i_int_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    i_els_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates phys data cards, form #0.
        """

        if isinstance(self.iunr, literal.Integer) and self.iunr not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.iunr=}')

        if isinstance(self.coilf, literal.Real) and not (
            self.coilf == 0 or 0.001 < self.coilf < 1.001 or 1.001 < self.coilf < 2.001 or self.coilf == 3 or 3.001 < self.coilf < 4.001 or self.coilf == 5
        ):
            raise abc.Error('Invalid value.', f'{self.coilf}')

        if isinstance(self.cutn, literal.Integer) and not (self.cutn >= 0 or self.cutn == -1 or self.cutn > self.emax):
            raise abc.Error('Invalid value.', f'{self.emax=}')

        if isinstance(self.ngam, literal.Integer) and self.ngam not in {0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.ngam=}')

        if isinstance(self.i_int_model, literal.Integer) and self.i_int_model not in {-1, 0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.i_int_model=}')

        if isinstance(self.i_els_model, literal.Integer) and self.i_els_model not in {-1, 0}:
            raise abc.Error('Invalid value.', f'{self.i_els_model=}')


class Phys_1(Phys):
    """
    Represents phys data cards, form #1.

    Attributes:
        keyword: phys data card `PHYS:P` symbol.
        emcpf: phys data card `emcpf` parameter.
        ides: phys data card `ides` parameter.
        nocoh: phys data card `nocoh` parameter.
        ispn: phys data card `ispn` parameter.
        nodop: phys data card `nodop` parameter.
        j: phys data card `J` parameter.
        fism: phys data card `fism` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PHYS:P'] | str = abc.Terminal[r'PHYS:P']('PHYS:P')
    emcpf: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ides: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    nocoh: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    ispn: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    nodop: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    fism: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates phys data cards, form #1.
        """

        if isinstance(self.ides, literal.Integer) and self.ides not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.ides=}')

        if isinstance(self.nocoh, literal.Integer) and self.nocoh not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.nocoh=}')

        if isinstance(self.ispn, literal.Integer) and self.ispn not in {-1, 0, 1}:
            raise abc.Error('Invalid value.', f'{self.ispn=}')

        if isinstance(self.nodop, literal.Integer) and self.nodop not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.nodop=}')

        if isinstance(self.fism, literal.Integer) and self.fism not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.fism=}')


class Phys_2(Phys):
    """
    Represents phys data cards, form #2.

    Attributes:
        keyword: phys data card `PHYS:E` symbol.
        emax: phys data card `emax` parameter.
        ides: phys data card `ides` parameter.
        iphot: phys data card `iphot` parameter.
        ibad: phys data card `ibad` parameter.
        istrg: phys data card `istrg` parameter.
        bnum: phys data card `bnum` parameter.
        xnum: phys data card `xnum` parameter.
        rnok: phys data card `rnok` parameter.
        enum: phys data card `enum` parameter.
        numb: phys data card `numb` parameter.
        i_mcs_model: phys data card `i_mcs_model` parameter.
        mode_electron_elastic: phys data card `mode_electron_elastic` parameter.
        j: phys data card `J` parameter.
        efac: phys data card `efac` parameter.
        electron_method_boundary: phys data card `electron_method_boundary` parameter.
        ckvnum: phys data card `ckvnum` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PHYS:E'] | str = abc.Terminal[r'PHYS:E']('PHYS:E')
    emax: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ides: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    iphot: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    ibad: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    istrg: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    bnum: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    xnum: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    rnok: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    enum: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    numb: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    i_mcs_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    mode_electron_elastic: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    efac: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    electron_method_boundary: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ckvnum: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates phys data cards, form #2.
        """

        if isinstance(self.ides, literal.Integer) and self.ides not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.ides=}')

        if isinstance(self.iphot, literal.Integer) and self.iphot not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.iphot=}')

        if isinstance(self.ibad, literal.Integer) and self.ibad not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.ibad=}')

        if isinstance(self.istrg, literal.Integer) and self.istrg not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.istrg=}')

        if isinstance(self.bnum, literal.Real) and not (self.bnum >= 0 or self.bnum == 0):
            raise abc.Error('Invalid value.', f'{self.bnum=}')

        if isinstance(self.xnum, literal.Real) and not (self.xnum == 0 or self.xnum > 0):
            raise abc.Error('Invalid value.', f'{self.xnum=}')

        if isinstance(self.rnok, literal.Integer) and not (self.rnok == 0 or self.rnok > 0):
            raise abc.Error('Invalid value.', f'{self.rnok=}')

        if isinstance(self.numb, literal.Integer) and not (self.numb == 0 or self.numb > 0):
            raise abc.Error('Invalid value.', f'{self.numb=}')

        if isinstance(self.i_mcs_model, literal.Integer) and self.i_mcs_model not in {-1, 0}:
            raise abc.Error('Invalid value.', f'{self.i_mcs_model=}')

        if isinstance(self.mode_electron_elastic, literal.Integer) and self.mode_electron_elastic not in {0, 2}:
            raise abc.Error('Invalid value.', f'{self.mode_electron_elastic=}')

        if isinstance(self.efac, literal.Real) and not (0.8 <= self.efac <= 0.99):
            raise abc.Error('Invalid value.', f'{self.efac=}')

        if isinstance(self.ckvnum, literal.Real) and not (0 <= self.ckvnum < 1):
            raise abc.Error('Invalid value.', f'{self.ckvnum=}')


class Phys_3(Phys):
    """
    Represents phys data cards, form #3.

    Attributes:
        keyword: phys data card `PHYS:H` symbol.
        emax: phys data card `emax` parameter.
        ean: phys data card `ean` parameter.
        tabl: phys data card `tabl` parameter.
        j_0: phys data card `J` parameter, #0.
        istrg: phys data card `istrg` parameter.
        j_1: phys data card `J` parameter, #1.
        recl: phys data card `recl` parameter.
        j_2: phys data card `J` parameter, #2.
        j_3: phys data card `J` parameter, #3.
        j_4: phys data card `J` parameter, #4.
        i_mcs_model: phys data card `i_mcs_model` parameter.
        i_int_model: phys data card `i_int_model` parameter.
        i_els_model: phys data card `i_els_model` parameter.
        efac: phys data card `efac` parameter.
        j_5: phys data card `J` parameter, #5.
        ckvnum: phys data card `ckvnum` parameter.
        drp: phys data card `drp` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PHYS:H'] | str = abc.Terminal[r'PHYS:H']('PHYS:H')
    emax: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ean: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    tabl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    j_0: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    istrg: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j_1: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    recl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    j_2: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_3: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_4: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    i_mcs_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    i_int_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    i_els_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    efac: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    j_5: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    ckvnum: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    drp: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates phys data cards, form #3.
        """

        if isinstance(self.tabl, literal.Real) and not (self.tabl == -1 or self.tabl >= 0):
            raise abc.Error('Invalid value.', f'{self.tabl=}')

        if isinstance(self.istrg, literal.Integer) and self.istrg not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.istrg=}')

        if isinstance(self.recl, literal.Real) and not (0 <= self.recl <= 1):
            raise abc.Error('Invalid value.', f'{self.recl=}')

        if isinstance(self.i_mcs_model, literal.Integer) and self.i_mcs_model not in {-1, 0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.i_mcs_model=}')

        if isinstance(self.i_int_model, literal.Integer) and self.i_int_model not in {-1, 0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.i_int_model=}')

        if isinstance(self.i_els_model, literal.Integer) and self.i_els_model not in {-1, 0}:
            raise abc.Error('Invalid value.', f'{self.i_els_model=}')

        if isinstance(self.efac, literal.Real) and not (0.8 <= self.efac <= 0.99):
            raise abc.Error('Invalid value.', f'{self.efac=}')

        if isinstance(self.ckvnum, literal.Real) and not (0 <= self.ckvnum < 1):
            raise abc.Error('Invalid value.', f'{self.ckvnum=}')

        if isinstance(self.drp, literal.Real) and not (0 <= self.drp or self.drp == -1):
            raise abc.Error('Invalid value.', f'{self.drp=}')


class Phys_4(Phys):
    """
    Represents phys data cards, form #4.

    Attributes:
        keyword: phys data card `PHYS` symbol.
        colon: phys data card `:` symbol.
        particle: phys data card `particle` parameter.
        emax: phys data card `emax` parameter.
        j_0: phys data card `J` parameter, #0.
        j_1: phys data card `J` parameter, #1.
        j_2: phys data card `J` parameter, #2.
        istrg: phys data card `istrg` parameter.
        j_3: phys data card `J` parameter, #3.
        xmunum: phys data card `xmunum` parameter.
        xmugam: phys data card `xmugam` parameter.
        j_4: phys data card `J` parameter, #4.
        j_5: phys data card `J` parameter, #5.
        i_mcs_model: phys data card `i_mcs_model` parameter.
        i_int_model: phys data card `i_int_model` parameter.
        i_els_model: phys data card `i_els_model` parameter.
        efac: phys data card `efac` parameter.
        j_6: phys data card `J` parameter, #6.
        ckvnum: phys data card `ckvnum` parameter.
        drp: phys data card `drp` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PHYS'] | str = abc.Terminal[r'PHYS']('PHYS')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    emax: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    j_0: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_1: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_2: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    istrg: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j_3: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    xmunum: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    xmugam: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    j_4: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_5: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    i_mcs_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    i_int_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    i_els_model: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    efac: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    j_6: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    ckvnum: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    drp: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates phys data cards, form #4.
        """

        if self.particle in {'n', 'e', 'h', 'p'}:
            raise abc.Error('Invalid value.', f'{self.particle=}')

        if isinstance(self.istrg, literal.Integer) and self.istrg not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.istrg=}')

        if isinstance(self.xmunum, literal.Integer) and self.xmunum not in {-1, 1}:
            raise abc.Error('Invalid value.', f'{self.xmunum=}')

        if isinstance(self.i_mcs_model, literal.Integer) and self.i_mcs_model not in {-1, 0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.i_mcs_model=}')

        if isinstance(self.i_int_model, literal.Integer) and self.i_int_model not in {-1, 0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.i_int_model=}')

        if isinstance(self.i_els_model, literal.Integer) and self.i_els_model not in {-1, 0}:
            raise abc.Error('Invalid value.', f'{self.i_els_model=}')

        if isinstance(self.efac, literal.Real) and not (0.8 <= self.efac <= 0.99):
            raise abc.Error('Invalid value.', f'{self.efac=}')

        if isinstance(self.ckvnum, literal.Real) and not (0 <= self.ckvnum < 1):
            raise abc.Error('Invalid value.', f'{self.ckvnum=}')

        if isinstance(self.drp, literal.Real) and not (0 <= self.drp or self.drp == -1):
            raise abc.Error('Invalid value.', f'{self.drp=}')

import dataclasses

from . import inp
from .Inp import Inp
from .utils import types
from .utils import errors


@dataclasses.dataclass
class GeometryEntryBuilder:
    """
    Builds ``GeometryEntry``.

    Attributes:
        infix: Geometry infix formula.
    """

    infix: str

    def __and__(a, b):
        """
        Unites ``GeometryEntryBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``GeometryEntryBuilder`` union.
        """

        return GeometryEntryBuilder(infix=f'{a.infix}:{b.infix}')

    def __or__(a, b):
        """
        Intersects ``GeometryEntryBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``GeometryEntryBuilder`` intersection.
        """

        return GeometryEntryBuilder(infix=f'{a.infix} {b.infix}')

    def __invert__(self):
        """
        Inverts ``GeometryEntryBuilder``.

        Returns:
            ``GeometryEntryBuilder`` complement.
        """

        return GeometryEntryBuilder(infix=f'#{self.infix}')

    def build(self):
        """
        Builds ``GeometryEntryBuilder`` into ``GeometryEntry``.

        Returns:
            ``GeometryEntry`` for ``GeometryEntryBuilder``.
        """

        return types.GeometryEntry(infix=types.String(self.infix))


@dataclasses.dataclass
class CellOptionBuilder:
    """
    Builds ``CellOption_``.

    Attributes:
        mnemonic: surface option mnemonic.
        parameter: surface option parameters.
    """

    mnemonic: str
    parameter: str
    suffix: str = ''
    designator: str = ''

    def build(self):
        """
        Builds ``CellOptionBuilder`` into ``CellOption_``.

        Returns:
            ``CellOption_`` for ``CellOptionBuilder``.
        """

        error = None

        for subclasses in inp.cell.CellOption_._SUBCLASSES.values():
            for subcls in subclasses:
                try:
                    return subcls.from_mcnp(
                        f'{self.mnemonic}{self.suffix if self.suffix else ""}{f":{self.designator}" if self.designator else ""} {self.parameter}'
                    )
                except errors.InpError as err:
                    error = err

        raise error


@dataclasses.dataclass
class CellBuilder:
    """
    Builds ``Cell``.

    Attributes:
        number: cell number.
        material: cell material.
        density: cell density.
        geometry: cell geometry.
        options: cell options.
    """

    number: int | types.Integer
    material: int | types.Integer
    geometry: GeometryEntryBuilder
    options: tuple[CellOptionBuilder] = tuple()
    density: float | types.Real = None
    atoms_or_grams: bool = True

    def build(self):
        """
        Builds ``CellBuilder`` into ``Cell``.

        Returns:
            ``Cell`` for ``CellBuilder``.
        """

        return inp.Cell(
            number=types.Integer(self.number),
            material=types.Integer(self.material),
            density=types.Real(self.density * 1 if self.atoms_or_grams else -1)
            if self.density
            else None,
            geometry=self.geometry.build(),
            options=types.Tuple([option.build() for option in self.options]),
        )


@dataclasses.dataclass
class SurfaceBuilder:
    """
    Builds ``Surface``.

    Attributes:
        number: surface number.
        transform: surface transformation.
        option: surface option.
        prefix: surface kind setting.
    """

    number: int
    mnemonic: str
    parameter: str
    prefix: str = None
    transform: int = None

    def build(self):
        """
        Builds ``SurfaceBuilder`` into ``Surface``.

        Returns:
            ``Surface`` for ``SurfaceBuilder``.
        """

        error = None
        option = None

        for subclasses in inp.surface.SurfaceOption_._SUBCLASSES.values():
            for subcls in subclasses:
                try:
                    option = subcls.from_mcnp(f'{self.mnemonic} {self.parameter}')
                except errors.InpError as err:
                    error = err

        if not option:
            raise error

        return inp.Surface(
            number=types.Integer(self.number),
            option=option,
            prefix=self.prefix,
            transform=types.Integer(self.transform) if self.transform else None,
        )


@dataclasses.dataclass
class DataBuilder:
    """
    Builds ``Data``.

    Attributes:
        mnemonic: surface mnemonic.
        parameter: surface parameters.
    """

    mnemonic: str
    parameter: str
    suffix: str = ''
    designator: str = ''

    def build(self):
        """
        Builds ``DataBuilder`` into ``Data``.

        Returns:
            ``Data`` for ``DataBuilder``.
        """

        error = None
        option = None

        for subcls in inp.data.DataOption_._SUBCLASSES[self.mnemonic]:
            try:
                option = subcls.from_mcnp(
                    f'{self.mnemonic}{self.suffix if self.suffix else ""}{f":{self.designator}" if self.designator else ""} {self.parameter}'
                )
            except errors.InpError as err:
                error = err

        if not option:
            raise error

        return inp.Data(
            option=option,
        )


@dataclasses.dataclass
class InpBuilder:
    """
    Builds ``Inp``.

    Attributes:
        message: INP message.
        title: INP title.
        cells: INP cell card block.
        surfaces: INP surface card block.
        data: INP data card block.
        other: INP other block.
    """

    title: str
    cells: tuple[CellBuilder] = tuple()
    surfaces: tuple[SurfaceBuilder] = tuple()
    data: tuple[DataBuilder] = tuple()
    message: str = ''
    other: str = ''

    def append(self, card: CellBuilder | SurfaceBuilder | DataBuilder):
        """
        Stores ``Card_`` in ``InpBuilder``,

        Parameters:
            card: ``Card_`` to add.
        """

        if isinstance(card, CellBuilder):
            self.cells = (*self.cells, card)
        elif isinstance(card, SurfaceBuilder):
            self.surfaces = (*self.surfaces, card)
        elif isinstance(card, DataBuilder):
            self.data = (*self.data, card)

    def build(self):
        """
        Builds ``InpBuilder`` into ``Inp``.

        Returns:
            ``Inp`` for ``InpBuilder``.
        """

        return Inp(
            title=self.title,
            message=self.message,
            other=self.other,
            cells=types.Tuple([cell.build() for cell in self.cells]),
            cells_comments=types.Tuple([]),
            surfaces=types.Tuple([surface.build() for surface in self.surfaces]),
            surfaces_comments=types.Tuple([]),
            data=types.Tuple([data.build() for data in self.data]),
            data_comments=types.Tuple([]),
        )

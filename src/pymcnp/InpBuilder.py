import math
import dataclasses

from . import inp
from .Inp import Inp
from .utils import types
from .utils import errors


@dataclasses.dataclass
class GeometryBuilder:
    """
    Builds ``Geometry``.

    Attributes:
        infix: Geometry infix formula.
    """

    infix: str

    @staticmethod
    def unbuild(geometry: types.Geometry):
        """
        Generates ``GeometryBuilder`` from ``Geometry``.

        Parameter:
            geoemtry: ``Geometry`` to unbuild.

        Returns:
            ``GeometryBuilder`` for ``Geometry``.
        """

        return GeometryBuilder(infix=geometry.infix)

    def __and__(a, b):
        """
        Unites ``GeometryBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``GeometryBuilder`` union.
        """

        return GeometryBuilder(infix=f'{a.infix}:{b.infix}')

    def __or__(a, b):
        """
        Intersects ``GeometryBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``GeometryBuilder`` intersection.
        """

        return GeometryBuilder(infix=f'{a.infix} {b.infix}')

    def __invert__(self):
        """
        Inverts ``GeometryBuilder``.

        Returns:
            ``GeometryBuilder`` complement.
        """

        return GeometryBuilder(infix=f'#{self.infix}')

    def build(self):
        """
        Builds ``GeometryBuilder`` into ``Geometry``.

        Returns:
            ``Geometry`` for ``GeometryBuilder``.
        """

        return types.Geometry(infix=types.String(self.infix))


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

    @staticmethod
    def unbuild(option: inp.cell.CellOption_):
        """
        Generates ``CellOptionBuilder`` from ``CellOption_``.

        Parameter:
            option: ``CellOption_`` to unbuild.

        Returns:
            ``CellOptionBuilder`` for ``CellOption_``.
        """

        return CellOptionBuilder(
            mnemonic=option._KEYWORD,
            parameter=option.value.to_mcnp(),
            suffix=option.suffix.to_mcnp() if hasattr(option, 'suffix') else '',
            designator=option.designator.to_mcnp() if hasattr(option, 'designator') else '',
        )

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
    geometry: GeometryBuilder
    options: dict[str, CellOptionBuilder] = dataclasses.field(default_factory=lambda: ({}))
    density: float | types.Real = None
    atoms_or_grams: bool = True

    def append(self, option: CellOptionBuilder):
        """
        Stores ``Option_`` in ``CellBuilder``,

        Parameters:
            option: ``Option_`` to add.
        """

        self.options[
            f'{option.mnemonic}{option.suffix if hasattr(option, "suffix") else ""}:{option.designator if hasattr(option, "designator") else ""}'
        ] = option

    @staticmethod
    def unbuild(cell: inp.Cell):
        """
        Generates ``CellBuilder`` from ``Cell``.

        Parameter:
            cell: ``Cell` to unbuild.

        Returns:
            ``CellBuilder`` for ``Cell``.
        """

        return CellBuilder(
            number=cell.number.value,
            material=cell.material.value,
            density=math.abs(cell.density.value),
            atoms_or_grams=cell.density > 0,
            options={option._KEYWORD: CellOptionBuilder.unbuild(option) for option in cell.options},
            geometry=GeometryBuilder.unbuild(cell.geometry),
        )

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
            options=types.Tuple([option.build() for option in self.options.values()]),
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

    @staticmethod
    def unbuild(surface: inp.Surface):
        """
        Generates ``SurfaceBuilder`` from ``Surface``.

        Parameter:
            surface: ``Surface` to unbuild.

        Returns:
            ``SurfaceBuilder`` for ``Surface``.
        """

        return SurfaceBuilder(
            number=surface.number.value,
            parameter=surface.option.value.to_mcnp(),
            transform=surface.transform.value,
            mnemonic=surface.option._KEYWORD,
            prefix=surface.prefix,
        )

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

    @staticmethod
    def unbuild(data: inp.Data):
        """
        Generates ``DataBuilder`` from ``Data``.

        Parameter:
            data: ``Data` to unbuild.

        Returns:
            ``DataBuilder`` for ``Data``.
        """

        return DataBuilder(
            mnemonic=data.option._KEYWORD,
            parameter=data.option.value.to_mcnp(),
            suffix=data.option.suffix.to_mcnp() if hasattr(data.option, 'suffix') else '',
            designator=data.option.designator.to_mcnp()
            if hasattr(data.option, 'designator')
            else '',
        )

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
    cells: dict[str, CellBuilder] = dataclasses.field(default_factory=lambda: ({}))
    surfaces: dict[str, SurfaceBuilder] = dataclasses.field(default_factory=lambda: ({}))
    data: dict[str, DataBuilder] = dataclasses.field(default_factory=lambda: ({}))
    message: str = ''
    other: str = ''

    def append(self, card: CellBuilder | SurfaceBuilder | DataBuilder):
        """
        Stores ``Card_`` in ``InpBuilder``,

        Parameters:
            card: ``Card_`` to add.
        """

        if isinstance(card, CellBuilder):
            self.cells[card.number] = card
        elif isinstance(card, SurfaceBuilder):
            self.surfaces[card.number] = card
        elif isinstance(card, DataBuilder):
            self.data[card.mnemonic + card.suffix if hasattr(card, 'suffix') else ''] = card

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
            cells=types.Tuple([cell.build() for cell in self.cells.values()]),
            cells_comments=types.Tuple([]),
            surfaces=types.Tuple([surface.build() for surface in self.surfaces.values()]),
            surfaces_comments=types.Tuple([]),
            data=types.Tuple([data.build() for data in self.data.values()]),
            data_comments=types.Tuple([]),
        )

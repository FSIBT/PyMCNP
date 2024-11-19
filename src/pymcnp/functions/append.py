from . import modify
from .. import files


def append_cells(inpt: files.inp.Inp, *cells: files.inp.Cell):
    modify.modify(inpt, cells=(inpt.cells | {cell.ident: cell for cell in cells}))


def append_surfaces(inpt: files.inp.Inp, *surfaces: files.inp.Surface):
    modify.modify(inpt, surfaces=(inpt.surfaces | {surface.ident: surface for surface in surfaces}))


def append_data(inpt: files.inp.Inp, data: files.inp.Data):
    if data.mnemonic in files.inp.data.Data.GEOMETRY_MNEMONICS:
        modify.modify(inpt, data_geometry=(inpt.data_geometry | {data.ident: data}))
    elif data.mnemonic in files.inp.data.Data.MATERIAL_MNEMONICS:
        modify.modify(inpt, data_material=(inpt.data_material | {data.ident: data}))
    elif data.mnemonic in files.inp.data.Data.PHYSICS_MNEMONICS:
        modify.modify(inpt, data_physics=(inpt.data_physics | {data.ident: data}))
    elif data.mnemonic in files.inp.data.Data.SOURCE_MNEMONICS:
        modify.modify(inpt, data_source=(inpt.data_source | {data.ident: data}))
    elif data.mnemonic in files.inp.data.Data.TALLY_MNEMONICS:
        modify.modify(inpt, data_tally=(inpt.data_tally | {data.ident: data}))
    elif data.mnemonic in files.inp.data.Data.VARIENCE_MNEMONICS:
        modify.modify(inpt, data_variance=(inpt.data_variance | {data.ident: data}))
    elif data.mnemonic in files.inp.data.Data.MICELLANEOUS_MNEMONICS:
        modify.modify(inpt, data_micellaneous=(inpt.data_micellaneous | {data.ident: data}))
    else:
        assert False


def append_cell_option(cell: files.inp.Cell, *options: files.inp.CellOption):
    modify.modify(cell, options=(cell.options | {option.keyword: option for option in options}))


def append_data_option(data: files.inp.Cell, *options: files.inp.DataOption):
    modify.modify(data, options=(data.options | {option.keyword: option for option in options}))

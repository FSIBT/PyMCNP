import typing

from ..... import abc
from ..Embed import Embed


class Hdf5file(Embed):
    """
    Represents hdf5file embed data options.

    Attributes:
        keyword: hdf5file embed data option ``r'HDF5FILE'`` symbol.
        equals: hdf5file embed data option ``r'='`` symbol.
        filename: hdf5file embed data option ``filename`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'HDF5FILE'] | str = abc.Terminal[r'HDF5FILE']('HDF5FILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str

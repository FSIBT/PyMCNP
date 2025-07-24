import types

from ._shape import Shape
from . import pyvista

Endpoint = types.ModuleType

__all__ = [
    'Shape',
    'Endpoint',
    'pyvista',
]

import re

import pymcnp


def _subclasses(cls: type) -> set[type]:
    found = set()
    for sub in cls.__subclasses__():
        found |= {sub, *_subclasses(sub)}
    return found


def test_field_names_spell_preamble_and_postamble() -> None:
    # The fixed text before and after a value is a ``*_preamble`` or ``*_postamble`` field.
    misspelt = re.compile(r'pre(?!amble)[a-z]*able|post(?!amble)[a-z]*able')
    names = {f'{cls.__name__}.{name}' for cls in _subclasses(pymcnp.abc.Nonterminal) for name in getattr(cls, '_fields', {})}
    assert not [name for name in names if misspelt.search(name)]
    assert {'Header.version_preamble', 'Footer.dump_number_postamble', 'Meshtal.particle_postamble', 'Meshtal.labels_postamble'} <= names


def test_parallelepiped() -> None:
    assert pymcnp.abc.Parallelepiped.__name__ == 'Parallelepiped'
    assert not hasattr(pymcnp.abc, 'Parallelipiped')


def test_package_is_typed() -> None:
    # PEP 561 marker, so that type checkers use PyMCNP's annotations; pyproject.toml ships it in the wheel.
    import importlib.resources

    assert (importlib.resources.files('pymcnp') / 'py.typed').is_file()


def test_tally_and_cell_forms_say_what_they_are() -> None:
    # ``help()`` names the MCNP card form of each class, so ``F_1`` is found as the point detector.
    data = pymcnp.inp.card.data
    assert all(f'F{n}' in data.F_0.__doc__ for n in (1, 2, 4, 6, 7, 8))
    assert 'point detector' in data.F_1.__doc__ and 'ring detector' in data.F_2.__doc__
    assert all(f'``{name}``' in data.F.__doc__ for name in ('F_0', 'F_1', 'F_2'))
    assert 't:' in data.F_0.__doc__
    card = pymcnp.inp.card
    assert 'material' in card.Cell_0.__doc__ and 'void' in card.Cell_1.__doc__ and 'LIKE n BUT' in card.Cell_2.__doc__


def test_public_namespace_has_no_private_or_stray_names() -> None:
    # ``from pymcnp import *`` binds public names only, and ``dir(pymcnp)`` shows no imported helpers.
    assert not [name for name in pymcnp.__all__ if name.startswith('_') and name != '__version__']
    assert not hasattr(pymcnp, 'importlib')
    public = {name for name in dir(pymcnp) if not name.startswith('_')}
    assert public == set(pymcnp.__all__) - {'__version__'}
    namespace: dict = {}
    exec('from pymcnp import *', namespace)
    assert '_cli' not in namespace and '_show' not in namespace and 'Inp' in namespace

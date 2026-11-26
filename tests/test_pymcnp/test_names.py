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

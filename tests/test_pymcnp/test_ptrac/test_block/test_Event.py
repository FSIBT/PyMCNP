import pytest

import pymcnp
from .... import classes


class Test_Event(classes.Test_FromMcnp, classes.Test_ToDataframe):
    element = pymcnp.ptrac.block.Event

    EXAMPLES_FROM_MCNP_VALID = [
        '       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01',
        '       3000         1        40         1         4         4         0\n   0.00000E+00  0.00000E+00  0.00000E+00 -0.23578E+00  0.82756E-02 -0.97177E+00  0.14100E+02  0.10000E+01  0.00000E+00',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '       3000         1        40        14         2\n   0.74673E+01  0.47397E+01  0.30091E+01',
    ]


# P-line values: position, then, with ``WRITE=ALL`` (forms 3 and 4), direction, energy, weight, and time.
POSITION = ('0.10000E+01', '0.20000E+01', '0.30000E+01')
DIRECTION = ('0.40000E+01', '0.50000E+01', '0.60000E+01')
ENERGY, WEIGHT, TIME = '0.70000E+01', '0.80000E+01', '0.90000E+01'


def _event(name: str) -> pymcnp.ptrac.block.Event:
    """
    Parses an event block of class ``name`` whose J-line values are 11, 12, 13, ... in field order.
    """

    kind = getattr(pymcnp.ptrac.block, name)
    fields = list(kind._fields)
    j = len(fields[fields.index('type') + 1 : fields.index('newline')])
    p = (*POSITION, *DIRECTION, ENERGY, WEIGHT, TIME) if name[-1] in '34' else POSITION
    event, remainder = kind.from_mcnp('       3000' + ''.join(f'{value:>10}' for value in range(11, 11 + j)) + '\n ' + ''.join(f'{value:>13}' for value in p))
    assert remainder == ''
    assert type(event) is kind
    return event


# (class, material, zaid, surface): J-line values per the field order of each class, e.g., ``EventBank_4`` is
# node, nxs(2,iex), ntyn, ipt, ncl, mat, ncp.
EVENTS = [
    ('EventSource_1', '14', None, None),
    ('EventSource_2', '15', None, None),
    ('EventSource_3', '14', None, None),
    ('EventSource_4', '15', None, None),
    ('EventBank_1', '15', '12', None),
    ('EventBank_2', '16', '12', None),
    ('EventBank_3', '15', '12', None),
    ('EventBank_4', '16', '12', None),
    ('EventSurface_1', '15', None, '12'),
    ('EventSurface_2', '16', None, '12'),
    ('EventSurface_3', '15', None, '12'),
    ('EventSurface_4', '16', None, '12'),
    ('EventCollision_1', '15', '12', None),
    ('EventCollision_2', '16', '12', None),
    ('EventCollision_3', '15', '12', None),
    ('EventCollision_4', '16', '12', None),
    ('EventTermination_1', '15', None, None),
    ('EventTermination_2', '16', None, None),
    ('EventTermination_3', '15', None, None),
    ('EventTermination_4', '16', None, None),
]


def _strip(value: object) -> object:
    if isinstance(value, tuple):
        return tuple(str(item).strip() for item in value)
    return None if value is None else str(value).strip()


@pytest.mark.parametrize(('name', 'material', 'zaid', 'surface'), EVENTS)
def test_properties(name: str, material: str, zaid: str | None, surface: str | None) -> None:
    event = _event(name)
    full = name[-1] in '34'

    assert _strip(event.material) == material
    assert _strip(event.position) == POSITION
    assert _strip(event.zaid) == zaid
    assert _strip(event.surface) == surface
    assert _strip(event.direction) == (DIRECTION if full else None)
    assert _strip(event.energy) == (ENERGY if full else None)
    assert _strip(event.weight) == (WEIGHT if full else None)
    assert _strip(event.time) == (TIME if full else None)


def test_base_class_parses_to_a_form() -> None:
    event, _ = pymcnp.ptrac.block.Event.from_mcnp(Test_Event.EXAMPLES_FROM_MCNP_VALID[0])

    assert type(event) is pymcnp.ptrac.block.EventSource_1
    assert (_strip(event.material), _strip(event.position)) == ('2', ('0.74673E+01', '0.47397E+01', '0.30091E+01'))


@pytest.mark.parametrize('name', [name for name, *_ in EVENTS if name[-1] in '24'])
def test_particle_is_ipt(name: str) -> None:
    event = _event(name)

    assert event.particle == event.pbl_i_ipt
    assert event.particle != event.ncl_pbl_i_icl


@pytest.mark.parametrize('name', [name for name, *_ in EVENTS if name[-1] in '13'])
def test_particle_is_none_without_ipt(name: str) -> None:
    # Forms 1 and 3 do not write PBL%I%IPT.
    assert _event(name).particle is None

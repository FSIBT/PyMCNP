import pandas

from ... import abc

COLUMNS = (
    'cell',
    'tracks',
    'population',
    'collisions',
    'collisions_weighted',
    'number_weighted_energy',
    'flux_weighted_energy',
    'average_track_weight',
    'average_track_mfp',
)


def to_dataframe(block) -> pandas.DataFrame:
    """
    Generates dataframes from activity tables (print table 126), one row per cell, plus a final `total` row.

    Parameters:
        block: Neutron or photon activity block.

    Returns:
        Dataframe with the columns `COLUMNS`, the `total` row only has tracks, population, collisions and weighted collisions.

    Raises:
        Error: Invalid table row.
    """

    rows = []
    for line in str(block.table_body).splitlines():
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 10:
            raise abc.Error('Invalid table row.', f'{line=}')
        rows.append({'cell': fields[1], **dict(zip(COLUMNS[1:3], map(int, fields[2:4]))), 'collisions': int(fields[4]), **dict(zip(COLUMNS[4:], map(float, fields[5:])))})

    frame = pandas.DataFrame(rows, columns=list(COLUMNS))
    frame['cell'] = frame['cell'].astype(int)
    total = {
        'cell': None,
        'tracks': int(str(block.table_total_tracks)),
        'population': int(str(block.table_total_population)),
        'collisions': int(str(block.table_total_collisions)),
        'collisions_weighted': float(str(block.table_total_weighted_collisions)),
    }
    frame = pandas.concat([frame, pandas.DataFrame([total], columns=list(COLUMNS))], ignore_index=True)
    frame['cell'] = frame['cell'].astype('Int64')
    return frame

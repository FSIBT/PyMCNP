import pathlib

import pandas

_INTEGERS = ('nps', 'creation_code', 'cell', 'material', 'surface', 'facet', 'zaid', 'parent_zaid', 'track')
_STRINGS = ('type', 'particle')


COLUMNS = tuple('nps type creation_code particle cell material surface facet zaid x y z u v w energy weight time track parent_zaid'.split())


def to_dataframe(rows: list[dict]) -> pandas.DataFrame:
    """
    Converts rows from `Event.to_dict` (optionally with `track` and `parent_zaid`) to a dataframe with proper dtypes:
    nullable `Int64` for integer columns, `string` for names, `float64` for the rest.
    """

    frame = pandas.DataFrame(rows, columns=None if rows else list(COLUMNS))
    for column in frame.columns:
        if column in _INTEGERS:
            frame[column] = frame[column].astype('Int64')
        elif column in _STRINGS:
            frame[column] = frame[column].astype('string')
        else:
            frame[column] = frame[column].astype('float64')
    return frame


class ParquetWriter:
    """
    Writes dataframes to one parquet file chunk by chunk, with `pyarrow` if installed, else `fastparquet`.
    """

    def __init__(self, path: pathlib.Path | str):
        self.path = pathlib.Path(path)
        self.temporary = self.path.with_name(self.path.name + '.partial')
        self.temporary.unlink(missing_ok=True)
        self._writer = None
        self._started = False

    def write(self, rows: list[dict]):
        frame = to_dataframe(rows)
        try:
            import pyarrow
            import pyarrow.parquet
        except ImportError:
            frame.to_parquet(self.temporary, engine='fastparquet', append=self._started)
        else:
            table = pyarrow.Table.from_pandas(frame, preserve_index=False)
            if self._writer is None:
                self._writer = pyarrow.parquet.ParquetWriter(self.temporary, table.schema)
            self._writer.write_table(table)
        self._started = True

    def close(self):
        if self._writer is not None:
            self._writer.close()
        if not self._started:
            to_dataframe([]).to_parquet(self.temporary)
        self.temporary.replace(self.path)

    def abort(self):
        if self._writer is not None:
            self._writer.close()
        self.temporary.unlink(missing_ok=True)

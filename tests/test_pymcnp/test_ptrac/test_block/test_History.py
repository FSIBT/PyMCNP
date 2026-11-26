import pymcnp
from .... import classes


HISTORY = '         12      1000\n       4000         1        40        10         1\n   0.00000E+00  0.00000E+00  0.00000E+00\n       3000         2     92238        16        10         1\n  -0.13113E+01 -0.64468E+00  0.55020E+00\n       3000         3         1        11        11         0\n  -0.30173E+01 -0.14341E+01  0.37201E+01\n       5000         4         2         9        12         0\n  -0.34878E+01 -0.16517E+01  0.45943E+01\n       2007         4         1         1        12         0\n  -0.34878E+01 -0.16517E+01  0.45943E+01\n       3000         2     92238        -2        10         1\n  -0.13113E+01 -0.64468E+00  0.55020E+00\n       3000         3         1        18        11         0\n  -0.17062E+01  0.25558E+01  0.39442E+01\n       5000         4         2        15        12         0\n  -0.17941E+01  0.32689E+01  0.47005E+01\n       9000         4         1         2        12         0\n  -0.17941E+01  0.32689E+01  0.47005E+01'


class Test_Tracks:
    def test_tracks(self) -> None:
        history, _ = pymcnp.ptrac.block.History.from_mcnp(HISTORY)
        tracks = list(history.tracks)

        assert len(tracks) == 2
        assert tracks[0].parent is None
        assert tracks[1].parent is tracks[0]
        assert [track.index for track in tracks] == [0, 1]
        assert all(track.nps == 12 for track in tracks)
        assert tracks[0].creation.type is pymcnp.ptrac.EventType.SOURCE
        assert tracks[1].creation.type is pymcnp.ptrac.EventType.BANK
        assert tracks[0].particle is None


class Test_History(classes.Test_FromMcnpIter, classes.Test_ToDataframe):
    element = pymcnp.ptrac.block.History

    EXAMPLES_FROM_MCNP_VALID = [
        '       1071      1000\n       3000         1        40        15         2\n  -0.19652E+01 -0.47816E+01 -0.20412E+00\n       3000         2     15012         9        16         1\n  -0.18262E+01 -0.47726E+01 -0.18684E+00\n       3000         3     13012       171        13         2\n  -0.11783E+01 -0.47307E+01 -0.10626E+00\n       3000         4     13012         8        16         1\n  -0.97926E+00 -0.47179E+01 -0.81516E-01\n       3000         5     10010        44        11         2\n  -0.53388E+00 -0.46891E+01 -0.26131E-01\n       3000         6      8010       163        16         1\n  -0.92519E+00 -0.35997E+01  0.98944E+00\n       9000         7     15012       169        15         2\n  -0.14671E+01 -0.28438E+01  0.11291E+01',
        '          9      1000\n       3000         1        40        10         1\n   0.00000E+00  0.00000E+00  0.00000E+00\n       4000         2         1         0        11         2\n  -0.11841E+01  0.46074E+01 -0.15393E+01\n       4000         3     92238        16        11         2\n  -0.14180E+01  0.55175E+01 -0.18433E+01\n       3000         3     92238        91        11         2\n  -0.62901E+00  0.45393E+01 -0.28033E+01\n       5000         4         2        61        12         0\n   0.17518E+01  0.57383E+01  0.57509E-01\n       2007         4         1         1        12         0\n   0.17518E+01  0.57383E+01  0.57509E-01\n       3000         3     92238        -2        11         2\n  -0.14180E+01  0.55175E+01 -0.18433E+01\n       5000         4         2        48        12         0\n  -0.14320E+01  0.55289E+01 -0.18385E+01\n       9000         4         1         2        12         0\n  -0.14320E+01  0.55289E+01 -0.18385E+01',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        '       1071      1000\n       3000         1        40        15         2\n  -0.19652E+01 -0.47816E+01 -0.20412E+00\n       3000         2     15012         9        16         1\n  -0.18262E+01 -0.47726E+01 -0.18684E+00\n       3000         3     13012       171        13         2\n  -0.11783E+01 -0.47307E+01 -0.10626E+00\n       3000         4     13012         8        16         1\n  -0.97926E+00 -0.47179E+01 -0.81516E-01\n       3000         5     10010        44        11         2\n  -0.53388E+00 -0.46891E+01 -0.26131E-01\n       3000         6      8010       163        16         1\n  -0.92519E+00 -0.35997E+01  0.98944E+00',
        '       1071      1000\n       3000         1        40        15         2\n  -0.19652E+01 -0.47816E+01 -0.20412E+00\n       3000         2     15012         9        16         1\n  -0.18262E+01 -0.47726E+01 -0.18684E+00\n       3000         3     13012       171        13         2\n  -0.11783E+01 -0.47307E+01 -0.10626E+00\n       3000         4     13012         8        16         1\n  -0.97926E+00 -0.47179E+01 -0.81516E-01\n       3000         5     10010        44        11         2\n  -0.53388E+00 -0.46891E+01 -0.26131E-01\n       8000         6      8010       163        16         1\n  -0.92519E+00 -0.35997E+01  0.98944E+00',
        'hello',
    ]

    EXAMPLES_TO_DATAFRAME = [
        '       1071      1000\n       3000         1        40        15         2\n  -0.19652E+01 -0.47816E+01 -0.20412E+00\n       3000         2     15012         9        16         1\n  -0.18262E+01 -0.47726E+01 -0.18684E+00\n       3000         3     13012       171        13         2\n  -0.11783E+01 -0.47307E+01 -0.10626E+00\n       3000         4     13012         8        16         1\n  -0.97926E+00 -0.47179E+01 -0.81516E-01\n       3000         5     10010        44        11         2\n  -0.53388E+00 -0.46891E+01 -0.26131E-01\n       3000         6      8010       163        16         1\n  -0.92519E+00 -0.35997E+01  0.98944E+00\n       9000         7     15012       169        15         2\n  -0.14671E+01 -0.28438E+01  0.11291E+01',
    ]


def test_subclass_from_mcnp_returns_subclass() -> None:
    class MyHistory(pymcnp.ptrac.block.History):
        pass

    history, _ = MyHistory.from_mcnp(HISTORY)
    assert type(history) is MyHistory
    assert history.to_mcnp() == pymcnp.ptrac.block.History.from_mcnp(HISTORY)[0].to_mcnp()


def test_truncated_from_mcnp_reads_the_complete_events() -> None:
    # Cut in the last event's P line: the events before it are kept, and a subclass gets its own type.
    source = '\n'.join(HISTORY.split('\n')[:-1])
    truncated, remainder = pymcnp.ptrac.block.HistoryTruncated.from_mcnp(source)
    history, _ = pymcnp.ptrac.block.History.from_mcnp(HISTORY)
    # Like every other ``from_mcnp``, it returns ``(obj, remainder)``; the remainder is the cut event's J line.
    assert remainder == HISTORY.split('\n')[-2]
    assert (truncated.nps, truncated.event_type) == (history.nps, history.event_type)
    assert [event.to_mcnp() for event in truncated.events] == [event.to_mcnp() for event in history.events[:-1]]

    class MyTruncated(pymcnp.ptrac.block.HistoryTruncated):
        pass

    assert type(MyTruncated.from_mcnp(source)[0]) is MyTruncated


def test_truncated_from_mcnp_of_complete_events_leaves_no_remainder() -> None:
    # Cut between two events: nothing is left over.
    source = '\n'.join(HISTORY.split('\n')[:-2])
    truncated, remainder = pymcnp.ptrac.block.HistoryTruncated.from_mcnp(source)
    assert remainder == ''
    assert len(truncated.events) == 8

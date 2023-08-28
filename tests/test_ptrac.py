import mcnptools


def test_header():
    with open("tests/ptrac_testdata.txt") as f:
        header = mcnptools.ptrac.parser.Header(f)

    assert header.program == "mcnp"
    assert header.version == "6"
    assert header.program_date == "05/08/13"
    assert header.run_date == "05/11/20"
    assert header.run_time == "20:01:17"
    assert header.name == "simulation ptrac"

    assert header.keywords == {
        "Buffer": 100.0,
        "Cell": 224.0,
        "Event": [1.0, 2.0, 3.0],
        "File": 1.0,
        "Max": 10000000.0,
        "Tally": 1.0,
        "Type": [2.0, 1.0],
        "Value": 0.0,
        "Write": 2.0,
    }
    assert header.IDS["nps"] == ["NPS", "first event type", "NCL", "JPTAL", "TAL"]
    assert header.IDS["initial source"] == [
        "next event type",
        "NODE",
        "NSR",
        "IPT",
        "NCL",
        "MAT",
        "NCP",
        "XXX",
        "YYY",
        "ZZZ",
        "UUU",
        "VVV",
        "WWW",
        "ERG",
        "WGT",
        "TME",
    ]
    assert header.IDS["bank"] == [
        "next event type",
        "NODE",
        "NXS",
        "NTYN/MTP",
        "IPT",
        "NCL",
        "MAT",
        "NCP",
        "XXX",
        "YYY",
        "ZZZ",
        "UUU",
        "VVV",
        "WWW",
        "ERG",
        "WGT",
        "TME",
    ]
    assert header.IDS["surface"] == [
        "next event type",
        "NODE",
        "Surface number",
        "angle with surface normal",
        "IPT",
        "NCL",
        "MAT",
        "NCP",
        "XXX",
        "YYY",
        "ZZZ",
        "UUU",
        "VVV",
        "WWW",
        "ERG",
        "WGT",
        "TME",
    ]
    assert header.IDS["collision"] == [
        "next event type",
        "NODE",
        "NXS",
        "NTYN/MTP",
        "IPT",
        "NCL",
        "MAT",
        "NCP",
        "XXX",
        "YYY",
        "ZZZ",
        "UUU",
        "VVV",
        "WWW",
        "ERG",
        "WGT",
        "TME",
    ]
    assert header.IDS["termination"] == [
        "next event type",
        "NODE",
        "termination type",
        "branch number for this history",
        "IPT",
        "NCL",
        "MAT",
        "NCP",
        "XXX",
        "YYY",
        "ZZZ",
        "UUU",
        "VVV",
        "WWW",
        "ERG",
        "WGT",
        "TME",
    ]


def test_read_file():
    filename = "tests/ptrac_testdata.txt"
    handler = mcnptools.ptrac.handler.HistoryHandler()
    mcnptools.ptrac.read_file(filename, handle_history=handler)

    assert handler.data[0].history[0].event_type == "initial source"
    assert handler.data[0].history[0].particle == "neutron"
    assert handler.data[0].history[0].node == 1.0
    assert handler.data[0].history[0].pos.x == -25.5
    assert handler.data[0].history[0].energy == 14.1
    assert handler.data[0].history[0].cell_number == 77

    assert handler.data[0].history[4].event_type == "Photon from Neutron"
    assert handler.data[0].history[4].particle == "photon"
    assert handler.data[0].history[4].node == 3.0
    assert handler.data[0].history[4].pos.x == 9.7205
    assert handler.data[0].history[4].energy == 4.439
    assert handler.data[0].history[4].cell_number == 221
    assert handler.data[0].history[4].time == 0.74153

    assert handler.data[1].history[3].event_type == "surface"
    assert handler.data[1].history[3].node == 4.0
    assert handler.data[1].history[3].pos.x == 187.23
    assert handler.data[1].history[3].energy == 13.947
    assert handler.data[1].history[3].cell_number == 99
    assert handler.data[1].history[3].time == 7.8563

import pytest

from main import draw_doors


@pytest.mark.parametrize(
    "opened_doors,answer,expected_doors",
    [
        (
            [],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |  2  |  |  3  |\n"""
            """  |    ०|  |    ०|  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |_____|  |_____|\n\n"""
        ),
        (
            [],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |  2  |  |  3  |\n"""
            """  |    ०|  |    ०|  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |_____|  |_____|\n\n"""
        ),
        (
            [],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |  2  |  |  3  |\n"""
            """  |    ०|  |    ०|  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |_____|  |_____|\n\n"""
        ),
        (
            [1],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |  2  |  |  3  |\n"""
            """  |     |  |    ०|  |    ०|\n"""
            """  |   💰|  |     |  |     |\n"""
            """  | 💰💰|  |_____|  |_____|\n\n"""
        ),
        (
            [1],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |  2  |  |  3  |\n"""
            """  |     |  |    ०|  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |_____|  |_____|\n\n"""
        ),
        (
            [1],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |  2  |  |  3  |\n"""
            """  |     |  |    ०|  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |_____|  |_____|\n\n"""
        ),
        (
            [2],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |     |  |  3  |\n"""
            """  |    ०|  |     |  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |     |  |_____|\n\n"""
        ),
        (
            [2],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |     |  |  3  |\n"""
            """  |    ०|  |     |  |    ०|\n"""
            """  |     |  |   💰|  |     |\n"""
            """  |_____|  | 💰💰|  |_____|\n\n"""
        ),
        (
            [2],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |     |  |  3  |\n"""
            """  |    ०|  |     |  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |     |  |_____|\n\n"""
        ),
        (
            [3],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |  2  |  |     |\n"""
            """  |    ०|  |    ०|  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |_____|  |     |\n\n"""
        ),
        (
            [3],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |  2  |  |     |\n"""
            """  |    ०|  |    ०|  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |_____|  |     |\n\n"""
        ),
        (
            [3],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |  2  |  |     |\n"""
            """  |    ०|  |    ०|  |     |\n"""
            """  |     |  |     |  |   💰|\n"""
            """  |_____|  |_____|  | 💰💰|\n\n"""
        ),
        (
            [1, 2],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |  3  |\n"""
            """  |     |  |     |  |    ०|\n"""
            """  |   💰|  |     |  |     |\n"""
            """  | 💰💰|  |     |  |_____|\n\n"""
        ),
        (
            [1, 2],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |  3  |\n"""
            """  |     |  |     |  |    ०|\n"""
            """  |     |  |   💰|  |     |\n"""
            """  |     |  | 💰💰|  |_____|\n\n"""
        ),
        (
            [1, 2],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |  3  |\n"""
            """  |     |  |     |  |    ०|\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |_____|\n\n"""
        ),
        (
            [1, 3],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |  2  |  |     |\n"""
            """  |     |  |    ०|  |     |\n"""
            """  |   💰|  |     |  |     |\n"""
            """  | 💰💰|  |_____|  |     |\n\n"""
        ),
        (
            [1, 3],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |  2  |  |     |\n"""
            """  |     |  |    ०|  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |_____|  |     |\n\n"""
        ),
        (
            [1, 3],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |  2  |  |     |\n"""
            """  |     |  |    ०|  |     |\n"""
            """  |     |  |     |  |   💰|\n"""
            """  |     |  |_____|  | 💰💰|\n\n"""
        ),
        (
            [2, 3],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |     |  |     |\n"""
            """  |    ०|  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |_____|  |     |  |     |\n\n"""
        ),
        (
            [2, 3],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |     |  |     |\n"""
            """  |    ०|  |     |  |     |\n"""
            """  |     |  |   💰|  |     |\n"""
            """  |_____|  | 💰💰|  |     |\n\n"""
        ),
        (
            [2, 3],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |  1  |  |     |  |     |\n"""
            """  |    ०|  |     |  |     |\n"""
            """  |     |  |     |  |   💰|\n"""
            """  |_____|  |     |  | 💰💰|\n\n"""
        ),
        (
            [1, 2, 3],
            1,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |   💰|  |     |  |     |\n"""
            """  | 💰💰|  |     |  |     |\n\n"""
        ),
        (
            [1, 2, 3],
            2,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |   💰|  |     |\n"""
            """  |     |  | 💰💰|  |     |\n\n"""
        ),
        (
            [1, 2, 3],
            3,
            """   _____    _____    _____\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |     |\n"""
            """  |     |  |     |  |   💰|\n"""
            """  |     |  |     |  | 💰💰|\n\n"""
        ),
    ]

)
def test_draw_doors(capsys, opened_doors, answer, expected_doors):
    draw_doors(opened_doors, answer)
    stdout, stderr = capsys.readouterr()
    assert stdout == expected_doors
    assert stderr == ""
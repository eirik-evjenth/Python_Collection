from billeter import billet_pris

def test_billet_pris():
    assert billet_pris(6) == 63
    assert billet_pris(10) == 63
    assert billet_pris(17) == 63

    assert billet_pris(18) == 157
    assert billet_pris(35) == 157
    assert billet_pris(66) == 157

    assert billet_pris(67) == 79
    assert billet_pris(80) == 79
    assert billet_pris(100) == 79

    assert billet_pris(0) == 0
    assert billet_pris(5) == 0

import pytest

@pytest.mark.parametrize("alder,pris",[
        (6, 63),
        (10, 63),
        (17, 63),
        (18, 157),
        (35, 157),
        (66, 157),
        (67, 79),
        (80, 79),
        (100, 79),
        (0, 0),
        (5, 0),
    ])
def test_billetpriser(alder, pris):
    assert billet_pris(alder) == pris
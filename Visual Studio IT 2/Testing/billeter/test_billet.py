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

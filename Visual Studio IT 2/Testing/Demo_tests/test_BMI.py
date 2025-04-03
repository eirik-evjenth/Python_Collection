from BMI import BMI_kalkulator
import pytest

@pytest.mark.parametrize("vekt,høyde,BMI", [
    (60, 1.6, "Normal vekt"),
    (200000, 1.75, "Fedme, grad 3"),
    (100, 1.65, "Fedme, grad 2"),
    (100, 1.74, "Fedme, grad 1"),
    (90, 1.9, "Normal vekt"),
    (110, 2.0, "Overvektig"),
    (55, 1.6, "Normal vekt"),
    (65, 1.7, "Normal vekt"),
    (0, 1.6, "Undervekt"), 
])
def test_BMI(vekt, høyde, BMI):
    assert BMI_kalkulator(vekt, høyde) == BMI

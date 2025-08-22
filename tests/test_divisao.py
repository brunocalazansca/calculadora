import pytest
from Calculadora import Calculadora

# Abrevia o nome da classe para simplificar
@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.parametrize("numerador, denominador, resultado_esperado", [
    (1, 2, 0.5),
    (500, 5, 100),
    (80, 4, 20),
    (44, 44, 1),
    (100, 4, 25),
])

def test_divisao(calc, numerador, denominador, resultado_esperado):
    assert calc.divisao(numerador, denominador) == resultado_esperado

def test_divisao_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divisao(5, 0)
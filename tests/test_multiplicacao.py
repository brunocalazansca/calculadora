import pytest
from Calculadora import Calculadora

# Abrevia o nome da classe para simplificar
@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.parametrize("lista_valores, resultado_esperado", [
    ([1, 2, 3], 6),
    ([1, 1, 2, 2], 4),
    ([10, -100, 80], -80000),
    ([0, 5], 0),
    ([-1, 1, -2, 2], -4),
    ([77, 66, 55], 279510),
    ([], 0)
])

def test_multiplicacao(calc, lista_valores, resultado_esperado):
    assert calc.multiplicacao(lista_valores) == resultado_esperado
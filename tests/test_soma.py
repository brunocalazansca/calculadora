import pytest
from Calculadora import Calculadora

# Abrevia o nome da classe para simplificar
@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.parametrize("lista_valores, resultado_esperado", [
    ([1, 2, 3], 6),
    ([-1, 1, -2, 2], 0),
    ([10, -100, 80], -10),
    ([33, 77], 110),
    ([], 0)
])

def test_soma(calc, lista_valores, resultado_esperado):
    assert calc.soma(lista_valores) == resultado_esperado
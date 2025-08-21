import pytest
from Calculadora import Calculadora

# Abrevia o nome da classe para simplificar
@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.parametrize("lista_valores, resultado_esperado", [
    ([15, 5, 10], 0),
    ([-1, 1, -2, 2], -2),
    ([77, 66, 55], -44),
    ([1024, 768], 256),
    ([], 0)
])

def test_subtracao(calc, lista_valores, resultado_esperado):
    assert calc.subtracao(lista_valores) == resultado_esperado
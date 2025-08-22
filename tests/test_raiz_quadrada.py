import pytest
from Calculadora import Calculadora

# Abrevia o nome da classe para simplificar
@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.parametrize("valor, resultado", [
    (16, 4),
    (4, 2),
    (36, 6),
    (81, 9),
    (121, 11),
    (400, 20)
])

def test_raiz_quadrada(calc, valor, resultado):
    assert calc.raiz_quadrada(valor) == resultado

def test_raiz_quadrada_numero_negativo(calc):
    with pytest.raises(ValueError):
        calc.raiz_quadrada(-1)
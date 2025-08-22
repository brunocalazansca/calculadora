import pytest
from Calculadora import Calculadora

# Abrevia o nome da classe para simplificar
@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.parametrize("valor, resultado", [
    (5, 120),
    (2, 2),
    (3, 6),
    (4, 24),
    (6, 720),
    (0, 1)
])

def test_fatorial(calc, valor, resultado):
    assert calc.fatorial(valor) == resultado

def test_fatorial_numero_negativo(calc):
    with pytest.raises(ValueError):
        calc.fatorial(-1)
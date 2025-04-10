import pytest 
from imc_diego import calcular_imc

@pytest.mark.parametrize("peso, altura, expected", [
    (40, 1.70, "Muito abaixo do peso ideal" ),
    (50, 1.70, "Abaixo do peso" ),
    (50, 1.60, "Peso Normal" ),
    (50, 1.40, "Acima do peso" ),
    (70, 1.50, "Obesidade grau 1" ),
    (70, 1.40, "Obesidade grau 2" ),
    
    
    ])

def test_calcular_imc(peso, altura, expected):
    assert calcular_imc(peso, altura) == (expected)

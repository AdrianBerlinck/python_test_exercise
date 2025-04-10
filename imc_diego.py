def calcular_imc(peso, altura):
    
    imc = peso / (altura * altura)

    if imc < 17:
        return("Muito abaixo do peso ideal")
    elif imc >= 17 and imc < 18.5:
        return("Abaixo do peso")
    elif imc >= 18.5 and imc < 25:
        return("Peso Normal")
    elif imc >= 25 and imc < 30:
        return("Acima do peso")
    elif imc >= 30 and imc < 35:
        return("Obesidade grau 1")
    elif imc >= 35 and imc < 40:
        return("Obesidade grau 2")
    else:
        return("Obesidade grau 3")

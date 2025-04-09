def calcular_imc(peso, altura) :
# peso em kg e altura em cm
    
    imc = peso/(altura*altura)
    print(imc)
    if imc < 17 :
        print('Abaixo do peso ideal');
    elif imc < 18.49 :
        print('Abaixo do peso');
    elif imc < 24.99 :
        print('Peso normal');
    elif imc < 29.99 :
        print('Acima do peso');
    elif imc < 34.99 :
        print('Obesidade grau 1');
    elif imc < 39.99 :
        print('Obesidade grau 2');
    elif imc < 39.99 :
        print('Obesidade grau 3(morbida)');


    print(f"Seu IMC é: {imc:.2f}")




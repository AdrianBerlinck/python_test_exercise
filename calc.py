def Calc(num1, num2, operador):

    if operador == '+':
        return num1 + num2
    if operador == '-':
        return num1 - num2
    if operador == '*':
        return num1 * num2
    if operador == '/' and num1 !=0 or num2 !=0:
        return num1 / num2
   
        
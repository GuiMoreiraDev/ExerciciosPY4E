peso = input("Informe seu peso: ")
altura = input("Informe sua altura: ")
try:
    fpeso = float(peso)
    faltura = float(altura)
except:
    print("Valor invalido")
    exit()

imc = fpeso / (faltura**2)

if (imc < 18.5):
    print('{:.2f}'.format(imc))
    print("Abaixo do peso")
elif (imc < 24.9):
    print('{:.2f}'.format(imc))
    print("Peso normal")
elif (imc < 29.9):
    print('{:.2f}'.format(imc))
    print("Pre-obesidade")
elif (imc < 34.9):
    print('{:.2f}'.format(imc))
    print("Obesidade grau 1")
elif (imc < 39.9):
    print('{:.2f}'.format(imc))
    print("Obesidade grau 2")
else:
    print('{:.2f}'.format(imc))
    print("Obesidade grau 3")

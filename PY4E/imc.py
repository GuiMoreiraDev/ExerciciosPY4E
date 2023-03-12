peso = input("Informe seu peso: ")
altura = input("Informe sua altura: ")

try:
    fpeso = float(peso)
    faltura = float(altura)
except:
    print("Valor invalido!")
    exit()
imc = fpeso / (faltura**2)
print('{:.2f}' .format(imc))

horas = input("Horas trabalhadas na semana: ")
v_horas = input("Valor da hora normal: ")
try:
    fhoras = float(horas)
    fv_horas = float(v_horas) 
except:
    print("Valor invalido!")
    exit()

salar = fhoras * fv_horas
print(salar)

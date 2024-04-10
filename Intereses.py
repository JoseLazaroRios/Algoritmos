print("Calculadora de Intereses Bancarios")
saldo = float(input("Ingrese su saldo inicial: "))


if saldo < 810000.00:
    interes = 0.03
else:
    interes = 0.04


saldo_final = saldo * (1 + interes)
print("Su saldo al final del primer año es:", saldo_final)

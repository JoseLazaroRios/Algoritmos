x = 1.0

a = float(input("Ingrese el valor de 'a': "))

for k in range(1, 11):
    x = 0.5 * (x + a / x)
    print("La raíz después de", k, "iteraciones es", x)

print("La raíz cuadrada de", a, "es aproximadamente", x)




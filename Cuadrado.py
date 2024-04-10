print("Dibujo de un cuadrado")
N = int(input("Ingrese el número de asteriscos de cada lado del cuadrado: "))

print("*" * N)
for i in range(N - 2):

    print("*", end="")

    for j in range(N - 2):

        print(" ", end="")
    print("*")
print("*" * N)
